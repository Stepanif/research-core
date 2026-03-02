from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def _extract_dataset_id(stdout: str) -> str:
    for line in stdout.splitlines():
        if line.startswith("REGISTERED dataset_id="):
            return line.split("=", 1)[1].strip()
    raise AssertionError(f"Missing dataset id in output: {stdout}")


def _extract_runset_id(stdout: str) -> str:
    for line in stdout.splitlines():
        if line.startswith("RUNSET_CREATED runset_id="):
            return line.split("=", 1)[1].strip()
    raise AssertionError(f"Missing runset id in output: {stdout}")


def _build_linked_run(runner: CliRunner, repo_root: Path, tmp_path: Path, dataset_id: str) -> str:
    fixture_path = repo_root / "tests" / "fixtures" / "raw_small_sample.txt"
    schema_path = repo_root / "schemas" / "canon.schema.v1.json"
    colmap_path = repo_root / "schemas" / "colmap.raw_vendor_v1.json"
    psa_schema_path = repo_root / "schemas" / "psa.schema.v1.json"

    run_dir = tmp_path / "run"
    for args in [
        [
            "canon",
            "--in",
            str(fixture_path),
            "--out",
            "run",
            "--instrument",
            "ES",
            "--tf",
            "1min",
            "--schema",
            str(schema_path),
            "--colmap",
            str(colmap_path),
        ],
        ["psa", "--in", str(run_dir / "canon.parquet"), "--out", "run", "--schema", str(psa_schema_path)],
        ["observe", "summary", "--run", "run"],
        ["observe", "profile", "--run", "run"],
        ["lineage", "build", "--run", "run", "--catalog", "catalog", "--raw-dataset-id", dataset_id],
    ]:
        result = runner.invoke(app, args)
        assert result.exit_code == 0, result.stdout

    payload = json.loads((run_dir / "canon.manifest.json").read_text(encoding="utf-8"))
    return str(payload["output_files"]["canon.parquet"]["canonical_table_sha256"])


def test_runset_materialize_smoke(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent

    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()

    raw_root = tmp_path / "raw"
    raw_root.mkdir(parents=True, exist_ok=True)
    fixture_path = repo_root / "tests" / "fixtures" / "raw_small_sample.txt"
    (raw_root / "sample.txt").write_text(fixture_path.read_text(encoding="utf-8"), encoding="utf-8")

    reg = runner.invoke(app, ["dataset", "register", "raw", "--catalog", "catalog", "--root", "raw", "--desc", "raw-source"])
    assert reg.exit_code == 0, reg.stdout
    dataset_id = _extract_dataset_id(reg.stdout)

    canon_hash = _build_linked_run(runner, repo_root=repo_root, tmp_path=tmp_path, dataset_id=dataset_id)

    runset_spec = tmp_path / "runset.json"
    runset_spec.write_text(
        json.dumps(
            {
                "runset_version": "v1",
                "name": "runset-materialize-smoke",
                "datasets": [dataset_id],
                "runs": [
                    {
                        "run_ref": "run",
                        "dataset_id": dataset_id,
                        "canon_table_sha256": canon_hash,
                    }
                ],
                "policy": {
                    "allow_materialize_missing": False,
                    "require_lineage_links": True,
                    "require_bidirectional": True,
                },
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    create = runner.invoke(app, ["runset", "create", "--catalog", "catalog", "--spec", str(runset_spec)])
    assert create.exit_code == 0, create.stdout
    runset_id = _extract_runset_id(create.stdout)

    out_dir = tmp_path / "runset_outputs"
    materialize = runner.invoke(
        app,
        [
            "runset",
            "materialize",
            "--catalog",
            "catalog",
            "--id",
            runset_id,
            "--runs-root",
            str(tmp_path / "runs_root"),
            "--project-out",
            str(out_dir),
        ],
    )
    assert materialize.exit_code == 0, materialize.stdout

    target_dir = out_dir / runset_id
    assert (target_dir / "runset.materialize.summary.json").exists()
    assert (target_dir / "runset.materialize.manifest.json").exists()

    summary = json.loads((target_dir / "runset.materialize.summary.json").read_text(encoding="utf-8"))
    assert summary["totals"]["datasets"] == 1
    assert summary["datasets"][0]["status"] in {"REUSED", "MATERIALIZED"}
    assert summary["conflicts"] == []

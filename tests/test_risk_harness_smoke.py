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


def test_risk_run_and_runset_smoke(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent
    fixture_path = repo_root / "tests" / "fixtures" / "raw_small_sample.txt"
    schema_path = repo_root / "schemas" / "canon.schema.v1.json"
    colmap_path = repo_root / "schemas" / "colmap.raw_vendor_v1.json"
    psa_schema_path = repo_root / "schemas" / "psa.schema.v1.json"

    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()

    raw_root = tmp_path / "raw"
    raw_root.mkdir(parents=True, exist_ok=True)
    (raw_root / "sample.txt").write_text(fixture_path.read_text(encoding="utf-8"), encoding="utf-8")

    reg = runner.invoke(app, ["dataset", "register", "raw", "--catalog", "catalog", "--root", "raw", "--desc", "raw-source"])
    assert reg.exit_code == 0, reg.stdout
    dataset_id = _extract_dataset_id(reg.stdout)

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

    risk_run = runner.invoke(app, ["risk", "run", "--run", "run"])
    assert risk_run.exit_code == 0, risk_run.stdout

    risk_summary_path = run_dir / "risk" / "risk.summary.json"
    risk_manifest_path = run_dir / "risk" / "risk.summary.manifest.json"
    assert risk_summary_path.exists()
    assert risk_manifest_path.exists()

    risk_summary = json.loads(risk_summary_path.read_text(encoding="utf-8"))
    assert risk_summary["risk_version"] == "v1"
    assert risk_summary["counts"]["row_count"] > 0
    assert "instability_score" in risk_summary

    canon_manifest = json.loads((run_dir / "canon.manifest.json").read_text(encoding="utf-8"))
    canon_hash = canon_manifest["output_files"]["canon.parquet"]["canonical_table_sha256"]

    runset_spec = tmp_path / "runset_risk_smoke.json"
    runset_spec.write_text(
        json.dumps(
            {
                "runset_version": "v1",
                "name": "runset-risk-smoke",
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

    risk_runset = runner.invoke(
        app,
        ["risk", "runset", "--catalog", "catalog", "--id", runset_id, "--out", "risk_out"],
    )
    assert risk_runset.exit_code == 0, risk_runset.stdout

    runset_summary_path = tmp_path / "risk_out" / runset_id / "risk.runset.summary.json"
    runset_manifest_path = tmp_path / "risk_out" / runset_id / "risk.runset.manifest.json"
    assert runset_summary_path.exists()
    assert runset_manifest_path.exists()

    runset_summary = json.loads(runset_summary_path.read_text(encoding="utf-8"))
    assert runset_summary["runset_risk_version"] == "v1"
    assert runset_summary["run_count"] == 1
    assert len(runset_summary["per_run"]) == 1

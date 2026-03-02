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


def test_runset_materialize_conflict_fail_loud(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent

    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()

    raw_root = tmp_path / "raw"
    raw_root.mkdir(parents=True, exist_ok=True)
    fixture_path = repo_root / "tests" / "fixtures" / "raw_small_sample.txt"
    (raw_root / "sample.txt").write_text(fixture_path.read_text(encoding="utf-8"), encoding="utf-8")

    reg = runner.invoke(app, ["dataset", "register", "raw", "--catalog", "catalog", "--root", "raw"])
    assert reg.exit_code == 0, reg.stdout
    dataset_id = _extract_dataset_id(reg.stdout)

    schema_path = repo_root / "schemas" / "canon.schema.v1.json"
    colmap_path = repo_root / "schemas" / "colmap.raw_vendor_v1.json"

    canon = runner.invoke(
        app,
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
    )
    assert canon.exit_code == 0, canon.stdout

    lineage = runner.invoke(app, ["lineage", "build", "--run", "run", "--catalog", "catalog", "--raw-dataset-id", dataset_id])
    assert lineage.exit_code == 0, lineage.stdout

    spec_path = tmp_path / "runset_conflict.json"
    spec_path.write_text(
        json.dumps(
            {
                "runset_version": "v1",
                "datasets": [dataset_id],
                "runs": [
                    {
                        "run_ref": "run",
                        "dataset_id": dataset_id,
                        "canon_table_sha256": "deadbeef-conflict",
                    }
                ],
                "policy": {
                    "allow_materialize_missing": False,
                    "require_lineage_links": False,
                    "require_bidirectional": False,
                },
            },
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    create = runner.invoke(app, ["runset", "create", "--catalog", "catalog", "--spec", str(spec_path)])
    assert create.exit_code == 0, create.stdout
    runset_id = _extract_runset_id(create.stdout)

    result = runner.invoke(
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
            str(tmp_path / "out"),
        ],
    )
    assert result.exit_code != 0
    message = str(result.exception or result.stdout).lower()
    assert "conflict" in message or "fail-loud" in message

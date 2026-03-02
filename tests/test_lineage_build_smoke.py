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


def _build_run_with_observe(
    runner: CliRunner,
    run_dir: Path,
    fixture_path: Path,
    schema_path: Path,
    colmap_path: Path,
    psa_schema_path: Path,
) -> None:
    canon = runner.invoke(
        app,
        [
            "canon",
            "--in",
            str(fixture_path),
            "--out",
            str(run_dir),
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

    psa = runner.invoke(
        app,
        ["psa", "--in", str(run_dir / "canon.parquet"), "--out", str(run_dir), "--schema", str(psa_schema_path)],
    )
    assert psa.exit_code == 0, psa.stdout

    observe_summary = runner.invoke(app, ["observe", "summary", "--run", str(run_dir)])
    assert observe_summary.exit_code == 0, observe_summary.stdout

    observe_profile = runner.invoke(app, ["observe", "profile", "--run", str(run_dir)])
    assert observe_profile.exit_code == 0, observe_profile.stdout


def test_lineage_build_smoke(monkeypatch: object, tmp_path: Path) -> None:
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
    raw_dataset_id = _extract_dataset_id(reg.stdout)

    run_dir = tmp_path / "run"
    _build_run_with_observe(
        runner,
        run_dir,
        fixture_path=fixture_path,
        schema_path=schema_path,
        colmap_path=colmap_path,
        psa_schema_path=psa_schema_path,
    )

    lineage_build = runner.invoke(
        app,
        [
            "lineage",
            "build",
            "--run",
            "run",
            "--catalog",
            "catalog",
            "--raw-dataset-id",
            raw_dataset_id,
        ],
    )
    assert lineage_build.exit_code == 0, lineage_build.stdout

    lineage_path = run_dir / "lineage" / "lineage.json"
    lineage_manifest_path = run_dir / "lineage" / "lineage.manifest.json"
    assert lineage_path.exists()
    assert lineage_manifest_path.exists()

    lineage_payload = json.loads(lineage_path.read_text(encoding="utf-8"))
    assert lineage_payload["lineage_version"] == "v1"
    assert lineage_payload["inputs"]["raw_dataset_id"] == raw_dataset_id

    index_path = tmp_path / "catalog" / "links" / "dataset_to_runs.index.json"
    assert index_path.exists()
    index_payload = json.loads(index_path.read_text(encoding="utf-8"))
    assert raw_dataset_id in index_payload["datasets"]
    assert len(index_payload["datasets"][raw_dataset_id]["runs"]) == 1

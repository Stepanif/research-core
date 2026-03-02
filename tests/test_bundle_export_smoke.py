from __future__ import annotations

import zipfile
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


REQUIRED_ARCHIVE_PATHS = {
    "bundle/run/canon.parquet",
    "bundle/run/canon.manifest.json",
    "bundle/run/psa.parquet",
    "bundle/run/psa.manifest.json",
    "bundle/run/observe/observe.summary.json",
    "bundle/run/observe/observe.summary.manifest.json",
    "bundle/run/observe/observe.profile.json",
    "bundle/run/observe/observe.profile.manifest.json",
    "bundle/registry/registry_entry.json",
    "bundle/bundle.manifest.json",
    "bundle/README_BUNDLE.txt",
}


def _build_run(runner: CliRunner, run_dir: Path) -> None:
    for args in [
        [
            "canon",
            "--in",
            "tests/fixtures/raw_small_sample.txt",
            "--out",
            str(run_dir),
            "--instrument",
            "ES",
            "--tf",
            "1min",
            "--schema",
            "schemas/canon.schema.v1.json",
            "--colmap",
            "schemas/colmap.raw_vendor_v1.json",
        ],
        ["psa", "--in", str(run_dir / "canon.parquet"), "--out", str(run_dir)],
        ["observe", "summary", "--run", str(run_dir)],
        ["observe", "profile", "--run", str(run_dir)],
        ["registry", "refresh", "--run", str(run_dir)],
    ]:
        result = runner.invoke(app, args)
        assert result.exit_code == 0, result.stdout


def test_bundle_export_smoke(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

    bundle_path = tmp_path / "bundle.zip"
    result = runner.invoke(app, ["bundle", "export", "--run", str(run_dir), "--out", str(bundle_path)])
    assert result.exit_code == 0, result.stdout
    assert bundle_path.exists()

    with zipfile.ZipFile(bundle_path, "r") as archive:
        names = set(archive.namelist())
    assert REQUIRED_ARCHIVE_PATHS.issubset(names)

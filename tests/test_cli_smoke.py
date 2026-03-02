from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app


def test_cli_help_smoke() -> None:
    runner = CliRunner()
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "canon" in result.stdout


def test_cli_minimal_canon_run_creates_artifacts(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    runner = CliRunner()
    run_dir = tmp_path / "run"
    result = runner.invoke(
        app,
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
    )
    assert result.exit_code == 0, result.stdout
    assert (run_dir / "canon.parquet").exists()
    assert (run_dir / "canon.manifest.json").exists()
    assert (run_dir / "canon.contract.json").exists()
    assert (run_dir / "logs" / "canon.log").exists()

from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


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


def test_doctor_run_smoke(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

    result = runner.invoke(app, ["doctor", "run", "--run", str(run_dir)])
    assert result.exit_code == 0, result.stdout
    assert "RESEARCH DOCTOR v1" in result.stdout
    assert "REQUIRED FILES" in result.stdout
    assert "HASH INTEGRITY" in result.stdout
    assert "INVARIANTS" in result.stdout
    assert "RESULT" in result.stdout
    assert "[FAIL]" not in result.stdout

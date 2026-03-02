from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def _build_run(runner: CliRunner, run_dir: Path) -> None:
    canon = runner.invoke(
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
    assert canon.exit_code == 0, canon.stdout

    psa = runner.invoke(app, ["psa", "--in", str(run_dir / "canon.parquet"), "--out", str(run_dir)])
    assert psa.exit_code == 0, psa.stdout

    summary = runner.invoke(app, ["observe", "summary", "--run", str(run_dir)])
    assert summary.exit_code == 0, summary.stdout

    profile = runner.invoke(app, ["observe", "profile", "--run", str(run_dir)])
    assert profile.exit_code == 0, profile.stdout


def test_registry_refresh_fails_on_observe_mutation(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"
    _build_run(runner, run_dir)

    first = runner.invoke(app, ["registry", "refresh", "--run", str(run_dir)])
    assert first.exit_code == 0, first.stdout

    index_path = run_dir.parent / "index.json"
    before = index_path.read_text(encoding="utf-8")

    summary_json_path = run_dir / "observe" / "observe.summary.json"
    summary_json_path.write_text(summary_json_path.read_text(encoding="utf-8") + " \n", encoding="utf-8")

    second = runner.invoke(app, ["registry", "refresh", "--run", str(run_dir)])
    assert second.exit_code != 0
    assert second.exception is not None
    assert "Manifest hash mismatch" in str(second.exception)

    after = index_path.read_text(encoding="utf-8")
    assert before == after

from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from research_core.cli import app


def test_release_notes_fail_loud(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    result = runner.invoke(app, ["release", "notes", "--from", "not-a-real-ref", "--to", "phase14-v1"])
    assert result.exit_code != 0

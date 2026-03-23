from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app
from tests._release_helpers import init_release_fixture_repo


def test_release_notes_smoke(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = init_release_fixture_repo(tmp_path / "repo", ["phase13-v1", "phase14-v1"])
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(cli_module, "_repo_root", lambda: repo_root)

    runner = CliRunner()
    one = runner.invoke(app, ["release", "notes", "--from", "phase13-v1", "--to", "phase14-v1"])
    two = runner.invoke(app, ["release", "notes", "--from", "phase13-v1", "--to", "phase14-v1"])

    assert one.exit_code == 0, one.stdout
    assert two.exit_code == 0, two.stdout
    assert one.stdout == two.stdout

    lines = [line for line in one.stdout.splitlines() if line.strip()]
    assert lines[0] == "Release notes: phase13-v1..phase14-v1"
    assert len(lines) >= 2
    assert lines[1].startswith("- ")

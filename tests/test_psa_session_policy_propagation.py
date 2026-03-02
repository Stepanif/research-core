from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def _write_session_boundary_fixture(path: Path) -> None:
    path.write_text(
        "Date,Time,Open,High,Low,Close,Up,Down\n"
        "03/07/2024,08:00,100.0,101.0,99.0,100.5,10,5\n"
        "03/07/2024,10:00,100.5,101.5,100.0,101.0,11,6\n"
        "03/07/2024,17:00,101.0,102.0,99.5,100.0,12,7\n",
        encoding="utf-8",
    )


def test_psa_session_policy_propagation(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    fixture = tmp_path / "raw_session_boundary.txt"
    _write_session_boundary_fixture(fixture)
    runner = CliRunner()

    for policy in ["full", "rth", "eth"]:
        run_dir = tmp_path / policy
        canon_result = runner.invoke(
            app,
            [
                "canon",
                "--in",
                str(fixture),
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
                "--session-policy",
                policy,
            ],
        )
        assert canon_result.exit_code == 0, canon_result.stdout

        psa_result = runner.invoke(app, ["psa", "--in", str(run_dir / "canon.parquet"), "--out", str(run_dir)])
        assert psa_result.exit_code == 0, psa_result.stdout

        canon_manifest = json.loads((run_dir / "canon.manifest.json").read_text(encoding="utf-8"))
        psa_manifest = json.loads((run_dir / "psa.manifest.json").read_text(encoding="utf-8"))

        assert psa_manifest["session"]["session_policy"] == canon_manifest["session_policy"]
        assert psa_manifest["session"]["rth_start"] == canon_manifest["rth_start"]
        assert psa_manifest["session"]["rth_end"] == canon_manifest["rth_end"]
        assert psa_manifest["session"]["tz"] == "America/New_York"

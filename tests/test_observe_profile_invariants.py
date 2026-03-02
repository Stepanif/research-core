from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def test_observe_profile_invariants(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")

    runner = CliRunner()
    run_dir = tmp_path / "run"

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

    observe = runner.invoke(app, ["observe", "profile", "--run", str(run_dir)])
    assert observe.exit_code == 0, observe.stdout

    profile = json.loads((run_dir / "observe" / "observe.profile.json").read_text(encoding="utf-8"))
    psa_df = pd.read_parquet(run_dir / "psa.parquet")

    by_date_total = sum(int(item["bar_count"]) for item in profile["by_date"].values())
    windows_total = sum(int(item["bar_count"]) for item in profile["time_windows"]["windows"])

    assert by_date_total == len(psa_df)
    assert windows_total == len(psa_df)

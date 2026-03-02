from __future__ import annotations

from pathlib import Path

import pandas as pd
from typer.testing import CliRunner

import research_core.cli as cli_module
from research_core.cli import app


def test_observe_invariant_row_count_match(monkeypatch: object, tmp_path: Path) -> None:
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

    tampered = pd.read_parquet(run_dir / "psa.parquet").iloc[:-1].copy()
    tampered.to_parquet(run_dir / "psa.parquet", index=False)

    observe = runner.invoke(app, ["observe", "summary", "--run", str(run_dir)])
    assert observe.exit_code != 0
    assert "row_count_match" in str(observe.exception)

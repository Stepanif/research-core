from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset, sweep_to_baseline_root
from research_core.cli import app


def test_baseline_promote_immutability(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)

    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-baseline-promote-immutability")
    baseline_root = tmp_path / "baselines"
    _card_path, baseline_id = sweep_to_baseline_root(runner, tmp_path, runset_id, baseline_root)

    refresh = runner.invoke(app, ["baseline", "index", "refresh", "--root", str(baseline_root)])
    assert refresh.exit_code == 0, refresh.stdout

    promote_1 = runner.invoke(
        app,
        [
            "baseline",
            "promote",
            "--root",
            str(baseline_root),
            "--runset",
            runset_id,
            "--baseline-id",
            baseline_id,
            "--label",
            "prod",
        ],
    )
    assert promote_1.exit_code == 0, promote_1.stdout

    promote_2 = runner.invoke(
        app,
        [
            "baseline",
            "promote",
            "--root",
            str(baseline_root),
            "--runset",
            runset_id,
            "--baseline-id",
            baseline_id,
            "--label",
            "prod",
        ],
    )
    assert promote_2.exit_code == 0, promote_2.stdout

    promote_3 = runner.invoke(
        app,
        [
            "baseline",
            "promote",
            "--root",
            str(baseline_root),
            "--runset",
            runset_id,
            "--baseline-id",
            "DIFFERENT_BASELINE_ID",
            "--label",
            "prod",
        ],
    )
    assert promote_3.exit_code != 0
    assert promote_3.exception is not None

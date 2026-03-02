from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset, sweep_to_baseline_root
from research_core.cli import app


def test_risk_drift_fail_without_promotion(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)
    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-risk-drift-fail-no-promo")

    baseline_root = tmp_path / "baselines"
    sweep_to_baseline_root(runner, tmp_path, runset_id, baseline_root)
    refresh = runner.invoke(app, ["baseline", "index", "refresh", "--root", str(baseline_root)])
    assert refresh.exit_code == 0, refresh.stdout

    result = runner.invoke(
        app,
        [
            "risk",
            "drift",
            "--catalog",
            "catalog",
            "--root",
            "baselines",
            "--runset",
            runset_id,
            "--out",
            "drift_out",
        ],
    )
    assert result.exit_code != 0

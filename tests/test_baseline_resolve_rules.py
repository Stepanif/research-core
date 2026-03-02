from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset, sweep_to_baseline_root
from research_core.cli import app


def test_baseline_resolve_rules(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)

    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-baseline-resolve-rules")
    baseline_root = tmp_path / "baselines"
    card_path, baseline_id = sweep_to_baseline_root(runner, tmp_path, runset_id, baseline_root)

    refresh = runner.invoke(app, ["baseline", "index", "refresh", "--root", str(baseline_root)])
    assert refresh.exit_code == 0, refresh.stdout

    missing_label = runner.invoke(
        app,
        ["baseline", "resolve", "--root", str(baseline_root), "--runset", runset_id, "--label", "prod"],
    )
    assert missing_label.exit_code != 0

    promote = runner.invoke(
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
    assert promote.exit_code == 0, promote.stdout

    resolved_with_label = runner.invoke(
        app,
        ["baseline", "resolve", "--root", str(baseline_root), "--runset", runset_id, "--label", "prod"],
    )
    assert resolved_with_label.exit_code == 0, resolved_with_label.stdout
    assert f"baseline_path={card_path.resolve().as_posix()}" in resolved_with_label.stdout
    assert f"baseline_id={baseline_id}" in resolved_with_label.stdout
    assert "label=prod" in resolved_with_label.stdout

    resolved_default = runner.invoke(app, ["baseline", "resolve", "--root", str(baseline_root), "--runset", runset_id])
    assert resolved_default.exit_code == 0, resolved_default.stdout
    assert f"baseline_id={baseline_id}" in resolved_default.stdout

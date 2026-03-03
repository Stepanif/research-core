from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset_at, create_runset, prepare_promoted_baseline_root
from research_core.cli import app


def test_risk_dashboard_fail_fast(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_ok, _run_dir_ok, canon_hash_ok = build_small_run_with_dataset_at(
        runner,
        tmp_path,
        run_dir_name="run_ok",
        raw_root_name="raw_ok",
    )
    dataset_missing, _run_dir_missing, canon_hash_missing = build_small_run_with_dataset_at(
        runner,
        tmp_path,
        run_dir_name="run_missing",
        raw_dataset_id=dataset_ok,
        instrument="NQ",
    )
    runset_ok = create_runset(
        runner,
        tmp_path,
        dataset_ok,
        canon_hash_ok,
        "runset-dashboard-fail-ok",
        run_ref="run_ok",
    )
    runset_missing = create_runset(
        runner,
        tmp_path,
        dataset_missing,
        canon_hash_missing,
        "runset-dashboard-fail-missing",
        run_ref="run_missing",
    )

    baseline_root = tmp_path / "baselines"
    prepare_promoted_baseline_root(runner, tmp_path, runset_ok, baseline_root, label="prod")

    runsets_path = tmp_path / "runsets.json"
    runsets_path.write_text(
        json.dumps({"runset_ids": [runset_missing, runset_ok]}, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        [
            "risk",
            "dashboard",
            "--catalog",
            "catalog",
            "--root",
            "baselines",
            "--runsets",
            str(runsets_path),
            "--out",
            "dashboard_out",
        ],
    )
    assert result.exit_code != 0
    assert not (tmp_path / "dashboard_out" / "dashboard.summary.json").exists()
    assert not (tmp_path / "dashboard_out" / "dashboard.summary.manifest.json").exists()

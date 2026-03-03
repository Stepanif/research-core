from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset_at, create_runset, prepare_promoted_baseline_root
from research_core.cli import app


def test_risk_dashboard_smoke(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_a, _run_dir_a, canon_hash_a = build_small_run_with_dataset_at(
        runner,
        tmp_path,
        run_dir_name="run_a",
        raw_root_name="raw_a",
    )
    dataset_b, _run_dir_b, canon_hash_b = build_small_run_with_dataset_at(
        runner,
        tmp_path,
        run_dir_name="run_b",
        raw_dataset_id=dataset_a,
        instrument="NQ",
    )
    runset_a = create_runset(runner, tmp_path, dataset_a, canon_hash_a, "runset-dashboard-smoke-a", run_ref="run_a")
    runset_b = create_runset(runner, tmp_path, dataset_b, canon_hash_b, "runset-dashboard-smoke-b", run_ref="run_b")

    baseline_root = tmp_path / "baselines"
    prepare_promoted_baseline_root(runner, tmp_path, runset_a, baseline_root, label="prod")
    prepare_promoted_baseline_root(runner, tmp_path, runset_b, baseline_root, label="prod")

    runsets_path = tmp_path / "runsets.json"
    runsets_path.write_text(
        json.dumps({"runset_ids": [runset_b, runset_a]}, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n",
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
    assert result.exit_code == 0, result.stdout

    summary_path = tmp_path / "dashboard_out" / "dashboard.summary.json"
    manifest_path = tmp_path / "dashboard_out" / "dashboard.summary.manifest.json"
    assert summary_path.exists()
    assert manifest_path.exists()

    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    assert summary["dashboard_version"] == "v1"
    assert summary["runset_count"] == 2
    assert [entry["runset_id"] for entry in summary["entries"]] == sorted([runset_a, runset_b])

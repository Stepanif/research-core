from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset, prepare_promoted_baseline_root
from research_core.cli import app


def test_risk_drift_smoke(monkeypatch: object, tmp_path: Path) -> None:
    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)
    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-risk-drift-smoke")

    baseline_root = tmp_path / "baselines"
    prepare_promoted_baseline_root(runner, tmp_path, runset_id, baseline_root, label="prod")

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
    assert result.exit_code == 0, result.stdout

    report_path = tmp_path / "drift_out" / runset_id / "drift.report.json"
    manifest_path = tmp_path / "drift_out" / runset_id / "drift.report.manifest.json"
    assert report_path.exists()
    assert manifest_path.exists()

    report_payload = json.loads(report_path.read_text(encoding="utf-8"))
    assert report_payload["drift_version"] == "v1"
    assert report_payload["drift_classification"]["status"] == "NO_DRIFT"
    assert report_payload["checks"]["per_run_vector_match"] is True

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from typer.testing import CliRunner

import research_core.cli as cli_module
from tests._baseline_helpers import build_small_run_with_dataset, create_runset, prepare_promoted_baseline_root
from research_core.cli import app


def _manifest_canonical_hash(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    data = {key: value for key, value in payload.items() if key != "drift_manifest_canonical_sha256"}
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()


def test_risk_drift_golden_fixture_regression(monkeypatch: object, tmp_path: Path) -> None:
    repo_root = Path(__file__).parent.parent

    monkeypatch.setenv("RESEARCH_CREATED_UTC", "2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(cli_module, "_git_commit_or_unknown", lambda _: "unknown")
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    dataset_id, _run_dir, canon_hash = build_small_run_with_dataset(runner, tmp_path)
    runset_id = create_runset(runner, tmp_path, dataset_id, canon_hash, "runset-risk-drift-golden")

    baseline_root = tmp_path / "baselines"
    prepare_promoted_baseline_root(runner, tmp_path, runset_id, baseline_root, label="prod")

    drift = runner.invoke(
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
    assert drift.exit_code == 0, drift.stdout

    report_path = tmp_path / "drift_out" / runset_id / "drift.report.json"
    manifest_path = tmp_path / "drift_out" / runset_id / "drift.report.manifest.json"

    report_hash = hashlib.sha256(report_path.read_bytes()).hexdigest()
    manifest_hash = _manifest_canonical_hash(manifest_path)

    expected_report_hash = (
        repo_root / "tests" / "golden" / "drift_report_small_sample_v1.report.json.sha256"
    ).read_text(encoding="utf-8").strip()
    expected_manifest_hash = (
        repo_root / "tests" / "golden" / "drift_report_small_sample_v1.manifest.json.sha256"
    ).read_text(encoding="utf-8").strip()

    assert report_hash == expected_report_hash
    assert manifest_hash == expected_manifest_hash

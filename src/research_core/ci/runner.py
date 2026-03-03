from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.baselines.index import refresh_baseline_index
from research_core.ci.config import load_ci_config
from research_core.ci.io import read_json_object
from research_core.ci.writer import write_ci_artifacts
from research_core.risk.dashboard import run_risk_dashboard
from research_core.util.buildmeta import get_created_utc
from research_core.util.types import ValidationError


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="ci run requires RESEARCH_CREATED_UTC")


def run_ci_pipeline(*, config_path: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()
    config = load_ci_config(config_path)

    baseline_root = Path(config["baseline_root"])
    catalog_dir = Path(config["catalog_dir"])
    runsets_path = Path(config["runsets_path"])
    out_dir = Path(config["out_dir"])
    label = str(config["label"])
    fail_on_drift = bool(config["fail_on_drift"])
    fail_on_checksum_mismatch = bool(config["fail_on_checksum_mismatch"])

    refresh_baseline_index(root=baseline_root)
    run_risk_dashboard(
        catalog_dir=catalog_dir,
        baseline_root=baseline_root,
        runsets_path=runsets_path,
        out_dir=out_dir,
        label=label,
    )

    dashboard_summary_path = out_dir / "dashboard.summary.json"
    dashboard_manifest_path = out_dir / "dashboard.summary.manifest.json"
    dashboard_summary_payload = read_json_object(dashboard_summary_path, name="dashboard summary")
    dashboard_manifest_payload = read_json_object(dashboard_manifest_path, name="dashboard manifest")

    artifacts = write_ci_artifacts(
        created_utc=created_utc,
        config_path=config_path,
        runsets_path=runsets_path,
        baseline_root=baseline_root,
        out_dir=out_dir,
        fail_on_drift=fail_on_drift,
        fail_on_checksum_mismatch=fail_on_checksum_mismatch,
        dashboard_summary_path=dashboard_summary_path,
        dashboard_summary_payload=dashboard_summary_payload,
        dashboard_manifest_path=dashboard_manifest_path,
        dashboard_manifest_payload=dashboard_manifest_payload,
    )

    results = artifacts["summary"].get("results")
    if not isinstance(results, dict):
        raise ValidationError("Invalid ci summary results payload")
    status = results.get("status")
    if status not in {"PASS", "FAIL"}:
        raise ValidationError("Invalid ci summary status")
    drift_count = results.get("drift_count")
    checksum_mismatch_count = results.get("checksum_mismatch_count")
    if not isinstance(drift_count, int):
        raise ValidationError("Invalid ci summary drift_count")
    if not isinstance(checksum_mismatch_count, int):
        raise ValidationError("Invalid ci summary checksum_mismatch_count")

    should_fail = False
    if fail_on_drift and drift_count > 0:
        should_fail = True
    if fail_on_checksum_mismatch and checksum_mismatch_count > 0:
        should_fail = True

    return {
        "status": status,
        "should_fail": should_fail,
        "drift_count": drift_count,
        "checksum_mismatch_count": checksum_mismatch_count,
        "summary": artifacts["summary"],
        "manifest": artifacts["manifest"],
        "summary_path": artifacts["summary_path"],
        "manifest_path": artifacts["manifest_path"],
    }

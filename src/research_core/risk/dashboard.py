from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_core.risk.dashboard_writer import write_dashboard_artifacts
from research_core.risk.drift import run_risk_drift
from research_core.util.buildmeta import get_created_utc
from research_core.util.types import ValidationError


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="Risk dashboard requires RESEARCH_CREATED_UTC")


def _load_runset_ids(runsets_path: Path) -> list[str]:
    if not runsets_path.exists() or not runsets_path.is_file():
        raise ValidationError(f"Runsets file does not exist: {runsets_path}")

    try:
        payload = json.loads(runsets_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid runsets JSON: {runsets_path}: {exc}") from exc

    if not isinstance(payload, dict):
        raise ValidationError("Runsets file must be an object with key 'runset_ids'")
    if set(payload.keys()) != {"runset_ids"}:
        raise ValidationError("Runsets file supports only the 'runset_ids' key")

    runset_ids = payload.get("runset_ids")
    if not isinstance(runset_ids, list):
        raise ValidationError("Runsets file field 'runset_ids' must be a JSON array")

    normalized: list[str] = []
    seen: set[str] = set()
    for index, value in enumerate(runset_ids):
        if not isinstance(value, str) or not value:
            raise ValidationError(f"runset_ids[{index}] must be a non-empty string")
        if value in seen:
            raise ValidationError(f"Duplicate runset id in runsets file: {value}")
        seen.add(value)
        normalized.append(value)

    return sorted(normalized)


def run_risk_dashboard(
    *,
    catalog_dir: Path,
    baseline_root: Path,
    runsets_path: Path,
    out_dir: Path,
    label: str = "prod",
) -> dict[str, Any]:
    if not isinstance(label, str) or not label:
        raise ValidationError("Risk dashboard requires a non-empty label")

    created_utc = _require_created_utc()
    runset_ids = _load_runset_ids(runsets_path)

    out_dir.mkdir(parents=True, exist_ok=True)
    drift_out = out_dir / "drift"

    runset_drift_artifacts: list[dict[str, Any]] = []
    for runset_id in runset_ids:
        result = run_risk_drift(
            catalog_dir=catalog_dir,
            baseline_root=baseline_root,
            runset_id=runset_id,
            label=label,
            out_dir=drift_out,
        )
        drift = result["drift"]
        runset_drift_artifacts.append(
            {
                "runset_id": runset_id,
                "report_path": Path(drift["report_path"]),
                "manifest_path": Path(drift["manifest_path"]),
            }
        )

    dashboard = write_dashboard_artifacts(
        created_utc=created_utc,
        label=label,
        runsets_path=runsets_path,
        runset_drift_artifacts=runset_drift_artifacts,
        out_dir=out_dir,
    )

    return {
        "runset_count": len(runset_ids),
        "summary_path": dashboard["summary_path"],
        "manifest_path": dashboard["manifest_path"],
    }

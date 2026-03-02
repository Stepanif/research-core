from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.baselines.resolve import resolve_baseline
from research_core.risk.diff_writer import write_baseline_diff_artifacts
from research_core.risk.drift_writer import write_drift_artifacts
from research_core.risk.sweep import run_risk_sweep
from research_core.util.buildmeta import get_created_utc
from research_core.util.types import ValidationError


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="Risk drift requires RESEARCH_CREATED_UTC")


def run_risk_drift(
    *,
    catalog_dir: Path,
    baseline_root: Path,
    runset_id: str,
    label: str = "prod",
    out_dir: Path,
) -> dict[str, Any]:
    if not isinstance(label, str) or not label:
        raise ValidationError("Risk drift requires a non-empty label")

    created_utc = _require_created_utc()

    drift_root = out_dir / runset_id
    current_out = drift_root / "current"
    diff_out = drift_root / "diff"

    sweep_result = run_risk_sweep(catalog_dir=catalog_dir, runset_id=runset_id, out_dir=current_out)
    current_card_path = Path(sweep_result["baseline_card_path"])
    current_manifest_path = Path(sweep_result["baseline_card_manifest_path"])

    resolved_reference = resolve_baseline(root=baseline_root, runset_id=runset_id, label=label)
    reference_card_path = Path(resolved_reference["card_path"])
    reference_manifest_path = reference_card_path.with_name("baseline.card.manifest.json")
    if not reference_manifest_path.exists() or not reference_manifest_path.is_file():
        raise ValidationError(f"Missing reference baseline manifest: {reference_manifest_path}")

    diff_result = write_baseline_diff_artifacts(a_path=reference_card_path, b_path=current_card_path, out_dir=diff_out)
    diff_path = Path(diff_result["diff_path"])
    diff_manifest_path = Path(diff_result["manifest_path"])

    runset_entry_path = catalog_dir / "runsets" / "entries" / f"{runset_id}.json"
    dataset_index_path = catalog_dir / "links" / "dataset_to_runs.index.json"
    if not runset_entry_path.exists() or not runset_entry_path.is_file():
        raise ValidationError(f"Missing runset entry for risk drift: {runset_entry_path}")
    if not dataset_index_path.exists() or not dataset_index_path.is_file():
        raise ValidationError(f"Missing dataset_to_runs index for risk drift: {dataset_index_path}")

    drift_root.mkdir(parents=True, exist_ok=True)
    drift_result = write_drift_artifacts(
        created_utc=created_utc,
        runset_id=runset_id,
        label=label,
        baseline_root=baseline_root,
        runset_entry_path=runset_entry_path,
        dataset_to_runs_index_path=dataset_index_path,
        reference_card_path=reference_card_path,
        reference_manifest_path=reference_manifest_path,
        current_card_path=current_card_path,
        current_manifest_path=current_manifest_path,
        diff_path=diff_path,
        diff_manifest_path=diff_manifest_path,
        out_dir=drift_root,
    )

    return {
        "current": sweep_result,
        "diff": diff_result,
        "drift": drift_result,
    }
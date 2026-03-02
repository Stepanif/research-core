from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.risk.contracts import (
    DRIFT_MANIFEST_VERSION,
    DRIFT_REPORT_VERSION,
    DRIFT_STATUS_JACCARD_THRESHOLD,
    DRIFT_STATUS_MEAN_DELTA_ABS_THRESHOLD,
)
from research_core.runsets.io import canonical_hash, canonical_json_bytes, read_json, write_canonical_json
from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.types import ValidationError


def _read_json_object(path: Path, name: str) -> dict[str, Any]:
    if not path.exists() or not path.is_file():
        raise ValidationError(f"Missing required file for {name}: {path}")
    payload = read_json(path)
    if not isinstance(payload, dict):
        raise ValidationError(f"Invalid JSON object payload for {name}: {path}")
    return payload


def _baseline_info(card_path: Path, name: str) -> dict[str, str]:
    payload = _read_json_object(card_path, name)
    if payload.get("card_version") != "v1":
        raise ValidationError(f"Unsupported baseline card version for {name}")

    checksums = payload.get("checksums")
    if not isinstance(checksums, dict):
        raise ValidationError(f"Missing checksums in baseline card for {name}")
    baseline_id = checksums.get("per_run_vector_sha256")
    if not isinstance(baseline_id, str) or not baseline_id:
        raise ValidationError(f"Missing checksums.per_run_vector_sha256 in baseline card for {name}")

    expected_hash = payload.get("baseline_card_canonical_sha256")
    if not isinstance(expected_hash, str) or not expected_hash:
        raise ValidationError(f"Missing baseline_card_canonical_sha256 in baseline card for {name}")
    actual_hash = canonical_hash(payload, self_field="baseline_card_canonical_sha256")
    if expected_hash != actual_hash:
        raise ValidationError(f"Baseline card canonical hash mismatch for {name}")

    return {
        "baseline_id": baseline_id,
        "baseline_card_canonical_sha256": expected_hash,
    }


def _diff_projection(diff_path: Path) -> dict[str, Any]:
    payload = _read_json_object(diff_path, "diff")

    diff_hash = payload.get("baseline_diff_canonical_sha256")
    if not isinstance(diff_hash, str) or not diff_hash:
        raise ValidationError("Missing baseline_diff_canonical_sha256 in baseline diff")
    actual_diff_hash = canonical_hash(payload, self_field="baseline_diff_canonical_sha256")
    if actual_diff_hash != diff_hash:
        raise ValidationError("Baseline diff canonical hash mismatch")

    deltas = payload.get("deltas")
    if not isinstance(deltas, dict):
        raise ValidationError("Missing deltas in baseline diff")
    instability_mean_delta = deltas.get("instability_mean_delta")
    if not isinstance(instability_mean_delta, (int, float)):
        raise ValidationError("Missing numeric deltas.instability_mean_delta in baseline diff")

    overlap = payload.get("worst5_overlap")
    if not isinstance(overlap, dict):
        raise ValidationError("Missing worst5_overlap in baseline diff")
    worst5_jaccard = overlap.get("jaccard")
    if not isinstance(worst5_jaccard, (int, float)):
        raise ValidationError("Missing numeric worst5_overlap.jaccard in baseline diff")

    checksum = payload.get("checksum")
    if not isinstance(checksum, dict):
        raise ValidationError("Missing checksum in baseline diff")
    per_run_vector_match = checksum.get("per_run_vector_match")
    if not isinstance(per_run_vector_match, bool):
        raise ValidationError("Missing boolean checksum.per_run_vector_match in baseline diff")

    classification = payload.get("classification")
    if not isinstance(classification, dict):
        raise ValidationError("Missing classification in baseline diff")
    classification_label = classification.get("label")
    if not isinstance(classification_label, str) or not classification_label:
        raise ValidationError("Missing classification.label in baseline diff")

    return {
        "diff_canonical_sha256": diff_hash,
        "classification_label": classification_label,
        "instability_mean_delta": float(instability_mean_delta),
        "worst5_jaccard": float(worst5_jaccard),
        "per_run_vector_match": per_run_vector_match,
    }


def _drift_classification(*, instability_mean_delta: float, worst5_jaccard: float) -> dict[str, str]:
    if abs(instability_mean_delta) >= DRIFT_STATUS_MEAN_DELTA_ABS_THRESHOLD or worst5_jaccard <= DRIFT_STATUS_JACCARD_THRESHOLD:
        if abs(instability_mean_delta) >= DRIFT_STATUS_MEAN_DELTA_ABS_THRESHOLD and worst5_jaccard <= DRIFT_STATUS_JACCARD_THRESHOLD:
            rationale = "instability_mean_delta>=5.0 and worst5_jaccard<=0.40"
        elif abs(instability_mean_delta) >= DRIFT_STATUS_MEAN_DELTA_ABS_THRESHOLD:
            rationale = "instability_mean_delta>=5.0"
        else:
            rationale = "worst5_jaccard<=0.40"
        return {
            "status": "DRIFT",
            "rationale": rationale,
        }

    return {
        "status": "NO_DRIFT",
        "rationale": "below fixed drift thresholds",
    }


def write_drift_artifacts(
    *,
    created_utc: str,
    runset_id: str,
    label: str,
    baseline_root: Path,
    runset_entry_path: Path,
    dataset_to_runs_index_path: Path,
    reference_card_path: Path,
    reference_manifest_path: Path,
    current_card_path: Path,
    current_manifest_path: Path,
    diff_path: Path,
    diff_manifest_path: Path,
    out_dir: Path,
) -> dict[str, Any]:
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError("Risk drift requires created_utc")

    if not out_dir.exists() or not out_dir.is_dir():
        raise ValidationError(f"Risk drift output directory does not exist: {out_dir}")

    reference_info = _baseline_info(reference_card_path, "reference")
    current_info = _baseline_info(current_card_path, "current")
    diff_info = _diff_projection(diff_path)

    report_payload: dict[str, Any] = {
        "drift_version": DRIFT_REPORT_VERSION,
        "created_utc": created_utc,
        "runset_id": runset_id,
        "label": label,
        "reference": {
            "baseline_root": baseline_root.as_posix(),
            "baseline_path": reference_card_path.resolve().relative_to(baseline_root.resolve()).as_posix(),
            "baseline_id": reference_info["baseline_id"],
            "baseline_card_canonical_sha256": reference_info["baseline_card_canonical_sha256"],
        },
        "current": {
            "baseline_path": current_card_path.resolve().relative_to(out_dir.resolve()).as_posix(),
            "baseline_id": current_info["baseline_id"],
            "baseline_card_canonical_sha256": current_info["baseline_card_canonical_sha256"],
        },
        "diff": {
            "diff_path": diff_path.resolve().relative_to(out_dir.resolve()).as_posix(),
            "diff_canonical_sha256": diff_info["diff_canonical_sha256"],
            "classification_label": diff_info["classification_label"],
            "instability_mean_delta": diff_info["instability_mean_delta"],
            "worst5_jaccard": diff_info["worst5_jaccard"],
        },
        "checks": {
            "per_run_vector_match": diff_info["per_run_vector_match"],
        },
    }

    report_payload["drift_classification"] = _drift_classification(
        instability_mean_delta=report_payload["diff"]["instability_mean_delta"],
        worst5_jaccard=report_payload["diff"]["worst5_jaccard"],
    )
    report_payload["drift_report_canonical_sha256"] = canonical_hash(
        report_payload,
        self_field="drift_report_canonical_sha256",
    )

    report_bytes = canonical_json_bytes(report_payload)

    manifest_payload: dict[str, Any] = {
        "manifest_version": DRIFT_MANIFEST_VERSION,
        "created_utc": created_utc,
        "inputs": sorted(
            [
                {
                    "path": "catalog/runsets/entries/{runset_id}.json".format(runset_id=runset_id),
                    "sha256": sha256_file(runset_entry_path),
                    "bytes": int(runset_entry_path.stat().st_size),
                },
                {
                    "path": "catalog/links/dataset_to_runs.index.json",
                    "sha256": sha256_file(dataset_to_runs_index_path),
                    "bytes": int(dataset_to_runs_index_path.stat().st_size),
                },
                {
                    "path": "reference/baseline.card.json",
                    "sha256": sha256_file(reference_card_path),
                    "bytes": int(reference_card_path.stat().st_size),
                },
                {
                    "path": "reference/baseline.card.manifest.json",
                    "sha256": sha256_file(reference_manifest_path),
                    "bytes": int(reference_manifest_path.stat().st_size),
                },
                {
                    "path": current_card_path.resolve().relative_to(out_dir.resolve()).as_posix(),
                    "sha256": sha256_file(current_card_path),
                    "bytes": int(current_card_path.stat().st_size),
                },
                {
                    "path": current_manifest_path.resolve().relative_to(out_dir.resolve()).as_posix(),
                    "sha256": sha256_file(current_manifest_path),
                    "bytes": int(current_manifest_path.stat().st_size),
                },
                {
                    "path": diff_path.resolve().relative_to(out_dir.resolve()).as_posix(),
                    "sha256": sha256_file(diff_path),
                    "bytes": int(diff_path.stat().st_size),
                },
                {
                    "path": diff_manifest_path.resolve().relative_to(out_dir.resolve()).as_posix(),
                    "sha256": sha256_file(diff_manifest_path),
                    "bytes": int(diff_manifest_path.stat().st_size),
                },
            ],
            key=lambda item: str(item["path"]),
        ),
        "outputs": {
            "drift.report.json": {
                "sha256": sha256_bytes(report_bytes),
                "bytes": len(report_bytes),
            }
        },
    }
    manifest_payload["drift_manifest_canonical_sha256"] = canonical_hash(
        manifest_payload,
        self_field="drift_manifest_canonical_sha256",
    )

    report_path = out_dir / "drift.report.json"
    manifest_path = out_dir / "drift.report.manifest.json"
    report_tmp = out_dir / "drift.report.json.tmp"
    manifest_tmp = out_dir / "drift.report.manifest.json.tmp"

    report_tmp.write_bytes(report_bytes)
    write_canonical_json(manifest_tmp, manifest_payload)
    report_tmp.replace(report_path)
    manifest_tmp.replace(manifest_path)

    return {
        "report": report_payload,
        "manifest": manifest_payload,
        "report_path": report_path,
        "manifest_path": manifest_path,
    }
from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.risk.contracts import DASHBOARD_MANIFEST_VERSION, DASHBOARD_VERSION
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


def _require_str(payload: dict[str, Any], field: str, context: str) -> str:
    value = payload.get(field)
    if not isinstance(value, str) or not value:
        raise ValidationError(f"Missing {field} in {context}")
    return value


def _require_number(payload: dict[str, Any], field: str, context: str) -> float:
    value = payload.get(field)
    if not isinstance(value, (int, float)):
        raise ValidationError(f"Missing numeric {field} in {context}")
    return float(value)


def _require_bool(payload: dict[str, Any], field: str, context: str) -> bool:
    value = payload.get(field)
    if not isinstance(value, bool):
        raise ValidationError(f"Missing boolean {field} in {context}")
    return value


def _project_dashboard_entry(*, runset_id: str, report_path: Path, manifest_path: Path) -> dict[str, Any]:
    report = _read_json_object(report_path, f"drift report for {runset_id}")
    if report.get("drift_version") != "v1":
        raise ValidationError(f"Unsupported drift version in report for {runset_id}")

    reference = report.get("reference")
    if not isinstance(reference, dict):
        raise ValidationError(f"Missing reference section in drift report for {runset_id}")
    current = report.get("current")
    if not isinstance(current, dict):
        raise ValidationError(f"Missing current section in drift report for {runset_id}")
    diff = report.get("diff")
    if not isinstance(diff, dict):
        raise ValidationError(f"Missing diff section in drift report for {runset_id}")
    checks = report.get("checks")
    if not isinstance(checks, dict):
        raise ValidationError(f"Missing checks section in drift report for {runset_id}")
    drift_classification = report.get("drift_classification")
    if not isinstance(drift_classification, dict):
        raise ValidationError(f"Missing drift_classification section in drift report for {runset_id}")

    status = _require_str(drift_classification, "status", f"drift report for {runset_id}")
    if status not in {"DRIFT", "NO_DRIFT"}:
        raise ValidationError(f"Invalid drift status in drift report for {runset_id}: {status}")

    manifest = _read_json_object(manifest_path, f"drift manifest for {runset_id}")
    expected_manifest_hash = _require_str(
        manifest,
        "drift_manifest_canonical_sha256",
        f"drift manifest for {runset_id}",
    )
    actual_manifest_hash = canonical_hash(manifest, self_field="drift_manifest_canonical_sha256")
    if expected_manifest_hash != actual_manifest_hash:
        raise ValidationError(f"Drift manifest canonical hash mismatch for {runset_id}")

    return {
        "runset_id": runset_id,
        "status": status,
        "instability_mean_delta": _require_number(diff, "instability_mean_delta", f"drift report for {runset_id}"),
        "worst5_jaccard": _require_number(diff, "worst5_jaccard", f"drift report for {runset_id}"),
        "per_run_vector_match": _require_bool(checks, "per_run_vector_match", f"drift report for {runset_id}"),
        "reference_baseline_id": _require_str(reference, "baseline_id", f"drift report for {runset_id}"),
        "current_baseline_id": _require_str(current, "baseline_id", f"drift report for {runset_id}"),
        "diff_classification_label": _require_str(diff, "classification_label", f"drift report for {runset_id}"),
        "drift_report_sha256": sha256_file(report_path),
        "drift_manifest_canonical_sha256": expected_manifest_hash,
    }


def write_dashboard_artifacts(
    *,
    created_utc: str,
    label: str,
    runsets_path: Path,
    runset_drift_artifacts: list[dict[str, Any]],
    out_dir: Path,
) -> dict[str, Any]:
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError("Risk dashboard requires created_utc")
    if not isinstance(label, str) or not label:
        raise ValidationError("Risk dashboard requires non-empty label")
    if not out_dir.exists() or not out_dir.is_dir():
        raise ValidationError(f"Risk dashboard output directory does not exist: {out_dir}")
    if not runsets_path.exists() or not runsets_path.is_file():
        raise ValidationError(f"Missing runsets file: {runsets_path}")

    entries: list[dict[str, Any]] = []
    for item in runset_drift_artifacts:
        runset_id = item.get("runset_id")
        report_path = item.get("report_path")
        manifest_path = item.get("manifest_path")
        if not isinstance(runset_id, str) or not runset_id:
            raise ValidationError("Invalid runset_id in dashboard drift artifacts")
        if not isinstance(report_path, Path):
            raise ValidationError(f"Invalid report_path type for runset {runset_id}")
        if not isinstance(manifest_path, Path):
            raise ValidationError(f"Invalid manifest_path type for runset {runset_id}")
        entries.append(_project_dashboard_entry(runset_id=runset_id, report_path=report_path, manifest_path=manifest_path))

    entries_sorted = sorted(entries, key=lambda item: str(item["runset_id"]))
    counts = {
        "DRIFT": sum(1 for item in entries_sorted if item["status"] == "DRIFT"),
        "NO_DRIFT": sum(1 for item in entries_sorted if item["status"] == "NO_DRIFT"),
    }
    checksum_mismatch_count = sum(1 for item in entries_sorted if not item["per_run_vector_match"])

    top_abs_instability_delta_5 = [
        {
            "runset_id": item["runset_id"],
            "instability_mean_delta": item["instability_mean_delta"],
        }
        for item in sorted(
            entries_sorted,
            key=lambda item: (-abs(float(item["instability_mean_delta"])), str(item["runset_id"])),
        )[:5]
    ]

    lowest_jaccard_5 = [
        {
            "runset_id": item["runset_id"],
            "worst5_jaccard": item["worst5_jaccard"],
        }
        for item in sorted(
            entries_sorted,
            key=lambda item: (float(item["worst5_jaccard"]), str(item["runset_id"])),
        )[:5]
    ]

    summary_payload: dict[str, Any] = {
        "dashboard_version": DASHBOARD_VERSION,
        "created_utc": created_utc,
        "label": label,
        "runset_count": len(entries_sorted),
        "entries": entries_sorted,
        "aggregates": {
            "counts": counts,
            "checksum_mismatch_count": checksum_mismatch_count,
            "top_abs_instability_delta_5": top_abs_instability_delta_5,
            "lowest_jaccard_5": lowest_jaccard_5,
        },
    }
    summary_payload["dashboard_canonical_sha256"] = canonical_hash(
        summary_payload,
        self_field="dashboard_canonical_sha256",
    )
    summary_bytes = canonical_json_bytes(summary_payload)

    inputs = [
        {
            "path": runsets_path.name,
            "sha256": sha256_file(runsets_path),
            "bytes": int(runsets_path.stat().st_size),
        }
    ]
    for item in sorted(runset_drift_artifacts, key=lambda value: str(value["runset_id"])):
        runset_id = str(item["runset_id"])
        report_path = item["report_path"]
        manifest_path = item["manifest_path"]
        if not isinstance(report_path, Path) or not isinstance(manifest_path, Path):
            raise ValidationError(f"Invalid drift artifact paths for runset {runset_id}")
        inputs.append(
            {
                "path": report_path.resolve().relative_to(out_dir.resolve()).as_posix(),
                "sha256": sha256_file(report_path),
                "bytes": int(report_path.stat().st_size),
            }
        )
        inputs.append(
            {
                "path": manifest_path.resolve().relative_to(out_dir.resolve()).as_posix(),
                "sha256": sha256_file(manifest_path),
                "bytes": int(manifest_path.stat().st_size),
            }
        )

    manifest_payload: dict[str, Any] = {
        "manifest_version": DASHBOARD_MANIFEST_VERSION,
        "created_utc": created_utc,
        "inputs": sorted(inputs, key=lambda item: str(item["path"])),
        "outputs": {
            "dashboard.summary.json": {
                "sha256": sha256_bytes(summary_bytes),
                "bytes": len(summary_bytes),
            }
        },
    }
    manifest_payload["dashboard_manifest_canonical_sha256"] = canonical_hash(
        manifest_payload,
        self_field="dashboard_manifest_canonical_sha256",
    )

    summary_path = out_dir / "dashboard.summary.json"
    manifest_path = out_dir / "dashboard.summary.manifest.json"
    summary_tmp = out_dir / "dashboard.summary.json.tmp"
    manifest_tmp = out_dir / "dashboard.summary.manifest.json.tmp"

    summary_tmp.write_bytes(summary_bytes)
    write_canonical_json(manifest_tmp, manifest_payload)
    summary_tmp.replace(summary_path)
    manifest_tmp.replace(manifest_path)

    return {
        "summary": summary_payload,
        "manifest": manifest_payload,
        "summary_path": summary_path,
        "manifest_path": manifest_path,
    }

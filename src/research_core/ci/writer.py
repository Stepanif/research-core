from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.baselines.contracts import BASELINE_INDEX_FILE
from research_core.ci.contracts import CI_SUMMARY_MANIFEST_VERSION, CI_SUMMARY_VERSION
from research_core.runsets.io import canonical_hash, canonical_json_bytes, read_json, write_canonical_json
from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.types import ValidationError


def write_ci_artifacts(
    *,
    created_utc: str,
    config_path: Path,
    runsets_path: Path,
    baseline_root: Path,
    out_dir: Path,
    fail_on_drift: bool,
    fail_on_checksum_mismatch: bool,
    dashboard_summary_path: Path,
    dashboard_summary_payload: dict[str, Any],
    dashboard_manifest_path: Path,
    dashboard_manifest_payload: dict[str, Any],
) -> dict[str, Any]:
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError("ci summary requires created_utc")

    baseline_index_path = baseline_root / BASELINE_INDEX_FILE
    if not baseline_index_path.exists() or not baseline_index_path.is_file():
        raise ValidationError(f"Missing baseline index: {baseline_index_path}")
    baseline_index_payload = read_json(baseline_index_path)
    if not isinstance(baseline_index_payload, dict):
        raise ValidationError(f"Invalid baseline index payload: {baseline_index_path}")

    dashboard_outputs = dashboard_summary_payload.get("aggregates")
    if not isinstance(dashboard_outputs, dict):
        raise ValidationError("Invalid dashboard summary payload: missing aggregates")
    counts = dashboard_outputs.get("counts")
    if not isinstance(counts, dict):
        raise ValidationError("Invalid dashboard summary payload: missing aggregates.counts")

    drift_count_raw = counts.get("DRIFT")
    if not isinstance(drift_count_raw, int):
        raise ValidationError("Invalid dashboard summary payload: counts.DRIFT must be int")
    checksum_mismatch_raw = dashboard_outputs.get("checksum_mismatch_count")
    if not isinstance(checksum_mismatch_raw, int):
        raise ValidationError("Invalid dashboard summary payload: checksum_mismatch_count must be int")

    dashboard_manifest_canonical = dashboard_manifest_payload.get("dashboard_manifest_canonical_sha256")
    if not isinstance(dashboard_manifest_canonical, str) or not dashboard_manifest_canonical:
        raise ValidationError("Invalid dashboard manifest payload: missing dashboard_manifest_canonical_sha256")

    ci_status = "PASS"
    if drift_count_raw > 0:
        ci_status = "FAIL"
    if checksum_mismatch_raw > 0 and fail_on_checksum_mismatch:
        ci_status = "FAIL"

    summary_payload: dict[str, Any] = {
        "ci_summary_version": CI_SUMMARY_VERSION,
        "created_utc": created_utc,
        "inputs": {
            "config_sha256": sha256_file(config_path),
            "runsets_sha256": sha256_file(runsets_path),
            "baseline_index_canonical_sha256": canonical_hash(baseline_index_payload),
        },
        "outputs": {
            "dashboard_summary_sha256": sha256_file(dashboard_summary_path),
            "dashboard_manifest_canonical_sha256": dashboard_manifest_canonical,
        },
        "results": {
            "status": ci_status,
            "drift_count": drift_count_raw,
            "checksum_mismatch_count": checksum_mismatch_raw,
            "fail_on_drift": fail_on_drift,
            "fail_on_checksum_mismatch": fail_on_checksum_mismatch,
        },
        "pointers": {
            "dashboard_dir": out_dir.as_posix(),
        },
    }
    summary_payload["ci_summary_canonical_sha256"] = canonical_hash(
        summary_payload,
        self_field="ci_summary_canonical_sha256",
    )
    summary_bytes = canonical_json_bytes(summary_payload)

    manifest_payload: dict[str, Any] = {
        "manifest_version": CI_SUMMARY_MANIFEST_VERSION,
        "created_utc": created_utc,
        "inputs": sorted(
            [
                {
                    "path": "ci.config.json",
                    "sha256": sha256_file(config_path),
                    "bytes": int(config_path.stat().st_size),
                },
                {
                    "path": runsets_path.name,
                    "sha256": sha256_file(runsets_path),
                    "bytes": int(runsets_path.stat().st_size),
                },
                {
                    "path": f"baseline/{BASELINE_INDEX_FILE}",
                    "sha256": sha256_file(baseline_index_path),
                    "bytes": int(baseline_index_path.stat().st_size),
                },
                {
                    "path": dashboard_summary_path.resolve().relative_to(out_dir.resolve()).as_posix(),
                    "sha256": sha256_file(dashboard_summary_path),
                    "bytes": int(dashboard_summary_path.stat().st_size),
                },
                {
                    "path": dashboard_manifest_path.resolve().relative_to(out_dir.resolve()).as_posix(),
                    "sha256": sha256_file(dashboard_manifest_path),
                    "bytes": int(dashboard_manifest_path.stat().st_size),
                },
            ],
            key=lambda item: str(item["path"]),
        ),
        "outputs": {
            "ci.summary.json": {
                "sha256": sha256_bytes(summary_bytes),
                "bytes": len(summary_bytes),
            }
        },
    }
    manifest_payload["ci_manifest_canonical_sha256"] = canonical_hash(
        manifest_payload,
        self_field="ci_manifest_canonical_sha256",
    )

    summary_path = out_dir / "ci.summary.json"
    manifest_path = out_dir / "ci.summary.manifest.json"
    summary_tmp = out_dir / "ci.summary.json.tmp"
    manifest_tmp = out_dir / "ci.summary.manifest.json.tmp"
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

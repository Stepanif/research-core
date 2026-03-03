from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.ci_doctor.contracts import CI_DOCTOR_MANIFEST_VERSION, CI_DOCTOR_SUMMARY_VERSION
from research_core.runsets.io import canonical_hash, canonical_json_bytes, write_canonical_json
from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.types import ValidationError


def write_ci_doctor_artifacts(
    *,
    created_utc: str,
    config_path: Path,
    runsets_path: Path,
    out_dir: Path,
    label: str,
    runset_count: int,
    checks: dict[str, Any],
    status: str,
    failures: list[dict[str, Any]],
    catalog_dir: Path,
    baseline_root: Path,
    input_paths: list[Path],
) -> dict[str, Any]:
    if status not in {"PASS", "FAIL"}:
        raise ValidationError(f"Invalid ci doctor status: {status}")

    summary_payload: dict[str, Any] = {
        "ci_doctor_version": CI_DOCTOR_SUMMARY_VERSION,
        "created_utc": created_utc,
        "label": label,
        "runset_count": runset_count,
        "results": {
            "status": status,
            "failures": failures,
        },
        "checks": checks,
        "pointers": {
            "baseline_root": baseline_root.as_posix(),
            "catalog_dir": catalog_dir.as_posix(),
        },
    }
    summary_payload["ci_doctor_canonical_sha256"] = canonical_hash(
        summary_payload,
        self_field="ci_doctor_canonical_sha256",
    )
    summary_bytes = canonical_json_bytes(summary_payload)

    inputs = [
        {
            "path": "doctor.json",
            "sha256": sha256_file(config_path),
            "bytes": int(config_path.stat().st_size),
        },
        {
            "path": runsets_path.name,
            "sha256": sha256_file(runsets_path),
            "bytes": int(runsets_path.stat().st_size),
        },
    ]
    manifest_payload: dict[str, Any] = {
        "manifest_version": CI_DOCTOR_MANIFEST_VERSION,
        "created_utc": created_utc,
        "inputs": sorted(inputs, key=lambda item: str(item["path"])),
        "outputs": {
            "ci.doctor.summary.json": {
                "sha256": sha256_bytes(summary_bytes),
                "bytes": len(summary_bytes),
            }
        },
    }
    manifest_payload["ci_doctor_manifest_canonical_sha256"] = canonical_hash(
        manifest_payload,
        self_field="ci_doctor_manifest_canonical_sha256",
    )

    out_dir.mkdir(parents=True, exist_ok=True)
    summary_path = out_dir / "ci.doctor.summary.json"
    manifest_path = out_dir / "ci.doctor.summary.manifest.json"
    summary_tmp = out_dir / "ci.doctor.summary.json.tmp"
    manifest_tmp = out_dir / "ci.doctor.summary.manifest.json.tmp"

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

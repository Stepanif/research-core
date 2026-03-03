from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

from research_core.pilot.contracts import (
    PILOT_MANIFEST_HASH_FIELD,
    PILOT_SUMMARY_FILE,
    PILOT_SUMMARY_HASH_FIELD,
    PILOT_SUMMARY_MANIFEST_FILE,
    PILOT_RUN_VERSION,
)
from research_core.runsets.io import canonical_hash, canonical_json_bytes, write_canonical_json
from research_core.util.hashing import sha256_bytes, sha256_file


def _stable_hash(payload: dict[str, Any]) -> str:
    data = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    import hashlib

    return hashlib.sha256(data).hexdigest()


def _summary_hash(summary_payload: dict[str, Any]) -> str:
    clone = dict(summary_payload)
    checksums = clone.get("checksums")
    if isinstance(checksums, dict):
        checksums_clone = dict(cast(dict[str, Any], checksums))
        checksums_clone.pop(PILOT_SUMMARY_HASH_FIELD, None)
        clone["checksums"] = checksums_clone
    return _stable_hash(clone)


def build_pilot_summary(
    *,
    created_utc: str,
    label: str,
    runset_id: str,
    baseline_id: str,
    baseline_card_path: str,
    drift_report_path: str,
    doctor_summary_path: str,
    failures: list[dict[str, str]],
    generated_runset_spec_canonical_sha256: str,
) -> dict[str, Any]:
    status = "PASS" if not failures else "FAIL"
    ordered_failures = sorted(
        failures,
        key=lambda item: (str(item.get("stage", "")), str(item.get("detail", ""))),
    )

    summary: dict[str, Any] = {
        "pilot_run_version": PILOT_RUN_VERSION,
        "created_utc": created_utc,
        "label": label,
        "runset_id": runset_id,
        "baseline_id": baseline_id,
        "artifacts": {
            "baseline_card_path": baseline_card_path,
            "drift_report_path": drift_report_path,
            "doctor_summary_path": doctor_summary_path,
        },
        "results": {
            "status": status,
            "failures": ordered_failures,
        },
        "checksums": {
            "generated_runset_spec_canonical_sha256": generated_runset_spec_canonical_sha256,
            PILOT_SUMMARY_HASH_FIELD: "",
        },
    }
    summary["checksums"][PILOT_SUMMARY_HASH_FIELD] = _summary_hash(summary)
    return summary


def _manifest_input_rows(inputs: list[Path], output_root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    root_resolved = output_root.resolve()
    parent_resolved = root_resolved.parent

    for path in sorted(set(path.resolve() for path in inputs if path.exists() and path.is_file()), key=lambda item: item.as_posix()):
        if path.is_relative_to(root_resolved):
            rel = path.relative_to(root_resolved).as_posix()
        elif path.is_relative_to(parent_resolved):
            rel = path.relative_to(parent_resolved).as_posix()
        else:
            rel = path.as_posix()
        rows.append(
            {
                "path": rel,
                "sha256": sha256_file(path),
                "bytes": int(path.stat().st_size),
            }
        )
    return rows


def build_pilot_manifest(*, created_utc: str, output_root: Path, inputs: list[Path], summary_bytes: bytes) -> dict[str, Any]:
    manifest: dict[str, Any] = {
        "manifest_version": "v1",
        "created_utc": created_utc,
        "inputs": _manifest_input_rows(inputs, output_root=output_root),
        "outputs": {
            PILOT_SUMMARY_FILE: {
                "sha256": sha256_bytes(summary_bytes),
                "bytes": len(summary_bytes),
            }
        },
    }
    manifest[PILOT_MANIFEST_HASH_FIELD] = canonical_hash(manifest, self_field=PILOT_MANIFEST_HASH_FIELD)
    return manifest


def write_pilot_artifacts(*, out_dir: Path, summary_payload: dict[str, Any], manifest_inputs: list[Path]) -> dict[str, Path | dict[str, Any]]:
    summary_bytes = canonical_json_bytes(summary_payload)
    manifest_payload = build_pilot_manifest(
        created_utc=str(summary_payload["created_utc"]),
        output_root=out_dir,
        inputs=manifest_inputs,
        summary_bytes=summary_bytes,
    )

    out_dir.mkdir(parents=True, exist_ok=True)
    summary_path = out_dir / PILOT_SUMMARY_FILE
    manifest_path = out_dir / PILOT_SUMMARY_MANIFEST_FILE
    summary_tmp = out_dir / f"{PILOT_SUMMARY_FILE}.tmp"
    manifest_tmp = out_dir / f"{PILOT_SUMMARY_MANIFEST_FILE}.tmp"

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

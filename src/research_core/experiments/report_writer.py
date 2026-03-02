from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from research_core.util.hashing import sha256_bytes, sha256_file, sha256_json
from research_core.util.types import ValidationError


def report_bytes(report_payload: dict[str, Any]) -> bytes:
    return (json.dumps(report_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def _manifest_hash_without_self(payload: dict[str, Any]) -> str:
    return sha256_json({key: value for key, value in payload.items() if key != "report_manifest_canonical_sha256"})


def build_report_manifest(
    run_dir: Path,
    report_payload: dict[str, Any],
) -> dict[str, Any]:
    created_utc = os.environ.get("RESEARCH_CREATED_UTC")
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError("Experiment report manifest requires RESEARCH_CREATED_UTC for deterministic created_utc")

    experiments_root = run_dir / "experiments"
    input_paths: list[tuple[str, Path]] = []

    index_path = experiments_root / "experiments.index.json"
    input_paths.append(("experiments.index.json", index_path))

    promotions_path = experiments_root / "promotions.json"
    if promotions_path.exists():
        input_paths.append(("promotions.json", promotions_path))

    experiments = report_payload.get("index_snapshot", {}).get("experiments", [])
    if not isinstance(experiments, list):
        raise ValidationError("Invalid report payload index_snapshot.experiments for report manifest")
    for entry in experiments:
        if not isinstance(entry, dict):
            raise ValidationError("Invalid experiment entry in report payload")
        exp_id = entry.get("exp_id")
        if not isinstance(exp_id, str) or not exp_id:
            raise ValidationError("Invalid exp_id in report payload entry")
        manifest_path = experiments_root / exp_id / "exp.manifest.json"
        input_paths.append((f"{exp_id}/exp.manifest.json", manifest_path))

    for _, path in input_paths:
        if not path.exists():
            raise ValidationError(f"Missing required report manifest input file: {path}")

    report_payload_bytes = report_bytes(report_payload)
    payload: dict[str, Any] = {
        "manifest_version": "v1",
        "created_utc": created_utc,
        "inputs": [
            {
                "path": relative_path,
                "bytes": file_path.stat().st_size,
                "sha256": sha256_file(file_path),
            }
            for relative_path, file_path in sorted(input_paths, key=lambda item: item[0])
        ],
        "outputs": {
            "experiments.report.json": {
                "bytes": len(report_payload_bytes),
                "sha256": sha256_bytes(report_payload_bytes),
            }
        },
    }
    payload["report_manifest_canonical_sha256"] = _manifest_hash_without_self(payload)
    return payload


def write_report_artifacts(
    run_dir: Path,
    report_payload: dict[str, Any],
    report_manifest_payload: dict[str, Any],
) -> None:
    experiments_root = run_dir / "experiments"
    experiments_root.mkdir(parents=True, exist_ok=True)

    (experiments_root / "experiments.report.json").write_bytes(report_bytes(report_payload))
    (experiments_root / "experiments.report.manifest.json").write_bytes(
        (json.dumps(report_manifest_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")
    )

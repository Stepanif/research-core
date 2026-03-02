from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from research_core.util.hashing import sha256_bytes, sha256_file, sha256_json
from research_core.util.io import read_json
from research_core.util.types import ValidationError


def write_transition_matrix(path: Path, payload: dict[str, Any]) -> None:
    path.write_bytes(transition_matrix_bytes(payload))


def transition_matrix_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def _manifest_hash_without_self(payload: dict[str, Any]) -> str:
    clone = dict(payload)
    clone.pop("exp_manifest_canonical_sha256", None)
    return sha256_json(clone)


def _required_string(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value:
        raise ValidationError(f"Missing required manifest field: {key}")
    return value


def _load_input_hashes(run_dir: Path) -> dict[str, str]:
    psa_manifest_path = run_dir / "psa.manifest.json"
    if not psa_manifest_path.exists():
        raise ValidationError(f"Missing required psa manifest for experiment: {psa_manifest_path}")

    psa_manifest_payload = read_json(psa_manifest_path)
    psa_manifest_canonical_sha256 = sha256_json(psa_manifest_payload)

    psa_output = psa_manifest_payload.get("output_files", {}).get("psa.parquet", {})
    psa_canonical_table_sha256 = psa_output.get("canonical_table_sha256")
    if not isinstance(psa_canonical_table_sha256, str) or not psa_canonical_table_sha256:
        raise ValidationError("psa.manifest.json missing output_files.psa.parquet.canonical_table_sha256")

    inputs: dict[str, str] = {
        "psa_manifest_canonical_sha256": psa_manifest_canonical_sha256,
        "psa_canonical_table_sha256": psa_canonical_table_sha256,
    }

    canon_manifest_path = run_dir / "canon.manifest.json"
    if canon_manifest_path.exists():
        canon_manifest_payload = read_json(canon_manifest_path)
        canon_output = canon_manifest_payload.get("output_files", {}).get("canon.parquet", {})
        canon_canonical_table_sha256 = canon_output.get("canonical_table_sha256")
        if isinstance(canon_canonical_table_sha256, str) and canon_canonical_table_sha256:
            inputs["canon_canonical_table_sha256"] = canon_canonical_table_sha256
            inputs["canon_manifest_canonical_sha256"] = sha256_json(canon_manifest_payload)

    return inputs


def build_experiment_manifest(
    run_dir: Path,
    exp_id: str,
    spec_payload: dict[str, Any],
    transition_matrix_payload: dict[str, Any],
) -> dict[str, Any]:
    created_utc = os.environ.get("RESEARCH_CREATED_UTC")
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError("Experiment run requires RESEARCH_CREATED_UTC for deterministic created_utc")

    spec_canonical_sha256 = sha256_json(spec_payload)
    inputs = _load_input_hashes(run_dir)
    transition_payload_bytes = transition_matrix_bytes(transition_matrix_payload)

    payload: dict[str, Any] = {
        "manifest_version": "v1",
        "exp_id": exp_id,
        "spec_canonical_sha256": spec_canonical_sha256,
        "inputs": inputs,
        "outputs": {
            "transition_matrix.json": {
                "bytes": len(transition_payload_bytes),
                "sha256": sha256_bytes(transition_payload_bytes),
            }
        },
        "created_utc": created_utc,
    }
    payload["exp_manifest_canonical_sha256"] = _manifest_hash_without_self(payload)
    return payload


def write_experiment_manifest(path: Path, payload: dict[str, Any]) -> None:
    serialized = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"
    path.write_bytes(serialized.encode("utf-8"))


def ensure_experiment_immutable(
    exp_dir: Path,
    expected_manifest_payload: dict[str, Any],
) -> None:
    if not exp_dir.exists():
        return

    manifest_path = exp_dir / "exp.manifest.json"
    transition_path = exp_dir / "transition_matrix.json"

    if not manifest_path.exists() or not transition_path.exists():
        raise ValidationError(f"Experiment immutability violation: missing required files in existing exp_dir {exp_dir}")

    existing_manifest = read_json(manifest_path)
    existing_self_hash = _required_string(existing_manifest, "exp_manifest_canonical_sha256")
    recalculated_existing_hash = _manifest_hash_without_self(existing_manifest)
    if existing_self_hash != recalculated_existing_hash:
        raise ValidationError(
            f"Experiment immutability violation: exp.manifest hash field mismatch for {manifest_path}"
        )

    recorded_output = existing_manifest.get("outputs", {}).get("transition_matrix.json", {})
    recorded_output_sha = recorded_output.get("sha256")
    if not isinstance(recorded_output_sha, str) or not recorded_output_sha:
        raise ValidationError("Experiment immutability violation: manifest missing outputs.transition_matrix.json.sha256")

    actual_output_sha = sha256_file(transition_path)
    if actual_output_sha != recorded_output_sha:
        raise ValidationError(
            "Experiment immutability violation: transition_matrix.json bytes differ from recorded manifest hash"
        )

    expected_self_hash = _required_string(expected_manifest_payload, "exp_manifest_canonical_sha256")
    if existing_self_hash != expected_self_hash:
        raise ValidationError(
            f"Experiment immutability violation: existing manifest hash differs for exp_id={expected_manifest_payload['exp_id']}"
        )

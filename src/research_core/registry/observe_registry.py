from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_core.util.hashing import sha256_file, sha256_json
from research_core.util.io import read_json, write_json
from research_core.util.types import ValidationError


def _canonical_manifest_sha256(path: Path) -> str:
    payload = read_json(path)
    return sha256_json(payload)


def _require(path: Path, description: str) -> None:
    if not path.exists():
        raise ValidationError(f"Missing required {description}: {path}")


def _verify_output_file_hashes(run_dir: Path, manifest_path: Path) -> None:
    payload = read_json(manifest_path)
    output_files = payload.get("output_files")
    if not isinstance(output_files, dict):
        raise ValidationError(f"Manifest missing output_files block: {manifest_path}")

    for output_name, output_info in sorted(output_files.items(), key=lambda item: item[0]):
        if not isinstance(output_info, dict):
            raise ValidationError(f"Invalid output metadata for {output_name} in {manifest_path}")
        expected_sha = output_info.get("sha256")
        if not isinstance(expected_sha, str) or not expected_sha:
            continue

        explicit_path = output_info.get("path") if isinstance(output_info.get("path"), str) else output_name
        candidates = [run_dir / explicit_path, run_dir / output_name, run_dir / "logs" / output_name]
        output_path = next((path for path in candidates if path.exists()), None)
        if output_path is None:
            raise ValidationError(f"Manifest output file does not exist for key={output_name}: {candidates[0]}")
        actual_sha = sha256_file(output_path)
        if actual_sha != expected_sha:
            raise ValidationError(
                f"Manifest hash mismatch for {output_name}: expected={expected_sha} actual={actual_sha}"
            )


def _observe_entry(run_dir: Path) -> dict[str, Any]:
    observe_dir = run_dir / "observe"
    entry: dict[str, Any] = {}

    summary_manifest_path = observe_dir / "observe.summary.manifest.json"
    if summary_manifest_path.exists():
        _verify_output_file_hashes(run_dir=observe_dir, manifest_path=summary_manifest_path)
        summary_path = observe_dir / "observe.summary.json"
        _require(summary_path, "observe summary artifact")
        entry["summary"] = {
            "summary_json_sha256": sha256_file(summary_path),
            "manifest_canonical_sha256": _canonical_manifest_sha256(summary_manifest_path),
            "manifest_path": "observe/observe.summary.manifest.json",
        }

    profile_manifest_path = observe_dir / "observe.profile.manifest.json"
    if profile_manifest_path.exists():
        _verify_output_file_hashes(run_dir=observe_dir, manifest_path=profile_manifest_path)
        profile_path = observe_dir / "observe.profile.json"
        _require(profile_path, "observe profile artifact")
        entry["profile"] = {
            "profile_json_sha256": sha256_file(profile_path),
            "manifest_canonical_sha256": _canonical_manifest_sha256(profile_manifest_path),
            "manifest_path": "observe/observe.profile.manifest.json",
        }

    return entry


def build_registry_run_entry(run_dir: Path) -> dict[str, Any]:
    canon_manifest_path = run_dir / "canon.manifest.json"
    canon_contract_path = run_dir / "canon.contract.json"
    canon_parquet_path = run_dir / "canon.parquet"

    _require(canon_manifest_path, "canon manifest")
    _require(canon_contract_path, "canon contract")
    _require(canon_parquet_path, "canon parquet")

    _verify_output_file_hashes(run_dir=run_dir, manifest_path=canon_manifest_path)

    canon_manifest = read_json(canon_manifest_path)
    instrument = canon_manifest.get("instrument")
    tf = canon_manifest.get("tf")
    session_policy = canon_manifest.get("session_policy")
    if not isinstance(instrument, str) or not instrument:
        raise ValidationError("canon.manifest.json missing instrument")
    if not isinstance(tf, str) or not tf:
        raise ValidationError("canon.manifest.json missing tf")
    if not isinstance(session_policy, str) or not session_policy:
        raise ValidationError("canon.manifest.json missing session_policy")

    entry: dict[str, Any] = {
        "run_id": run_dir.name,
        "instrument": instrument,
        "tf": tf,
        "session_policy": session_policy,
        "manifest_hash": sha256_file(canon_manifest_path),
        "contract_hash": sha256_file(canon_contract_path),
        "canon": {
            "canonical_table_sha256": canon_manifest["output_files"]["canon.parquet"]["canonical_table_sha256"],
            "manifest_canonical_sha256": _canonical_manifest_sha256(canon_manifest_path),
        },
    }

    psa_manifest_path = run_dir / "psa.manifest.json"
    psa_parquet_path = run_dir / "psa.parquet"
    if psa_manifest_path.exists() or psa_parquet_path.exists():
        _require(psa_manifest_path, "psa manifest")
        _require(psa_parquet_path, "psa parquet")
        _verify_output_file_hashes(run_dir=run_dir, manifest_path=psa_manifest_path)

        psa_manifest = read_json(psa_manifest_path)
        entry["psa"] = {
            "canonical_table_sha256": psa_manifest["output_files"]["psa.parquet"]["canonical_table_sha256"],
            "manifest_canonical_sha256": _canonical_manifest_sha256(psa_manifest_path),
        }

    observe = _observe_entry(run_dir)
    if observe:
        entry["observe"] = observe

    return entry


def _index_path_for_run(run_dir: Path) -> Path:
    return run_dir.parent / "index.json"


def _load_or_init_index(index_path: Path) -> dict[str, Any]:
    if not index_path.exists():
        return {"index_version": "v1", "runs": []}

    payload = read_json(index_path)
    if not isinstance(payload, dict) or not isinstance(payload.get("runs"), list):
        raise ValidationError(f"Invalid registry index structure: {index_path}")
    payload.pop("index_sha256", None)
    return payload


def refresh_registry_for_run(run_dir: Path) -> dict[str, Any]:
    entry = build_registry_run_entry(run_dir)
    index_path = _index_path_for_run(run_dir)
    index_payload = _load_or_init_index(index_path)

    runs = index_payload["runs"]
    existing = next((item for item in runs if item.get("run_id") == entry["run_id"]), None)
    if existing is None:
        runs.append(entry)
    else:
        if existing != entry:
            raise ValidationError(
                f"Immutability violation for run_id={entry['run_id']}: stored registry hashes differ from current artifacts"
            )

    index_payload["runs"] = sorted(
        runs,
        key=lambda item: (
            str(item.get("instrument", "")),
            str(item.get("tf", "")),
            str(item.get("run_id", "")),
        ),
    )
    index_payload["index_sha256"] = sha256_json(index_payload)
    write_json(index_path, index_payload)
    return entry


def show_registry_run(run_dir: Path) -> dict[str, Any]:
    entry = build_registry_run_entry(run_dir)
    payload: dict[str, Any] = {
        "instrument": entry["instrument"],
        "tf": entry["tf"],
        "session_policy": entry["session_policy"],
        "canon": {
            "manifest_canonical_sha256": entry["canon"]["manifest_canonical_sha256"],
            "canonical_table_sha256": entry["canon"]["canonical_table_sha256"],
        },
        "psa": entry.get("psa"),
        "observe": {
            "summary": entry.get("observe", {}).get("summary"),
            "profile": entry.get("observe", {}).get("profile"),
        },
    }
    return payload

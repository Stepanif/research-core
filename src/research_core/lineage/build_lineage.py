from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from research_core.datasets.catalog import show_dataset
from research_core.lineage.contracts import LINEAGE_VERSION, REQUIRED_ENV_VAR_CREATED_UTC
from research_core.lineage.writer import canonical_hash, canonical_json_bytes, update_dataset_to_runs_index, write_lineage_artifacts
from research_core.util.buildmeta import get_created_utc, get_git_commit
from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.types import ValidationError


def _read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValidationError(f"Invalid JSON payload at: {path}")
    return payload


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="Lineage build requires RESEARCH_CREATED_UTC")


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _git_commit_or_unknown(repo_root: Path) -> str:
    return get_git_commit(repo_root)


def _run_dir_ref(run_dir: Path) -> str:
    cwd = Path.cwd().resolve()
    resolved = run_dir.resolve()
    if resolved.is_relative_to(cwd):
        return resolved.relative_to(cwd).as_posix()
    return run_dir.name


def _extract_tz_from_contract(contract_payload: dict[str, Any]) -> str:
    ts_type = contract_payload.get("schema_contract", {}).get("types", {}).get("ts")
    if not isinstance(ts_type, str):
        raise ValidationError("canon.contract.json missing schema_contract.types.ts")
    if "," not in ts_type or not ts_type.endswith("]"):
        raise ValidationError(f"Unsupported ts type format for timezone extraction: {ts_type}")
    return ts_type.split(",", 1)[1].rstrip("]").strip()


def _source_files_sha256(canon_manifest: dict[str, Any]) -> str:
    files = canon_manifest.get("input_files")
    if not isinstance(files, list):
        raise ValidationError("canon.manifest.json missing input_files")
    listing: list[tuple[str, str]] = []
    for item in files:
        if not isinstance(item, dict):
            raise ValidationError("canon.manifest.json has invalid input_files row")
        path = item.get("path")
        sha = item.get("sha256")
        if not isinstance(path, str) or not path or not isinstance(sha, str) or not sha:
            raise ValidationError("canon.manifest.json input_files row missing path/sha256")
        listing.append((path, sha))
    lines = [f"{sha}  {path}\n" for path, sha in sorted(listing, key=lambda x: x[0])]
    return sha256_bytes("".join(lines).encode("utf-8"))


def _schema_colmap_hashes(canon_contract: dict[str, Any]) -> tuple[str, str]:
    schema_contract = canon_contract.get("schema_contract")
    colmap_contract = canon_contract.get("colmap_contract")
    if not isinstance(schema_contract, dict):
        raise ValidationError("canon.contract.json missing schema_contract")
    if not isinstance(colmap_contract, dict):
        raise ValidationError("canon.contract.json missing colmap_contract")
    schema_sha = sha256_bytes(canonical_json_bytes(schema_contract).rstrip(b"\n"))
    colmap_sha = sha256_bytes(canonical_json_bytes(colmap_contract).rstrip(b"\n"))
    return schema_sha, colmap_sha


def _canonical_json_hash_from_file(path: Path) -> str:
    payload = _read_json(path)
    return canonical_hash(payload)


def _validate_dataset_id_if_present(catalog_dir: Path, dataset_id: str | None) -> None:
    if isinstance(dataset_id, str) and dataset_id:
        show_dataset(catalog_root=catalog_dir, dataset_id=dataset_id)


def _tool_versions(canon_manifest: dict[str, Any], psa_manifest: dict[str, Any] | None, observe_summary_manifest: dict[str, Any] | None, observe_profile_manifest: dict[str, Any] | None) -> dict[str, str]:
    versions: dict[str, str] = {}
    if canon_manifest.get("manifest_version") == "v1":
        versions["canon"] = "v1"
    if isinstance(psa_manifest, dict):
        version = psa_manifest.get("psa_version")
        if isinstance(version, str) and version:
            versions["psa"] = version
    if isinstance(observe_summary_manifest, dict) or isinstance(observe_profile_manifest, dict):
        versions["observe"] = "v1"
    return {key: versions[key] for key in sorted(versions)}


def build_lineage_for_run(
    run_dir: Path,
    catalog_dir: Path,
    raw_dataset_id: str | None = None,
    canon_dataset_id: str | None = None,
) -> dict[str, Any]:
    created_utc = _require_created_utc()
    _validate_dataset_id_if_present(catalog_dir, raw_dataset_id)
    _validate_dataset_id_if_present(catalog_dir, canon_dataset_id)

    canon_manifest_path = run_dir / "canon.manifest.json"
    canon_contract_path = run_dir / "canon.contract.json"
    if not canon_manifest_path.exists() or not canon_manifest_path.is_file():
        raise ValidationError(f"Missing canon.manifest.json in run dir: {run_dir}")
    if not canon_contract_path.exists() or not canon_contract_path.is_file():
        raise ValidationError(f"Missing canon.contract.json in run dir: {run_dir}")

    canon_manifest = _read_json(canon_manifest_path)
    canon_contract = _read_json(canon_contract_path)
    psa_manifest_path = run_dir / "psa.manifest.json"
    observe_summary_manifest_path = run_dir / "observe" / "observe.summary.manifest.json"
    observe_profile_manifest_path = run_dir / "observe" / "observe.profile.manifest.json"

    psa_manifest = _read_json(psa_manifest_path) if psa_manifest_path.exists() else None
    observe_summary_manifest = _read_json(observe_summary_manifest_path) if observe_summary_manifest_path.exists() else None
    observe_profile_manifest = _read_json(observe_profile_manifest_path) if observe_profile_manifest_path.exists() else None

    canon_meta = canon_manifest.get("output_files", {}).get("canon.parquet", {})
    canon_table_sha256 = canon_meta.get("canonical_table_sha256")
    if not isinstance(canon_table_sha256, str) or not canon_table_sha256:
        raise ValidationError("canon.manifest.json missing canonical_table_sha256")

    artifacts: dict[str, Any] = {"canon_table_sha256": canon_table_sha256}
    if isinstance(psa_manifest, dict):
        psa_hash = psa_manifest.get("output_files", {}).get("psa.parquet", {}).get("canonical_table_sha256")
        if isinstance(psa_hash, str) and psa_hash:
            artifacts["psa_table_sha256"] = psa_hash
    if observe_summary_manifest_path.exists():
        artifacts["observe_summary_manifest_sha256"] = _canonical_json_hash_from_file(observe_summary_manifest_path)
    if observe_profile_manifest_path.exists():
        artifacts["observe_profile_manifest_sha256"] = _canonical_json_hash_from_file(observe_profile_manifest_path)

    schema_sha256, colmap_sha256 = _schema_colmap_hashes(canon_contract)

    inputs: dict[str, Any] = {
        "source_files_sha256": _source_files_sha256(canon_manifest),
        "schema_sha256": schema_sha256,
        "colmap_sha256": colmap_sha256,
    }
    if isinstance(raw_dataset_id, str) and raw_dataset_id:
        inputs["raw_dataset_id"] = raw_dataset_id
    if isinstance(canon_dataset_id, str) and canon_dataset_id:
        inputs["canon_dataset_id"] = canon_dataset_id

    repo_root = _repo_root()
    payload: dict[str, Any] = {
        "lineage_version": LINEAGE_VERSION,
        "created_utc": created_utc,
        "run_ref": {
            "run_dir_ref": _run_dir_ref(run_dir),
            "instrument": canon_manifest.get("instrument"),
            "tf": canon_manifest.get("tf"),
            "session_policy": canon_manifest.get("session_policy"),
            "tz": _extract_tz_from_contract(canon_contract),
            "rth_start": canon_manifest.get("rth_start"),
            "rth_end": canon_manifest.get("rth_end"),
        },
        "inputs": inputs,
        "build": {
            "git_commit": _git_commit_or_unknown(repo_root),
            "tool_versions": _tool_versions(canon_manifest, psa_manifest, observe_summary_manifest, observe_profile_manifest),
        },
        "artifacts": artifacts,
    }

    for key in ["instrument", "tf", "session_policy", "tz", "rth_start", "rth_end"]:
        value = payload["run_ref"].get(key)
        if not isinstance(value, str) or not value:
            raise ValidationError(f"Missing lineage run_ref field: {key}")

    payload["lineage_canonical_sha256"] = canonical_hash({k: v for k, v in payload.items() if k != "lineage_canonical_sha256"})

    manifest_inputs: list[dict[str, Any]] = [
        {
            "path": "canon.manifest.json",
            "sha256": sha256_file(canon_manifest_path),
            "bytes": int(canon_manifest_path.stat().st_size),
        },
        {
            "path": "canon.contract.json",
            "sha256": sha256_file(canon_contract_path),
            "bytes": int(canon_contract_path.stat().st_size),
        },
        {
            "path": "canon.contract.json#schema_contract",
            "sha256": schema_sha256,
            "bytes": len(canonical_json_bytes(canon_contract["schema_contract"]).rstrip(b"\n")),
        },
        {
            "path": "canon.contract.json#colmap_contract",
            "sha256": colmap_sha256,
            "bytes": len(canonical_json_bytes(canon_contract["colmap_contract"]).rstrip(b"\n")),
        },
    ]
    if psa_manifest_path.exists():
        manifest_inputs.append(
            {
                "path": "psa.manifest.json",
                "sha256": sha256_file(psa_manifest_path),
                "bytes": int(psa_manifest_path.stat().st_size),
            }
        )
    if observe_summary_manifest_path.exists():
        manifest_inputs.append(
            {
                "path": "observe/observe.summary.manifest.json",
                "sha256": sha256_file(observe_summary_manifest_path),
                "bytes": int(observe_summary_manifest_path.stat().st_size),
            }
        )
    if observe_profile_manifest_path.exists():
        manifest_inputs.append(
            {
                "path": "observe/observe.profile.manifest.json",
                "sha256": sha256_file(observe_profile_manifest_path),
                "bytes": int(observe_profile_manifest_path.stat().st_size),
            }
        )

    write_lineage_artifacts(run_dir=run_dir, lineage_payload=payload, inputs=manifest_inputs)

    link_dataset_ids = [
        item
        for item in [raw_dataset_id, canon_dataset_id]
        if isinstance(item, str) and item
    ]
    if link_dataset_ids:
        update_dataset_to_runs_index(catalog_dir=catalog_dir, lineage_payload=payload, dataset_ids=link_dataset_ids)

    return payload

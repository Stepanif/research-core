from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_core.lineage.contracts import LINK_INDEX_VERSION
from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.types import ValidationError


def canonical_json_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def canonical_hash(payload: dict[str, Any]) -> str:
    return sha256_bytes(canonical_json_bytes(payload).rstrip(b"\n"))


def _immutable_write(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = canonical_json_bytes(payload)
    if path.exists():
        existing = path.read_bytes()
        if existing != encoded:
            raise ValidationError(f"Immutable lineage artifact conflict at: {path}")
        return
    path.write_bytes(encoded)


def write_lineage_artifacts(run_dir: Path, lineage_payload: dict[str, Any], inputs: list[dict[str, Any]]) -> tuple[Path, Path]:
    lineage_dir = run_dir / "lineage"
    lineage_path = lineage_dir / "lineage.json"
    manifest_path = lineage_dir / "lineage.manifest.json"

    _immutable_write(lineage_path, lineage_payload)

    lineage_output = {
        "path": "lineage/lineage.json",
        "sha256": sha256_file(lineage_path),
        "bytes": int(lineage_path.stat().st_size),
    }
    manifest_payload: dict[str, Any] = {
        "manifest_version": "v1",
        "inputs": sorted(inputs, key=lambda item: str(item["path"])),
        "outputs": {"lineage.json": lineage_output},
    }
    manifest_payload["lineage_manifest_canonical_sha256"] = canonical_hash(
        {k: v for k, v in manifest_payload.items() if k != "lineage_manifest_canonical_sha256"}
    )

    _immutable_write(manifest_path, manifest_payload)
    return lineage_path, manifest_path


def _load_json_if_exists(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValidationError(f"Invalid JSON payload at {path}")
    return payload


def update_dataset_to_runs_index(catalog_dir: Path, lineage_payload: dict[str, Any], dataset_ids: list[str]) -> Path:
    links_dir = catalog_dir / "links"
    index_path = links_dir / "dataset_to_runs.index.json"

    created_utc = lineage_payload["created_utc"]
    run_ref = lineage_payload["run_ref"]["run_dir_ref"]
    lineage_hash = lineage_payload["lineage_canonical_sha256"]
    canon_table_sha256 = lineage_payload["artifacts"]["canon_table_sha256"]

    existing = _load_json_if_exists(index_path)
    if existing is None:
        payload: dict[str, Any] = {
            "index_version": LINK_INDEX_VERSION,
            "created_utc": created_utc,
            "datasets": {},
        }
    else:
        payload = existing
        if payload.get("index_version") != LINK_INDEX_VERSION:
            raise ValidationError(f"Unsupported dataset_to_runs index version: {payload.get('index_version')}")
        if not isinstance(payload.get("datasets"), dict):
            raise ValidationError("Invalid dataset_to_runs index datasets payload")

    datasets = payload["datasets"]
    assert isinstance(datasets, dict)

    for dataset_id in sorted(set(dataset_ids)):
        row = datasets.get(dataset_id)
        if row is None:
            row = {"runs": []}
            datasets[dataset_id] = row
        if not isinstance(row, dict):
            raise ValidationError("Invalid dataset_to_runs row payload")
        runs = row.get("runs")
        if not isinstance(runs, list):
            raise ValidationError("Invalid dataset_to_runs runs payload")

        for item in runs:
            if not isinstance(item, dict):
                raise ValidationError("Invalid dataset_to_runs run record")
            if item.get("canon_table_sha256") == canon_table_sha256 and item.get("run_lineage_canonical_sha256") != lineage_hash:
                raise ValidationError(
                    f"Lineage immutability violation for dataset_id={dataset_id} canon_table_sha256={canon_table_sha256}"
                )

        candidate = {
            "run_ref": run_ref,
            "run_lineage_canonical_sha256": lineage_hash,
            "canon_table_sha256": canon_table_sha256,
            "created_utc": created_utc,
        }

        exists = any(
            isinstance(item, dict)
            and item.get("run_ref") == candidate["run_ref"]
            and item.get("run_lineage_canonical_sha256") == candidate["run_lineage_canonical_sha256"]
            and item.get("canon_table_sha256") == candidate["canon_table_sha256"]
            and item.get("created_utc") == candidate["created_utc"]
            for item in runs
        )
        if not exists:
            runs.append(candidate)

        row["runs"] = sorted(
            runs,
            key=lambda item: (str(item.get("canon_table_sha256", "")), str(item.get("run_ref", ""))),
        )

    payload["datasets"] = {key: datasets[key] for key in sorted(datasets)}
    _immutable_or_replace_sorted(index_path, payload)
    return index_path


def _immutable_or_replace_sorted(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = canonical_json_bytes(payload)
    if path.exists():
        existing = path.read_bytes()
        if existing == encoded:
            return
    path.write_bytes(encoded)

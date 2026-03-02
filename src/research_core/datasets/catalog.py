from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from research_core.datasets.contracts import (
    DATASET_KIND_CANON_V1,
    DATASET_KIND_RAW_VENDOR_V1,
    DATASET_KINDS_V1,
    DATASET_VERSION,
    DEFAULT_CANON_TZ,
    INDEX_VERSION,
    REQUIRED_ENV_VAR_CREATED_UTC,
)
from research_core.datasets.fingerprint import (
    enumerate_root_files,
    enumerate_specific_files,
    files_sha256,
    source_counts,
    stable_root_ref,
)
from research_core.datasets.io import canonical_json_bytes, read_json, write_canonical_json
from research_core.util.hashing import sha256_bytes
from research_core.util.types import ValidationError


def _require_created_utc() -> str:
    value = os.environ.get(REQUIRED_ENV_VAR_CREATED_UTC)
    if not isinstance(value, str) or not value:
        raise ValidationError("Dataset catalog operations require RESEARCH_CREATED_UTC")
    return value


def _catalog_paths(catalog_root: Path) -> tuple[Path, Path]:
    return catalog_root / "datasets.index.json", catalog_root / "entries"


def _entry_path(entries_dir: Path, dataset_id: str) -> Path:
    return entries_dir / f"{dataset_id}.json"


def _hash_without_field(payload: dict[str, Any], field_name: str) -> str:
    body = {key: value for key, value in payload.items() if key != field_name}
    return sha256_bytes(canonical_json_bytes(body).rstrip(b"\n"))


def _dataset_id_payload(kind: str, files_hash: str, file_count: int, total_bytes: int, canon_table_sha256: str | None, tz: str | None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "kind": kind,
        "files_sha256": files_hash,
        "file_count": file_count,
        "total_bytes": total_bytes,
    }
    if canon_table_sha256 is not None:
        payload["canon_table_sha256"] = canon_table_sha256
    if tz is not None:
        payload["tz"] = tz
    return payload


def _compute_dataset_id(payload: dict[str, Any]) -> str:
    return sha256_bytes(canonical_json_bytes(payload).rstrip(b"\n"))


def _build_entry(
    *,
    kind: str,
    created_utc: str,
    source_root_ref: str,
    source_files: list[dict[str, Any]],
    dataset_id: str,
    files_hash: str,
    canon_table_sha256: str | None,
    description: str | None,
    tz: str | None,
) -> dict[str, Any]:
    file_count, total_bytes = source_counts(source_files)
    source = {
        "root": source_root_ref,
        "files": sorted(source_files, key=lambda item: str(item["path"])),
        "file_count": file_count,
        "total_bytes": total_bytes,
    }
    fingerprint: dict[str, Any] = {"files_sha256": files_hash}
    if canon_table_sha256 is not None:
        fingerprint["canon_table_sha256"] = canon_table_sha256

    entry: dict[str, Any] = {
        "dataset_version": DATASET_VERSION,
        "dataset_id": dataset_id,
        "kind": kind,
        "created_utc": created_utc,
        "source": source,
        "fingerprint": fingerprint,
    }
    if tz is not None:
        entry["tz"] = tz
    if isinstance(description, str) and description:
        entry["description"] = description

    entry["dataset_entry_canonical_sha256"] = _hash_without_field(entry, "dataset_entry_canonical_sha256")
    return entry


def _read_or_init_index(index_path: Path, created_utc: str) -> dict[str, Any]:
    if index_path.exists():
        payload = read_json(index_path)
        if not isinstance(payload, dict):
            raise ValidationError(f"Invalid catalog index payload: {index_path}")
        if payload.get("index_version") != INDEX_VERSION:
            raise ValidationError(f"Unsupported dataset catalog index version: {payload.get('index_version')}")
        datasets = payload.get("datasets")
        if not isinstance(datasets, dict):
            raise ValidationError(f"Invalid catalog index datasets mapping: {index_path}")
        return payload

    return {
        "index_version": INDEX_VERSION,
        "created_utc": created_utc,
        "datasets": {},
    }


def _validate_entry_integrity(entry: dict[str, Any], expected_dataset_id: str | None = None) -> None:
    dataset_version = entry.get("dataset_version")
    if dataset_version != DATASET_VERSION:
        raise ValidationError(f"Unsupported dataset version: {dataset_version}")

    kind = entry.get("kind")
    if kind not in DATASET_KINDS_V1:
        raise ValidationError(f"Unsupported dataset kind: {kind}")

    dataset_id = entry.get("dataset_id")
    if not isinstance(dataset_id, str) or not dataset_id:
        raise ValidationError("Invalid dataset_id in dataset entry")
    if expected_dataset_id is not None and dataset_id != expected_dataset_id:
        raise ValidationError("Dataset entry id mismatch")

    source = entry.get("source")
    if not isinstance(source, dict):
        raise ValidationError("Invalid dataset source payload")
    files = source.get("files")
    if not isinstance(files, list):
        raise ValidationError("Invalid dataset source files payload")

    fingerprint = entry.get("fingerprint")
    if not isinstance(fingerprint, dict):
        raise ValidationError("Invalid dataset fingerprint payload")

    files_hash = fingerprint.get("files_sha256")
    if not isinstance(files_hash, str) or not files_hash:
        raise ValidationError("Missing files_sha256 in dataset fingerprint")

    file_count, total_bytes = source_counts(files)
    if source.get("file_count") != file_count:
        raise ValidationError("Dataset source file_count mismatch")
    if source.get("total_bytes") != total_bytes:
        raise ValidationError("Dataset source total_bytes mismatch")

    recomputed_files_sha = files_sha256(files)
    if recomputed_files_sha != files_hash:
        raise ValidationError("Dataset files_sha256 mismatch")

    tz_value = entry.get("tz")
    canon_table_sha256 = fingerprint.get("canon_table_sha256")
    if kind == DATASET_KIND_CANON_V1:
        if tz_value != DEFAULT_CANON_TZ:
            raise ValidationError("canon_v1 dataset requires tz=America/New_York")
        if not isinstance(canon_table_sha256, str) or not canon_table_sha256:
            raise ValidationError("canon_v1 dataset missing canon_table_sha256")

    id_payload = _dataset_id_payload(
        kind=kind,
        files_hash=files_hash,
        file_count=file_count,
        total_bytes=total_bytes,
        canon_table_sha256=canon_table_sha256 if isinstance(canon_table_sha256, str) else None,
        tz=tz_value if isinstance(tz_value, str) and tz_value else None,
    )
    recomputed_dataset_id = _compute_dataset_id(id_payload)
    if dataset_id != recomputed_dataset_id:
        raise ValidationError("Dataset id mismatch against deterministic fingerprint payload")

    existing_hash = entry.get("dataset_entry_canonical_sha256")
    recomputed_hash = _hash_without_field(entry, "dataset_entry_canonical_sha256")
    if not isinstance(existing_hash, str) or existing_hash != recomputed_hash:
        raise ValidationError("Dataset entry canonical hash mismatch")


def _write_immutable_entry(path: Path, payload: dict[str, Any]) -> None:
    if path.exists():
        existing = read_json(path)
        if canonical_json_bytes(existing) != canonical_json_bytes(payload):
            raise ValidationError(f"Immutable dataset entry conflict at: {path}")
        return
    write_canonical_json(path, payload)


def _upsert_index(index_path: Path, dataset_id: str, kind: str, created_utc: str, entry_rel_path: str) -> dict[str, Any]:
    index_payload = _read_or_init_index(index_path, created_utc=created_utc)
    datasets = index_payload["datasets"]
    assert isinstance(datasets, dict)

    index_record = {
        "kind": kind,
        "created_utc": created_utc,
        "entry_path": entry_rel_path,
    }

    if dataset_id in datasets:
        existing = datasets[dataset_id]
        if not isinstance(existing, dict):
            raise ValidationError("Invalid existing dataset index record")
        if canonical_json_bytes(existing) != canonical_json_bytes(index_record):
            raise ValidationError(f"Immutable dataset index conflict for dataset_id={dataset_id}")
    else:
        datasets[dataset_id] = index_record

    ordered = {key: datasets[key] for key in sorted(datasets)}
    index_payload["datasets"] = ordered
    write_canonical_json(index_path, index_payload)
    return index_payload


def register_raw_dataset(catalog_root: Path, root_dir: Path, description: str | None = None, tz: str | None = None) -> dict[str, Any]:
    created_utc = _require_created_utc()
    files = enumerate_root_files(root_dir)
    files_hash = files_sha256(files)
    file_count, total_bytes = source_counts(files)

    id_payload = _dataset_id_payload(
        kind=DATASET_KIND_RAW_VENDOR_V1,
        files_hash=files_hash,
        file_count=file_count,
        total_bytes=total_bytes,
        canon_table_sha256=None,
        tz=tz if isinstance(tz, str) and tz else None,
    )
    dataset_id = _compute_dataset_id(id_payload)

    entry = _build_entry(
        kind=DATASET_KIND_RAW_VENDOR_V1,
        created_utc=created_utc,
        source_root_ref=stable_root_ref(root_dir),
        source_files=files,
        dataset_id=dataset_id,
        files_hash=files_hash,
        canon_table_sha256=None,
        description=description,
        tz=tz if isinstance(tz, str) and tz else None,
    )
    _validate_entry_integrity(entry)

    index_path, entries_dir = _catalog_paths(catalog_root)
    entry_path = _entry_path(entries_dir, dataset_id)
    entry_rel = Path("entries") / f"{dataset_id}.json"

    _write_immutable_entry(entry_path, entry)
    _upsert_index(
        index_path=index_path,
        dataset_id=dataset_id,
        kind=DATASET_KIND_RAW_VENDOR_V1,
        created_utc=created_utc,
        entry_rel_path=entry_rel.as_posix(),
    )
    return entry


def _canon_files_and_hashes(run_dir: Path) -> tuple[list[dict[str, Any]], str, str]:
    manifest_path = run_dir / "canon.manifest.json"
    parquet_path = run_dir / "canon.parquet"
    if not manifest_path.exists() or not manifest_path.is_file():
        raise ValidationError(f"Missing canon.manifest.json in run dir: {run_dir}")
    if not parquet_path.exists() or not parquet_path.is_file():
        raise ValidationError(f"Missing canon.parquet in run dir: {run_dir}")

    manifest = read_json(manifest_path)
    output_files = manifest.get("output_files")
    if not isinstance(output_files, dict):
        raise ValidationError("canon.manifest.json missing output_files")
    canon_meta = output_files.get("canon.parquet")
    if not isinstance(canon_meta, dict):
        raise ValidationError("canon.manifest.json missing canon.parquet output metadata")
    canon_table_sha256 = canon_meta.get("canonical_table_sha256")
    if not isinstance(canon_table_sha256, str) or not canon_table_sha256:
        raise ValidationError("canon.manifest.json missing canonical_table_sha256")

    rel_files = ["canon.manifest.json", "canon.parquet"]
    contract_path = run_dir / "canon.contract.json"
    if contract_path.exists() and contract_path.is_file():
        rel_files.append("canon.contract.json")

    files = enumerate_specific_files(run_dir, rel_files)
    return files, files_sha256(files), canon_table_sha256


def register_canon_dataset(catalog_root: Path, run_dir: Path, description: str | None = None) -> dict[str, Any]:
    created_utc = _require_created_utc()
    files, files_hash, canon_table_sha256 = _canon_files_and_hashes(run_dir)
    file_count, total_bytes = source_counts(files)

    id_payload = _dataset_id_payload(
        kind=DATASET_KIND_CANON_V1,
        files_hash=files_hash,
        file_count=file_count,
        total_bytes=total_bytes,
        canon_table_sha256=canon_table_sha256,
        tz=DEFAULT_CANON_TZ,
    )
    dataset_id = _compute_dataset_id(id_payload)

    entry = _build_entry(
        kind=DATASET_KIND_CANON_V1,
        created_utc=created_utc,
        source_root_ref=stable_root_ref(run_dir),
        source_files=files,
        dataset_id=dataset_id,
        files_hash=files_hash,
        canon_table_sha256=canon_table_sha256,
        description=description,
        tz=DEFAULT_CANON_TZ,
    )
    _validate_entry_integrity(entry)

    index_path, entries_dir = _catalog_paths(catalog_root)
    entry_path = _entry_path(entries_dir, dataset_id)
    entry_rel = Path("entries") / f"{dataset_id}.json"

    _write_immutable_entry(entry_path, entry)
    _upsert_index(
        index_path=index_path,
        dataset_id=dataset_id,
        kind=DATASET_KIND_CANON_V1,
        created_utc=created_utc,
        entry_rel_path=entry_rel.as_posix(),
    )
    return entry


def list_datasets(catalog_root: Path) -> list[dict[str, str]]:
    index_path, _ = _catalog_paths(catalog_root)
    if not index_path.exists():
        return []
    payload = read_json(index_path)
    if not isinstance(payload, dict):
        raise ValidationError(f"Invalid catalog index payload: {index_path}")
    datasets = payload.get("datasets")
    if not isinstance(datasets, dict):
        raise ValidationError(f"Invalid catalog index datasets mapping: {index_path}")

    rows: list[dict[str, str]] = []
    for dataset_id in sorted(datasets):
        item = datasets[dataset_id]
        if not isinstance(item, dict):
            raise ValidationError("Invalid dataset index row payload")
        kind = item.get("kind")
        created_utc = item.get("created_utc")
        entry_path = item.get("entry_path")
        if not isinstance(kind, str) or not isinstance(created_utc, str) or not isinstance(entry_path, str):
            raise ValidationError("Invalid dataset index row fields")
        rows.append(
            {
                "dataset_id": dataset_id,
                "kind": kind,
                "created_utc": created_utc,
                "entry_path": entry_path,
            }
        )
    return rows


def show_dataset(catalog_root: Path, dataset_id: str) -> dict[str, Any]:
    _, entries_dir = _catalog_paths(catalog_root)
    entry_path = _entry_path(entries_dir, dataset_id)
    if not entry_path.exists() or not entry_path.is_file():
        raise ValidationError(f"Dataset entry not found: {entry_path}")
    payload = read_json(entry_path)
    if not isinstance(payload, dict):
        raise ValidationError(f"Invalid dataset entry payload: {entry_path}")
    _validate_entry_integrity(payload, expected_dataset_id=dataset_id)
    return payload


def validate_dataset(catalog_root: Path, dataset_id: str) -> tuple[bool, str]:
    entry = show_dataset(catalog_root=catalog_root, dataset_id=dataset_id)
    kind = str(entry["kind"])
    source = entry["source"]
    assert isinstance(source, dict)
    source_root = source["root"]
    if not isinstance(source_root, str) or not source_root:
        raise ValidationError("Dataset source.root is invalid")

    root_path = Path(source_root)
    if not root_path.is_absolute():
        root_path = (Path.cwd() / root_path).resolve()

    expected_files = source["files"]
    assert isinstance(expected_files, list)
    rel_files = [str(item["path"]) for item in expected_files]
    current_files = enumerate_specific_files(root_path, rel_files)
    current_files_hash = files_sha256(current_files)

    expected_fingerprint = entry["fingerprint"]
    assert isinstance(expected_fingerprint, dict)
    expected_files_hash = expected_fingerprint["files_sha256"]
    if current_files_hash != expected_files_hash:
        return False, f"FAIL dataset_id={dataset_id} reason=files_sha256_mismatch"

    if kind == DATASET_KIND_CANON_V1:
        manifest = read_json(root_path / "canon.manifest.json")
        current_canon = manifest.get("output_files", {}).get("canon.parquet", {}).get("canonical_table_sha256")
        expected_canon = expected_fingerprint.get("canon_table_sha256")
        if not isinstance(current_canon, str) or current_canon != expected_canon:
            return False, f"FAIL dataset_id={dataset_id} reason=canon_table_sha256_mismatch"

    return True, f"PASS dataset_id={dataset_id}"

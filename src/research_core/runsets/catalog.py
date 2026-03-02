from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.runsets.contracts import RUNSET_INDEX_VERSION
from research_core.runsets.ids import runset_id_from_fingerprint
from research_core.runsets.io import canonical_hash, canonical_json_bytes, read_json, write_canonical_json
from research_core.runsets.spec import load_runset_spec
from research_core.runsets.validate import validate_runset_payload
from research_core.util.types import ValidationError


def _catalog_paths(catalog_root: Path) -> tuple[Path, Path]:
    runsets_dir = catalog_root / "runsets"
    return runsets_dir / "runsets.index.json", runsets_dir / "entries"


def _entry_path(entries_dir: Path, runset_id: str) -> Path:
    return entries_dir / f"{runset_id}.json"


def _read_or_init_index(index_path: Path, created_utc: str) -> dict[str, Any]:
    if index_path.exists():
        payload = read_json(index_path)
        if not isinstance(payload, dict):
            raise ValidationError(f"Invalid RunSet catalog index payload: {index_path}")
        if payload.get("index_version") != RUNSET_INDEX_VERSION:
            raise ValidationError(f"Unsupported RunSet catalog index version: {payload.get('index_version')}")
        runsets = payload.get("runsets")
        if not isinstance(runsets, dict):
            raise ValidationError(f"Invalid RunSet catalog index runsets mapping: {index_path}")
        return payload

    return {
        "index_version": RUNSET_INDEX_VERSION,
        "created_utc": created_utc,
        "runsets": {},
    }


def _immutable_write(path: Path, payload: dict[str, Any]) -> None:
    if path.exists():
        existing = read_json(path)
        if canonical_json_bytes(existing) != canonical_json_bytes(payload):
            raise ValidationError(f"Immutable RunSet entry conflict at: {path}")
        return
    write_canonical_json(path, payload)


def _upsert_index(index_path: Path, runset_id: str, created_utc: str, entry_rel_path: str) -> dict[str, Any]:
    index_payload = _read_or_init_index(index_path, created_utc=created_utc)
    runsets = index_payload["runsets"]
    assert isinstance(runsets, dict)

    record = {
        "created_utc": created_utc,
        "entry_path": entry_rel_path,
    }

    if runset_id in runsets:
        existing = runsets[runset_id]
        if not isinstance(existing, dict):
            raise ValidationError("Invalid existing RunSet index record")
        if canonical_json_bytes(existing) != canonical_json_bytes(record):
            raise ValidationError(f"Immutable RunSet index conflict for runset_id={runset_id}")
    else:
        runsets[runset_id] = record

    index_payload["runsets"] = {key: runsets[key] for key in sorted(runsets)}
    write_canonical_json(index_path, index_payload)
    return index_payload


def _build_entry(spec_payload: dict[str, Any]) -> dict[str, Any]:
    fingerprint = spec_payload["fingerprint"]
    runset_id = runset_id_from_fingerprint(fingerprint)

    entry: dict[str, Any] = {
        "runset_version": spec_payload["runset_version"],
        "runset_id": runset_id,
        "created_utc": spec_payload["created_utc"],
        "datasets": spec_payload["datasets"],
        "runs": spec_payload["runs"],
        "policy": spec_payload["policy"],
        "fingerprint": fingerprint,
    }
    if "name" in spec_payload:
        entry["name"] = spec_payload["name"]

    entry["runset_entry_canonical_sha256"] = canonical_hash(entry, self_field="runset_entry_canonical_sha256")
    return entry


def create_runset(catalog_root: Path, spec_path: Path) -> dict[str, Any]:
    spec_payload = load_runset_spec(spec_path)
    entry = _build_entry(spec_payload)

    ok, text = validate_runset_payload(catalog_root=catalog_root, runset_payload=entry)
    if not ok:
        raise ValidationError(text)

    index_path, entries_dir = _catalog_paths(catalog_root)
    runset_id = str(entry["runset_id"])
    entry_path = _entry_path(entries_dir, runset_id)
    entry_rel = Path("entries") / f"{runset_id}.json"

    _immutable_write(entry_path, entry)
    _upsert_index(
        index_path=index_path,
        runset_id=runset_id,
        created_utc=str(entry["created_utc"]),
        entry_rel_path=entry_rel.as_posix(),
    )
    return entry


def list_runsets(catalog_root: Path) -> list[dict[str, str]]:
    index_path, _ = _catalog_paths(catalog_root)
    if not index_path.exists():
        return []

    payload = read_json(index_path)
    if not isinstance(payload, dict):
        raise ValidationError(f"Invalid RunSet catalog index payload: {index_path}")
    runsets = payload.get("runsets")
    if not isinstance(runsets, dict):
        raise ValidationError(f"Invalid RunSet catalog index runsets mapping: {index_path}")

    rows: list[dict[str, str]] = []
    for runset_id in sorted(runsets):
        item = runsets[runset_id]
        if not isinstance(item, dict):
            raise ValidationError("Invalid RunSet index row payload")
        created_utc = item.get("created_utc")
        entry_path = item.get("entry_path")
        if not isinstance(created_utc, str) or not isinstance(entry_path, str):
            raise ValidationError("Invalid RunSet index row fields")
        rows.append(
            {
                "runset_id": runset_id,
                "created_utc": created_utc,
                "entry_path": entry_path,
            }
        )
    return rows


def show_runset(catalog_root: Path, runset_id: str) -> dict[str, Any]:
    _, entries_dir = _catalog_paths(catalog_root)
    path = _entry_path(entries_dir, runset_id)
    if not path.exists() or not path.is_file():
        raise ValidationError(f"RunSet entry not found: {path}")

    payload = read_json(path)
    if not isinstance(payload, dict):
        raise ValidationError(f"Invalid RunSet entry payload: {path}")

    expected_hash = canonical_hash(payload, self_field="runset_entry_canonical_sha256")
    actual_hash = payload.get("runset_entry_canonical_sha256")
    if not isinstance(actual_hash, str) or actual_hash != expected_hash:
        raise ValidationError("RunSet entry canonical hash mismatch")

    expected_id = runset_id_from_fingerprint(payload.get("fingerprint", {}))
    if payload.get("runset_id") != runset_id or expected_id != runset_id:
        raise ValidationError("RunSet entry runset_id mismatch")

    return payload


def validate_runset(catalog_root: Path, runset_id: str) -> tuple[bool, str]:
    payload = show_runset(catalog_root=catalog_root, runset_id=runset_id)
    return validate_runset_payload(catalog_root=catalog_root, runset_payload=payload)

from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.baselines.contracts import (
    BASELINE_CARD_FILE,
    BASELINE_CARD_MANIFEST_FILE,
    BASELINE_INDEX_FILE,
    BASELINE_INDEX_VERSION,
    BASELINE_MANIFEST_SELF_HASH_FIELD,
)
from research_core.baselines.io import read_json_object, write_json_object
from research_core.runsets.io import canonical_hash
from research_core.util.buildmeta import get_created_utc
from research_core.util.hashing import sha256_file
from research_core.util.types import ValidationError


def baseline_index_path(root: Path) -> Path:
    return root / BASELINE_INDEX_FILE


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="Baseline index refresh requires RESEARCH_CREATED_UTC")


def _load_or_init_index(path: Path, created_utc: str) -> dict[str, Any]:
    if not path.exists():
        return {
            "index_version": BASELINE_INDEX_VERSION,
            "created_utc": created_utc,
            "runsets": {},
        }

    payload = read_json_object(path)
    if payload.get("index_version") != BASELINE_INDEX_VERSION:
        raise ValidationError(f"Unsupported baseline index version in {path}")
    runsets = payload.get("runsets")
    if not isinstance(runsets, dict):
        raise ValidationError(f"Invalid runsets block in {path}")
    return payload


def _runset_entry(root: Path, runset_id: str) -> dict[str, str]:
    runset_dir = root / runset_id
    card_path = runset_dir / BASELINE_CARD_FILE
    manifest_path = runset_dir / BASELINE_CARD_MANIFEST_FILE

    if not card_path.exists() or not card_path.is_file():
        raise ValidationError(f"Missing baseline card for runset_id={runset_id}: {card_path}")
    if not manifest_path.exists() or not manifest_path.is_file():
        raise ValidationError(f"Missing baseline card manifest for runset_id={runset_id}: {manifest_path}")

    card_payload = read_json_object(card_path)
    checksums = card_payload.get("checksums")
    if not isinstance(checksums, dict):
        raise ValidationError(f"Invalid baseline card checksums for runset_id={runset_id}")
    baseline_id = checksums.get("per_run_vector_sha256")
    if not isinstance(baseline_id, str) or not baseline_id:
        raise ValidationError(f"Missing per_run_vector_sha256 in baseline card for runset_id={runset_id}")

    manifest_payload = read_json_object(manifest_path)
    manifest_hash = canonical_hash(manifest_payload, self_field=BASELINE_MANIFEST_SELF_HASH_FIELD)

    return {
        "baseline_id": baseline_id,
        "card_sha256": sha256_file(card_path),
        "manifest_canonical_sha256": manifest_hash,
        "path": f"{runset_id}/{BASELINE_CARD_FILE}",
    }


def refresh_baseline_index(root: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()
    if not root.exists() or not root.is_dir():
        raise ValidationError(f"Baseline root does not exist: {root}")

    discovered: dict[str, dict[str, str]] = {}
    for item in sorted([child for child in root.iterdir() if child.is_dir()], key=lambda value: value.name):
        runset_id = item.name
        entry = _runset_entry(root=root, runset_id=runset_id)
        discovered[runset_id] = entry

    path = baseline_index_path(root)
    existing = _load_or_init_index(path, created_utc=created_utc)
    existing_runsets = existing.get("runsets", {})
    assert isinstance(existing_runsets, dict)

    for runset_id, entry in sorted(discovered.items(), key=lambda kv: kv[0]):
        existing_entry = existing_runsets.get(runset_id)
        if isinstance(existing_entry, dict):
            existing_baseline_id = existing_entry.get("baseline_id")
            if isinstance(existing_baseline_id, str) and existing_baseline_id != entry["baseline_id"]:
                raise ValidationError(
                    f"Baseline index immutability violation for runset_id={runset_id}: existing baseline_id differs from on-disk baseline"
                )

    payload = {
        "index_version": BASELINE_INDEX_VERSION,
        "created_utc": created_utc,
        "runsets": {runset_id: discovered[runset_id] for runset_id in sorted(discovered.keys())},
    }
    write_json_object(path, payload)
    return payload


def show_baseline_index(root: Path, runset_id: str | None = None) -> dict[str, Any]:
    path = baseline_index_path(root)
    if not path.exists():
        raise ValidationError(f"Missing baseline index file: {path}")

    payload = read_json_object(path)
    if payload.get("index_version") != BASELINE_INDEX_VERSION:
        raise ValidationError(f"Unsupported baseline index version in {path}")
    runsets = payload.get("runsets")
    if not isinstance(runsets, dict):
        raise ValidationError(f"Invalid runsets block in {path}")

    if runset_id is None:
        return payload

    entry = runsets.get(runset_id)
    if not isinstance(entry, dict):
        raise ValidationError(f"runset_id not found in baseline index: {runset_id}")

    return {
        "runset_id": runset_id,
        **{key: entry[key] for key in sorted(entry.keys())},
    }
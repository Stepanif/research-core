from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.baselines.contracts import BASELINE_PROMOTIONS_FILE, BASELINE_PROMOTIONS_VERSION
from research_core.baselines.io import read_json_object, write_json_object
from research_core.baselines.resolve import resolve_baseline
from research_core.util.buildmeta import get_created_utc
from research_core.util.types import ValidationError


def baseline_promotions_path(root: Path) -> Path:
    return root / BASELINE_PROMOTIONS_FILE


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="Baseline promote requires RESEARCH_CREATED_UTC")


def _load_or_init(path: Path, created_utc: str) -> dict[str, Any]:
    if not path.exists():
        return {
            "promotions_version": BASELINE_PROMOTIONS_VERSION,
            "created_utc": created_utc,
            "labels": {},
        }

    payload = read_json_object(path)
    if payload.get("promotions_version") != BASELINE_PROMOTIONS_VERSION:
        raise ValidationError(f"Unsupported baseline promotions version in {path}")
    labels = payload.get("labels")
    if not isinstance(labels, dict):
        raise ValidationError(f"Invalid labels block in {path}")
    return payload


def promote_baseline(*, root: Path, runset_id: str, baseline_id: str, label: str) -> dict[str, Any]:
    created_utc = _require_created_utc()
    if not isinstance(label, str) or not label:
        raise ValidationError("label must be a non-empty string")
    if not isinstance(runset_id, str) or not runset_id:
        raise ValidationError("runset_id must be a non-empty string")
    if not isinstance(baseline_id, str) or not baseline_id:
        raise ValidationError("baseline_id must be a non-empty string")

    resolved = resolve_baseline(root=root, runset_id=runset_id)
    if resolved["baseline_id"] != baseline_id:
        raise ValidationError(
            f"baseline_id mismatch for runset_id={runset_id}: provided baseline_id does not match on-disk baseline"
        )

    path = baseline_promotions_path(root)
    payload = _load_or_init(path, created_utc=created_utc)
    labels = payload.get("labels", {})
    assert isinstance(labels, dict)

    label_map = labels.get(label)
    if label_map is None:
        label_map = {}
    if not isinstance(label_map, dict):
        raise ValidationError(f"Invalid promotion mapping for label={label}")

    existing = label_map.get(runset_id)
    if isinstance(existing, str) and existing != baseline_id:
        raise ValidationError(
            f"Baseline promotions immutability violation for label={label} runset_id={runset_id}: existing baseline_id differs"
        )

    if existing == baseline_id:
        return {
            "promotions_version": BASELINE_PROMOTIONS_VERSION,
            "created_utc": payload.get("created_utc", created_utc),
            "labels": {
                key: {runset: labels[key][runset] for runset in sorted(labels[key].keys())}
                for key in sorted(labels.keys())
            },
        }

    label_map[runset_id] = baseline_id
    labels[label] = {runset: label_map[runset] for runset in sorted(label_map.keys())}

    output = {
        "promotions_version": BASELINE_PROMOTIONS_VERSION,
        "created_utc": created_utc,
        "labels": {
            key: {runset: labels[key][runset] for runset in sorted(labels[key].keys())}
            for key in sorted(labels.keys())
        },
    }
    write_json_object(path, output)
    return output
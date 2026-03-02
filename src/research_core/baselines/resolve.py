from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.baselines.contracts import (
    BASELINE_CARD_FILE,
    BASELINE_CARD_VERSION,
    BASELINE_INDEX_FILE,
    BASELINE_INDEX_VERSION,
    BASELINE_PROMOTIONS_FILE,
    BASELINE_PROMOTIONS_VERSION,
    DEFAULT_LABEL_PRIORITY,
)
from research_core.baselines.io import read_json_object
from research_core.util.types import ValidationError


def _require_non_empty(value: Any, field_name: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValidationError(f"Missing or invalid field: {field_name}")
    return value


def _disk_candidate(root: Path, runset_id: str) -> dict[str, str]:
    card_path = root / runset_id / BASELINE_CARD_FILE
    if not card_path.exists() or not card_path.is_file():
        raise ValidationError(f"Missing baseline card for runset_id={runset_id}: {card_path}")

    card_payload = read_json_object(card_path)
    card_version = card_payload.get("card_version")
    if card_version != BASELINE_CARD_VERSION:
        raise ValidationError(f"Unsupported baseline card version for runset_id={runset_id}: {card_version}")

    checksums = card_payload.get("checksums")
    if not isinstance(checksums, dict):
        raise ValidationError(f"Invalid baseline card checksums for runset_id={runset_id}")
    baseline_id = _require_non_empty(checksums.get("per_run_vector_sha256"), "checksums.per_run_vector_sha256")

    return {
        "runset_id": runset_id,
        "baseline_id": baseline_id,
        "card_path": card_path.resolve().as_posix(),
    }


def _validate_index_if_present(root: Path, runset_id: str, disk: dict[str, str]) -> None:
    index_path = root / BASELINE_INDEX_FILE
    if not index_path.exists():
        return

    payload = read_json_object(index_path)
    if payload.get("index_version") != BASELINE_INDEX_VERSION:
        raise ValidationError(f"Unsupported baseline index version in {index_path}")
    runsets = payload.get("runsets")
    if not isinstance(runsets, dict):
        raise ValidationError(f"Invalid runsets block in {index_path}")

    entry = runsets.get(runset_id)
    if not isinstance(entry, dict):
        raise ValidationError(f"baseline.index.json missing runset_id={runset_id}; run baseline index refresh")

    entry_baseline_id = _require_non_empty(entry.get("baseline_id"), "runsets.<runset_id>.baseline_id")
    if entry_baseline_id != disk["baseline_id"]:
        raise ValidationError(
            f"baseline.index.json mismatch for runset_id={runset_id}: index baseline_id differs from on-disk baseline"
        )


def _read_promotions(root: Path) -> dict[str, Any] | None:
    path = root / BASELINE_PROMOTIONS_FILE
    if not path.exists():
        return None

    payload = read_json_object(path)
    if payload.get("promotions_version") != BASELINE_PROMOTIONS_VERSION:
        raise ValidationError(f"Unsupported baseline promotions version in {path}")
    labels = payload.get("labels")
    if not isinstance(labels, dict):
        raise ValidationError(f"Invalid labels block in {path}")
    return payload


def _resolve_with_label(*, root: Path, runset_id: str, disk: dict[str, str], label: str) -> dict[str, str]:
    promotions = _read_promotions(root)
    if promotions is None:
        raise ValidationError(f"Missing baseline promotions file for label resolution: {root / BASELINE_PROMOTIONS_FILE}")

    labels = promotions["labels"]
    label_map = labels.get(label)
    if not isinstance(label_map, dict):
        raise ValidationError(f"Missing baseline promotion label={label}")

    promoted = label_map.get(runset_id)
    if not isinstance(promoted, str) or not promoted:
        raise ValidationError(f"Missing baseline promotion mapping for label={label} runset_id={runset_id}")
    if promoted != disk["baseline_id"]:
        raise ValidationError(
            f"Baseline promotion mismatch for label={label} runset_id={runset_id}: promoted baseline_id differs from on-disk baseline"
        )

    return {
        "runset_id": runset_id,
        "baseline_id": promoted,
        "card_path": disk["card_path"],
        "label": label,
    }


def resolve_baseline(*, root: Path, runset_id: str, label: str | None = None) -> dict[str, str]:
    disk = _disk_candidate(root=root, runset_id=runset_id)
    _validate_index_if_present(root=root, runset_id=runset_id, disk=disk)

    if isinstance(label, str) and label:
        return _resolve_with_label(root=root, runset_id=runset_id, disk=disk, label=label)

    promotions = _read_promotions(root)
    if isinstance(promotions, dict):
        labels = promotions["labels"]
        for candidate in DEFAULT_LABEL_PRIORITY:
            label_map = labels.get(candidate)
            if not isinstance(label_map, dict):
                continue
            promoted = label_map.get(runset_id)
            if not isinstance(promoted, str) or not promoted:
                continue
            if promoted != disk["baseline_id"]:
                raise ValidationError(
                    f"Baseline promotion mismatch for label={candidate} runset_id={runset_id}: promoted baseline_id differs from on-disk baseline"
                )
            return {
                "runset_id": runset_id,
                "baseline_id": promoted,
                "card_path": disk["card_path"],
                "label": candidate,
            }

    return {
        "runset_id": runset_id,
        "baseline_id": disk["baseline_id"],
        "card_path": disk["card_path"],
    }
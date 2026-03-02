from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.baselines.contracts import BASELINE_CARD_FILE
from research_core.runsets.io import read_json, write_canonical_json
from research_core.util.types import ValidationError


def read_json_object(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    if not isinstance(payload, dict):
        raise ValidationError(f"Invalid JSON object payload: {path}")
    return payload


def write_json_object(path: Path, payload: dict[str, Any]) -> None:
    write_canonical_json(path, payload)


def baseline_card_path(root: Path, runset_id: str) -> Path:
    return root / runset_id / BASELINE_CARD_FILE
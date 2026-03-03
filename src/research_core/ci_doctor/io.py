from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_core.util.types import ValidationError


def read_json_object(path: Path, *, name: str) -> dict[str, Any]:
    if not path.exists() or not path.is_file():
        raise ValidationError(f"Missing {name}: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid JSON for {name}: {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValidationError(f"Expected JSON object for {name}: {path}")
    return payload


def read_runset_ids(path: Path) -> list[str]:
    payload = read_json_object(path, name="runsets file")
    if set(payload.keys()) != {"runset_ids"}:
        raise ValidationError("runsets file supports only object key 'runset_ids'")
    runset_ids = payload.get("runset_ids")
    if not isinstance(runset_ids, list):
        raise ValidationError("runsets file field 'runset_ids' must be an array")

    seen: set[str] = set()
    out: list[str] = []
    for index, value in enumerate(runset_ids):
        if not isinstance(value, str) or not value:
            raise ValidationError(f"runset_ids[{index}] must be non-empty string")
        if value in seen:
            raise ValidationError(f"Duplicate runset_id in runsets file: {value}")
        seen.add(value)
        out.append(value)
    return sorted(out)

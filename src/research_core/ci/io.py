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

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def canonical_json_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")


def write_plan_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical_json_bytes(payload))


def read_plan_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

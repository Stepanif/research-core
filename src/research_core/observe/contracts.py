from __future__ import annotations

from typing import Any

from research_core.util.types import ValidationError

OBSERVE_MANIFEST_VERSION = "v1"
OBSERVE_TOOL_VERSION = "observer v1"

BIT_NAMES: dict[int, str] = {
    0: "STATE_CHANGE",
    1: "P_CHANGE",
    2: "S_CHANGE",
    3: "A_CHANGE",
    4: "P_FLIP",
    5: "S_FLIP",
    6: "A_FLIP",
}


def ordered_bit_names() -> list[str]:
    return [BIT_NAMES[index] for index in sorted(BIT_NAMES.keys())]


def require_manifest_field(payload: dict[str, Any], key: str) -> Any:
    if key not in payload:
        raise ValidationError(f"Missing required manifest field: {key}")
    return payload[key]


def assert_invariant(name: str, condition: bool, message: str) -> dict[str, Any]:
    if not condition:
        raise ValidationError(f"Invariant failed [{name}]: {message}")
    return {"name": name, "pass": True}

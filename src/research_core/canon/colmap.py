from __future__ import annotations

from typing import Any

from research_core.util.types import ContractError

REQUIRED_RAW_COLUMNS = ["Date", "Time", "Open", "High", "Low", "Close", "Up", "Down"]


def validate_colmap(colmap_payload: dict[str, Any]) -> dict[str, str]:
    mapping = colmap_payload.get("mapping")
    if not isinstance(mapping, dict):
        raise ContractError("colmap.mapping must be an object")
    for raw_col in REQUIRED_RAW_COLUMNS:
        if raw_col not in mapping:
            raise ContractError(f"colmap missing required raw column mapping: {raw_col}")
    return {str(k): str(v) for k, v in mapping.items()}

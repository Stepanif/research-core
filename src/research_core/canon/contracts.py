from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from research_core.util.io import read_json
from research_core.util.types import ContractError


@dataclass(frozen=True)
class SessionPolicy:
    name: str
    rth_start: str
    rth_end: str


@dataclass(frozen=True)
class CanonContract:
    schema_path: Path
    schema_version: str
    colmap_path: Path
    colmap_version: str
    keep_updown: bool
    include_instrument_tf_columns: bool
    session_policy: SessionPolicy


def _require_version(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value:
        raise ContractError(f"Missing required contract field: {key}")
    return value


def load_schema_contract(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    _require_version(payload, "schema_version")
    required_columns = payload.get("required_columns")
    if not isinstance(required_columns, list) or not required_columns:
        raise ContractError("Schema contract must declare non-empty required_columns")
    return payload


def load_colmap_contract(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    _require_version(payload, "colmap_version")
    mapping = payload.get("mapping")
    if not isinstance(mapping, dict) or not mapping:
        raise ContractError("Colmap contract must declare mapping")
    return payload

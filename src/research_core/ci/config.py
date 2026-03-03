from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.ci.contracts import CI_VERSION
from research_core.ci.io import read_json_object
from research_core.util.types import ValidationError


def _require_str(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value:
        raise ValidationError(f"ci config requires non-empty string field: {key}")
    return value


def _optional_bool(payload: dict[str, Any], key: str, default: bool) -> bool:
    value = payload.get(key)
    if value is None:
        return default
    if not isinstance(value, bool):
        raise ValidationError(f"ci config field must be boolean: {key}")
    return value


def _optional_str(payload: dict[str, Any], key: str, default: str) -> str:
    value = payload.get(key)
    if value is None:
        return default
    if not isinstance(value, str) or not value:
        raise ValidationError(f"ci config field must be non-empty string when provided: {key}")
    return value


def load_ci_config(config_path: Path) -> dict[str, Any]:
    payload = read_json_object(config_path, name="ci config")

    allowed = {
        "ci_version",
        "created_utc",
        "catalog_dir",
        "baseline_root",
        "runsets_path",
        "out_dir",
        "label",
        "fail_on_drift",
        "fail_on_checksum_mismatch",
    }
    extra = sorted(key for key in payload.keys() if key not in allowed)
    if extra:
        raise ValidationError(f"ci config has unsupported fields: {extra}")

    version = payload.get("ci_version")
    if version != CI_VERSION:
        raise ValidationError(f"Unsupported ci config version: {version}")

    catalog_dir = Path(_require_str(payload, "catalog_dir"))
    baseline_root = Path(_require_str(payload, "baseline_root"))
    runsets_path = Path(_require_str(payload, "runsets_path"))
    out_dir = Path(_require_str(payload, "out_dir"))

    return {
        "ci_version": CI_VERSION,
        "config_path": config_path,
        "catalog_dir": catalog_dir,
        "baseline_root": baseline_root,
        "runsets_path": runsets_path,
        "out_dir": out_dir,
        "label": _optional_str(payload, "label", "prod"),
        "fail_on_drift": _optional_bool(payload, "fail_on_drift", True),
        "fail_on_checksum_mismatch": _optional_bool(payload, "fail_on_checksum_mismatch", True),
    }

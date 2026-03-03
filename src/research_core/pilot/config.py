from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.pilot.contracts import (
    DEFAULT_DOCTOR_OUT_SUBDIR,
    DEFAULT_DRIFT_OUT_SUBDIR,
    DEFAULT_LABEL,
    DEFAULT_REQUIRE_PROMOTED_BASELINE,
    PILOT_OPS_SCHEMA_PATH,
    PILOT_OPS_VERSION,
    PILOT_RUNSET_KIND,
)
from research_core.runsets.io import read_json
from research_core.util.types import ValidationError


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _resolve_schema_path(schema_path: Path) -> Path:
    resolved = schema_path
    if not resolved.is_absolute() and not resolved.exists():
        repo_schema = (_repo_root() / resolved).resolve()
        if repo_schema.exists():
            resolved = repo_schema
    if not resolved.exists() or not resolved.is_file():
        raise ValidationError(f"Pilot ops schema file does not exist: {schema_path}")
    return resolved


def _require_str(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value:
        raise ValidationError(f"pilot ops config requires non-empty string field: {key}")
    return value


def _optional_str(payload: dict[str, Any], key: str, default: str) -> str:
    value = payload.get(key)
    if value is None:
        return default
    if not isinstance(value, str) or not value:
        raise ValidationError(f"pilot ops config field must be non-empty string when provided: {key}")
    return value


def _optional_bool(payload: dict[str, Any], key: str, default: bool) -> bool:
    value = payload.get(key)
    if value is None:
        return default
    if not isinstance(value, bool):
        raise ValidationError(f"pilot ops config field must be boolean: {key}")
    return value


def load_pilot_ops_config(config_path: Path, schema_path: Path = PILOT_OPS_SCHEMA_PATH) -> dict[str, Any]:
    if not config_path.exists() or not config_path.is_file():
        raise ValidationError(f"Pilot ops config file does not exist: {config_path}")

    resolved_schema_path = _resolve_schema_path(schema_path)

    payload = read_json(config_path)
    schema_payload = read_json(resolved_schema_path)
    allowed = {
        "pilot_ops_version",
        "catalog_dir",
        "datasets_path",
        "baseline_root",
        "label",
        "out_dir",
        "runset_kind",
        "require_promoted_baseline",
        "doctor_out_subdir",
        "drift_out_subdir",
    }
    extras = sorted(key for key in payload.keys() if key not in allowed)
    if extras:
        raise ValidationError(f"pilot ops config has unsupported fields: {extras}")

    expected_version = schema_payload.get("properties", {}).get("pilot_ops_version", {}).get("const", PILOT_OPS_VERSION)
    version = _require_str(payload, "pilot_ops_version")
    if version != expected_version:
        raise ValidationError(f"Unsupported pilot_ops_version: {version}")

    expected_kind = schema_payload.get("properties", {}).get("runset_kind", {}).get("const", PILOT_RUNSET_KIND)
    runset_kind = _require_str(payload, "runset_kind")
    if runset_kind != expected_kind:
        raise ValidationError(f"Unsupported runset_kind: {runset_kind}")

    require_promoted_baseline = _optional_bool(
        payload,
        "require_promoted_baseline",
        DEFAULT_REQUIRE_PROMOTED_BASELINE,
    )
    if require_promoted_baseline is not True:
        raise ValidationError("pilot ops config require_promoted_baseline must be true in v1")

    return {
        "pilot_ops_version": PILOT_OPS_VERSION,
        "config_path": config_path,
        "catalog_dir": Path(_require_str(payload, "catalog_dir")),
        "datasets_path": Path(_require_str(payload, "datasets_path")),
        "baseline_root": Path(_require_str(payload, "baseline_root")),
        "label": _optional_str(payload, "label", DEFAULT_LABEL),
        "out_dir": Path(_require_str(payload, "out_dir")),
        "runset_kind": PILOT_RUNSET_KIND,
        "require_promoted_baseline": True,
        "doctor_out_subdir": _optional_str(payload, "doctor_out_subdir", DEFAULT_DOCTOR_OUT_SUBDIR),
        "drift_out_subdir": _optional_str(payload, "drift_out_subdir", DEFAULT_DRIFT_OUT_SUBDIR),
    }

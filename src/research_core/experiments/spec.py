from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.util.io import read_json
from research_core.util.types import ValidationError

DEFAULT_SPEC_SCHEMA_PATH = Path("schemas/experiment.spec.schema.v1.json")


def _require_string(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value:
        raise ValidationError(f"Experiment spec missing required string field: {key}")
    return value


def load_experiment_spec(
    spec_path: Path,
    schema_path: Path = DEFAULT_SPEC_SCHEMA_PATH,
) -> dict[str, Any]:
    if not spec_path.exists():
        raise ValidationError(f"Experiment spec file does not exist: {spec_path}")
    if not schema_path.exists():
        raise ValidationError(f"Experiment spec schema file does not exist: {schema_path}")

    payload = read_json(spec_path)
    schema_payload = read_json(schema_path)

    if not isinstance(payload, dict):
        raise ValidationError("Experiment spec must be a JSON object")

    allowed_top = {"spec_version", "kind", "params"}
    unexpected_top = sorted([key for key in payload.keys() if key not in allowed_top])
    if unexpected_top:
        raise ValidationError(f"Experiment spec contains unsupported top-level fields: {unexpected_top}")

    spec_version = _require_string(payload, "spec_version")
    expected_spec_version = schema_payload.get("properties", {}).get("spec_version", {}).get("const", "v1")
    if spec_version != expected_spec_version:
        raise ValidationError(f"Unsupported experiment spec_version: {spec_version}")

    kind = _require_string(payload, "kind")
    expected_kind = schema_payload.get("properties", {}).get("kind", {}).get("const", "transition_matrix")
    if kind != expected_kind:
        raise ValidationError(f"Unsupported experiment kind: {kind}")

    params_raw = payload.get("params")
    if params_raw is None:
        params_raw = {}
    if not isinstance(params_raw, dict):
        raise ValidationError("Experiment spec params must be a JSON object")

    allowed_params = {"transition_scope", "include_event_bits"}
    unexpected_params = sorted([key for key in params_raw.keys() if key not in allowed_params])
    if unexpected_params:
        raise ValidationError(f"Experiment spec contains unsupported params fields: {unexpected_params}")

    transition_scope = params_raw.get("transition_scope", "global")
    if not isinstance(transition_scope, str):
        raise ValidationError("Experiment spec params.transition_scope must be a string")
    expected_scope = (
        schema_payload.get("properties", {})
        .get("params", {})
        .get("properties", {})
        .get("transition_scope", {})
        .get("const", "global")
    )
    if transition_scope != expected_scope:
        raise ValidationError(f"Unsupported params.transition_scope: {transition_scope}")

    include_event_bits = params_raw.get("include_event_bits", False)
    if not isinstance(include_event_bits, bool):
        raise ValidationError("Experiment spec params.include_event_bits must be boolean")

    return {
        "spec_version": spec_version,
        "kind": kind,
        "params": {
            "transition_scope": transition_scope,
            "include_event_bits": include_event_bits,
        },
    }

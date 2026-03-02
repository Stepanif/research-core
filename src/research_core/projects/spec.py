from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.util.io import read_json
from research_core.util.types import ValidationError

DEFAULT_PROJECT_SCHEMA_PATH = Path("schemas/project.schema.v1.json")


def _require_string(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value:
        raise ValidationError(f"Project spec missing required string field: {key}")
    return value


def _require_string_list(payload: dict[str, Any], key: str) -> list[str]:
    value = payload.get(key)
    if not isinstance(value, list) or not value:
        raise ValidationError(f"Project spec missing required non-empty list field: {key}")
    output: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item:
            raise ValidationError(f"Project spec field {key} contains invalid item: {item}")
        output.append(item)
    return output


def load_project_spec(spec_path: Path, schema_path: Path = DEFAULT_PROJECT_SCHEMA_PATH) -> dict[str, Any]:
    if not spec_path.exists():
        raise ValidationError(f"Project spec file does not exist: {spec_path}")
    if not schema_path.exists():
        raise ValidationError(f"Project schema file does not exist: {schema_path}")

    payload = read_json(spec_path)
    if not isinstance(payload, dict):
        raise ValidationError("Project spec must be a JSON object")

    allowed = {"project_version", "name", "created_utc", "runs", "spec_dirs", "output_dir", "policy", "notes"}
    unexpected = sorted([key for key in payload.keys() if key not in allowed])
    if unexpected:
        raise ValidationError(f"Project spec contains unsupported fields: {unexpected}")

    project_version = _require_string(payload, "project_version")
    if project_version != "v1":
        raise ValidationError(f"Unsupported project_version: {project_version}")

    name = _require_string(payload, "name")
    runs = _require_string_list(payload, "runs")
    spec_dirs = _require_string_list(payload, "spec_dirs")
    output_dir = _require_string(payload, "output_dir")

    policy_raw = payload.get("policy")
    if not isinstance(policy_raw, dict):
        raise ValidationError("Project spec requires policy object")

    allowed_policy = {"fail_fast", "require_observe"}
    unexpected_policy = sorted([key for key in policy_raw.keys() if key not in allowed_policy])
    if unexpected_policy:
        raise ValidationError(f"Project spec policy contains unsupported fields: {unexpected_policy}")

    fail_fast = policy_raw.get("fail_fast", True)
    if fail_fast is not True:
        raise ValidationError("Project spec policy.fail_fast must be true for v1")

    require_observe = policy_raw.get("require_observe", False)
    if not isinstance(require_observe, bool):
        raise ValidationError("Project spec policy.require_observe must be boolean")

    notes = payload.get("notes")
    if notes is not None and not isinstance(notes, str):
        raise ValidationError("Project spec notes must be string when provided")

    return {
        "project_version": "v1",
        "name": name,
        "runs": [Path(item).as_posix() for item in runs],
        "spec_dirs": [Path(item).as_posix() for item in spec_dirs],
        "output_dir": Path(output_dir).as_posix(),
        "policy": {
            "fail_fast": True,
            "require_observe": require_observe,
        },
        **({"notes": notes} if isinstance(notes, str) else {}),
    }

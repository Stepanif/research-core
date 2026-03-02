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

    resolved_schema_path = schema_path
    if not resolved_schema_path.is_absolute() and not resolved_schema_path.exists():
        repo_root_schema = (Path(__file__).resolve().parents[3] / resolved_schema_path).resolve()
        if repo_root_schema.exists():
            resolved_schema_path = repo_root_schema

    if not resolved_schema_path.exists():
        raise ValidationError(f"Project schema file does not exist: {schema_path}")

    payload = read_json(spec_path)
    if not isinstance(payload, dict):
        raise ValidationError("Project spec must be a JSON object")

    allowed = {"project_version", "name", "created_utc", "runs", "datasets", "spec_dirs", "output_dir", "policy", "notes"}
    unexpected = sorted([key for key in payload.keys() if key not in allowed])
    if unexpected:
        raise ValidationError(f"Project spec contains unsupported fields: {unexpected}")

    project_version = _require_string(payload, "project_version")
    if project_version != "v1":
        raise ValidationError(f"Unsupported project_version: {project_version}")

    name = _require_string(payload, "name")
    has_runs = "runs" in payload
    has_datasets = "datasets" in payload
    if has_runs == has_datasets:
        raise ValidationError("Project spec must include exactly one of runs or datasets")

    runs = _require_string_list(payload, "runs") if has_runs else None
    datasets_raw = payload.get("datasets") if has_datasets else None
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

    datasets: list[dict[str, Any]] | None = None
    if has_datasets:
        if not isinstance(datasets_raw, list) or not datasets_raw:
            raise ValidationError("Project spec datasets must be a non-empty list")
        datasets = []
        for item in datasets_raw:
            if not isinstance(item, dict):
                raise ValidationError("Project spec datasets contains non-object entry")

            allowed_dataset = {
                "dataset_id",
                "instrument",
                "tf",
                "session_policy",
                "rth_start",
                "rth_end",
                "schema_path",
                "colmap_path",
                "note",
            }
            unexpected_dataset = sorted([key for key in item.keys() if key not in allowed_dataset])
            if unexpected_dataset:
                raise ValidationError(f"Project dataset ref contains unsupported fields: {unexpected_dataset}")

            dataset_id = _require_string(item, "dataset_id")
            instrument = _require_string(item, "instrument")
            tf = _require_string(item, "tf")
            session_policy = _require_string(item, "session_policy")
            if session_policy not in {"full", "rth", "eth"}:
                raise ValidationError(f"Project dataset ref has unsupported session_policy: {session_policy}")

            schema_path_value = _require_string(item, "schema_path")
            colmap_path_value = _require_string(item, "colmap_path")

            dataset_entry: dict[str, Any] = {
                "dataset_id": dataset_id,
                "instrument": instrument,
                "tf": tf,
                "session_policy": session_policy,
                "schema_path": Path(schema_path_value).as_posix(),
                "colmap_path": Path(colmap_path_value).as_posix(),
            }

            if session_policy == "rth":
                dataset_entry["rth_start"] = _require_string(item, "rth_start")
                dataset_entry["rth_end"] = _require_string(item, "rth_end")
            else:
                if "rth_start" in item:
                    rth_start = item.get("rth_start")
                    if not isinstance(rth_start, str) or not rth_start:
                        raise ValidationError("Project dataset ref rth_start must be non-empty string when provided")
                    dataset_entry["rth_start"] = rth_start
                if "rth_end" in item:
                    rth_end = item.get("rth_end")
                    if not isinstance(rth_end, str) or not rth_end:
                        raise ValidationError("Project dataset ref rth_end must be non-empty string when provided")
                    dataset_entry["rth_end"] = rth_end

            note = item.get("note")
            if note is not None:
                if not isinstance(note, str):
                    raise ValidationError("Project dataset ref note must be string when provided")
                dataset_entry["note"] = note

            datasets.append(dataset_entry)

    result = {
        "project_version": "v1",
        "name": name,
        "spec_dirs": [Path(item).as_posix() for item in spec_dirs],
        "output_dir": Path(output_dir).as_posix(),
        "policy": {
            "fail_fast": True,
            "require_observe": require_observe,
        },
        **({"notes": notes} if isinstance(notes, str) else {}),
    }
    if runs is not None:
        result["runs"] = [Path(item).as_posix() for item in runs]
    if datasets is not None:
        result["datasets"] = datasets
    return result

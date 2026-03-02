from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from research_core.runsets.contracts import DEFAULT_POLICY, DEFAULT_REQUIRED_ARTIFACTS, REQUIRED_ENV_VAR_CREATED_UTC, RUNSET_VERSION
from research_core.runsets.io import canonical_hash, read_json
from research_core.util.types import ValidationError

DEFAULT_RUNSET_SCHEMA_PATH = Path("schemas/runset.schema.v1.json")


def _require_created_utc() -> str:
    value = os.environ.get(REQUIRED_ENV_VAR_CREATED_UTC)
    if not isinstance(value, str) or not value:
        raise ValidationError("RunSet operations require RESEARCH_CREATED_UTC")
    return value


def _require_string(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value:
        raise ValidationError(f"RunSet spec missing required string field: {key}")
    return value


def _normalize_required_artifacts(payload: dict[str, Any] | None) -> dict[str, bool]:
    if payload is None:
        return dict(DEFAULT_REQUIRED_ARTIFACTS)
    if not isinstance(payload, dict):
        raise ValidationError("RunSet run ref required_artifacts must be object")

    allowed = set(DEFAULT_REQUIRED_ARTIFACTS.keys())
    unexpected = sorted([key for key in payload.keys() if key not in allowed])
    if unexpected:
        raise ValidationError(f"RunSet run ref required_artifacts has unsupported fields: {unexpected}")

    normalized: dict[str, bool] = {}
    for key, default_value in DEFAULT_REQUIRED_ARTIFACTS.items():
        value = payload.get(key, default_value)
        if not isinstance(value, bool):
            raise ValidationError(f"RunSet run ref required_artifacts.{key} must be boolean")
        normalized[key] = value
    return normalized


def _normalize_runs(payload: dict[str, Any]) -> list[dict[str, Any]]:
    raw_runs = payload.get("runs", [])
    if not isinstance(raw_runs, list):
        raise ValidationError("RunSet spec runs must be a list")

    normalized: list[dict[str, Any]] = []
    for item in raw_runs:
        if not isinstance(item, dict):
            raise ValidationError("RunSet spec runs contains non-object entry")

        allowed = {"run_ref", "dataset_id", "canon_table_sha256", "required_artifacts"}
        unexpected = sorted([key for key in item.keys() if key not in allowed])
        if unexpected:
            raise ValidationError(f"RunSet run ref contains unsupported fields: {unexpected}")

        run_ref = _require_string(item, "run_ref")

        row: dict[str, Any] = {"run_ref": run_ref}
        dataset_id = item.get("dataset_id")
        if dataset_id is not None:
            if not isinstance(dataset_id, str) or not dataset_id:
                raise ValidationError("RunSet run ref dataset_id must be a non-empty string when provided")
            row["dataset_id"] = dataset_id

        canon_table_sha256 = item.get("canon_table_sha256")
        if canon_table_sha256 is not None:
            if not isinstance(canon_table_sha256, str) or not canon_table_sha256:
                raise ValidationError("RunSet run ref canon_table_sha256 must be a non-empty string when provided")
            row["canon_table_sha256"] = canon_table_sha256

        row["required_artifacts"] = _normalize_required_artifacts(item.get("required_artifacts"))
        normalized.append(row)

    return sorted(
        normalized,
        key=lambda item: (
            str(item.get("dataset_id", "")),
            str(item.get("canon_table_sha256", "")),
            str(item.get("run_ref", "")),
        ),
    )


def _normalize_policy(payload: dict[str, Any]) -> dict[str, bool]:
    raw_policy = payload.get("policy", {})
    if not isinstance(raw_policy, dict):
        raise ValidationError("RunSet spec policy must be object")

    allowed = set(DEFAULT_POLICY.keys())
    unexpected = sorted([key for key in raw_policy.keys() if key not in allowed])
    if unexpected:
        raise ValidationError(f"RunSet policy contains unsupported fields: {unexpected}")

    normalized: dict[str, bool] = {}
    for key, default_value in DEFAULT_POLICY.items():
        value = raw_policy.get(key, default_value)
        if not isinstance(value, bool):
            raise ValidationError(f"RunSet policy {key} must be boolean")
        normalized[key] = value
    return normalized


def _normalize_datasets(payload: dict[str, Any]) -> list[str]:
    raw = payload.get("datasets")
    if not isinstance(raw, list):
        raise ValidationError("RunSet spec datasets must be a list")
    if not raw:
        raise ValidationError("RunSet spec datasets must be non-empty")

    values: list[str] = []
    for item in raw:
        if not isinstance(item, str) or not item:
            raise ValidationError("RunSet spec datasets contains invalid dataset_id")
        values.append(item)

    return sorted(set(values))


def _fingerprint_payload(*, datasets: list[str], runs: list[dict[str, Any]], policy: dict[str, bool]) -> dict[str, str]:
    return {
        "datasets_sha256": canonical_hash({"datasets": datasets}),
        "runs_sha256": canonical_hash({"runs": runs}),
        "policy_sha256": canonical_hash({"policy": policy}),
    }


def load_runset_spec(spec_path: Path, schema_path: Path = DEFAULT_RUNSET_SCHEMA_PATH) -> dict[str, Any]:
    if not spec_path.exists():
        raise ValidationError(f"RunSet spec file does not exist: {spec_path}")

    resolved_schema_path = schema_path
    if not resolved_schema_path.is_absolute() and not resolved_schema_path.exists():
        repo_root_schema = (Path(__file__).resolve().parents[3] / resolved_schema_path).resolve()
        if repo_root_schema.exists():
            resolved_schema_path = repo_root_schema
    if not resolved_schema_path.exists():
        raise ValidationError(f"RunSet schema file does not exist: {schema_path}")

    payload = read_json(spec_path)
    if not isinstance(payload, dict):
        raise ValidationError("RunSet spec must be a JSON object")

    allowed = {
        "runset_version",
        "runset_id",
        "created_utc",
        "name",
        "datasets",
        "runs",
        "policy",
        "fingerprint",
        "runset_entry_canonical_sha256",
    }
    unexpected = sorted([key for key in payload.keys() if key not in allowed])
    if unexpected:
        raise ValidationError(f"RunSet spec contains unsupported fields: {unexpected}")

    runset_version = _require_string(payload, "runset_version")
    if runset_version != RUNSET_VERSION:
        raise ValidationError(f"Unsupported runset_version: {runset_version}")

    created_utc = _require_created_utc()
    datasets = _normalize_datasets(payload)
    runs = _normalize_runs(payload)
    policy = _normalize_policy(payload)

    fingerprint = _fingerprint_payload(datasets=datasets, runs=runs, policy=policy)

    normalized: dict[str, Any] = {
        "runset_version": RUNSET_VERSION,
        "created_utc": created_utc,
        "datasets": datasets,
        "runs": runs,
        "policy": policy,
        "fingerprint": fingerprint,
    }

    name = payload.get("name")
    if name is not None:
        if not isinstance(name, str) or not name:
            raise ValidationError("RunSet spec name must be a non-empty string when provided")
        normalized["name"] = name

    return normalized

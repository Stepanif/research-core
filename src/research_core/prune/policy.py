from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_core.prune.contracts import PRUNE_POLICY_VERSION
from research_core.util.types import ValidationError


def _read_json_object(path: Path) -> dict[str, Any]:
    if not path.exists() or not path.is_file():
        raise ValidationError(f"Missing prune policy file: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Invalid prune policy JSON: {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValidationError("Prune policy must be a JSON object")
    return payload


def _require_bool(payload: dict[str, Any], key: str) -> bool:
    value = payload.get(key)
    if not isinstance(value, bool):
        raise ValidationError(f"Prune policy field must be boolean: {key}")
    return value


def _require_int(payload: dict[str, Any], key: str) -> int:
    value = payload.get(key)
    if not isinstance(value, int) or value < 0:
        raise ValidationError(f"Prune policy field must be non-negative integer: {key}")
    return value


def load_prune_policy(policy_path: Path) -> dict[str, Any]:
    payload = _read_json_object(policy_path)
    if payload.get("policy_version") != PRUNE_POLICY_VERSION:
        raise ValidationError(f"Unsupported prune policy version: {payload.get('policy_version')}")

    keep = payload.get("keep")
    delete = payload.get("delete")
    safety = payload.get("safety")
    if not isinstance(keep, dict) or not isinstance(delete, dict) or not isinstance(safety, dict):
        raise ValidationError("Prune policy must include object sections: keep, delete, safety")

    baselines = keep.get("baselines")
    if not isinstance(baselines, dict):
        raise ValidationError("Prune policy keep.baselines must be an object")
    ci_outputs = keep.get("ci_outputs")
    if ci_outputs is not None and not isinstance(ci_outputs, dict):
        raise ValidationError("Prune policy keep.ci_outputs must be an object when provided")

    plan_logs = delete.get("plan_logs")
    if not isinstance(plan_logs, dict):
        raise ValidationError("Prune policy delete.plan_logs must be an object")

    return {
        "policy_version": PRUNE_POLICY_VERSION,
        "path": policy_path,
        "keep": {
            "manifests": _require_bool(keep, "manifests"),
            "contracts": _require_bool(keep, "contracts"),
            "goldens": _require_bool(keep, "goldens"),
            "baselines": {
                "promoted_only": _require_bool(baselines, "promoted_only"),
                "keep_index": _require_bool(baselines, "keep_index"),
            },
            "ci_outputs": {
                "keep_latest_n": _require_int(ci_outputs, "keep_latest_n")
            }
            if isinstance(ci_outputs, dict)
            else None,
        },
        "delete": {
            "run_intermediates": _require_bool(delete, "run_intermediates"),
            "plan_logs": {
                "keep_latest_n": _require_int(plan_logs, "keep_latest_n"),
            },
        },
        "safety": {
            "require_dry_run_first": _require_bool(safety, "require_dry_run_first"),
            "refuse_if_unrecognized_paths": _require_bool(safety, "refuse_if_unrecognized_paths"),
        },
    }

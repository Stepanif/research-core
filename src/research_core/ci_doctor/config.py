from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.ci_doctor.contracts import CI_DOCTOR_VERSION
from research_core.ci_doctor.io import read_json_object
from research_core.util.types import ValidationError


def _require_str(payload: dict[str, Any], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value:
        raise ValidationError(f"ci doctor config requires non-empty string: {key}")
    return value


def _optional_str(payload: dict[str, Any], key: str, default: str) -> str:
    value = payload.get(key)
    if value is None:
        return default
    if not isinstance(value, str) or not value:
        raise ValidationError(f"ci doctor config field must be non-empty string when provided: {key}")
    return value


def _optional_bool(payload: dict[str, Any], key: str, default: bool) -> bool:
    value = payload.get(key)
    if value is None:
        return default
    if not isinstance(value, bool):
        raise ValidationError(f"ci doctor config field must be boolean: {key}")
    return value


def _required_true(payload: dict[str, Any], key: str) -> bool:
    value = payload.get(key)
    if value is None:
        return True
    if value is not True:
        raise ValidationError(f"ci doctor config field must be true: {key}")
    return True


def load_ci_doctor_config(config_path: Path) -> dict[str, Any]:
    payload = read_json_object(config_path, name="ci doctor config")

    allowed = {
        "doctor_version",
        "catalog_dir",
        "baseline_root",
        "runsets_path",
        "out_dir",
        "label",
        "checks",
        "bundles",
        "dashboard",
    }
    extras = sorted(key for key in payload.keys() if key not in allowed)
    if extras:
        raise ValidationError(f"ci doctor config has unsupported fields: {extras}")

    if payload.get("doctor_version") != CI_DOCTOR_VERSION:
        raise ValidationError(f"Unsupported doctor_version: {payload.get('doctor_version')}")

    checks_payload = payload.get("checks")
    if not isinstance(checks_payload, dict):
        raise ValidationError("ci doctor config requires checks object")

    bundles_payload = payload.get("bundles")
    if bundles_payload is not None and not isinstance(bundles_payload, list):
        raise ValidationError("ci doctor config bundles must be a list when provided")
    dashboard_payload = payload.get("dashboard")
    if dashboard_payload is not None and not isinstance(dashboard_payload, dict):
        raise ValidationError("ci doctor config dashboard must be an object when provided")

    bundles: list[dict[str, Path]] = []
    if isinstance(bundles_payload, list):
        for index, item in enumerate(bundles_payload):
            if not isinstance(item, dict):
                raise ValidationError(f"ci doctor bundles[{index}] must be object")
            zip_path = item.get("zip")
            if not isinstance(zip_path, str) or not zip_path:
                raise ValidationError(f"ci doctor bundles[{index}].zip must be non-empty string")
            bundles.append({"zip": Path(zip_path)})

    dashboard: dict[str, Path] | None = None
    if isinstance(dashboard_payload, dict):
        summary_path = dashboard_payload.get("summary_path")
        manifest_path = dashboard_payload.get("manifest_path")
        if not isinstance(summary_path, str) or not summary_path:
            raise ValidationError("ci doctor dashboard.summary_path must be non-empty string")
        if not isinstance(manifest_path, str) or not manifest_path:
            raise ValidationError("ci doctor dashboard.manifest_path must be non-empty string")
        dashboard = {
            "summary_path": Path(summary_path),
            "manifest_path": Path(manifest_path),
        }

    checks = {
        "verify_baseline_root": _required_true(checks_payload, "verify_baseline_root"),
        "verify_promotions": _required_true(checks_payload, "verify_promotions"),
        "verify_runsets": _required_true(checks_payload, "verify_runsets"),
        "verify_bundles": _optional_bool(checks_payload, "verify_bundles", False),
        "verify_dashboard": _optional_bool(checks_payload, "verify_dashboard", False),
    }

    return {
        "doctor_version": CI_DOCTOR_VERSION,
        "config_path": config_path,
        "catalog_dir": Path(_require_str(payload, "catalog_dir")),
        "baseline_root": Path(_require_str(payload, "baseline_root")),
        "runsets_path": Path(_require_str(payload, "runsets_path")),
        "out_dir": Path(_require_str(payload, "out_dir")),
        "label": _optional_str(payload, "label", "prod"),
        "checks": checks,
        "bundles": bundles,
        "dashboard": dashboard,
    }

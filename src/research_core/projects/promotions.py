from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from research_core.projects.index import projects_index_path
from research_core.projects.registry_io import read_json_file, write_canonical_json
from research_core.util.buildmeta import get_created_utc
from research_core.util.types import ValidationError


def projects_promotions_path(output_dir: Path) -> Path:
    return output_dir / "projects.promotions.json"


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="Project promote requires RESEARCH_CREATED_UTC for deterministic created_utc")


def _project_exists_in_index(output_dir: Path, project_id: str) -> bool:
    index_path = projects_index_path(output_dir)
    if not index_path.exists():
        raise ValidationError(f"Missing projects index file (run refresh first): {index_path}")

    payload = read_json_file(index_path)
    projects = payload.get("projects")
    if not isinstance(projects, dict):
        raise ValidationError(f"Invalid projects index format: {index_path}")
    return project_id in projects


def _load_or_init_promotions(path: Path, created_utc: str) -> dict[str, Any]:
    if not path.exists():
        return {
            "promotions_version": "v1",
            "created_utc": created_utc,
            "labels": {},
        }

    payload = read_json_file(path)
    if not isinstance(payload, dict):
        raise ValidationError(f"Invalid projects promotions payload: {path}")
    if payload.get("promotions_version") != "v1":
        raise ValidationError(f"Unsupported projects promotions version in {path}")
    labels = payload.get("labels")
    if not isinstance(labels, dict):
        raise ValidationError(f"Invalid labels block in {path}")
    return payload


def promote_project(output_dir: Path, project_id: str, label: str) -> dict[str, Any]:
    created_utc = _require_created_utc()
    if not _project_exists_in_index(output_dir=output_dir, project_id=project_id):
        raise ValidationError(f"project_id not found in projects index: {project_id}")

    path = projects_promotions_path(output_dir)
    payload = _load_or_init_promotions(path, created_utc=created_utc)
    labels = payload.get("labels", {})

    existing = labels.get(label)
    if isinstance(existing, str) and existing != project_id:
        raise ValidationError(
            f"Project promotions immutability violation for label={label}: existing project_id={existing} differs from requested project_id={project_id}"
        )

    if existing == project_id:
        return {
            "promotions_version": "v1",
            "created_utc": payload.get("created_utc", created_utc),
            "labels": {key: labels[key] for key in sorted(labels.keys())},
        }

    labels[label] = project_id
    output_payload = {
        "promotions_version": "v1",
        "created_utc": created_utc,
        "labels": {key: labels[key] for key in sorted(labels.keys())},
    }
    write_canonical_json(path, output_payload)
    return output_payload

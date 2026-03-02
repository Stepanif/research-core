from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from research_core.projects.registry_io import read_json_file, write_canonical_json
from research_core.util.hashing import sha256_file, sha256_json
from research_core.util.types import ValidationError


def projects_index_path(output_dir: Path) -> Path:
    return output_dir / "projects.index.json"


def _require_created_utc() -> str:
    created_utc = os.environ.get("RESEARCH_CREATED_UTC")
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError("Project index refresh requires RESEARCH_CREATED_UTC for deterministic created_utc")
    return created_utc


def _manifest_canonical_hash(path: Path) -> str:
    payload = read_json_file(path)
    return sha256_json(payload)


def _project_entry(output_dir: Path, project_dir: Path) -> dict[str, Any]:
    summary_path = project_dir / "project.summary.json"
    manifest_path = project_dir / "project.manifest.json"
    if not summary_path.exists() or not manifest_path.exists():
        raise ValidationError(f"Invalid project directory missing required files: {project_dir}")

    summary_payload = read_json_file(summary_path)
    manifest_payload = read_json_file(manifest_path)

    project_version = summary_payload.get("project_version")
    name = summary_payload.get("name")
    created_utc = manifest_payload.get("created_utc")
    if not isinstance(project_version, str) or not project_version:
        raise ValidationError(f"Invalid project_version in summary: {summary_path}")
    if not isinstance(name, str) or not name:
        raise ValidationError(f"Invalid name in summary: {summary_path}")
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError(f"Invalid created_utc in manifest: {manifest_path}")

    project_id = project_dir.name
    project_dir_rel = project_dir.relative_to(output_dir).as_posix() + "/"

    entry: dict[str, Any] = {
        "project_version": project_version,
        "name": name,
        "project_dir": project_dir_rel,
        "summary_sha256": sha256_file(summary_path),
        "manifest_canonical_sha256": _manifest_canonical_hash(manifest_path),
        "created_utc": created_utc,
    }

    report_path = project_dir / "project.report.json"
    report_manifest_path = project_dir / "project.report.manifest.json"
    if report_path.exists() and report_manifest_path.exists():
        entry["report_sha256"] = sha256_file(report_path)
        entry["report_manifest_canonical_sha256"] = _manifest_canonical_hash(report_manifest_path)

    return project_id, entry


def _load_or_init_index(path: Path, created_utc: str) -> dict[str, Any]:
    if not path.exists():
        return {
            "index_version": "v1",
            "created_utc": created_utc,
            "projects": {},
        }

    payload = read_json_file(path)
    if not isinstance(payload, dict):
        raise ValidationError(f"Invalid projects index payload: {path}")
    if payload.get("index_version") != "v1":
        raise ValidationError(f"Unsupported projects index version in {path}")
    projects = payload.get("projects")
    if not isinstance(projects, dict):
        raise ValidationError(f"Invalid projects block in {path}")
    return payload


def refresh_projects_index(output_dir: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()
    if not output_dir.exists() or not output_dir.is_dir():
        raise ValidationError(f"Project output-dir does not exist: {output_dir}")

    discovered: dict[str, Any] = {}
    for path in sorted([item for item in output_dir.iterdir() if item.is_dir()], key=lambda item: item.name):
        summary_path = path / "project.summary.json"
        manifest_path = path / "project.manifest.json"
        if summary_path.exists() and manifest_path.exists():
            project_id, entry = _project_entry(output_dir=output_dir, project_dir=path)
            discovered[project_id] = entry

    index_path = projects_index_path(output_dir)
    existing = _load_or_init_index(index_path, created_utc=created_utc)
    existing_projects = existing.get("projects", {})

    for project_id, entry in sorted(discovered.items(), key=lambda item: item[0]):
        existing_entry = existing_projects.get(project_id)
        if existing_entry is not None and existing_entry != entry:
            raise ValidationError(
                f"Project index immutability violation for project_id={project_id}: stored hashes differ from on-disk project artifacts"
            )

    output_payload = {
        "index_version": "v1",
        "created_utc": created_utc,
        "projects": {project_id: discovered[project_id] for project_id in sorted(discovered.keys())},
    }
    write_canonical_json(index_path, output_payload)
    return output_payload


def list_projects(output_dir: Path) -> list[str]:
    path = projects_index_path(output_dir)
    if not path.exists():
        return []
    payload = read_json_file(path)
    projects = payload.get("projects")
    if not isinstance(projects, dict):
        raise ValidationError(f"Invalid projects index format: {path}")
    return sorted(projects.keys())


def show_project_index_entry(output_dir: Path, project_id: str) -> dict[str, Any]:
    path = projects_index_path(output_dir)
    if not path.exists():
        raise ValidationError(f"Missing projects index file: {path}")

    payload = read_json_file(path)
    projects = payload.get("projects")
    if not isinstance(projects, dict):
        raise ValidationError(f"Invalid projects index format: {path}")

    entry = projects.get(project_id)
    if not isinstance(entry, dict):
        raise ValidationError(f"project_id not found in projects index: {project_id}")

    result = {"project_id": project_id}
    for key in sorted(entry.keys()):
        result[key] = entry[key]
    return result

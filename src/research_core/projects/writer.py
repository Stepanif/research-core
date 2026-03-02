from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.projects.contracts import canonical_json_bytes, canonical_json_sha256, file_entry
from research_core.util.hashing import sha256_bytes


def write_project_summary(path: Path, payload: dict[str, Any]) -> None:
    path.write_bytes(canonical_json_bytes(payload))


def build_project_manifest(
    created_utc: str,
    input_entries: list[dict[str, Any]],
    summary_payload: dict[str, Any],
    report_payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    outputs = {
        "project.summary.json": {
            "bytes": len(canonical_json_bytes(summary_payload)),
            "sha256": sha256_bytes(canonical_json_bytes(summary_payload)),
        }
    }

    if report_payload is not None:
        outputs["project.report.json"] = {
            "bytes": len(canonical_json_bytes(report_payload)),
            "sha256": sha256_bytes(canonical_json_bytes(report_payload)),
        }

    payload: dict[str, Any] = {
        "manifest_version": "v1",
        "created_utc": created_utc,
        "inputs": sorted(input_entries, key=lambda item: str(item.get("path", ""))),
        "outputs": outputs,
    }
    payload["project_manifest_canonical_sha256"] = canonical_json_sha256(payload, self_hash_key="project_manifest_canonical_sha256")
    return payload


def write_project_manifest(path: Path, payload: dict[str, Any]) -> None:
    path.write_bytes(canonical_json_bytes(payload))


def write_project_readme(path: Path, project_id: str, project_name: str, runs: list[str], spec_dirs: list[str]) -> None:
    lines = [
        "Research Core Project Runner",
        "",
        f"project_id: {project_id}",
        f"name: {project_name}",
        "",
        "runs:",
    ]
    for item in runs:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("spec_dirs:")
    for item in spec_dirs:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("Determinism:")
    lines.append("- All JSON outputs use canonical serialization")
    lines.append("- IDs are hash-derived")
    lines.append("")
    path.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))


def file_input(path_label: str, file_path: Path) -> dict[str, Any]:
    return file_entry(path_label=path_label, file_path=file_path)

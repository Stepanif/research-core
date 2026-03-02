from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.doctor.contracts import PROJECT_REQUIRED_FILES
from research_core.doctor.formatting import CheckItem, render_doctor_text
from research_core.util.hashing import sha256_file, sha256_json
from research_core.util.io import read_json


def _canonical_hash_without_self(payload: dict[str, Any], self_key: str) -> str:
    return sha256_json({key: value for key, value in payload.items() if key != self_key})


def _record(section: list[CheckItem], check_id: str, ok: bool, detail: str) -> None:
    section.append(CheckItem(check_id=check_id, ok=ok, detail=detail))


def _verify_manifest_outputs(manifest_path: Path, outputs_key: str, section: list[CheckItem], prefix: str) -> None:
    payload = read_json(manifest_path)
    outputs = payload.get(outputs_key)
    if not isinstance(outputs, dict):
        _record(section, f"{prefix}.outputs_block", False, f"missing/invalid {outputs_key}")
        return

    for output_name in sorted(outputs.keys()):
        output_info = outputs[output_name]
        if not isinstance(output_info, dict):
            _record(section, f"{prefix}.output.{output_name}", False, "invalid output metadata")
            continue
        expected_sha = output_info.get("sha256")
        if not isinstance(expected_sha, str) or not expected_sha:
            _record(section, f"{prefix}.output.{output_name}", False, "missing sha256")
            continue

        rel_path = output_info.get("path") if isinstance(output_info.get("path"), str) else output_name
        output_path = manifest_path.parent / rel_path
        if not output_path.exists():
            _record(section, f"{prefix}.output.{output_name}", False, f"missing {rel_path}")
            continue
        _record(section, f"{prefix}.output.{output_name}", sha256_file(output_path) == expected_sha, rel_path)


def _verify_optional_canonical_fields(payload: dict[str, Any], section: list[CheckItem], prefix: str) -> None:
    canonical_keys = sorted(
        [
            key
            for key, value in payload.items()
            if isinstance(value, str) and (key == "canonical_json_sha256" or key.endswith("_canonical_sha256"))
        ]
    )
    for key in canonical_keys:
        expected = payload[key]
        actual = _canonical_hash_without_self(payload, key)
        _record(section, f"{prefix}.{key}", actual == expected, "canonical")


def doctor_project_text(output_dir: Path, project_id: str) -> tuple[str, bool]:
    required: list[CheckItem] = []
    hash_integrity: list[CheckItem] = []
    invariants: list[CheckItem] = []
    optionals: list[CheckItem] = []

    project_dir = output_dir / project_id
    _record(required, "required.project_dir", project_dir.exists() and project_dir.is_dir(), f"{project_id}/")

    for rel_path in sorted(PROJECT_REQUIRED_FILES):
        _record(required, f"required.{rel_path}", (project_dir / rel_path).exists(), rel_path)

    project_manifest_path = project_dir / "project.manifest.json"
    if project_manifest_path.exists():
        manifest_payload = read_json(project_manifest_path)
        _verify_manifest_outputs(project_manifest_path, "outputs", hash_integrity, "manifest.project")
        _verify_optional_canonical_fields(manifest_payload, hash_integrity, "manifest.project")

    project_report_path = project_dir / "project.report.json"
    project_report_manifest_path = project_dir / "project.report.manifest.json"
    if project_report_path.exists() or project_report_manifest_path.exists():
        pair_ok = project_report_path.exists() and project_report_manifest_path.exists()
        _record(optionals, "optional.project_report_pair", pair_ok, "project.report.json + manifest")
        if pair_ok:
            report_manifest_payload = read_json(project_report_manifest_path)
            _verify_manifest_outputs(project_report_manifest_path, "outputs", optionals, "optional.manifest.project_report")
            _verify_optional_canonical_fields(report_manifest_payload, optionals, "optional.manifest.project_report")

    index_path = output_dir / "projects.index.json"
    _record(invariants, "invariant.projects_index_exists", index_path.exists(), "projects.index.json")
    if index_path.exists() and project_manifest_path.exists() and (project_dir / "project.summary.json").exists():
        index_payload = read_json(index_path)
        projects = index_payload.get("projects") if isinstance(index_payload, dict) else None
        if not isinstance(projects, dict):
            _record(invariants, "invariant.projects_index_format", False, "invalid projects index format")
        else:
            entry = projects.get(project_id)
            _record(invariants, "invariant.project_in_index", isinstance(entry, dict), project_id)
            if isinstance(entry, dict):
                summary_sha = sha256_file(project_dir / "project.summary.json")
                manifest_sha = sha256_json(read_json(project_manifest_path))
                _record(
                    invariants,
                    "invariant.index_summary_sha",
                    entry.get("summary_sha256") == summary_sha,
                    f"project.summary.json",
                )
                _record(
                    invariants,
                    "invariant.index_manifest_canonical_sha",
                    entry.get("manifest_canonical_sha256") == manifest_sha,
                    "project.manifest.json",
                )

                if project_report_path.exists() and project_report_manifest_path.exists():
                    report_sha = sha256_file(project_report_path)
                    report_manifest_sha = sha256_json(read_json(project_report_manifest_path))
                    expected_report_sha = entry.get("report_sha256")
                    expected_report_manifest_sha = entry.get("report_manifest_canonical_sha256")
                    report_sha_ok = (expected_report_sha == report_sha) if expected_report_sha is not None else True
                    report_manifest_sha_ok = (
                        expected_report_manifest_sha == report_manifest_sha
                    ) if expected_report_manifest_sha is not None else True
                    _record(invariants, "invariant.index_report_sha", report_sha_ok, "project.report.json")
                    _record(
                        invariants,
                        "invariant.index_report_manifest_canonical_sha",
                        report_manifest_sha_ok,
                        "project.report.manifest.json",
                    )

    promotions_path = output_dir / "projects.promotions.json"
    if promotions_path.exists():
        promotions_payload = read_json(promotions_path)
        labels = promotions_payload.get("labels") if isinstance(promotions_payload, dict) else None
        if not isinstance(labels, dict):
            _record(optionals, "optional.projects.promotions.labels", False, "invalid labels")
        else:
            index_payload = read_json(index_path) if index_path.exists() else {}
            projects = index_payload.get("projects") if isinstance(index_payload, dict) else {}
            for label in sorted(labels.keys()):
                mapped_project_id = labels[label]
                ok = isinstance(mapped_project_id, str) and isinstance(projects, dict) and mapped_project_id in projects
                _record(optionals, f"optional.projects.promotions.{label}", ok, f"{label}->{mapped_project_id}")

    all_checks = required + hash_integrity + invariants + optionals
    all_ok = all(item.ok for item in all_checks)
    result = [CheckItem(check_id="result", ok=all_ok, detail="PASS" if all_ok else "FAIL")]

    text = render_doctor_text(
        input_lines=[f"output_dir={output_dir.as_posix()}", f"project_id={project_id}"],
        required=required,
        hash_integrity=hash_integrity,
        invariants=invariants,
        optionals=optionals,
        result=result,
    )
    return text, all_ok

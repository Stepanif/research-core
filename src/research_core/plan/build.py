from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from research_core.plan.contracts import PLAN_TASK_KIND_EXPERIMENT_BATCH, PLAN_TOOL_VERSION, PLAN_VERSION, REQUIRED_ENV_VAR_CREATED_UTC
from research_core.plan.io import canonical_json_bytes, write_plan_json
from research_core.projects.contracts import PROJECT_TOOL_VERSION, canonical_json_bytes as project_canonical_json_bytes, stable_path_label
from research_core.projects.spec import load_project_spec
from research_core.util.buildmeta import get_created_utc
from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.io import read_json
from research_core.util.types import ValidationError


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="Plan build requires RESEARCH_CREATED_UTC for deterministic created_utc")


def _resolve_path(path_value: str, base_dir: Path) -> Path:
    path = Path(path_value)
    if not path.is_absolute():
        path = (base_dir / path).resolve()
    return path


def _display_label(abs_path: Path, original_label: str, base_dir: Path) -> str:
    if abs_path.is_relative_to(base_dir):
        return abs_path.relative_to(base_dir).as_posix()
    return stable_path_label(original_label)


def _project_id(project_spec: dict[str, Any]) -> str:
    payload = {
        "spec": project_spec,
        "tool": {"research_project_version": PROJECT_TOOL_VERSION},
        "ordered": {
            "runs": sorted(project_spec["runs"]),
            "spec_dirs": sorted(project_spec["spec_dirs"]),
        },
    }
    return sha256_bytes(project_canonical_json_bytes(payload))


def _spec_listing(spec_dir: Path) -> list[dict[str, Any]]:
    if not spec_dir.exists() or not spec_dir.is_dir():
        raise ValidationError(f"Project spec_dir does not exist: {spec_dir}")
    files = sorted([path for path in spec_dir.iterdir() if path.is_file() and path.suffix.lower() == ".json"], key=lambda p: p.name)
    if not files:
        raise ValidationError(f"Project spec_dir contains no JSON specs: {spec_dir}")
    return [{"name": path.name, "sha256": sha256_file(path)} for path in files]


def _run_hashes(run_dir: Path) -> dict[str, str]:
    psa_manifest_path = run_dir / "psa.manifest.json"
    if not psa_manifest_path.exists():
        raise ValidationError(f"Missing required psa.manifest.json for run: {run_dir}")

    psa_manifest = read_json(psa_manifest_path)
    psa_hash = psa_manifest.get("output_files", {}).get("psa.parquet", {}).get("canonical_table_sha256")
    if not isinstance(psa_hash, str) or not psa_hash:
        raise ValidationError(f"psa.manifest.json missing canonical table hash for run: {run_dir}")

    run_hashes: dict[str, str] = {"psa_canonical_table_sha256": psa_hash}
    canon_manifest_path = run_dir / "canon.manifest.json"
    if canon_manifest_path.exists():
        canon_manifest = read_json(canon_manifest_path)
        canon_hash = canon_manifest.get("output_files", {}).get("canon.parquet", {}).get("canonical_table_sha256")
        if isinstance(canon_hash, str) and canon_hash:
            run_hashes["canon_canonical_table_sha256"] = canon_hash
    return run_hashes


def _batch_id(run_dir: Path, spec_dir_label: str, spec_dir_abs: Path) -> str:
    payload = {
        "run": _run_hashes(run_dir),
        "spec_dir": {
            "label": stable_path_label(spec_dir_label),
            "listing": _spec_listing(spec_dir_abs),
        },
        "tool": {"research_project_batch_version": PROJECT_TOOL_VERSION},
    }
    return sha256_bytes(project_canonical_json_bytes(payload))


def _task_id(task_payload: dict[str, Any]) -> str:
    return sha256_bytes(canonical_json_bytes(task_payload))


def _task_expected_outputs(batch_id: str) -> list[str]:
    return sorted(
        [
            f"experiments/batches/{batch_id}/batch.manifest.json",
            f"experiments/batches/{batch_id}/batch.summary.json",
        ]
    )


def build_plan(project_path: Path, out_path: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()
    project_spec = load_project_spec(project_path)

    base_dir = project_path.parent.resolve()
    runs_data = [{"source": label, "abs": _resolve_path(label, base_dir)} for label in project_spec["runs"]]
    for item in runs_data:
        item["label"] = _display_label(abs_path=item["abs"], original_label=item["source"], base_dir=base_dir)
    runs_data = sorted(runs_data, key=lambda item: str(item["label"]))

    spec_dirs_data = [{"source": label, "abs": _resolve_path(label, base_dir)} for label in project_spec["spec_dirs"]]
    for item in spec_dirs_data:
        item["label"] = _display_label(abs_path=item["abs"], original_label=item["source"], base_dir=base_dir)
    spec_dirs_data = sorted(spec_dirs_data, key=lambda item: str(item["label"]))

    output_abs = _resolve_path(project_spec["output_dir"], base_dir)
    output_label = _display_label(abs_path=output_abs, original_label=project_spec["output_dir"], base_dir=base_dir)

    project_id_spec = {
        "project_version": project_spec["project_version"],
        "name": project_spec["name"],
        "runs": [str(item["label"]) for item in runs_data],
        "spec_dirs": [str(item["label"]) for item in spec_dirs_data],
        "output_dir": output_label,
        "policy": project_spec["policy"],
        **({"notes": project_spec["notes"]} if "notes" in project_spec else {}),
    }
    project_id = _project_id(project_id_spec)

    tasks_raw: list[dict[str, Any]] = []
    for run_item in runs_data:
        for spec_item in spec_dirs_data:
            run_label = str(run_item["source"])
            run_abs = run_item["abs"]
            spec_label = str(spec_item["source"])
            spec_abs = spec_item["abs"]

            batch_id = _batch_id(run_dir=run_abs, spec_dir_label=str(spec_item["label"]), spec_dir_abs=spec_abs)
            out_abs = run_abs / "experiments" / "batches" / batch_id
            out_label = Path(run_label).as_posix().rstrip("/") + f"/experiments/batches/{batch_id}"

            task_base = {
                "kind": PLAN_TASK_KIND_EXPERIMENT_BATCH,
                "run_dir": Path(run_label).as_posix(),
                "spec_dir": Path(spec_label).as_posix(),
                "out_dir": out_label,
                "argv": [
                    "python",
                    "-m",
                    "research_core.cli",
                    "experiment",
                    "batch",
                    "--run",
                    str(run_abs),
                    "--spec-dir",
                    str(spec_abs),
                    "--out",
                    str(out_abs),
                ],
                "deps": [],
                "expected_outputs": _task_expected_outputs(batch_id=batch_id),
            }
            task = dict(task_base)
            task["task_id"] = _task_id(task_base)
            tasks_raw.append(task)

    tasks = sorted(tasks_raw, key=lambda item: (str(item["run_dir"]), str(item["spec_dir"]), str(item["task_id"])))

    payload = {
        "plan_version": PLAN_VERSION,
        "created_utc": created_utc,
        "project_id": project_id,
        "tasks": tasks,
        "tool": {"research_plan_version": PLAN_TOOL_VERSION},
    }

    write_plan_json(out_path, payload)
    return payload

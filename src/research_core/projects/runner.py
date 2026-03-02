from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from research_core.experiments.batch import run_experiment_batch
from research_core.projects.contracts import (
    PROJECT_MANIFEST_VERSION,
    PROJECT_REPORT_VERSION,
    PROJECT_TOOL_VERSION,
    PROJECT_VERSION,
    canonical_json_bytes,
    canonical_json_sha256,
    file_entry,
    stable_path_label,
)
from research_core.projects.spec import load_project_spec
from research_core.projects.writer import build_project_manifest, write_project_manifest, write_project_readme, write_project_summary
from research_core.util.hashing import sha256_bytes, sha256_file, sha256_json
from research_core.util.io import read_json
from research_core.util.types import ValidationError


def _resolve_path(path_value: str, base_dir: Path) -> Path:
    path = Path(path_value)
    if not path.is_absolute():
        path = (base_dir / path).resolve()
    return path


def _require_created_utc() -> str:
    created_utc = os.environ.get("RESEARCH_CREATED_UTC")
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError("Project runner requires RESEARCH_CREATED_UTC for deterministic created_utc")
    return created_utc


def _project_id(project_spec: dict[str, Any]) -> str:
    payload = {
        "spec": project_spec,
        "tool": {"research_project_version": PROJECT_TOOL_VERSION},
        "ordered": {
            "runs": sorted(project_spec["runs"]),
            "spec_dirs": sorted(project_spec["spec_dirs"]),
        },
    }
    return sha256_bytes(canonical_json_bytes(payload))


def _display_label(abs_path: Path, original_label: str, base_dir: Path) -> str:
    if abs_path.is_relative_to(base_dir):
        return abs_path.relative_to(base_dir).as_posix()
    return stable_path_label(original_label)


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
    return sha256_bytes(canonical_json_bytes(payload))


def _require_observe_artifacts(run_dir: Path) -> None:
    required = [
        run_dir / "observe" / "observe.summary.json",
        run_dir / "observe" / "observe.summary.manifest.json",
        run_dir / "observe" / "observe.profile.json",
        run_dir / "observe" / "observe.profile.manifest.json",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise ValidationError(f"Project policy require_observe=true but observe artifacts are missing: {missing}")


def _run_ref(run_dir: Path) -> dict[str, str]:
    run_ref: dict[str, str] = {}
    canon_manifest_path = run_dir / "canon.manifest.json"
    if canon_manifest_path.exists():
        canon_manifest = read_json(canon_manifest_path)
        for key in ["instrument", "tf", "session_policy", "rth_start", "rth_end"]:
            value = canon_manifest.get(key)
            if isinstance(value, str) and value:
                run_ref[key] = value

    psa_manifest_path = run_dir / "psa.manifest.json"
    if psa_manifest_path.exists():
        psa_manifest = read_json(psa_manifest_path)
        session = psa_manifest.get("session", {})
        if isinstance(session, dict):
            for key in ["session_policy", "tz", "rth_start", "rth_end"]:
                if key in run_ref:
                    continue
                value = session.get(key)
                if isinstance(value, str) and value:
                    run_ref[key] = value
    return run_ref


def _batch_artifact_paths(run_dir: Path, batch_id: str) -> tuple[Path, Path]:
    batch_dir = run_dir / "experiments" / "batches" / batch_id
    return batch_dir / "batch.summary.json", batch_dir / "batch.manifest.json"


def _validate_existing_batch(summary_path: Path, manifest_path: Path) -> dict[str, Any]:
    if not summary_path.exists() or not manifest_path.exists():
        raise ValidationError(f"Existing batch directory missing summary/manifest: {summary_path.parent}")

    manifest = read_json(manifest_path)
    output_info = manifest.get("outputs", {}).get("batch.summary.json", {})
    expected_sha = output_info.get("sha256")
    if not isinstance(expected_sha, str) or not expected_sha:
        raise ValidationError(f"Invalid batch manifest outputs hash: {manifest_path}")

    actual_sha = sha256_file(summary_path)
    if actual_sha != expected_sha:
        raise ValidationError(
            f"Batch summary hash mismatch for existing batch {summary_path.parent.name}: expected={expected_sha} actual={actual_sha}"
        )

    expected_manifest_hash = manifest.get("batch_manifest_canonical_sha256")
    actual_manifest_hash = sha256_json({key: value for key, value in manifest.items() if key != "batch_manifest_canonical_sha256"})
    if not isinstance(expected_manifest_hash, str) or expected_manifest_hash != actual_manifest_hash:
        raise ValidationError(f"Batch manifest canonical hash mismatch: {manifest_path}")
    return manifest


def run_project(project_path: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()
    project_spec = load_project_spec(project_path)
    if "runs" not in project_spec:
        raise ValidationError("project run requires explicit runs in project spec; use project materialize for datasets mode")

    base_dir = project_path.parent.resolve()
    runs_data = [
        {
            "source": label,
            "abs": _resolve_path(label, base_dir),
        }
        for label in project_spec["runs"]
    ]
    for item in runs_data:
        item["label"] = _display_label(abs_path=item["abs"], original_label=item["source"], base_dir=base_dir)
    runs_data = sorted(runs_data, key=lambda item: str(item["label"]))

    spec_dirs_data = [
        {
            "source": label,
            "abs": _resolve_path(label, base_dir),
        }
        for label in project_spec["spec_dirs"]
    ]
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

    for item in runs_data:
        label = str(item["label"])
        run_abs = item["abs"]
        if not run_abs.exists() or not run_abs.is_dir():
            raise ValidationError(f"Project run path does not exist: {label}")
        if project_spec["policy"]["require_observe"]:
            _require_observe_artifacts(run_abs)

    project_id = _project_id(project_id_spec)
    output_root = output_abs
    project_output_dir = output_root / project_id

    run_entries: list[dict[str, Any]] = []
    input_entries: list[dict[str, Any]] = [file_entry(path_label=stable_path_label(project_path.name), file_path=project_path)]

    total_batches = 0
    for run_item in runs_data:
        run_label = str(run_item["label"])
        run_abs = run_item["abs"]
        run_ref = _run_ref(run_abs)

        batch_entries: list[dict[str, Any]] = []
        for spec_item in spec_dirs_data:
            spec_dir_label = str(spec_item["label"])
            spec_dir_abs = spec_item["abs"]
            batch_id = _batch_id(run_dir=run_abs, spec_dir_label=spec_dir_label, spec_dir_abs=spec_dir_abs)
            batch_dir = run_abs / "experiments" / "batches" / batch_id

            summary_path, manifest_path = _batch_artifact_paths(run_abs, batch_id)
            if batch_dir.exists():
                manifest_payload = _validate_existing_batch(summary_path=summary_path, manifest_path=manifest_path)
            else:
                result = run_experiment_batch(run_dir=run_abs, spec_dir=spec_dir_abs, batch_dir=batch_dir)
                manifest_payload = result["manifest"]

            batch_entries.append(
                {
                    "spec_dir": stable_path_label(spec_dir_label),
                    "batch_id": batch_id,
                    "batch_summary_sha256": sha256_file(summary_path),
                    "batch_manifest_canonical_sha256": str(manifest_payload["batch_manifest_canonical_sha256"]),
                }
            )
            input_entries.append(
                file_entry(
                    path_label=f"{stable_path_label(run_label)}/experiments/batches/{batch_id}/batch.summary.json",
                    file_path=summary_path,
                )
            )
            input_entries.append(
                file_entry(
                    path_label=f"{stable_path_label(run_label)}/experiments/batches/{batch_id}/batch.manifest.json",
                    file_path=manifest_path,
                )
            )
            total_batches += 1

        experiments_index_path = run_abs / "experiments" / "experiments.index.json"
        if not experiments_index_path.exists():
            raise ValidationError(f"Missing experiments index for run after batch execution: {experiments_index_path}")
        experiments_index = read_json(experiments_index_path)
        experiments_count = len(experiments_index.get("experiments", {})) if isinstance(experiments_index.get("experiments", {}), dict) else 0

        run_entry: dict[str, Any] = {
            "run_path": stable_path_label(run_label),
            "batches": sorted(batch_entries, key=lambda item: (str(item["spec_dir"]), str(item["batch_id"]))),
            "experiment_count": experiments_count,
            "promotions_present": (run_abs / "experiments" / "promotions.json").exists(),
        }
        for key in ["instrument", "tf"]:
            value = run_ref.get(key)
            if isinstance(value, str) and value:
                run_entry[key] = value
        run_entries.append(run_entry)

    summary_payload: dict[str, Any] = {
        "project_id": project_id,
        "project_version": PROJECT_VERSION,
        "name": project_spec["name"],
        "created_utc": created_utc,
        "runs": sorted(run_entries, key=lambda item: str(item["run_path"])),
        "totals": {
            "runs": len(runs_data),
            "batches": total_batches,
            "succeeded": total_batches,
            "failed": 0,
        },
    }

    project_output_dir.mkdir(parents=True, exist_ok=True)
    summary_path = project_output_dir / "project.summary.json"
    write_project_summary(summary_path, summary_payload)

    manifest_payload = build_project_manifest(
        created_utc=created_utc,
        input_entries=input_entries,
        summary_payload=summary_payload,
    )
    write_project_manifest(project_output_dir / "project.manifest.json", manifest_payload)
    write_project_readme(
        project_output_dir / "README_PROJECT.txt",
        project_id=project_id,
        project_name=project_spec["name"],
        runs=[str(item["label"]) for item in runs_data],
        spec_dirs=[str(item["label"]) for item in spec_dirs_data],
    )

    return {
        "project_id": project_id,
        "summary": summary_payload,
        "manifest": manifest_payload,
        "output_dir": project_output_dir,
    }


def report_project(project_path: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()
    project_spec = load_project_spec(project_path)
    if "runs" not in project_spec:
        raise ValidationError("project report requires explicit runs in project spec")

    base_dir = project_path.parent.resolve()
    runs_data = [
        {
            "source": label,
            "abs": _resolve_path(label, base_dir),
        }
        for label in project_spec["runs"]
    ]
    for item in runs_data:
        item["label"] = _display_label(abs_path=item["abs"], original_label=item["source"], base_dir=base_dir)
    runs_data = sorted(runs_data, key=lambda item: str(item["label"]))

    spec_dirs_data = [
        {
            "source": label,
            "abs": _resolve_path(label, base_dir),
        }
        for label in project_spec["spec_dirs"]
    ]
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
    output_root = output_abs
    project_output_dir = output_root / project_id
    project_output_dir.mkdir(parents=True, exist_ok=True)

    run_entries: list[dict[str, Any]] = []
    input_entries: list[dict[str, Any]] = [file_entry(path_label=stable_path_label(project_path.name), file_path=project_path)]

    for run_item in runs_data:
        run_label = str(run_item["label"])
        run_abs = run_item["abs"]
        if not run_abs.exists() or not run_abs.is_dir():
            raise ValidationError(f"Project run path does not exist for project report: {run_label}")

        batch_entries: list[dict[str, Any]] = []
        for spec_item in spec_dirs_data:
            spec_dir_label = str(spec_item["label"])
            spec_dir_abs = spec_item["abs"]
            batch_id = _batch_id(run_dir=run_abs, spec_dir_label=spec_dir_label, spec_dir_abs=spec_dir_abs)
            summary_path, manifest_path = _batch_artifact_paths(run_abs, batch_id)
            if not summary_path.exists() or not manifest_path.exists():
                raise ValidationError(
                    f"Missing expected batch artifacts for project report run={run_label} spec_dir={spec_dir_label} batch_id={batch_id}"
                )

            manifest_payload = _validate_existing_batch(summary_path=summary_path, manifest_path=manifest_path)
            batch_entries.append(
                {
                    "spec_dir": stable_path_label(spec_dir_label),
                    "batch_id": batch_id,
                    "batch_summary_sha256": sha256_file(summary_path),
                    "batch_manifest_canonical_sha256": str(manifest_payload["batch_manifest_canonical_sha256"]),
                }
            )
            input_entries.append(file_entry(f"{stable_path_label(run_label)}/experiments/batches/{batch_id}/batch.summary.json", summary_path))
            input_entries.append(file_entry(f"{stable_path_label(run_label)}/experiments/batches/{batch_id}/batch.manifest.json", manifest_path))

        exp_report_path = run_abs / "experiments" / "experiments.report.json"
        exp_report_manifest_path = run_abs / "experiments" / "experiments.report.manifest.json"
        if not exp_report_path.exists() or not exp_report_manifest_path.exists():
            raise ValidationError(f"Missing expected experiment report artifacts for run: {run_label}")

        run_entries.append(
            {
                "run_path": stable_path_label(run_label),
                "batches": sorted(batch_entries, key=lambda item: (str(item["spec_dir"]), str(item["batch_id"]))),
                "experiments_report_sha256": sha256_file(exp_report_path),
                "experiments_report_manifest_canonical_sha256": sha256_json(
                    {
                        key: value
                        for key, value in read_json(exp_report_manifest_path).items()
                        if key != "report_manifest_canonical_sha256"
                    }
                ),
            }
        )
        input_entries.append(file_entry(f"{stable_path_label(run_label)}/experiments/experiments.report.json", exp_report_path))
        input_entries.append(file_entry(f"{stable_path_label(run_label)}/experiments/experiments.report.manifest.json", exp_report_manifest_path))

    report_payload: dict[str, Any] = {
        "report_version": PROJECT_REPORT_VERSION,
        "project_id": project_id,
        "project_version": PROJECT_VERSION,
        "name": project_spec["name"],
        "created_utc": created_utc,
        "runs": sorted(run_entries, key=lambda item: str(item["run_path"])),
        "totals": {
            "runs": len(run_entries),
            "batches": sum(len(item["batches"]) for item in run_entries),
        },
    }

    report_path = project_output_dir / "project.report.json"
    report_path.write_bytes(canonical_json_bytes(report_payload))

    report_manifest_payload: dict[str, Any] = {
        "manifest_version": PROJECT_MANIFEST_VERSION,
        "created_utc": created_utc,
        "inputs": sorted(input_entries, key=lambda item: str(item["path"])),
        "outputs": {
            "project.report.json": {
                "bytes": report_path.stat().st_size,
                "sha256": sha256_file(report_path),
            }
        },
    }
    report_manifest_payload["project_report_manifest_canonical_sha256"] = canonical_json_sha256(
        report_manifest_payload, self_hash_key="project_report_manifest_canonical_sha256"
    )
    (project_output_dir / "project.report.manifest.json").write_bytes(canonical_json_bytes(report_manifest_payload))

    return {
        "project_id": project_id,
        "report": report_payload,
        "manifest": report_manifest_payload,
        "output_dir": project_output_dir,
    }

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from research_core.doctor.run_doctor import doctor_run_text
from research_core.projects.materialize import materialize_project
from research_core.runsets.catalog import show_runset, validate_runset
from research_core.runsets.contracts import REQUIRED_ENV_VAR_CREATED_UTC
from research_core.runsets.io import canonical_hash, canonical_json_bytes, read_json, write_canonical_json
from research_core.util.buildmeta import get_created_utc
from research_core.util.hashing import sha256_bytes, sha256_file

from research_core.util.types import ValidationError


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="runset materialize requires RESEARCH_CREATED_UTC")


def _links_index_path(catalog_dir: Path) -> Path:
    return catalog_dir / "links" / "dataset_to_runs.index.json"


def _load_links_index(catalog_dir: Path) -> dict[str, Any]:
    path = _links_index_path(catalog_dir)
    if not path.exists() or not path.is_file():
        raise ValidationError(f"RunSet materialize missing dataset_to_runs index: {path}")
    payload = read_json(path)
    if not isinstance(payload, dict):
        raise ValidationError("RunSet materialize dataset_to_runs index payload invalid")
    datasets = payload.get("datasets")
    if not isinstance(datasets, dict):
        raise ValidationError("RunSet materialize dataset_to_runs datasets payload invalid")
    return payload


def _dataset_runs(index_payload: dict[str, Any], dataset_id: str) -> list[dict[str, Any]]:
    datasets = index_payload.get("datasets")
    assert isinstance(datasets, dict)
    row = datasets.get(dataset_id)
    if not isinstance(row, dict):
        return []

    runs = row.get("runs")
    if not isinstance(runs, list):
        raise ValidationError("RunSet materialize dataset_to_runs row runs payload invalid")

    normalized: list[dict[str, Any]] = []
    for item in runs:
        if not isinstance(item, dict):
            raise ValidationError("RunSet materialize dataset_to_runs run payload invalid")
        run_ref = item.get("run_ref")
        canon_hash = item.get("canon_table_sha256")
        lineage_hash = item.get("run_lineage_canonical_sha256")
        if not isinstance(run_ref, str) or not run_ref or not isinstance(canon_hash, str) or not canon_hash:
            raise ValidationError("RunSet materialize dataset_to_runs run missing run_ref/canon_table_sha256")
        row_payload: dict[str, Any] = {
            "run_ref": run_ref,
            "canon_table_sha256": canon_hash,
        }
        if isinstance(lineage_hash, str) and lineage_hash:
            row_payload["lineage_hash"] = lineage_hash
        normalized.append(row_payload)
    return sorted(normalized, key=lambda item: (str(item.get("canon_table_sha256", "")), str(item.get("run_ref", ""))))


def _explicit_runs_for_dataset(runset_payload: dict[str, Any], dataset_id: str) -> list[dict[str, Any]]:
    runs = runset_payload.get("runs")
    if not isinstance(runs, list):
        raise ValidationError("RunSet entry runs payload invalid")

    selected: list[dict[str, Any]] = []
    for item in runs:
        if not isinstance(item, dict):
            raise ValidationError("RunSet entry run payload invalid")
        if item.get("dataset_id") == dataset_id:
            selected.append(dict(item))

    return sorted(
        selected,
        key=lambda item: (
            str(item.get("dataset_id", "")),
            str(item.get("canon_table_sha256", "")),
            str(item.get("run_ref", "")),
        ),
    )


def _resolve_run_dir(run_ref: str, *, runs_root: Path, catalog_dir: Path) -> Path | None:
    ref_path = Path(run_ref)
    candidates: list[Path] = []

    if ref_path.is_absolute():
        candidates.append(ref_path)
    else:
        candidates.append((runs_root / ref_path).resolve())
        candidates.append((catalog_dir.parent / ref_path).resolve())
        candidates.append((Path.cwd() / ref_path).resolve())

    for candidate in candidates:
        if candidate.exists() and candidate.is_dir():
            return candidate
    return None


def _verify_run_required_artifacts(run_dir: Path, required_artifacts: dict[str, Any]) -> None:
    text, ok = doctor_run_text(run_dir=run_dir)
    if not ok:
        raise ValidationError(f"RunSet materialize selected run failed doctor run: {run_dir}\n{text}")

    required = {
        "canon": bool(required_artifacts.get("canon", True)),
        "psa": bool(required_artifacts.get("psa", True)),
        "observe": bool(required_artifacts.get("observe", True)),
        "experiments": bool(required_artifacts.get("experiments", False)),
    }
    if required["canon"] and not (run_dir / "canon.parquet").exists():
        raise ValidationError(f"RunSet materialize required artifact missing canon.parquet for run_ref={run_dir}")
    if required["psa"] and not (run_dir / "psa.parquet").exists():
        raise ValidationError(f"RunSet materialize required artifact missing psa.parquet for run_ref={run_dir}")
    if required["observe"] and not (run_dir / "observe" / "observe.summary.json").exists():
        raise ValidationError(f"RunSet materialize required artifact missing observe.summary.json for run_ref={run_dir}")
    if required["experiments"] and not (run_dir / "experiments" / "experiments.index.json").exists():
        raise ValidationError(f"RunSet materialize required artifact missing experiments.index.json for run_ref={run_dir}")


def _build_temp_project_spec(*, runset_payload: dict[str, Any], project_out: Path) -> dict[str, Any]:
    datasets = runset_payload.get("datasets")
    if not isinstance(datasets, list) or not all(isinstance(item, str) and item for item in datasets):
        raise ValidationError("RunSet entry datasets payload invalid")

    dataset_refs = [
        {
            "dataset_id": dataset_id,
            "instrument": "ES",
            "tf": "1min",
            "session_policy": "full",
            "schema_path": "schemas/canon.schema.v1.json",
            "colmap_path": "schemas/colmap.raw_vendor_v1.json",
        }
        for dataset_id in sorted(set(datasets))
    ]

    return {
        "project_version": "v1",
        "name": f"runset-materialize-{runset_payload['runset_id'][:12]}",
        "datasets": dataset_refs,
        "spec_dirs": ["tests/fixtures/exp_specs"],
        "output_dir": project_out.resolve().as_posix(),
        "policy": {"fail_fast": True, "require_observe": False},
    }


def _lineage_hash_for_run_ref(catalog_dir: Path, run_ref: str) -> str | None:
    index_payload = _load_links_index(catalog_dir)
    datasets = index_payload.get("datasets")
    assert isinstance(datasets, dict)
    for row in datasets.values():
        if not isinstance(row, dict):
            continue
        runs = row.get("runs")
        if not isinstance(runs, list):
            continue
        for run in runs:
            if not isinstance(run, dict):
                continue
            if run.get("run_ref") == run_ref:
                lineage_hash = run.get("run_lineage_canonical_sha256")
                if isinstance(lineage_hash, str) and lineage_hash:
                    return lineage_hash
    return None


def materialize_runset(*, catalog_dir: Path, runset_id: str, runs_root: Path, project_out: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()

    runset_payload = show_runset(catalog_root=catalog_dir, runset_id=runset_id)
    ok, text = validate_runset(catalog_root=catalog_dir, runset_id=runset_id)
    if not ok:
        raise ValidationError(text)

    policy = runset_payload.get("policy")
    if not isinstance(policy, dict):
        raise ValidationError("RunSet entry policy payload invalid")
    allow_materialize_missing = bool(policy.get("allow_materialize_missing", False))

    datasets = runset_payload.get("datasets")
    if not isinstance(datasets, list) or not all(isinstance(item, str) and item for item in datasets):
        raise ValidationError("RunSet entry datasets payload invalid")

    links_index_before = _load_links_index(catalog_dir)
    links_hash_before = canonical_hash(links_index_before)

    datasets_sorted = sorted(set([str(item) for item in datasets]))

    need_materialize = False
    for dataset_id in datasets_sorted:
        linked_runs = _dataset_runs(links_index_before, dataset_id)
        explicit = _explicit_runs_for_dataset(runset_payload, dataset_id)

        for row in explicit:
            canon_hash = row.get("canon_table_sha256")
            if isinstance(canon_hash, str) and canon_hash:
                present = any(item["canon_table_sha256"] == canon_hash for item in linked_runs)
                if not present:
                    raise ValidationError(
                        "RunSet materialize conflict fail-loud: explicit run canon_table_sha256 not present in dataset_to_runs links"
                    )

        if explicit:
            selected_row = explicit[0]
            run_ref = str(selected_row.get("run_ref"))
            resolved = _resolve_run_dir(run_ref, runs_root=runs_root.resolve(), catalog_dir=catalog_dir.resolve())
            if resolved is None and allow_materialize_missing:
                need_materialize = True
            if resolved is None and not allow_materialize_missing:
                raise ValidationError(
                    f"RunSet materialize could not resolve explicit run_ref={run_ref}; enable allow_materialize_missing to materialize"
                )
        elif not linked_runs:
            if not allow_materialize_missing:
                raise ValidationError(
                    f"RunSet materialize missing linked runs for dataset_id={dataset_id} and allow_materialize_missing=false"
                )
            need_materialize = True

    temp_project_spec_path: Path | None = None
    temp_project_spec_sha256: str | None = None
    materialized_dataset_ids: set[str] = set()

    if need_materialize:
        temp_payload = _build_temp_project_spec(runset_payload=runset_payload, project_out=project_out)
        temp_project_spec_path = project_out.resolve() / f".runset_materialize_{runset_id}.project.json"
        write_canonical_json(temp_project_spec_path, temp_payload)
        temp_project_spec_sha256 = sha256_file(temp_project_spec_path)

        result = materialize_project(project_path=temp_project_spec_path, catalog_dir=catalog_dir, runs_root=runs_root)
        runs_rows = result.get("summary", {}).get("runs", [])
        if isinstance(runs_rows, list):
            for row in runs_rows:
                if isinstance(row, dict) and isinstance(row.get("dataset_id"), str):
                    materialized_dataset_ids.add(str(row["dataset_id"]))

    links_index_after = _load_links_index(catalog_dir)
    links_hash_after = canonical_hash(links_index_after)

    conflicts: list[dict[str, str]] = []
    summary_rows: list[dict[str, Any]] = []

    for dataset_id in datasets_sorted:
        linked_runs = _dataset_runs(links_index_after, dataset_id)
        explicit = _explicit_runs_for_dataset(runset_payload, dataset_id)

        selected_from_links: dict[str, Any] | None = None
        if explicit:
            explicit_row = explicit[0]
            explicit_hash = explicit_row.get("canon_table_sha256")
            if isinstance(explicit_hash, str) and explicit_hash:
                matched = [item for item in linked_runs if item["canon_table_sha256"] == explicit_hash]
                if not matched:
                    raise ValidationError(
                        "RunSet materialize conflict fail-loud: explicit run canon_table_sha256 missing after materialize"
                    )
                selected_from_links = sorted(matched, key=lambda item: (item["canon_table_sha256"], item["run_ref"]))[0]
            else:
                matched_by_ref = [item for item in linked_runs if item["run_ref"] == explicit_row["run_ref"]]
                if matched_by_ref:
                    selected_from_links = sorted(matched_by_ref, key=lambda item: (item["canon_table_sha256"], item["run_ref"]))[0]
                elif linked_runs:
                    selected_from_links = linked_runs[0]

            if selected_from_links is None:
                raise ValidationError(f"RunSet materialize could not select explicit run for dataset_id={dataset_id}")
            required_artifacts = explicit_row.get("required_artifacts", {})
        else:
            if not linked_runs:
                raise ValidationError(f"RunSet materialize could not select linked run for dataset_id={dataset_id}")
            selected_from_links = linked_runs[0]
            required_artifacts = {"canon": True, "psa": True, "observe": True, "experiments": False}

        run_ref = str(selected_from_links["run_ref"])
        resolved_dir = _resolve_run_dir(run_ref, runs_root=runs_root.resolve(), catalog_dir=catalog_dir.resolve())
        if resolved_dir is None:
            if not allow_materialize_missing:
                raise ValidationError(f"RunSet materialize selected run_ref not resolvable: {run_ref}")
            conflicts.append({"dataset_id": dataset_id, "reason": "selected_run_unresolvable"})
            continue

        _verify_run_required_artifacts(resolved_dir, required_artifacts if isinstance(required_artifacts, dict) else {})

        summary_rows.append(
            {
                "dataset_id": dataset_id,
                "selected": {
                    "run_ref": run_ref,
                    "canon_table_sha256": str(selected_from_links["canon_table_sha256"]),
                    **(
                        {"lineage_hash": str(selected_from_links["lineage_hash"])}
                        if isinstance(selected_from_links.get("lineage_hash"), str)
                        else (
                            {"lineage_hash": _lineage_hash_for_run_ref(catalog_dir, run_ref)}
                            if _lineage_hash_for_run_ref(catalog_dir, run_ref) is not None
                            else {}
                        )
                    ),
                },
                "status": "MATERIALIZED" if dataset_id in materialized_dataset_ids else "REUSED",
            }
        )

    if conflicts:
        raise ValidationError(f"RunSet materialize conflicts detected: {conflicts}")

    summary_payload: dict[str, Any] = {
        "materialize_version": "v1",
        "runset_id": runset_id,
        "created_utc": created_utc,
        "datasets": sorted(summary_rows, key=lambda item: str(item["dataset_id"])),
        "totals": {
            "datasets": len(summary_rows),
            "reused": sum(1 for item in summary_rows if item["status"] == "REUSED"),
            "materialized": sum(1 for item in summary_rows if item["status"] == "MATERIALIZED"),
        },
        "conflicts": [],
    }

    output_dir = project_out / runset_id
    summary_path = output_dir / "runset.materialize.summary.json"
    manifest_path = output_dir / "runset.materialize.manifest.json"

    entry_path = catalog_dir / "runsets" / "entries" / f"{runset_id}.json"
    if not entry_path.exists() or not entry_path.is_file():
        raise ValidationError(f"RunSet entry not found during materialize output assembly: {entry_path}")

    manifest_inputs: list[dict[str, Any]] = [
        {
            "path": "runsets/entries/" + f"{runset_id}.json",
            "bytes": int(entry_path.stat().st_size),
            "sha256": sha256_file(entry_path),
        },
        {
            "path": "links/dataset_to_runs.index.json",
            "canonical_sha256": links_hash_after,
            "bytes": int(_links_index_path(catalog_dir).stat().st_size),
            "sha256": sha256_file(_links_index_path(catalog_dir)),
            "canonical_sha256_before": links_hash_before,
        },
    ]
    if temp_project_spec_path is not None and temp_project_spec_sha256 is not None:
        manifest_inputs.append(
            {
                "path": temp_project_spec_path.name,
                "bytes": int(temp_project_spec_path.stat().st_size),
                "sha256": temp_project_spec_sha256,
            }
        )

    summary_bytes = canonical_json_bytes(summary_payload)
    manifest_payload: dict[str, Any] = {
        "manifest_version": "v1",
        "created_utc": created_utc,
        "inputs": sorted(manifest_inputs, key=lambda item: str(item["path"])),
        "outputs": {
            "runset.materialize.summary.json": {
                "bytes": len(summary_bytes),
                "sha256": sha256_bytes(summary_bytes),
            }
        },
    }
    manifest_payload["runset_materialize_manifest_canonical_sha256"] = canonical_hash(
        manifest_payload,
        self_field="runset_materialize_manifest_canonical_sha256",
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    summary_path.write_bytes(summary_bytes)
    write_canonical_json(manifest_path, manifest_payload)

    return {
        "summary": summary_payload,
        "manifest": manifest_payload,
        "output_dir": output_dir,
    }

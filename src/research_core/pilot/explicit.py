from __future__ import annotations

from pathlib import Path
from typing import Any, cast

from research_core.runsets.io import canonical_hash, read_json
from research_core.util.types import ValidationError


def _load_json_object(path: Path, name: str) -> dict[str, Any]:
    if not path.exists() or not path.is_file():
        raise ValidationError(f"Pilot explicit generation missing {name}: {path}")
    return read_json(path)


def _find_single_dataset_to_runs_index(catalog_dir: Path) -> Path:
    matches = sorted(catalog_dir.rglob("dataset_to_runs.index.json"), key=lambda item: item.as_posix())
    if len(matches) != 1:
        raise ValidationError(
            f"Pilot explicit generation expected exactly 1 dataset_to_runs.index.json under {catalog_dir}, found {len(matches)}"
        )
    return matches[0]


def _es_datasets_sorted(datasets_payload: dict[str, Any]) -> list[dict[str, str]]:
    rows = datasets_payload.get("datasets")
    if not isinstance(rows, list):
        raise ValidationError("Pilot explicit generation datasets payload missing datasets array")
    rows_list = cast(list[Any], rows)

    selected: list[dict[str, str]] = []
    for row in rows_list:
        if not isinstance(row, dict):
            raise ValidationError("Pilot explicit generation datasets row must be an object")
        row_obj = cast(dict[str, Any], row)

        if str(row_obj.get("instrument", "")).upper() != "ES":
            continue

        dataset_id = row_obj.get("dataset_id")
        tf = row_obj.get("tf")
        if not isinstance(dataset_id, str) or not dataset_id:
            raise ValidationError("Pilot explicit generation invalid ES dataset_id")
        if not isinstance(tf, str) or not tf:
            raise ValidationError(f"Pilot explicit generation missing tf for dataset_id={dataset_id}")

        selected.append({"dataset_id": dataset_id, "tf": tf})

    if not selected:
        raise ValidationError("Pilot explicit generation found no ES datasets")

    return sorted(selected, key=lambda item: (item["tf"], item["dataset_id"]))


def _pick_explicit_run(index_payload: dict[str, Any], dataset_id: str) -> dict[str, str]:
    datasets = index_payload.get("datasets")
    if not isinstance(datasets, dict):
        raise ValidationError("Pilot explicit generation index missing datasets object")

    datasets_obj = cast(dict[str, Any], datasets)
    entry = datasets_obj.get(dataset_id)
    if not isinstance(entry, dict):
        raise ValidationError(f"Pilot explicit generation no dataset_to_runs entry for dataset_id={dataset_id}")
    entry_obj = cast(dict[str, Any], entry)

    runs = entry_obj.get("runs")
    if not isinstance(runs, list) or not runs:
        raise ValidationError(f"Pilot explicit generation no linked runs for dataset_id={dataset_id}")

    candidates: list[tuple[str, str]] = []
    runs_list = cast(list[Any], runs)
    for row in runs_list:
        if not isinstance(row, dict):
            raise ValidationError(f"Pilot explicit generation invalid run row for dataset_id={dataset_id}")
        row_obj = cast(dict[str, Any], row)
        run_ref = row_obj.get("run_ref")
        canon_sha = row_obj.get("canon_table_sha256")
        if not isinstance(run_ref, str) or not run_ref:
            raise ValidationError(f"Pilot explicit generation missing run_ref for dataset_id={dataset_id}")
        if not isinstance(canon_sha, str) or not canon_sha:
            raise ValidationError(f"Pilot explicit generation missing canon_table_sha256 for dataset_id={dataset_id}")
        candidates.append((run_ref, canon_sha))

    run_ref, canon_sha = sorted(candidates, key=lambda item: (item[0], item[1]))[0]
    return {
        "dataset_id": dataset_id,
        "run_ref": run_ref,
        "canon_table_sha256": canon_sha,
    }


def build_explicit_runset_spec(*, catalog_dir: Path, datasets_path: Path) -> dict[str, Any]:
    index_path = _find_single_dataset_to_runs_index(catalog_dir)
    index_payload = _load_json_object(index_path, "dataset_to_runs index")
    datasets_payload = _load_json_object(datasets_path, "pilot datasets")

    datasets = _es_datasets_sorted(datasets_payload)
    dataset_ids = [row["dataset_id"] for row in datasets]
    runs = [_pick_explicit_run(index_payload, dataset_id) for dataset_id in dataset_ids]

    return {
        "runset_version": "v1",
        "name": "PILOT_RUNSET_ES_EXPLICIT_FROM_INDEX",
        "datasets": dataset_ids,
        "runs": runs,
        "policy": {
            "allow_materialize_missing": False,
            "require_lineage_links": True,
            "require_bidirectional": True,
        },
    }


def explicit_runset_spec_sha256(spec_payload: dict[str, Any]) -> str:
    return canonical_hash(spec_payload)

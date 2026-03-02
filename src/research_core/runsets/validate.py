from __future__ import annotations

from pathlib import Path
from typing import Any

from research_core.datasets.catalog import show_dataset
from research_core.runsets.io import read_json
from research_core.util.types import ValidationError


def _catalog_links_index_path(catalog_root: Path) -> Path:
    return catalog_root / "links" / "dataset_to_runs.index.json"


def _load_dataset_to_runs_index(catalog_root: Path) -> dict[str, Any]:
    index_path = _catalog_links_index_path(catalog_root)
    if not index_path.exists() or not index_path.is_file():
        raise ValidationError(f"RunSet validation missing dataset_to_runs index: {index_path}")

    payload = read_json(index_path)
    if not isinstance(payload, dict):
        raise ValidationError("RunSet validation dataset_to_runs index payload invalid")

    datasets = payload.get("datasets")
    if not isinstance(datasets, dict):
        raise ValidationError("RunSet validation dataset_to_runs datasets payload invalid")
    return payload


def _dataset_linked_hashes(index_payload: dict[str, Any], dataset_id: str) -> set[str]:
    datasets = index_payload["datasets"]
    assert isinstance(datasets, dict)
    row = datasets.get(dataset_id)
    if not isinstance(row, dict):
        return set()

    runs = row.get("runs")
    if not isinstance(runs, list):
        raise ValidationError("RunSet validation dataset_to_runs row runs payload invalid")

    hashes: set[str] = set()
    for item in runs:
        if not isinstance(item, dict):
            raise ValidationError("RunSet validation dataset_to_runs run payload invalid")
        canon_hash = item.get("canon_table_sha256")
        if isinstance(canon_hash, str) and canon_hash:
            hashes.add(canon_hash)
    return hashes


def _explicit_hashes_for_dataset(runs: list[dict[str, Any]], dataset_id: str) -> set[str]:
    hashes: set[str] = set()
    for row in runs:
        run_dataset_id = row.get("dataset_id")
        if run_dataset_id != dataset_id:
            continue
        canon_hash = row.get("canon_table_sha256")
        if isinstance(canon_hash, str) and canon_hash:
            hashes.add(canon_hash)
    return hashes


def _ensure_datasets_exist(catalog_root: Path, dataset_ids: list[str]) -> None:
    for dataset_id in sorted(set(dataset_ids)):
        show_dataset(catalog_root=catalog_root, dataset_id=dataset_id)


def validate_runset_payload(catalog_root: Path, runset_payload: dict[str, Any]) -> tuple[bool, str]:
    dataset_ids_raw = runset_payload.get("datasets")
    runs_raw = runset_payload.get("runs")
    policy_raw = runset_payload.get("policy")

    if not isinstance(dataset_ids_raw, list) or not all(isinstance(item, str) and item for item in dataset_ids_raw):
        raise ValidationError("RunSet payload datasets is invalid")
    if not isinstance(runs_raw, list) or not all(isinstance(item, dict) for item in runs_raw):
        raise ValidationError("RunSet payload runs is invalid")
    if not isinstance(policy_raw, dict):
        raise ValidationError("RunSet payload policy is invalid")

    dataset_ids = sorted(set(dataset_ids_raw))
    runs = [dict(item) for item in runs_raw]

    _ensure_datasets_exist(catalog_root=catalog_root, dataset_ids=dataset_ids)

    require_lineage_links = bool(policy_raw.get("require_lineage_links", True))
    require_bidirectional = bool(policy_raw.get("require_bidirectional", True))

    if require_lineage_links:
        links_index = _load_dataset_to_runs_index(catalog_root=catalog_root)

        for dataset_id in dataset_ids:
            linked_hashes = _dataset_linked_hashes(links_index, dataset_id)
            explicit_hashes = _explicit_hashes_for_dataset(runs, dataset_id)

            if require_bidirectional and not linked_hashes and not explicit_hashes:
                raise ValidationError(
                    f"RunSet validation failed: dataset_id={dataset_id} has no dataset_to_runs links and no explicit canon_table_sha256 refs"
                )

        for row in runs:
            row_dataset_id = row.get("dataset_id")
            row_canon_hash = row.get("canon_table_sha256")
            if isinstance(row_dataset_id, str) and row_dataset_id:
                if row_dataset_id not in dataset_ids:
                    raise ValidationError(
                        f"RunSet validation failed: run ref dataset_id={row_dataset_id} not present in runset datasets"
                    )
                if isinstance(row_canon_hash, str) and row_canon_hash:
                    linked_hashes = _dataset_linked_hashes(links_index, row_dataset_id)
                    if row_canon_hash not in linked_hashes:
                        raise ValidationError(
                            "RunSet validation failed: explicit run ref canon_table_sha256 not linked in dataset_to_runs index"
                        )

    return True, f"PASS runset_id={runset_payload['runset_id']}"

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists() or not path.is_file():
        raise ValueError(f"JSON file not found: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"JSON root must be an object: {path}")
    return payload


def _find_single_index(catalog_dir: Path) -> Path:
    matches = sorted(catalog_dir.rglob("dataset_to_runs.index.json"))
    if len(matches) != 1:
        raise ValueError(
            f"Expected exactly 1 dataset_to_runs.index.json under {catalog_dir}, found {len(matches)}"
        )
    return matches[0]


def _es_dataset_ids(datasets_payload: dict[str, Any]) -> list[str]:
    rows = datasets_payload.get("datasets")
    if not isinstance(rows, list):
        raise ValueError("datasets payload missing 'datasets' array")

    ids: list[str] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("datasets payload row must be an object")
        if str(row.get("instrument", "")).upper() != "ES":
            continue
        dataset_id = row.get("dataset_id")
        if not isinstance(dataset_id, str) or not dataset_id:
            raise ValueError("datasets payload has invalid dataset_id for ES row")
        ids.append(dataset_id)

    if not ids:
        raise ValueError("No ES dataset_id entries found in datasets payload")
    return ids


def _pick_explicit_run(index_payload: dict[str, Any], dataset_id: str) -> dict[str, str]:
    datasets_map = index_payload.get("datasets")
    if not isinstance(datasets_map, dict):
        raise ValueError("dataset_to_runs index missing 'datasets' object")

    entry = datasets_map.get(dataset_id)
    if not isinstance(entry, dict):
        raise ValueError(f"No dataset_to_runs entry for dataset_id={dataset_id}")

    runs = entry.get("runs")
    if not isinstance(runs, list) or not runs:
        raise ValueError(f"No runs linked in dataset_to_runs index for dataset_id={dataset_id}")

    candidates: list[tuple[str, str]] = []
    for row in runs:
        if not isinstance(row, dict):
            raise ValueError(f"Invalid run row type for dataset_id={dataset_id}")
        run_ref = row.get("run_ref")
        canon_sha = row.get("canon_table_sha256")
        if not isinstance(run_ref, str) or not run_ref:
            raise ValueError(f"Missing run_ref in dataset_to_runs for dataset_id={dataset_id}")
        if not isinstance(canon_sha, str) or not canon_sha:
            raise ValueError(f"Missing canon_table_sha256 in dataset_to_runs for dataset_id={dataset_id}")
        candidates.append((run_ref, canon_sha))

    run_ref, canon_sha = sorted(candidates, key=lambda item: (item[0], item[1]))[0]
    return {
        "dataset_id": dataset_id,
        "run_ref": run_ref,
        "canon_table_sha256": canon_sha,
    }


def build_explicit_runset(*, catalog_dir: Path, datasets_path: Path, out_path: Path) -> dict[str, Any]:
    index_path = _find_single_index(catalog_dir)
    index_payload = _load_json(index_path)
    datasets_payload = _load_json(datasets_path)

    dataset_ids = _es_dataset_ids(datasets_payload)
    explicit_runs = [_pick_explicit_run(index_payload, dataset_id) for dataset_id in dataset_ids]

    payload: dict[str, Any] = {
        "runset_version": "v1",
        "name": "PILOT_RUNSET_ES_EXPLICIT_FROM_INDEX",
        "datasets": dataset_ids,
        "runs": explicit_runs,
        "policy": {
            "allow_materialize_missing": False,
            "require_lineage_links": True,
            "require_bidirectional": True,
        },
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate deterministic explicit runset spec from dataset_to_runs index"
    )
    parser.add_argument("--catalog", required=True, help="Catalog root (e.g., exec_outputs/catalog)")
    parser.add_argument("--datasets", required=True, help="Pilot datasets JSON (e.g., configs/pilot/datasets.pilot.json)")
    parser.add_argument("--out", required=True, help="Output runset spec path")
    args = parser.parse_args()

    payload = build_explicit_runset(
        catalog_dir=Path(args.catalog),
        datasets_path=Path(args.datasets),
        out_path=Path(args.out),
    )
    print(f"GENERATED_EXPLICIT_RUNSET datasets={len(payload['datasets'])} runs={len(payload['runs'])} out={args.out}")


if __name__ == "__main__":
    main()

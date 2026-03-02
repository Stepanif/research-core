from __future__ import annotations

import os
from pathlib import Path
from statistics import mean, median
from typing import Any

from research_core.runsets.catalog import show_runset, validate_runset
from research_core.runsets.io import canonical_hash, canonical_json_bytes, read_json, write_canonical_json
from research_core.risk.contracts import QUANTILES, REQUIRED_ENV_VAR_CREATED_UTC, RUNSET_RISK_MANIFEST_VERSION, RUNSET_RISK_VERSION
from research_core.risk.writer import write_risk_artifacts
from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.types import ValidationError


def _require_created_utc() -> str:
    value = os.environ.get(REQUIRED_ENV_VAR_CREATED_UTC)
    if not isinstance(value, str) or not value:
        raise ValidationError("Risk operations require RESEARCH_CREATED_UTC")
    return value


def _links_index_path(catalog_dir: Path) -> Path:
    return catalog_dir / "links" / "dataset_to_runs.index.json"


def _load_links_index(catalog_dir: Path) -> dict[str, Any]:
    path = _links_index_path(catalog_dir)
    if not path.exists() or not path.is_file():
        raise ValidationError(f"Risk runset missing dataset_to_runs index: {path}")
    payload = read_json(path)
    if not isinstance(payload, dict):
        raise ValidationError("Risk runset dataset_to_runs index payload invalid")
    datasets = payload.get("datasets")
    if not isinstance(datasets, dict):
        raise ValidationError("Risk runset dataset_to_runs datasets payload invalid")
    return payload


def _dataset_links(links_index: dict[str, Any], dataset_id: str) -> list[dict[str, str]]:
    datasets = links_index.get("datasets")
    assert isinstance(datasets, dict)
    row = datasets.get(dataset_id)
    if not isinstance(row, dict):
        return []

    runs = row.get("runs")
    if not isinstance(runs, list):
        raise ValidationError("Risk runset dataset_to_runs row runs payload invalid")

    output: list[dict[str, str]] = []
    for item in runs:
        if not isinstance(item, dict):
            raise ValidationError("Risk runset dataset_to_runs run payload invalid")
        run_ref = item.get("run_ref")
        canon_hash = item.get("canon_table_sha256")
        lineage_hash = item.get("run_lineage_canonical_sha256")
        if not isinstance(run_ref, str) or not run_ref or not isinstance(canon_hash, str) or not canon_hash:
            raise ValidationError("Risk runset dataset_to_runs run row missing run_ref/canon_table_sha256")
        payload = {
            "run_ref": run_ref,
            "canon_table_sha256": canon_hash,
            "lineage_hash": lineage_hash if isinstance(lineage_hash, str) else "",
        }
        output.append(payload)
    return sorted(output, key=lambda item: (item["canon_table_sha256"], item["run_ref"]))


def _resolve_run_dir(run_ref: str, catalog_dir: Path) -> Path | None:
    ref = Path(run_ref)
    candidates: list[Path] = []
    if ref.is_absolute():
        candidates.append(ref)
    else:
        candidates.append((Path.cwd() / ref).resolve())
        candidates.append((catalog_dir.parent / ref).resolve())

    for candidate in candidates:
        if candidate.exists() and candidate.is_dir():
            return candidate
    return None


def _explicit_rows_for_dataset(runset_payload: dict[str, Any], dataset_id: str) -> list[dict[str, Any]]:
    runs = runset_payload.get("runs")
    if not isinstance(runs, list):
        raise ValidationError("Risk runset runset entry runs payload invalid")

    output: list[dict[str, Any]] = []
    for row in runs:
        if not isinstance(row, dict):
            raise ValidationError("Risk runset runset entry run payload invalid")
        if row.get("dataset_id") == dataset_id:
            output.append(dict(row))

    return sorted(
        output,
        key=lambda item: (
            str(item.get("dataset_id", "")),
            str(item.get("canon_table_sha256", "")),
            str(item.get("run_ref", "")),
        ),
    )


def _quantile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    index = (len(ordered) - 1) * q
    lower = int(index)
    upper = min(lower + 1, len(ordered) - 1)
    if lower == upper:
        return ordered[lower]
    weight = index - lower
    return ordered[lower] * (1.0 - weight) + ordered[upper] * weight


def _select_runs(runset_payload: dict[str, Any], links_index: dict[str, Any]) -> list[dict[str, str]]:
    datasets = runset_payload.get("datasets")
    if not isinstance(datasets, list) or not all(isinstance(item, str) and item for item in datasets):
        raise ValidationError("Risk runset invalid runset datasets payload")

    selected: list[dict[str, str]] = []

    for dataset_id in sorted(set([str(item) for item in datasets])):
        links = _dataset_links(links_index, dataset_id)
        explicit = _explicit_rows_for_dataset(runset_payload, dataset_id)

        if explicit:
            for row in explicit:
                run_ref = row.get("run_ref")
                if not isinstance(run_ref, str) or not run_ref:
                    raise ValidationError("Risk runset explicit run_ref is invalid")

                canon_hash = row.get("canon_table_sha256")
                if isinstance(canon_hash, str) and canon_hash:
                    matching = [item for item in links if item["canon_table_sha256"] == canon_hash]
                    if not matching:
                        raise ValidationError(
                            "Risk runset conflict fail-loud: explicit canon_table_sha256 not present in dataset_to_runs"
                        )
                    chosen = sorted(matching, key=lambda item: item["run_ref"])[0]
                else:
                    matching_ref = [item for item in links if item["run_ref"] == run_ref]
                    if not matching_ref:
                        raise ValidationError(
                            "Risk runset conflict fail-loud: explicit run_ref not present in dataset_to_runs"
                        )
                    chosen = matching_ref[0]

                selected.append(
                    {
                        "dataset_id": dataset_id,
                        "run_ref": chosen["run_ref"],
                        "canon_table_sha256": chosen["canon_table_sha256"],
                        "lineage_hash": chosen["lineage_hash"],
                    }
                )
        else:
            if not links:
                raise ValidationError(f"Risk runset missing lineage links for dataset_id={dataset_id}")
            chosen = links[0]
            selected.append(
                {
                    "dataset_id": dataset_id,
                    "run_ref": chosen["run_ref"],
                    "canon_table_sha256": chosen["canon_table_sha256"],
                    "lineage_hash": chosen["lineage_hash"],
                }
            )

    return sorted(selected, key=lambda item: (item["dataset_id"], item["canon_table_sha256"], item["run_ref"]))


def compute_runset_risk(*, catalog_dir: Path, runset_id: str, out_dir: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()

    runset_payload = show_runset(catalog_root=catalog_dir, runset_id=runset_id)
    ok, text = validate_runset(catalog_root=catalog_dir, runset_id=runset_id)
    if not ok:
        raise ValidationError(text)

    links_index = _load_links_index(catalog_dir)
    selected_runs = _select_runs(runset_payload, links_index)

    per_run_rows: list[dict[str, Any]] = []
    per_run_psa_manifests: list[dict[str, str]] = []

    for selected in selected_runs:
        run_ref = selected["run_ref"]
        run_dir = _resolve_run_dir(run_ref, catalog_dir=catalog_dir)
        if run_dir is None:
            raise ValidationError(f"Risk runset could not resolve run_ref={run_ref}")

        per_run = write_risk_artifacts(run_dir)
        summary = per_run["summary"]

        psa_manifest_path = run_dir / "psa.manifest.json"
        per_run_psa_manifests.append(
            {
                "path": f"{run_ref}/psa.manifest.json",
                "sha256": sha256_file(psa_manifest_path),
                "bytes": int(psa_manifest_path.stat().st_size),
            }
        )

        per_run_rows.append(
            {
                "dataset_id": selected["dataset_id"],
                "run_ref": run_ref,
                "canon_table_sha256": selected["canon_table_sha256"],
                "psa_table_sha256": summary["inputs"]["psa_table_sha256"],
                "instability_score": summary["instability_score"],
                "event_rates_per_1000": summary["event_rates_per_1000"],
                "state_entropy_bits": summary["distributions"]["state_entropy_bits"],
                "transition_entropy_bits": summary["distributions"]["transition_entropy_bits"],
            }
        )

    ordered_rows = sorted(per_run_rows, key=lambda item: (item["dataset_id"], item["canon_table_sha256"], item["run_ref"]))
    run_count = len(ordered_rows)

    instability_values = [float(item["instability_score"]) for item in ordered_rows]
    event_rate_keys = sorted(ordered_rows[0]["event_rates_per_1000"].keys()) if ordered_rows else []

    event_rates_mean = {
        key: mean([float(row["event_rates_per_1000"][key]) for row in ordered_rows]) if ordered_rows else 0.0
        for key in event_rate_keys
    }

    worst_5 = sorted(
        ordered_rows,
        key=lambda item: (-float(item["instability_score"]), item["dataset_id"], item["canon_table_sha256"], item["run_ref"]),
    )[:5]

    summary_payload: dict[str, Any] = {
        "runset_risk_version": RUNSET_RISK_VERSION,
        "created_utc": created_utc,
        "runset_id": runset_id,
        "run_count": run_count,
        "per_run": ordered_rows,
        "aggregates": {
            "instability": {
                "mean": mean(instability_values) if instability_values else 0.0,
                "median": median(instability_values) if instability_values else 0.0,
                "p10": _quantile(instability_values, QUANTILES[0]),
                "p50": _quantile(instability_values, QUANTILES[1]),
                "p90": _quantile(instability_values, QUANTILES[2]),
            },
            "event_rates_mean_per_1000": event_rates_mean,
            "worst_5": worst_5,
        },
    }
    summary_payload["runset_risk_canonical_sha256"] = canonical_hash(summary_payload, self_field="runset_risk_canonical_sha256")

    output_root = out_dir / runset_id
    summary_path = output_root / "risk.runset.summary.json"
    manifest_path = output_root / "risk.runset.manifest.json"

    runset_entry_path = catalog_dir / "runsets" / "entries" / f"{runset_id}.json"
    links_path = _links_index_path(catalog_dir)

    summary_bytes = canonical_json_bytes(summary_payload)

    manifest_payload: dict[str, Any] = {
        "manifest_version": RUNSET_RISK_MANIFEST_VERSION,
        "created_utc": created_utc,
        "inputs": sorted(
            [
                {
                    "path": f"runsets/entries/{runset_id}.json",
                    "sha256": sha256_file(runset_entry_path),
                    "bytes": int(runset_entry_path.stat().st_size),
                },
                {
                    "path": "links/dataset_to_runs.index.json",
                    "sha256": sha256_file(links_path),
                    "bytes": int(links_path.stat().st_size),
                    "canonical_sha256": canonical_hash(links_index),
                },
                *per_run_psa_manifests,
            ],
            key=lambda item: str(item["path"]),
        ),
        "outputs": {
            "risk.runset.summary.json": {
                "sha256": sha256_bytes(summary_bytes),
                "bytes": len(summary_bytes),
            }
        },
    }
    manifest_payload["runset_risk_manifest_canonical_sha256"] = canonical_hash(
        manifest_payload,
        self_field="runset_risk_manifest_canonical_sha256",
    )

    output_root.mkdir(parents=True, exist_ok=True)
    summary_path.write_bytes(summary_bytes)
    write_canonical_json(manifest_path, manifest_payload)

    return {
        "summary": summary_payload,
        "manifest": manifest_payload,
        "summary_path": summary_path,
        "manifest_path": manifest_path,
    }

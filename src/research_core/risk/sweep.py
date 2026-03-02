from __future__ import annotations

from pathlib import Path
from statistics import mean
from typing import Any

from research_core.risk.runset_agg import compute_runset_risk
from research_core.runsets.io import canonical_hash, canonical_json_bytes, read_json, write_canonical_json
from research_core.util.buildmeta import get_created_utc
from research_core.util.hashing import sha256_bytes, sha256_file
from research_core.util.types import ValidationError

BASELINE_CARD_VERSION = "v1"
BASELINE_CARD_MANIFEST_VERSION = "v1"
REQUIRED_ENV_VAR_CREATED_UTC = "RESEARCH_CREATED_UTC"


def _require_created_utc() -> str:
    return get_created_utc(required=True, error_message="Risk operations require RESEARCH_CREATED_UTC")


def _hash_with_optional_self_field(payload: dict[str, Any], self_field: str) -> str:
    return canonical_hash(payload, self_field=self_field)


def _format_metric(value: Any) -> str:
    if value is None:
        return "NA"
    try:
        return f"{float(value):.6f}"
    except (TypeError, ValueError):
        return "NA"


def _mean_if_all_present(per_run_rows: list[dict[str, Any]], key: str) -> float | None:
    if not per_run_rows:
        return None

    values: list[float] = []
    for row in per_run_rows:
        if key not in row or row.get(key) is None:
            return None
        try:
            values.append(float(row[key]))
        except (TypeError, ValueError):
            return None
    return mean(values)


def _per_run_vector_sha256(per_run_rows: list[dict[str, Any]]) -> str:
    lines: list[str] = []

    for row in per_run_rows:
        if not isinstance(row, dict):
            raise ValidationError("Risk sweep per_run payload row must be an object")

        canon_table_sha256 = row.get("canon_table_sha256")
        run_ref = row.get("run_ref")
        if not isinstance(canon_table_sha256, str) or not canon_table_sha256:
            raise ValidationError("Risk sweep per_run row missing canon_table_sha256")
        if not isinstance(run_ref, str) or not run_ref:
            raise ValidationError("Risk sweep per_run row missing run_ref")

        rates = row.get("event_rates_per_1000")
        if rates is not None and not isinstance(rates, dict):
            raise ValidationError("Risk sweep per_run row event_rates_per_1000 must be an object when present")

        p_flip = rates.get("p_flip") if isinstance(rates, dict) else None
        a_flip = rates.get("a_flip") if isinstance(rates, dict) else None

        line = (
            f"{_format_metric(row.get('instability_score'))}|"
            f"{_format_metric(row.get('state_entropy_bits'))}|"
            f"{_format_metric(row.get('transition_entropy_bits'))}|"
            f"{_format_metric(p_flip)}|"
            f"{_format_metric(a_flip)}|"
            f"{canon_table_sha256}|"
            f"{run_ref}\n"
        )
        lines.append(line)

    ordered = sorted(lines)
    return sha256_bytes("".join(ordered).encode("utf-8"))


def _build_top_5_worst(per_run_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    sortable: list[dict[str, Any]] = []
    for row in per_run_rows:
        dataset_id = row.get("dataset_id")
        run_ref = row.get("run_ref")
        canon_table_sha256 = row.get("canon_table_sha256")
        instability_score = row.get("instability_score")

        if not isinstance(dataset_id, str) or not dataset_id:
            raise ValidationError("Risk sweep per_run row missing dataset_id")
        if not isinstance(run_ref, str) or not run_ref:
            raise ValidationError("Risk sweep per_run row missing run_ref")
        if not isinstance(canon_table_sha256, str) or not canon_table_sha256:
            raise ValidationError("Risk sweep per_run row missing canon_table_sha256")
        try:
            instability = float(instability_score)
        except (TypeError, ValueError):
            raise ValidationError("Risk sweep per_run row instability_score must be numeric")

        sortable.append(
            {
                "dataset_id": dataset_id,
                "run_ref": run_ref,
                "canon_table_sha256": canon_table_sha256,
                "instability_score": instability,
            }
        )

    return sorted(sortable, key=lambda item: (-item["instability_score"], item["dataset_id"], item["run_ref"]))[:5]


def run_risk_sweep(*, catalog_dir: Path, runset_id: str, out_dir: Path) -> dict[str, Any]:
    created_utc = _require_created_utc()

    runset_result = compute_runset_risk(catalog_dir=catalog_dir, runset_id=runset_id, out_dir=out_dir)

    summary_path = Path(runset_result["summary_path"])
    runset_manifest_path = Path(runset_result["manifest_path"])
    if not summary_path.exists() or not runset_manifest_path.exists():
        raise ValidationError("Risk sweep expected risk runset artifacts are missing")

    runset_entry_path = catalog_dir / "runsets" / "entries" / f"{runset_id}.json"
    links_index_path = catalog_dir / "links" / "dataset_to_runs.index.json"
    if not runset_entry_path.exists() or not links_index_path.exists():
        raise ValidationError("Risk sweep missing runset entry or dataset_to_runs index")

    summary_payload = read_json(summary_path)
    if not isinstance(summary_payload, dict):
        raise ValidationError("Risk sweep invalid risk.runset.summary.json payload")

    runset_manifest_payload = read_json(runset_manifest_path)
    if not isinstance(runset_manifest_payload, dict):
        raise ValidationError("Risk sweep invalid risk.runset.manifest.json payload")

    runset_manifest_hash = _hash_with_optional_self_field(
        runset_manifest_payload,
        self_field="runset_risk_manifest_canonical_sha256",
    )
    existing_manifest_hash = runset_manifest_payload.get("runset_risk_manifest_canonical_sha256")
    if isinstance(existing_manifest_hash, str) and existing_manifest_hash != runset_manifest_hash:
        raise ValidationError("Risk sweep detected inconsistent risk.runset.manifest.json canonical hash")

    runset_entry_payload = read_json(runset_entry_path)
    links_index_payload = read_json(links_index_path)

    per_run_rows = summary_payload.get("per_run")
    if not isinstance(per_run_rows, list):
        raise ValidationError("Risk sweep missing per_run list in risk.runset.summary.json")

    run_count = summary_payload.get("run_count")
    if not isinstance(run_count, int):
        raise ValidationError("Risk sweep missing run_count in risk.runset.summary.json")
    if run_count != len(per_run_rows):
        raise ValidationError("Risk sweep run_count does not match per_run length")

    aggregates = summary_payload.get("aggregates")
    if not isinstance(aggregates, dict):
        raise ValidationError("Risk sweep missing aggregates in risk.runset.summary.json")
    instability = aggregates.get("instability")
    if not isinstance(instability, dict):
        raise ValidationError("Risk sweep missing aggregates.instability in risk.runset.summary.json")

    baseline_card: dict[str, Any] = {
        "card_version": BASELINE_CARD_VERSION,
        "created_utc": created_utc,
        "runset_id": runset_id,
        "inputs": {
            "runset_entry_canonical_sha256": _hash_with_optional_self_field(
                runset_entry_payload,
                self_field="runset_entry_canonical_sha256",
            ),
            "dataset_to_runs_index_canonical_sha256": canonical_hash(links_index_payload),
            "risk_runset_manifest_canonical_sha256": runset_manifest_hash,
        },
        "key_metrics": {
            "run_count": run_count,
            "instability_mean": float(instability.get("mean", 0.0)),
            "instability_median": float(instability.get("median", 0.0)),
            "instability_p10": float(instability.get("p10", 0.0)),
            "instability_p90": float(instability.get("p90", 0.0)),
            "top_5_worst": _build_top_5_worst(per_run_rows),
        },
        "checksums": {
            "per_run_vector_sha256": _per_run_vector_sha256(per_run_rows),
        },
    }

    state_entropy_mean = _mean_if_all_present(per_run_rows, "state_entropy_bits")
    if state_entropy_mean is not None:
        baseline_card["key_metrics"]["state_entropy_mean"] = state_entropy_mean

    transition_entropy_mean = _mean_if_all_present(per_run_rows, "transition_entropy_bits")
    if transition_entropy_mean is not None:
        baseline_card["key_metrics"]["transition_entropy_mean"] = transition_entropy_mean

    baseline_card["baseline_card_canonical_sha256"] = canonical_hash(
        baseline_card,
        self_field="baseline_card_canonical_sha256",
    )

    baseline_card_bytes = canonical_json_bytes(baseline_card)

    baseline_card_manifest: dict[str, Any] = {
        "manifest_version": BASELINE_CARD_MANIFEST_VERSION,
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
                    "sha256": sha256_file(links_index_path),
                    "bytes": int(links_index_path.stat().st_size),
                },
                {
                    "path": "risk.runset.summary.json",
                    "sha256": sha256_file(summary_path),
                    "bytes": int(summary_path.stat().st_size),
                },
                {
                    "path": "risk.runset.manifest.json",
                    "sha256": sha256_file(runset_manifest_path),
                    "bytes": int(runset_manifest_path.stat().st_size),
                },
            ],
            key=lambda item: str(item["path"]),
        ),
        "outputs": {
            "baseline.card.json": {
                "sha256": sha256_bytes(baseline_card_bytes),
                "bytes": len(baseline_card_bytes),
            }
        },
    }
    baseline_card_manifest["baseline_card_manifest_canonical_sha256"] = canonical_hash(
        baseline_card_manifest,
        self_field="baseline_card_manifest_canonical_sha256",
    )

    output_root = out_dir / runset_id
    baseline_card_path = output_root / "baseline.card.json"
    baseline_card_manifest_path = output_root / "baseline.card.manifest.json"

    output_root.mkdir(parents=True, exist_ok=True)
    baseline_card_path.write_bytes(baseline_card_bytes)
    write_canonical_json(baseline_card_manifest_path, baseline_card_manifest)

    return {
        "summary_path": summary_path,
        "runset_manifest_path": runset_manifest_path,
        "baseline_card_path": baseline_card_path,
        "baseline_card_manifest_path": baseline_card_manifest_path,
    }

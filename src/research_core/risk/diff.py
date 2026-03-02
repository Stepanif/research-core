from __future__ import annotations

from typing import Any

from research_core.risk.contracts import (
    BASELINE_DIFF_VERSION,
    INSTABILITY_LESS_UNSTABLE_DELTA_THRESHOLD,
    INSTABILITY_MORE_UNSTABLE_DELTA_THRESHOLD,
)
from research_core.util.types import ValidationError


def _require_str(payload: dict[str, Any], key: str, context: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value:
        raise ValidationError(f"{context} missing required string field: {key}")
    return value


def _require_dict(payload: dict[str, Any], key: str, context: str) -> dict[str, Any]:
    value = payload.get(key)
    if not isinstance(value, dict):
        raise ValidationError(f"{context} missing required object field: {key}")
    return value


def _require_number(payload: dict[str, Any], key: str, context: str) -> float:
    value = payload.get(key)
    if not isinstance(value, (int, float)):
        raise ValidationError(f"{context} missing required numeric field: {key}")
    return float(value)


def _card_ref(card: dict[str, Any], context: str) -> dict[str, str]:
    _require_str(card, "card_version", context)
    if card["card_version"] != "v1":
        raise ValidationError(f"{context} card_version must be v1")

    runset_id = _require_str(card, "runset_id", context)
    baseline_card_canonical_sha256 = _require_str(card, "baseline_card_canonical_sha256", context)

    checksums = _require_dict(card, "checksums", context)
    per_run_vector_sha256 = _require_str(checksums, "per_run_vector_sha256", f"{context}.checksums")

    return {
        "runset_id": runset_id,
        "baseline_card_canonical_sha256": baseline_card_canonical_sha256,
        "per_run_vector_sha256": per_run_vector_sha256,
    }


def _worst5_keys(card: dict[str, Any], context: str) -> set[tuple[str, str, str]]:
    key_metrics = _require_dict(card, "key_metrics", context)
    top_5_worst = key_metrics.get("top_5_worst")
    if not isinstance(top_5_worst, list):
        raise ValidationError(f"{context}.key_metrics.top_5_worst must be a list")

    keys: set[tuple[str, str, str]] = set()
    for index, row in enumerate(top_5_worst):
        if not isinstance(row, dict):
            raise ValidationError(f"{context}.key_metrics.top_5_worst[{index}] must be an object")
        dataset_id = _require_str(row, "dataset_id", f"{context}.key_metrics.top_5_worst[{index}]")
        canon_table_sha256 = _require_str(row, "canon_table_sha256", f"{context}.key_metrics.top_5_worst[{index}]")
        run_ref = _require_str(row, "run_ref", f"{context}.key_metrics.top_5_worst[{index}]")
        keys.add((dataset_id, canon_table_sha256, run_ref))
    return keys


def _classification(instability_mean_delta: float) -> dict[str, str]:
    if instability_mean_delta >= INSTABILITY_MORE_UNSTABLE_DELTA_THRESHOLD:
        return {
            "label": "MORE_UNSTABLE",
            "rationale": "instability_mean_delta >= 5.0",
        }
    if instability_mean_delta <= INSTABILITY_LESS_UNSTABLE_DELTA_THRESHOLD:
        return {
            "label": "LESS_UNSTABLE",
            "rationale": "instability_mean_delta <= -5.0",
        }
    return {
        "label": "NO_CHANGE",
        "rationale": "-5.0 < instability_mean_delta < 5.0",
    }


def compare_baseline_cards(*, a_card: dict[str, Any], b_card: dict[str, Any], created_utc: str) -> dict[str, Any]:
    if not isinstance(created_utc, str) or not created_utc:
        raise ValidationError("created_utc is required")

    a_ref = _card_ref(a_card, "a")
    b_ref = _card_ref(b_card, "b")

    a_metrics = _require_dict(a_card, "key_metrics", "a")
    b_metrics = _require_dict(b_card, "key_metrics", "b")

    instability_mean_delta = _require_number(b_metrics, "instability_mean", "b.key_metrics") - _require_number(
        a_metrics, "instability_mean", "a.key_metrics"
    )
    instability_median_delta = _require_number(b_metrics, "instability_median", "b.key_metrics") - _require_number(
        a_metrics, "instability_median", "a.key_metrics"
    )
    instability_p10_delta = _require_number(b_metrics, "instability_p10", "b.key_metrics") - _require_number(
        a_metrics, "instability_p10", "a.key_metrics"
    )
    instability_p90_delta = _require_number(b_metrics, "instability_p90", "b.key_metrics") - _require_number(
        a_metrics, "instability_p90", "a.key_metrics"
    )

    deltas: dict[str, Any] = {
        "instability_mean_delta": instability_mean_delta,
        "instability_median_delta": instability_median_delta,
        "instability_p10_delta": instability_p10_delta,
        "instability_p90_delta": instability_p90_delta,
    }

    if "state_entropy_mean" in a_metrics and "state_entropy_mean" in b_metrics:
        deltas["state_entropy_mean_delta"] = _require_number(
            b_metrics, "state_entropy_mean", "b.key_metrics"
        ) - _require_number(a_metrics, "state_entropy_mean", "a.key_metrics")

    if "transition_entropy_mean" in a_metrics and "transition_entropy_mean" in b_metrics:
        deltas["transition_entropy_mean_delta"] = _require_number(
            b_metrics, "transition_entropy_mean", "b.key_metrics"
        ) - _require_number(a_metrics, "transition_entropy_mean", "a.key_metrics")

    a_worst5 = _worst5_keys(a_card, "a")
    b_worst5 = _worst5_keys(b_card, "b")
    union = a_worst5 | b_worst5
    intersection = a_worst5 & b_worst5

    union_count = len(union)
    intersection_count = len(intersection)
    jaccard = 1.0 if union_count == 0 else float(intersection_count) / float(union_count)

    per_run_vector_match = a_ref["per_run_vector_sha256"] == b_ref["per_run_vector_sha256"]

    return {
        "diff_version": BASELINE_DIFF_VERSION,
        "created_utc": created_utc,
        "a": a_ref,
        "b": b_ref,
        "deltas": deltas,
        "worst5_overlap": {
            "jaccard": jaccard,
            "intersection_count": intersection_count,
            "union_count": union_count,
        },
        "checksum": {
            "per_run_vector_match": per_run_vector_match,
        },
        "classification": _classification(instability_mean_delta),
    }

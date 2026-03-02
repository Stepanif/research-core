from __future__ import annotations

import math
from typing import Any

from research_core.risk.contracts import (
    EVENT_BITS,
    K_SET,
    WEIGHT_A_FLIP,
    WEIGHT_CONCENTRATION,
    WEIGHT_P_FLIP,
    WEIGHT_STATE_CHANGE,
)


def _safe_rate_per_1000(count: int, transition_count: int) -> float:
    if transition_count <= 0:
        return 0.0
    return (float(count) / float(transition_count)) * 1000.0


def _max_consecutive_true(bits: list[bool]) -> int:
    best = 0
    current = 0
    for value in bits:
        if value:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best


def _entropy_bits_from_counts(counts: dict[str, int]) -> float:
    total = sum(counts.values())
    if total <= 0:
        return 0.0
    entropy = 0.0
    for count in counts.values():
        if count <= 0:
            continue
        p = float(count) / float(total)
        entropy -= p * math.log2(p)
    return entropy


def _top_share_k(counts: dict[str, int], k: int) -> float:
    total = sum(counts.values())
    if total <= 0:
        return 0.0
    sorted_counts = sorted(counts.values(), reverse=True)
    top = sum(sorted_counts[:k])
    return float(top) / float(total)


def _transition_counts(states: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    if len(states) <= 1:
        return counts
    for index in range(1, len(states)):
        prev_state = states[index - 1]
        next_state = states[index]
        key = f"{prev_state}->{next_state}"
        counts[key] = counts.get(key, 0) + 1
    return counts


def _state_counts(states: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for state in states:
        counts[state] = counts.get(state, 0) + 1
    return counts


def compute_risk_metrics(*, event_mask: list[int], state_id: list[str]) -> dict[str, Any]:
    row_count = len(state_id)
    transition_count = max(row_count - 1, 0)

    event_counts: dict[str, int] = {}
    event_flags: dict[str, list[bool]] = {}

    for event_name, bit in EVENT_BITS.items():
        flags = [(mask & bit) != 0 for mask in event_mask]
        event_flags[event_name] = flags
        event_counts[event_name] = sum(1 for value in flags if value)

    event_rates_per_1000 = {
        event_name: _safe_rate_per_1000(event_counts[event_name], transition_count)
        for event_name in sorted(event_counts)
    }

    state_counts = _state_counts(state_id)
    transition_counts = _transition_counts(state_id)

    top_state_share_k = {str(k): _top_share_k(state_counts, k) for k in K_SET}
    top_transition_share_k = {str(k): _top_share_k(transition_counts, k) for k in K_SET}

    concentration_term = 1.0 - top_transition_share_k["10"]
    instability_score = (
        WEIGHT_STATE_CHANGE * event_rates_per_1000["state_change"]
        + WEIGHT_P_FLIP * event_rates_per_1000["p_flip"]
        + WEIGHT_A_FLIP * event_rates_per_1000["a_flip"]
        + WEIGHT_CONCENTRATION * concentration_term * 1000.0
    )

    return {
        "counts": {
            "row_count": row_count,
            "transition_count": transition_count,
        },
        "event_rates_per_1000": event_rates_per_1000,
        "streaks": {
            "max_state_change_streak": _max_consecutive_true(event_flags["state_change"]),
            "max_p_flip_streak": _max_consecutive_true(event_flags["p_flip"]),
            "max_a_flip_streak": _max_consecutive_true(event_flags["a_flip"]),
        },
        "distributions": {
            "state_entropy_bits": _entropy_bits_from_counts(state_counts),
            "transition_entropy_bits": _entropy_bits_from_counts(transition_counts),
            "top_state_share_k": top_state_share_k,
            "top_transition_share_k": top_transition_share_k,
        },
        "instability_score": instability_score,
    }

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Any

import pandas as pd

from research_core.psa.contracts import (
    EVENT_A_CHANGE,
    EVENT_A_FLIP,
    EVENT_P_CHANGE,
    EVENT_P_FLIP,
    EVENT_S_CHANGE,
    EVENT_S_FLIP,
    EVENT_STATE_CHANGE,
)
from research_core.util.types import ValidationError

EVENT_MASK_BITS: list[tuple[str, int]] = [
    ("state_change", EVENT_STATE_CHANGE),
    ("p_change", EVENT_P_CHANGE),
    ("s_change", EVENT_S_CHANGE),
    ("a_change", EVENT_A_CHANGE),
    ("p_flip", EVENT_P_FLIP),
    ("s_flip", EVENT_S_FLIP),
    ("a_flip", EVENT_A_FLIP),
]


def build_transition_matrix_from_psa(psa_path: Path, include_event_bits: bool) -> dict[str, Any]:
    if not psa_path.exists():
        raise ValidationError(f"Missing psa parquet for experiment: {psa_path}")

    psa_df = pd.read_parquet(psa_path)
    if "state_id" not in psa_df.columns:
        raise ValidationError("PSA parquet missing required column: state_id")
    if include_event_bits and "event_mask" not in psa_df.columns:
        raise ValidationError("PSA parquet missing required column for include_event_bits=true: event_mask")

    state_ids = [str(value) for value in psa_df["state_id"].tolist()]
    row_count = len(state_ids)

    transition_counter: Counter[tuple[str, str]] = Counter()
    nested: dict[str, dict[str, int]] = {}

    for index in range(1, row_count):
        prev_state = state_ids[index - 1]
        next_state = state_ids[index]
        transition_counter[(prev_state, next_state)] += 1

    prev_keys = sorted({key[0] for key in transition_counter.keys()})
    for prev_state in prev_keys:
        next_counts = {
            next_state: int(count)
            for (p_state, next_state), count in transition_counter.items()
            if p_state == prev_state
        }
        nested[prev_state] = {key: next_counts[key] for key in sorted(next_counts.keys())}

    top_transitions = [
        {"prev": prev_state, "next": next_state, "count": int(count)}
        for (prev_state, next_state), count in sorted(
            transition_counter.items(),
            key=lambda item: (-item[1], item[0][0], item[0][1]),
        )[:50]
    ]

    payload: dict[str, Any] = {
        "row_count": int(row_count),
        "transition_count": int(max(row_count - 1, 0)),
        "transitions": nested,
        "top_transitions": top_transitions,
    }

    if include_event_bits:
        bit_counts = {name: 0 for name, _ in EVENT_MASK_BITS}
        event_masks = psa_df["event_mask"].tolist()
        for index in range(1, row_count):
            mask = int(event_masks[index])
            for name, bit in EVENT_MASK_BITS:
                if mask & bit:
                    bit_counts[name] += 1
        payload["event_bit_transition_counts"] = bit_counts

    return payload

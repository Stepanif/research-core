from __future__ import annotations

import pandas as pd

from research_core.psa.contracts import (
    A_BEAR,
    A_BULL,
    A_DOJI,
    P_CONST,
    P_DOWN,
    P_UP,
    S_FLAT,
    compute_event_mask,
    make_state_id,
    validate_canon_input_v1,
)
from research_core.util.types import ValidationError


def run_psa_v1(canon_df: pd.DataFrame, psa_schema_payload: dict) -> pd.DataFrame:
    if canon_df.empty:
        raise ValidationError("PSA input is empty; fail-loud policy forbids empty input")

    validate_canon_input_v1(canon_df)

    output = canon_df[["ts", "instrument", "tf", "open", "close"]].copy()
    output["a"] = A_DOJI
    output.loc[output["close"] > output["open"], "a"] = A_BULL
    output.loc[output["close"] < output["open"], "a"] = A_BEAR

    close_delta = output["close"].diff()
    output["p"] = P_CONST
    output.loc[close_delta > 0, "p"] = P_UP
    output.loc[close_delta < 0, "p"] = P_DOWN
    output["s"] = S_FLAT

    output["state_id"] = [make_state_id(p_token, s_token, a_token) for p_token, s_token, a_token in zip(output["p"], output["s"], output["a"]) ]

    event_masks: list[int] = [0]
    for index in range(1, len(output)):
        previous = output.iloc[index - 1]
        current = output.iloc[index]
        event_masks.append(
            compute_event_mask(
                previous_p=previous["p"],
                previous_s=previous["s"],
                previous_a=previous["a"],
                current_p=current["p"],
                current_s=current["s"],
                current_a=current["a"],
            )
        )
    output["event_mask"] = event_masks

    required_columns = psa_schema_payload["required_columns"]
    missing = [column for column in required_columns if column not in output.columns]
    if missing:
        raise ValidationError(f"PSA output schema mismatch: missing required columns {missing}")

    ordered_columns = required_columns + ["p", "s"]
    return output[ordered_columns]

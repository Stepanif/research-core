from __future__ import annotations

import pandas as pd

from research_core.psa.contracts import validate_canon_input_v1
from research_core.util.types import ValidationError


ALIGN_BULL = "BULL"
ALIGN_BEAR = "BEAR"
ALIGN_DOJI = "DOJI"


def run_psa_v1(canon_df: pd.DataFrame, psa_schema_payload: dict) -> pd.DataFrame:
    validate_canon_input_v1(canon_df)

    output = canon_df[["ts", "instrument", "tf", "open", "close"]].copy()
    output["a"] = ALIGN_DOJI
    output.loc[output["close"] > output["open"], "a"] = ALIGN_BULL
    output.loc[output["close"] < output["open"], "a"] = ALIGN_BEAR

    required_columns = psa_schema_payload["required_columns"]
    missing = [column for column in required_columns if column not in output.columns]
    if missing:
        raise ValidationError(f"PSA output schema mismatch: missing required columns {missing}")

    return output[required_columns]

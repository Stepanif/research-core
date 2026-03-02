from __future__ import annotations

import pandas as pd

from research_core.util.types import ValidationError


def validate_canon_invariants(df: pd.DataFrame, keep_updown: bool) -> None:
    required = ["ts", "instrument", "tf", "open", "high", "low", "close", "volume"]
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValidationError(f"Missing required canon columns: {missing}")

    if df[required].isna().any().any():
        raise ValidationError("NaN values detected in required canon columns")

    if not df["ts"].is_monotonic_increasing:
        raise ValidationError("Canon timestamps must be monotonic increasing")
    if df["ts"].duplicated().any():
        raise ValidationError("Duplicate canon timestamps are forbidden")

    high_bad = df["high"] < df[["open", "close"]].max(axis=1)
    if high_bad.any():
        raise ValidationError("Invalid OHLC: high < max(open, close)")

    low_bad = df["low"] > df[["open", "close"]].min(axis=1)
    if low_bad.any():
        raise ValidationError("Invalid OHLC: low > min(open, close)")

    if (df["high"] < df["low"]).any():
        raise ValidationError("Invalid OHLC: high < low")

    if (df["volume"] < 0).any():
        raise ValidationError("Invalid volume: negative values are forbidden")

    if keep_updown:
        if "up" not in df.columns or "down" not in df.columns:
            raise ValidationError("keep_updown=true requires up/down columns")
        if (df["up"] < 0).any() or (df["down"] < 0).any():
            raise ValidationError("Invalid up/down: negative values are forbidden")

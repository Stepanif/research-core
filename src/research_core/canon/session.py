from __future__ import annotations

from datetime import time

import pandas as pd

from research_core.util.types import ValidationError


def parse_hhmm(value: str) -> time:
    try:
        hour_str, minute_str = value.split(":", 1)
        hour = int(hour_str)
        minute = int(minute_str)
        return time(hour=hour, minute=minute)
    except Exception as exc:  # noqa: BLE001
        raise ValidationError(f"Invalid HH:MM time value: {value}") from exc


def apply_session_policy(
    df: pd.DataFrame,
    session_policy: str,
    rth_start: str,
    rth_end: str,
) -> pd.DataFrame:
    if session_policy == "full":
        return df

    start_t = parse_hhmm(rth_start)
    end_t = parse_hhmm(rth_end)
    local_times = df["ts"].dt.tz_convert("America/New_York").dt.time
    in_rth = (local_times >= start_t) & (local_times <= end_t)

    if session_policy == "rth":
        return df.loc[in_rth].copy()
    if session_policy == "eth":
        return df.loc[~in_rth].copy()
    raise ValidationError(f"Unsupported session policy: {session_policy}")

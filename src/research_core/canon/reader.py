from __future__ import annotations

from pathlib import Path

import pandas as pd

from research_core.util.types import ParseError


def _sample_bad_rows(mask: pd.Series, frame: pd.DataFrame, limit: int = 5) -> str:
    bad_indices = frame.index[mask].tolist()[:limit]
    if not bad_indices:
        return ""
    sample = frame.loc[bad_indices].to_dict(orient="records")
    return f" bad_row_indices={bad_indices} sample={sample}"


def read_raw_file(path: Path) -> pd.DataFrame:
    try:
        frame = pd.read_csv(path, dtype=str)
    except Exception as exc:  # noqa: BLE001
        raise ParseError(f"Failed to read raw file: {path}") from exc

    if frame.empty:
        raise ParseError(f"Raw file is empty: {path}")
    return frame


def parse_timestamp(date_series: pd.Series, time_series: pd.Series) -> pd.Series:
    combined = date_series.str.strip() + " " + time_series.str.strip()
    parsed = pd.to_datetime(combined, format="%m/%d/%Y %H:%M", errors="coerce")
    bad = parsed.isna()
    if bad.any():
        raise ParseError(f"Timestamp parsing failed.{_sample_bad_rows(bad, pd.DataFrame({'Date': date_series, 'Time': time_series}))}")

    try:
        localized = parsed.dt.tz_localize("America/New_York", ambiguous="raise", nonexistent="raise")
    except Exception as exc:  # noqa: BLE001
        raise ParseError("Timestamp timezone localization failed due to DST ambiguity/nonexistent time") from exc
    return localized


def parse_float_column(name: str, values: pd.Series) -> pd.Series:
    parsed = pd.to_numeric(values, errors="coerce")
    bad = parsed.isna()
    if bad.any():
        raise ParseError(f"Numeric parsing failed for column={name}.{_sample_bad_rows(bad, pd.DataFrame({name: values}))}")
    return parsed.astype("float64")

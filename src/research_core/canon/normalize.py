from __future__ import annotations

from pathlib import Path

import pandas as pd

from research_core.canon.colmap import validate_colmap
from research_core.canon.contracts import load_colmap_contract, load_schema_contract
from research_core.canon.reader import parse_float_column, parse_timestamp, read_raw_file
from research_core.canon.session import apply_session_policy
from research_core.validate.invariants import validate_canon_invariants
from research_core.util.types import ParseError


def _required_raw_cols(mapping: dict[str, str]) -> list[str]:
    return [
        "Date",
        "Time",
        "Open",
        "High",
        "Low",
        "Close",
        "Up",
        "Down",
    ]


def canonicalize_file(
    input_path: Path,
    schema_path: Path,
    colmap_path: Path,
    instrument: str,
    tf: str,
    session_policy: str,
    rth_start: str,
    rth_end: str,
    keep_updown: bool,
) -> tuple[pd.DataFrame, dict, dict]:
    schema_payload = load_schema_contract(schema_path)
    colmap_payload = load_colmap_contract(colmap_path)
    mapping = validate_colmap(colmap_payload)

    raw_df = read_raw_file(input_path)
    missing = [col for col in _required_raw_cols(mapping) if col not in raw_df.columns]
    if missing:
        raise ParseError(f"Raw file missing required columns: {missing}")

    ts = parse_timestamp(raw_df["Date"], raw_df["Time"])
    open_col = parse_float_column("Open", raw_df["Open"])
    high_col = parse_float_column("High", raw_df["High"])
    low_col = parse_float_column("Low", raw_df["Low"])
    close_col = parse_float_column("Close", raw_df["Close"])
    up_col = parse_float_column("Up", raw_df["Up"])
    down_col = parse_float_column("Down", raw_df["Down"])

    canon_df = pd.DataFrame(
        {
            "ts": ts,
            "instrument": instrument,
            "tf": tf,
            "open": open_col,
            "high": high_col,
            "low": low_col,
            "close": close_col,
            "volume": (up_col + down_col).astype("float64"),
            "up": up_col,
            "down": down_col,
        }
    )

    if not canon_df["ts"].is_monotonic_increasing:
        raise ParseError("Input timestamps are non-monotonic; fail-loud policy forbids reordering")
    if canon_df["ts"].duplicated().any():
        duplicated = canon_df.loc[canon_df["ts"].duplicated(), "ts"].astype(str).head(5).tolist()
        raise ParseError(f"Duplicate timestamps detected; duplicates are forbidden. sample={duplicated}")

    canon_df = apply_session_policy(canon_df, session_policy, rth_start, rth_end)
    canon_df = canon_df.sort_values("ts", kind="mergesort").reset_index(drop=True)

    if not keep_updown:
        canon_df = canon_df.drop(columns=["up", "down"])

    canonical_order = ["ts", "instrument", "tf", "open", "high", "low", "close", "volume"]
    if keep_updown:
        canonical_order.extend(["up", "down"])
    canon_df = canon_df[canonical_order]

    validate_canon_invariants(canon_df, keep_updown=keep_updown)
    return canon_df, schema_payload, colmap_payload

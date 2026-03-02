from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from research_core.util.io import read_json
from research_core.util.types import ContractError, ValidationError

PSA_VERSION = "v1"

P_UP = "UP"
P_DOWN = "DOWN"
P_CONST = "CONST"

S_FLAT = "FLAT"

A_BULL = "BULL"
A_BEAR = "BEAR"
A_DOJI = "DOJI"

EVENT_STATE_CHANGE = 1 << 0
EVENT_P_CHANGE = 1 << 1
EVENT_S_CHANGE = 1 << 2
EVENT_A_CHANGE = 1 << 3
EVENT_P_FLIP = 1 << 4
EVENT_S_FLIP = 1 << 5
EVENT_A_FLIP = 1 << 6


def load_psa_schema_contract(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    version = payload.get("psa_version")
    if version != PSA_VERSION:
        raise ContractError(f"Unsupported psa_version: {version}")

    required_columns = payload.get("required_columns")
    if not isinstance(required_columns, list) or not required_columns:
        raise ContractError("PSA schema must declare non-empty required_columns")

    return payload


def validate_canon_input_v1(canon_df: pd.DataFrame) -> None:
    required = ["ts", "instrument", "tf", "open", "high", "low", "close", "volume"]
    missing = [column for column in required if column not in canon_df.columns]
    if missing:
        raise ValidationError(f"Canon schema mismatch: missing required columns {missing}")


def make_state_id(p_token: str, s_token: str, a_token: str) -> str:
    return f"PSA.v1|P={p_token}|S={s_token}|A={a_token}"


def is_p_flip(previous_p: str, current_p: str) -> bool:
    return (previous_p == P_UP and current_p == P_DOWN) or (previous_p == P_DOWN and current_p == P_UP)


def is_a_flip(previous_a: str, current_a: str) -> bool:
    return (previous_a == A_BULL and current_a == A_BEAR) or (previous_a == A_BEAR and current_a == A_BULL)


def compute_event_mask(
    previous_p: str,
    previous_s: str,
    previous_a: str,
    current_p: str,
    current_s: str,
    current_a: str,
) -> int:
    p_change = current_p != previous_p
    s_change = current_s != previous_s
    a_change = current_a != previous_a
    state_change = p_change or s_change or a_change

    mask = 0
    if state_change:
        mask |= EVENT_STATE_CHANGE
    if p_change:
        mask |= EVENT_P_CHANGE
    if s_change:
        mask |= EVENT_S_CHANGE
    if a_change:
        mask |= EVENT_A_CHANGE
    if is_p_flip(previous_p, current_p):
        mask |= EVENT_P_FLIP
    if s_change:
        mask |= EVENT_S_FLIP
    if is_a_flip(previous_a, current_a):
        mask |= EVENT_A_FLIP
    return mask

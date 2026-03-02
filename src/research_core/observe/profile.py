from __future__ import annotations

import json
import os
from collections import Counter
from pathlib import Path
from typing import Any

import pandas as pd

from research_core.observe.contracts import BIT_NAMES, assert_invariant, ordered_bit_names, require_manifest_field


def _event_bit_counts(event_masks: list[int]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for bit in sorted(BIT_NAMES.keys()):
        bit_name = BIT_NAMES[bit]
        counts[bit_name] = int(sum(1 for value in event_masks if (int(value) & (1 << bit)) != 0))
    return counts


def _session_from_manifests(canon_manifest: dict[str, Any], psa_manifest: dict[str, Any]) -> dict[str, str]:
    canon_policy = require_manifest_field(canon_manifest, "session_policy")
    canon_rth_start = require_manifest_field(canon_manifest, "rth_start")
    canon_rth_end = require_manifest_field(canon_manifest, "rth_end")

    psa_session = require_manifest_field(psa_manifest, "session")
    psa_policy = require_manifest_field(psa_session, "session_policy")
    psa_tz = require_manifest_field(psa_session, "tz")
    psa_rth_start = require_manifest_field(psa_session, "rth_start")
    psa_rth_end = require_manifest_field(psa_session, "rth_end")

    assert_invariant("profile_session_policy_match", canon_policy == psa_policy, "canon and psa session_policy differ")
    assert_invariant("profile_rth_start_match", canon_rth_start == psa_rth_start, "canon and psa rth_start differ")
    assert_invariant("profile_rth_end_match", canon_rth_end == psa_rth_end, "canon and psa rth_end differ")

    return {
        "session_policy": str(canon_policy),
        "tz": str(psa_tz),
        "rth_start": str(canon_rth_start),
        "rth_end": str(canon_rth_end),
    }


def _top_transitions(state_ids: list[str], top_n: int) -> list[dict[str, Any]]:
    transitions = Counter((previous, current) for previous, current in zip(state_ids[:-1], state_ids[1:]))
    ranked = sorted(transitions.items(), key=lambda item: (-item[1], item[0][0], item[0][1]))[:top_n]
    return [
        {
            "prev_state_id": previous,
            "next_state_id": current,
            "count": int(count),
        }
        for (previous, current), count in ranked
    ]


def _window_entries(psa_df: pd.DataFrame, tz: str) -> list[dict[str, Any]]:
    timestamps = psa_df["ts"]
    if timestamps.dt.tz is None:
        raise ValueError("psa ts must be timezone-aware")
    ny_ts = timestamps.dt.tz_convert(tz)

    window_floor = ny_ts.dt.floor("60min")
    keyed = psa_df.copy()
    keyed["_window_start"] = window_floor

    entries: list[dict[str, Any]] = []
    for window_start, window_df in keyed.groupby("_window_start", sort=True):
        state_counter = Counter(window_df["state_id"].astype(str).tolist())
        state_counts = {key: int(state_counter[key]) for key in sorted(state_counter.keys())}
        dominant_count = max(state_counts.values())
        dominant_candidates = sorted([key for key, value in state_counts.items() if value == dominant_count])
        dominant = dominant_candidates[0]

        masks = [int(value) for value in window_df["event_mask"].tolist()]
        state_ids = window_df["state_id"].astype(str).tolist()
        entries.append(
            {
                "window_start": window_start.isoformat(),
                "window_end": (window_start + pd.Timedelta(minutes=60)).isoformat(),
                "bar_count": int(len(window_df)),
                "dominant_state_id": dominant,
                "state_counts": state_counts,
                "event_bit_counts": _event_bit_counts(masks),
                "transition_count": int(max(len(state_ids) - 1, 0)),
            }
        )

    return entries


def build_observe_profile(run_dir: Path, top_n: int = 25) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    canon_manifest = json.loads((run_dir / "canon.manifest.json").read_text(encoding="utf-8"))
    psa_manifest = json.loads((run_dir / "psa.manifest.json").read_text(encoding="utf-8"))
    psa_df = pd.read_parquet(run_dir / "psa.parquet")

    session = _session_from_manifests(canon_manifest, psa_manifest)
    tz = session["tz"]

    ny_ts = psa_df["ts"].dt.tz_convert(tz)
    keyed = psa_df.copy()
    keyed["_date"] = ny_ts.dt.strftime("%Y-%m-%d")

    by_date: dict[str, Any] = {}
    for date_key, date_df in keyed.groupby("_date", sort=True):
        state_counter = Counter(date_df["state_id"].astype(str).tolist())
        state_counts = {key: int(state_counter[key]) for key in sorted(state_counter.keys())}
        masks = [int(value) for value in date_df["event_mask"].tolist()]
        states = date_df["state_id"].astype(str).tolist()

        by_date[date_key] = {
            "bar_count": int(len(date_df)),
            "start_ts": date_df["ts"].iloc[0].tz_convert(tz).isoformat(),
            "end_ts": date_df["ts"].iloc[-1].tz_convert(tz).isoformat(),
            "state_counts": state_counts,
            "event_bit_counts": _event_bit_counts(masks),
            "top_transitions": _top_transitions(states, top_n=top_n),
        }

    windows = _window_entries(psa_df, tz=tz)

    checks: list[dict[str, Any]] = []
    checks.append(
        assert_invariant(
            "profile_by_date_total_rows",
            sum(int(entry["bar_count"]) for entry in by_date.values()) == len(psa_df),
            "by_date total bar_count does not match psa row_count",
        )
    )
    checks.append(
        assert_invariant(
            "profile_window_total_rows",
            sum(int(entry["bar_count"]) for entry in windows) == len(psa_df),
            "time windows total bar_count does not match psa row_count",
        )
    )

    created_utc = os.environ.get("RESEARCH_CREATED_UTC") or str(require_manifest_field(canon_manifest, "created_utc"))

    profile: dict[str, Any] = {
        "profile_version": "v1",
        "run_ref": {
            "instrument": str(require_manifest_field(canon_manifest, "instrument")),
            "tf": str(require_manifest_field(canon_manifest, "tf")),
            "session_policy": session["session_policy"],
            "tz": session["tz"],
            "rth_start": session["rth_start"],
            "rth_end": session["rth_end"],
            "created_utc": created_utc,
        },
        "by_date": {key: by_date[key] for key in sorted(by_date.keys())},
        "time_windows": {
            "window_size_minutes": 60,
            "windows": windows,
        },
        "invariants": {
            "checks": checks,
            "bit_order": ordered_bit_names(),
        },
    }

    return profile, checks

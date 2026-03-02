from __future__ import annotations

import json
import os
from collections import Counter
from pathlib import Path
from typing import Any

import pandas as pd

from research_core.observe.contracts import BIT_NAMES, assert_invariant, require_manifest_field


def _sorted_counter(counter: Counter[str]) -> dict[str, int]:
    return {key: int(counter[key]) for key in sorted(counter.keys())}


def _top_counter(counter: Counter[str], top_n: int) -> dict[str, int]:
    ranked = sorted(counter.items(), key=lambda item: (-item[1], item[0]))[:top_n]
    return {key: int(value) for key, value in ranked}


def _sorted_transition_counts(counter: Counter[tuple[str, str]]) -> dict[str, dict[str, int]]:
    grouped: dict[str, dict[str, int]] = {}
    prev_keys = sorted({prev for prev, _ in counter.keys()})
    for prev in prev_keys:
        next_keys = sorted([next_state for from_state, next_state in counter.keys() if from_state == prev])
        grouped[prev] = {next_state: int(counter[(prev, next_state)]) for next_state in next_keys}
    return grouped


def _session_from_manifests(canon_manifest: dict[str, Any], psa_manifest: dict[str, Any]) -> dict[str, str]:
    canon_policy = require_manifest_field(canon_manifest, "session_policy")
    canon_rth_start = require_manifest_field(canon_manifest, "rth_start")
    canon_rth_end = require_manifest_field(canon_manifest, "rth_end")

    psa_session = require_manifest_field(psa_manifest, "session")
    psa_policy = require_manifest_field(psa_session, "session_policy")
    psa_tz = require_manifest_field(psa_session, "tz")
    psa_rth_start = require_manifest_field(psa_session, "rth_start")
    psa_rth_end = require_manifest_field(psa_session, "rth_end")

    assert_invariant(
        "session_policy_match",
        canon_policy == psa_policy,
        "canon and psa session_policy differ",
    )
    assert_invariant(
        "rth_start_match",
        canon_rth_start == psa_rth_start,
        "canon and psa rth_start differ",
    )
    assert_invariant(
        "rth_end_match",
        canon_rth_end == psa_rth_end,
        "canon and psa rth_end differ",
    )

    return {
        "session_policy": str(canon_policy),
        "tz": str(psa_tz),
        "rth_start": str(canon_rth_start),
        "rth_end": str(canon_rth_end),
    }


def build_observe_summary(run_dir: Path, top_n: int = 25) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    canon_manifest_path = run_dir / "canon.manifest.json"
    psa_manifest_path = run_dir / "psa.manifest.json"
    canon_parquet_path = run_dir / "canon.parquet"
    psa_parquet_path = run_dir / "psa.parquet"

    canon_manifest = json.loads(canon_manifest_path.read_text(encoding="utf-8"))
    psa_manifest = json.loads(psa_manifest_path.read_text(encoding="utf-8"))

    canon_df = pd.read_parquet(canon_parquet_path)
    psa_df = pd.read_parquet(psa_parquet_path)

    checks: list[dict[str, Any]] = []

    checks.append(assert_invariant("row_count_match", len(canon_df) == len(psa_df), "canon and psa row counts differ"))
    checks.append(
        assert_invariant(
            "start_ts_match",
            canon_df["ts"].iloc[0].isoformat() == psa_df["ts"].iloc[0].isoformat(),
            "canon and psa start_ts differ",
        )
    )
    checks.append(
        assert_invariant(
            "end_ts_match",
            canon_df["ts"].iloc[-1].isoformat() == psa_df["ts"].iloc[-1].isoformat(),
            "canon and psa end_ts differ",
        )
    )

    session = _session_from_manifests(canon_manifest, psa_manifest)

    state_counter = Counter(psa_df["state_id"].astype(str).tolist())
    event_counter_int = Counter(int(value) for value in psa_df["event_mask"].tolist())

    bit_counts: dict[str, int] = {}
    for bit, name in BIT_NAMES.items():
        bit_counts[name] = int(sum(1 for value in psa_df["event_mask"].tolist() if (int(value) & (1 << bit)) != 0))

    transitions = Counter(
        (str(previous), str(current))
        for previous, current in zip(psa_df["state_id"].astype(str).tolist()[:-1], psa_df["state_id"].astype(str).tolist()[1:])
    )

    input_files = require_manifest_field(canon_manifest, "input_files")
    input_paths = sorted([str(item["path"]) for item in input_files])

    created_utc = os.environ.get("RESEARCH_CREATED_UTC") or str(require_manifest_field(canon_manifest, "created_utc"))

    summary: dict[str, Any] = {
        "run_ref": {
            "instrument": str(require_manifest_field(canon_manifest, "instrument")),
            "tf": str(require_manifest_field(canon_manifest, "tf")),
            "session_policy": session["session_policy"],
            "tz": session["tz"],
            "rth_start": session["rth_start"],
            "rth_end": session["rth_end"],
            "created_utc": created_utc,
        },
        "canon_coverage": {
            "row_count": int(len(canon_df)),
            "start_ts": canon_df["ts"].iloc[0].isoformat(),
            "end_ts": canon_df["ts"].iloc[-1].isoformat(),
            "input_file_count": int(len(input_files)),
            "input_paths": input_paths,
            "canonical_table_sha256": str(canon_manifest["output_files"]["canon.parquet"]["canonical_table_sha256"]),
        },
        "psa_coverage": {
            "row_count": int(len(psa_df)),
            "start_ts": psa_df["ts"].iloc[0].isoformat(),
            "end_ts": psa_df["ts"].iloc[-1].isoformat(),
            "canonical_table_sha256": str(psa_manifest["output_files"]["psa.parquet"]["canonical_table_sha256"]),
        },
        "state_distribution": {
            "top_n": int(top_n),
            "top_counts": _top_counter(state_counter, top_n=top_n),
            "full_counts": _sorted_counter(state_counter),
        },
        "event_mask_distribution": {
            "counts": {str(key): int(event_counter_int[key]) for key in sorted(event_counter_int.keys())},
            "counts_by_bit": bit_counts,
        },
        "transition_counts": _sorted_transition_counts(transitions),
        "invariants": {"checks": checks},
    }

    return summary, checks

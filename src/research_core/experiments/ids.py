from __future__ import annotations

from typing import Any

from research_core.util.hashing import sha256_bytes, sha256_json
from research_core.util.io import canonical_json_bytes

EXPERIMENT_TOOL_VERSION = "v1"


def spec_canonical_sha256(spec_payload: dict[str, Any]) -> str:
    return sha256_json(spec_payload)


def exp_id_payload(
    spec_payload: dict[str, Any],
    psa_canonical_table_sha256: str,
    canon_canonical_table_sha256: str | None,
) -> dict[str, Any]:
    inputs: dict[str, Any] = {"psa_canonical_table_sha256": psa_canonical_table_sha256}
    if isinstance(canon_canonical_table_sha256, str) and canon_canonical_table_sha256:
        inputs["canon_canonical_table_sha256"] = canon_canonical_table_sha256

    return {
        "spec": spec_payload,
        "inputs": inputs,
        "tool": {"research_experiment_version": EXPERIMENT_TOOL_VERSION},
    }


def derive_experiment_id(
    spec_payload: dict[str, Any],
    psa_canonical_table_sha256: str,
    canon_canonical_table_sha256: str | None,
) -> tuple[str, dict[str, Any]]:
    payload = exp_id_payload(
        spec_payload=spec_payload,
        psa_canonical_table_sha256=psa_canonical_table_sha256,
        canon_canonical_table_sha256=canon_canonical_table_sha256,
    )
    exp_id = sha256_bytes(canonical_json_bytes(payload))
    return exp_id, payload

# Research PSA Spec v1

Phase 1 introduces PSA Core v1 with strict deterministic behavior.

## Scope

- Input: Phase 0 `canon.parquet` (Canon schema v1).
- Output: `psa.parquet` and `psa.manifest.json`.
- Version: `psa_version = v1`.

## Alignment Rule A (v1)

- `BULL` when `close > open`
- `BEAR` when `close < open`
- `DOJI` when `close == open`

No inference, smoothing, IBS bardir, PSE/Φ/corridors, or analytics are included in v1.

## Determinism Requirements

- Stable row order inherited from Canon input.
- Manifest JSON serialization uses sorted keys and compact separators.
- Manifest path fields never embed absolute paths.
- Canonical table hash is computed from Arrow IPC stream serialization of PSA table.

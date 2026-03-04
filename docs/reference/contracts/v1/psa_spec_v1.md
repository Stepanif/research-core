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

## State and Event Encoding (v1)

### state_id

`state_id` is a deterministic string for `(P,S,A)` using:

`PSA.v1|P={P}|S={S}|A={A}`

- `P`: `UP`, `DOWN`, `CONST`
- `S`: `FLAT`
- `A`: `BULL`, `BEAR`, `DOJI`

### event_mask (bitmask integer)

Fixed bit assignments:

- Bit 0: `STATE_CHANGE` (any change in `(P,S,A)`)
- Bit 1: `P_CHANGE`
- Bit 2: `S_CHANGE`
- Bit 3: `A_CHANGE`
- Bit 4: `P_FLIP` (`UP<->DOWN` only; `CONST` excluded)
- Bit 5: `S_FLIP` (`S != prior S`)
- Bit 6: `A_FLIP` (`BULL<->BEAR` only)

DOJI rules:

- `A_CHANGE` is true whenever `A != prior A`
- `A_FLIP` is true only for `BULL<->BEAR`; transitions involving `DOJI` are not flips

First row has no prior bar and must emit `event_mask = 0`.

## Log Stream

`psa.log` is written at run root as UTF-8 CSV with no header:

`ts,instrument,tf,P,S,A,state_id,event_mask`

- one line per bar
- deterministic row order (same as PSA dataframe)
- newline at EOF, LF line endings

## Determinism Requirements

- Stable row order inherited from Canon input.
- Manifest JSON serialization uses sorted keys and compact separators.
- Manifest path fields never embed absolute paths.
- Canonical table hash is computed from Arrow IPC stream serialization of PSA table.

# Research Canon Spec v1

## Raw Format

Authoritative raw columns:

`Date, Time, Open, High, Low, Close, Up, Down`

Date parse format is fixed as `MM/DD/YYYY` and time parse format is fixed as `HH:MM` (24h).
Any row that fails parsing fails the entire run.

## Timestamp + Timezone Rules

- `ts` is constructed as `Date + " " + Time`
- Parsed with exact format (no locale inference)
- Localized to `America/New_York`
- DST ambiguous or nonexistent local times fail-loud
- Canon timestamps are tz-aware and persisted in parquet as Arrow timestamp with timezone

## Session Policy (Data Layer)

- `full`: retain all rows
- `rth`: keep rows with local NY time `>= rth_start` and `<= rth_end`
- `eth`: keep complement of RTH (`< rth_start` or `> rth_end`)

Boundary contract is inclusive start and inclusive end.

## Canon Columns and Ordering

Required order:

1. `ts`
2. `instrument`
3. `tf`
4. `open`
5. `high`
6. `low`
7. `close`
8. `volume`

Optional when `keep_updown=true`:

9. `up`
10. `down`

`volume` is deterministically derived as `Up + Down`.

## Invariant Rules

- no NaN in required columns
- monotonic increasing `ts`
- duplicate `ts` forbidden
- `high >= max(open, close)`
- `low <= min(open, close)`
- `high >= low`
- `volume >= 0`
- if present, `up >= 0` and `down >= 0`

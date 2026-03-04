# Baseline Diff Spec v1

## Scope
`baseline.diff` v1 is a deterministic comparator over two `baseline.card.json` files.
It uses pure file inputs and introduces no discovery logic, tuning knobs, or new modeling.

## Command
- `risk diff --a <baseline.card.json> --b <baseline.card.json> --out <dir>`

## Outputs
- `<out>/baseline.diff.json`
- `<out>/baseline.diff.manifest.json`

## Inputs
Both `--a` and `--b` must be parseable baseline cards with:
- `card_version == "v1"`
- required card fields present for comparison

## Baseline diff fields
- `diff_version`: `"v1"`
- `created_utc`: `RESEARCH_CREATED_UTC`
- `a`: `{runset_id, baseline_card_canonical_sha256, per_run_vector_sha256}`
- `b`: `{runset_id, baseline_card_canonical_sha256, per_run_vector_sha256}`
- `deltas`:
  - `instability_mean_delta`
  - `instability_median_delta`
  - `instability_p10_delta`
  - `instability_p90_delta`
  - `state_entropy_mean_delta` (only when present in both cards)
  - `transition_entropy_mean_delta` (only when present in both cards)
- `worst5_overlap`:
  - `jaccard` over key tuples `(dataset_id, canon_table_sha256, run_ref)`
  - `intersection_count`
  - `union_count`
- `checksum`:
  - `per_run_vector_match`
- `classification`:
  - `label`: one of `MORE_UNSTABLE`, `LESS_UNSTABLE`, `NO_CHANGE`
  - `rationale`: short threshold rationale
- `baseline_diff_canonical_sha256`

## Fixed v1 thresholds
Defined in `risk/contracts.py`:
- If `instability_mean_delta >= +5.0` => `MORE_UNSTABLE`
- If `instability_mean_delta <= -5.0` => `LESS_UNSTABLE`
- Else => `NO_CHANGE`

## Manifest
`baseline.diff.manifest.json` includes:
- inputs: both baseline card files (`sha256`, `bytes`)
- outputs: `baseline.diff.json` (`sha256`, `bytes`)
- `baseline_diff_manifest_canonical_sha256`

All JSON outputs are canonical (`sort_keys=True`, compact separators) with trailing newline.

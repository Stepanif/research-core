# Risk Harness Spec v1

## Scope
Risk Harness v1 is read-only and deterministic. It uses PSA dynamics only (`state_id`, `event_mask`, and state transitions) and does not include PnL, execution assumptions, or modeling.

## Determinism
- `RESEARCH_CREATED_UTC` is required for all risk outputs.
- JSON output bytes are canonical: `json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\\n"`.
- Ordering is deterministic for per-run and runset aggregates.

## Per-run output
Command:
- `risk run --run <run_dir>`

Writes:
- `<run_dir>/risk/risk.summary.json`
- `<run_dir>/risk/risk.summary.manifest.json`

`risk.summary.json` (v1):
- `risk_version`, `created_utc`
- `run_ref`: `instrument`, `tf`, `session_policy`, `tz`, `rth_start`, `rth_end`
- `inputs.psa_table_sha256`
- `counts`: `row_count`, `transition_count`
- `event_rates_per_1000`: `state_change`, `p_change`, `s_change`, `a_change`, `p_flip`, `a_flip`
- `streaks`: max consecutive set bits for `state_change`, `p_flip`, `a_flip`
- `distributions`: state/transition entropy (base-2), top-k shares for k={1,5,10}
- `instability_score`
- `invariants`: `required_files_present`, `row_count_positive`
- `risk_summary_canonical_sha256`

### Instability score (fixed v1)
Weights are fixed constants:
- `w_state_change = 0.35`
- `w_p_flip = 0.25`
- `w_a_flip = 0.20`
- `w_concentration = 0.20`

Definitions:
- `concentration_term = 1.0 - top_transition_share_k[10]`
- `instability_score = w_state_change*state_change_per_1000 + w_p_flip*p_flip_per_1000 + w_a_flip*a_flip_per_1000 + w_concentration*concentration_term*1000.0`

## Per-run manifest
`risk.summary.manifest.json` includes:
- inputs: `psa.parquet`, `psa.manifest.json` (`sha256`, `bytes`)
- outputs: `risk.summary.json` (`sha256`, `bytes`)
- `risk_manifest_canonical_sha256`

## Runset aggregation output
Command:
- `risk runset --catalog <catalog_dir> --id <runset_id> --out <dir>`

Writes:
- `<out>/<runset_id>/risk.runset.summary.json`
- `<out>/<runset_id>/risk.runset.manifest.json`

Behavior:
- loads and validates runset entry
- uses dataset-to-runs links deterministically
- explicit run conflicts fail-loud
- resolves each selected `run_ref` to on-disk run dir deterministically; unresolved refs fail-loud
- computes per-run risk using the same code path as `risk run`

`risk.runset.summary.json` fields:
- `runset_risk_version`, `created_utc`, `runset_id`, `run_count`
- `per_run`: sorted by `(dataset_id, canon_table_sha256, run_ref)`
- `aggregates`:
  - `instability`: `mean`, `median`, `p10`, `p50`, `p90`
  - `event_rates_mean_per_1000`
  - `worst_5` runs by instability (deterministic tiebreak)
- `runset_risk_canonical_sha256`

Runset manifest includes:
- inputs: runset entry, dataset_to_runs index, per-run `psa.manifest.json` files used
- outputs: `risk.runset.summary.json` (`sha256`, `bytes`)
- `runset_risk_manifest_canonical_sha256`

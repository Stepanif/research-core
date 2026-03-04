# Baseline Card Spec v1

## Scope
Baseline Card v1 is a compact, deterministic projection of existing risk runset outputs.
It introduces no new modeling, tuning, or PnL semantics.

## Command
- `risk sweep --catalog <catalog_dir> --runset <runset_id> --out <dir>`

## Outputs
- `<out>/<runset_id>/baseline.card.json`
- `<out>/<runset_id>/baseline.card.manifest.json`

The sweep path reuses risk runset computation deterministically, then materializes the baseline card and manifest.

## Baseline card fields
- `card_version`: `"v1"`
- `created_utc`: required from `RESEARCH_CREATED_UTC`
- `runset_id`
- `inputs`:
  - `runset_entry_canonical_sha256`
  - `dataset_to_runs_index_canonical_sha256`
  - `risk_runset_manifest_canonical_sha256`
- `key_metrics` (projection from `risk.runset.summary.json`):
  - `run_count`
  - `instability_mean`
  - `instability_median`
  - `instability_p10`
  - `instability_p90`
  - `state_entropy_mean` (included only when present for all `per_run` rows)
  - `transition_entropy_mean` (included only when present for all `per_run` rows)
  - `top_5_worst`: list of `{dataset_id, run_ref, canon_table_sha256, instability_score}` sorted by `(-instability_score, dataset_id, run_ref)`
- `checksums`:
  - `per_run_vector_sha256`
- `baseline_card_canonical_sha256`

## per_run_vector_sha256 canonicalization
For each `per_run` entry, build one line:

`"<instability_score:.6f>|<state_entropy_bits:.6f>|<transition_entropy_bits:.6f>|<p_flip_per_1000:.6f>|<a_flip_per_1000:.6f>|<canon_table_sha256>|<run_ref>\n"`

Rules:
- Float formatting uses `f"{x:.6f}"`
- Missing or `None` float fields emit `"NA"`
- `canon_table_sha256` and `run_ref` are used as-is from deterministic upstream artifacts
- Lines are sorted lexicographically (byte order), joined as UTF-8, then SHA-256 hashed

## Manifest
`baseline.card.manifest.json` includes:
- inputs:
  - runset entry JSON
  - dataset-to-runs index JSON
  - `risk.runset.summary.json`
  - `risk.runset.manifest.json`
- outputs:
  - `baseline.card.json` (`sha256`, `bytes`)
- `baseline_card_manifest_canonical_sha256`

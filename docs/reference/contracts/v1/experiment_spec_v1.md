# Experiment Spec v1

## Scope
Phase 3 experiment harness is read-only on existing run artifacts. It does not modify canon/psa/observe semantics.

## Schema
Spec file path contract: `schemas/experiment.spec.schema.v1.json`

Top-level fields:
- `spec_version`: must be `"v1"`
- `kind`: must be `"transition_matrix"`
- `params.transition_scope`: must be `"global"`
- `params.include_event_bits`: optional boolean, default `false`

Defaults are deterministic and are applied during spec normalization.

## Canonicalization and hashing
Canonical JSON bytes are:
- `json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")`

`exp_id` is SHA256 of canonical JSON for:
- `spec`: normalized spec object
- `inputs.psa_canonical_table_sha256`: from `psa.manifest.json`
- `inputs.canon_canonical_table_sha256`: included only when available from `canon.manifest.json`
- `tool.research_experiment_version`: `"v1"`

## Outputs
For run dir `<run_dir>`, outputs are written to:
- `<run_dir>/experiments/<exp_id>/transition_matrix.json`
- `<run_dir>/experiments/<exp_id>/exp.manifest.json`
- `<run_dir>/experiments/experiments.index.json`

### `transition_matrix.json`
- `row_count`
- `transition_count`
- `transitions`: nested dict `{prev_state_id: {next_state_id: count}}` with sorted keys
- `top_transitions`: list sorted by `(-count, prev, next)`, max length 50
- optional `event_bit_transition_counts` when `include_event_bits=true`

### `exp.manifest.json`
- `manifest_version`: `"v1"`
- `exp_id`
- `spec_canonical_sha256`
- `inputs`:
  - `psa_manifest_canonical_sha256`
  - `psa_canonical_table_sha256`
  - optional canon manifest/table hashes when canon manifest available
- `outputs.transition_matrix.json`: `sha256` and `bytes`
- `created_utc`: must come from `RESEARCH_CREATED_UTC` (fail-loud if missing)
- `exp_manifest_canonical_sha256`: canonical JSON hash of the manifest payload itself

## Immutability
- If an experiment directory already exists and stored manifest hash differs from recomputed manifest hash, fail-loud.
- If existing output bytes do not match stored output hash, fail-loud.
- Per-run index update is deterministic and fail-loud if an existing `exp_id` entry would change.

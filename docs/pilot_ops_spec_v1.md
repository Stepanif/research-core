# Pilot Ops Spec v1

## Purpose

`pilot run` is a deterministic daily-ops wrapper for the Pilot Option C loop:

1. explicit runset generation
2. runset ensure + validate
3. baseline card ensure
4. promotion requirement check
5. risk drift
6. ci doctor (single runset, read-only)
7. one audit summary + one manifest

The command is fail-loud, deterministic, and `RESEARCH_CREATED_UTC`-driven.

## Command

```text
python -m research_core.cli pilot run --config <pilot.ops.json>
```

## Config (`pilot.ops.json`) v1

Required fields:

- `pilot_ops_version: "v1"`
- `catalog_dir`
- `datasets_path`
- `baseline_root`
- `label` (default `prod`)
- `out_dir`
- `runset_kind: "explicit_from_index"`
- `require_promoted_baseline: true`
- `doctor_out_subdir` (default `doctor`)
- `drift_out_subdir` (default `drift`)

Strict config: unknown fields are rejected.

## Fixed v1 behavior

- Explicit runset generation uses the same deterministic selection logic as `docs/scripts/gen_explicit_runset_from_index.py`.
- Ordering is deterministic:
  - datasets sorted by `(tf, dataset_id)`
  - run candidates sorted by `(run_ref, canon_table_sha256)`
- If runset already exists in catalog, it is reused.
- If baseline card manifest verifies, baseline is reused; otherwise `risk sweep` recomputes baseline card into `baseline_root`.
- Promotions are required for `label` (default `prod`). Missing promotion is fail-loud with explicit `baseline promote` instruction.
- `ci doctor` is run for exactly one runset.
- No subprocess shelling; internal modules are called directly.

## Artifacts

The command writes:

- `<out_dir>/pilot.run.summary.json`
- `<out_dir>/pilot.run.summary.manifest.json`

And stage artifacts under:

- `<out_dir>/<drift_out_subdir>/...`
- `<out_dir>/<doctor_out_subdir>/...`

### `pilot.run.summary.json` v1

Fields:

- `pilot_run_version: "v1"`
- `created_utc` (from `RESEARCH_CREATED_UTC`)
- `label`
- `runset_id`
- `baseline_id` (promoted baseline id for `label`)
- `artifacts`
  - `baseline_card_path`
  - `drift_report_path`
  - `doctor_summary_path`
- `results`
  - `status` (`PASS` | `FAIL`)
  - `failures[]` (`stage`, `detail`) sorted deterministically
- `checksums`
  - `generated_runset_spec_canonical_sha256`
  - `pilot_run_canonical_sha256` (canonical JSON hash excluding this field)

### `pilot.run.summary.manifest.json` v1

Fields:

- `manifest_version: "v1"`
- `created_utc`
- `inputs[]` (`path`, `sha256`, `bytes`) sorted by `path`
- `outputs.pilot.run.summary.json` (`sha256`, `bytes`)
- `pilot_run_manifest_canonical_sha256`

## Exit code

- `0` on `PASS`
- `1` on `FAIL`

## Stable stdout lines

The CLI prints:

- `PILOT_RUN status=PASS|FAIL`
- `runset_id=...`
- `baseline_id=...`
- `drift_report=...`
- `doctor_summary=...`
- `summary=...`
- `manifest=...`

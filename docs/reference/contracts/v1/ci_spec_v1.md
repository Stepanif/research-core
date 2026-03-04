# CI Runner Spec v1

## Purpose

`ci run` is a deterministic institutional entrypoint for baseline refresh + drift dashboard evaluation with an audit summary.

## Command

```text
ci run --config <ci.json>
```

## Config (`ci.json`) v1

Required fields:
- `ci_version`: `v1`
- `catalog_dir`
- `baseline_root`
- `runsets_path`
- `out_dir`

Optional fields:
- `created_utc` (ignored; `RESEARCH_CREATED_UTC` is authoritative)
- `label` (default `prod`)
- `fail_on_drift` (default `true`)
- `fail_on_checksum_mismatch` (default `true`)

Config is strict: unknown fields are rejected.

## Execution Order

1. Validate config and require `RESEARCH_CREATED_UTC`
2. Refresh baseline index (`baseline index refresh` path)
3. Run drift dashboard (`risk dashboard` path)
4. Evaluate CI result from `dashboard.summary.json`
5. Write:
   - `<out_dir>/ci.summary.json`
   - `<out_dir>/ci.summary.manifest.json`

## Result Rules

- `drift_count = aggregates.counts.DRIFT`
- `checksum_mismatch_count = aggregates.checksum_mismatch_count`
- `status = PASS` iff:
  - `drift_count == 0`, and
  - if `fail_on_checksum_mismatch == true`, then `checksum_mismatch_count == 0`
- else `status = FAIL`

Exit code behavior:
- exit 1 if `fail_on_drift == true` and `drift_count > 0`
- exit 1 if `fail_on_checksum_mismatch == true` and `checksum_mismatch_count > 0`

## `ci.summary.json` v1

Fields:
- `ci_summary_version`: `v1`
- `created_utc`
- `inputs`
  - `config_sha256`
  - `runsets_sha256`
  - `baseline_index_canonical_sha256`
- `outputs`
  - `dashboard_summary_sha256`
  - `dashboard_manifest_canonical_sha256`
- `results`
  - `status`
  - `drift_count`
  - `checksum_mismatch_count`
  - `fail_on_drift`
  - `fail_on_checksum_mismatch`
- `pointers.dashboard_dir`
- `ci_summary_canonical_sha256`

## `ci.summary.manifest.json` v1

Includes:
- `manifest_version: v1`
- `created_utc`
- sorted `inputs` (`config`, `runsets`, `baseline.index`, `dashboard.summary`, `dashboard.manifest`)
- `outputs.ci.summary.json` (`sha256`, `bytes`)
- `ci_manifest_canonical_sha256`

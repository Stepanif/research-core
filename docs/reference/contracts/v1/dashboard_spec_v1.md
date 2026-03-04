# Drift Dashboard Spec v1

## Purpose

`risk dashboard` executes `risk drift` for an explicit runset list and emits one deterministic dashboard summary.

It is read-only with respect to baseline root and does not change drift semantics.

## Command

```text
risk dashboard --catalog <catalog_dir> --root <baseline_root> --runsets <runsets.json> --out <dir> [--label prod]
```

## Runset List Input (strict)

`--runsets` must point to a JSON object with exactly one key:

```json
{"runset_ids":["runset-a","runset-b"]}
```

Rules:
- key must be exactly `runset_ids`
- value must be an array of non-empty strings
- duplicate runset ids are rejected
- runsets execute in deterministic ascending runset_id order

## Output Layout

```text
<out>/
  drift/
    <runset_id>/
      current/
      diff/
      drift.report.json
      drift.report.manifest.json
  dashboard.summary.json
  dashboard.summary.manifest.json
```

## DashboardSummary v1

Fields:
- `dashboard_version`: `v1`
- `created_utc`: `RESEARCH_CREATED_UTC`
- `label`
- `runset_count`
- `entries` sorted by `runset_id` asc. Each entry is projected from `drift.report.json`:
  - `runset_id`
  - `status` in `{NO_DRIFT, DRIFT}`
  - `instability_mean_delta`
  - `worst5_jaccard`
  - `per_run_vector_match`
  - `reference_baseline_id`
  - `current_baseline_id`
  - `diff_classification_label`
  - `drift_report_sha256` (byte hash of `drift.report.json`)
  - `drift_manifest_canonical_sha256` (canonical hash in `drift.report.manifest.json`)
- `aggregates`:
  - `counts`: `{DRIFT, NO_DRIFT}`
  - `checksum_mismatch_count`
  - `top_abs_instability_delta_5`: sorted by `(-abs(delta), runset_id)`
  - `lowest_jaccard_5`: sorted by `(jaccard asc, runset_id)`
- `dashboard_canonical_sha256`: canonical hash excluding this field

## Manifest v1

`dashboard.summary.manifest.json` includes:
- `manifest_version: v1`
- `created_utc`
- sorted `inputs` with `sha256` and `bytes`:
  - `runsets.json`
  - for each runset: `drift.report.json` and `drift.report.manifest.json`
- `outputs.dashboard.summary.json` with `sha256` and `bytes`
- `dashboard_manifest_canonical_sha256`

## Failure Behavior

- Fail-fast: stop on first runset drift failure.
- No dashboard summary/manifest is written unless all listed runsets succeed.
- Drift outputs for previously completed runsets may already exist when a later runset fails.

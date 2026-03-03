# CI Doctor Spec v1

## Purpose

`ci doctor` is a deterministic, read-only integrity gate for baseline/runset promotion state.

It validates integrity inputs and always writes an auditable summary + manifest, including on `FAIL`.

## Command

```text
ci doctor --config <doctor.json>
```

## Config (`doctor.json`) v1

Required fields:
- `doctor_version: "v1"`
- `catalog_dir`
- `baseline_root`
- `runsets_path`
- `out_dir`
- `checks`
  - `verify_baseline_root: true`
  - `verify_promotions: true`
  - `verify_runsets: true`

Optional fields:
- `label` (default `prod`)
- `checks.verify_bundles` (default `false`)
- `checks.verify_dashboard` (default `false`)
- `bundles` (required only when `verify_bundles=true`)
- `dashboard` (required only when `verify_dashboard=true`)

Config is strict: unknown fields are rejected.

`RESEARCH_CREATED_UTC` is required and authoritative for artifact timestamps.

## Read-Only Checks

Core checks (always enabled):
- `verify_baseline_root`: baseline index/promotions presence + runset card/manifest integrity
- `verify_promotions`: promoted baseline hash matches runset baseline card
- `verify_runsets`: runset catalog validation for each requested runset

Optional checks:
- `verify_bundles`: runs `doctor bundle-verify` logic for each configured bundle zip
- `verify_dashboard`: validates dashboard summary hash and dashboard manifest canonical hash

No refresh, recompute, or catalog mutation occurs.

## Output Artifacts

Writes to `<out_dir>`:
- `ci.doctor.summary.json`
- `ci.doctor.summary.manifest.json`

### `ci.doctor.summary.json` v1

Fields:
- `ci_doctor_version: "v1"`
- `created_utc`
- `label`
- `runset_count`
- `results`
  - `status` (`PASS` | `FAIL`)
  - `failures[]` (`check`, optional `runset_id`, `detail`)
- `checks`
  - `baseline_root_ok`
  - `promotions_ok`
  - `runsets_ok`
  - `bundles_ok` (`bool | null`)
  - `dashboard_ok` (`bool | null`)
- `pointers`
  - `baseline_root`
  - `catalog_dir`
- `ci_doctor_canonical_sha256`

### `ci.doctor.summary.manifest.json` v1

Fields:
- `manifest_version: "v1"`
- `created_utc`
- `inputs[]` (`path`, `sha256`, `bytes`)
- `outputs.ci.doctor.summary.json` (`sha256`, `bytes`)
- `ci_doctor_manifest_canonical_sha256`

## Exit Behavior

- Exit `0` when summary `results.status=PASS`
- Exit `1` when summary `results.status=FAIL`

CLI prints stable check lines, failure count, output paths, and final status line.

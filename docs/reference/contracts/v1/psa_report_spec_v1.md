# PSA Report Spec v1

## Purpose

`psa report` emits a deterministic summary artifact from existing `psa.parquet` output.

It captures stable alignment distribution, longest streaks, and transition counts so operators can compare runs later without ad-hoc analysis commands.

## Command

```text
python -m research_core.cli psa report --run <run_dir>
```

## Inputs

Required files in `<run_dir>`:

- `psa.parquet`
- `psa.manifest.json`

`RESEARCH_CREATED_UTC` is required and used as `created_utc`.

## Outputs

- `<run_dir>/psa.report.json`
- `<run_dir>/psa.report.manifest.json`

Writes are atomic (`.tmp` then replace) to avoid partial output artifacts.

## psa.report.json v1

Fields:

- `report_version: "v1"`
- `created_utc`
- `run_ref` (run directory name)
- `inputs`
  - `psa_parquet_sha256`
  - `psa_manifest_sha256`
  - optional `psa_canonical_table_sha256`
- `metrics`
  - `row_count`
  - `alignment_counts`
  - `alignment_percent` (fixed 6-dp strings)
  - `longest_streaks`
  - `transition_matrix_counts`
- `checksums`
  - `alignment_vector_sha256`
- `psa_report_canonical_sha256`

### Determinism rules

- `alignment_vector_sha256`:
  - concatenate `"<a>\\n"` for each row in original order
  - hash UTF-8 bytes with SHA-256
- canonical hash fields:
  - `json.dumps(obj_without_self, sort_keys=True, separators=(",", ":"), ensure_ascii=False)`
  - SHA-256 of UTF-8 bytes
- JSON file formatting:
  - `json.dumps(sort_keys=True, indent=2, ensure_ascii=False) + "\\n"`

## psa.report.manifest.json v1

Fields:

- `manifest_version: "v1"`
- `created_utc`
- `git_commit`
- `inputs[]` for:
  - `psa.parquet`
  - `psa.manifest.json`
- `outputs.psa.report.json`
- `manifest_canonical_sha256`

Input/output paths are run-relative (e.g., `psa.parquet`).

## CLI behavior

- On success prints:
  - `PSA_REPORT status=PASS`
  - `report=<path>`
  - `manifest=<path>`
- On validation failure exits non-zero (`1`) with fail-loud error.

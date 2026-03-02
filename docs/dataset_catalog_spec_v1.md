# Dataset Catalog Spec v1

## Purpose
Dataset catalog v1 provides deterministic, content-addressed registration for immutable datasets.

Catalog entries are JSON files under a user-provided catalog root. No database behavior is introduced.

## Schema
File: `schemas/dataset.catalog.schema.v1.json`

Top-level entry fields:
- `dataset_version`: `"v1"`
- `dataset_id`: content-addressed hash over canonical dataset fingerprint payload
- `kind`: `"raw_vendor_v1"` or `"canon_v1"`
- `created_utc`: required from `RESEARCH_CREATED_UTC`
- `tz`: required for `canon_v1` and must be `"America/New_York"`; optional for raw
- `description`: optional
- `source`: source root label + deterministic file listing and counts
- `fingerprint`: deterministic content fingerprints
- `dataset_entry_canonical_sha256`: canonical hash of entry excluding this field

## Catalog Layout
Given catalog root `<catalog>`:
- `<catalog>/datasets.index.json`
- `<catalog>/entries/<dataset_id>.json`

`datasets.index.json` shape:
- `index_version`: `"v1"`
- `created_utc`
- `datasets`: object keyed by `dataset_id` where each value includes:
  - `kind`
  - `created_utc`
  - `entry_path` (`entries/<dataset_id>.json`)

## Determinism Rules
- Raw registration enumerates files recursively under `--root` and sorts by root-relative forward-slash path.
- File listing entries contain `{path, bytes, sha256}`.
- `files_sha256` is computed over sorted lines in this exact form:

`sha256␠␠path\n`

- Dataset entry and index JSON are written as canonical bytes:

`json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\\n"`

- No wall-clock timestamps; `RESEARCH_CREATED_UTC` is required for registration.

## Dataset ID Rules
`dataset_id` is SHA256 of canonical JSON for:

- raw:
  - `kind`
  - `files_sha256`
  - `file_count`
  - `total_bytes`
  - optional `tz` when provided

- canon:
  - `kind`
  - `files_sha256`
  - `file_count`
  - `total_bytes`
  - `canon_table_sha256`
  - `tz` (`America/New_York`)

For `canon_v1`, `canon_table_sha256` must equal
`canon.manifest.json.output_files["canon.parquet"].canonical_table_sha256`.

## Immutability Rules
- If `entries/<dataset_id>.json` already exists, its payload must match exactly (canonical bytes) or registration fails.
- If `datasets.index.json` already references `dataset_id`, metadata (`kind`, `created_utc`, `entry_path`) must not change.
- Existing immutable records are never rewritten with different content.

## CLI
- `dataset register raw --catalog <dir> --root <dir> [--desc <text>] [--tz <tz>]`
- `dataset register canon --catalog <dir> --run <run_dir> [--desc <text>]`
- `dataset list --catalog <dir>`
- `dataset show --catalog <dir> --id <dataset_id>`
- `dataset validate --catalog <dir> --id <dataset_id>`

`dataset validate` recomputes current fingerprint from on-disk content and compares against the registered entry.
It prints deterministic PASS/FAIL text and exits non-zero on FAIL.
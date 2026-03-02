# Research Manifest Spec v1

Each run writes `canon.manifest.json` with:

- `manifest_version: v1`
- creation timestamp `created_utc` (ISO8601)
- run identity (`instrument`, `tf`, `session_policy`, RTH window)
- input file inventory with byte hashes
- rowcount and timespan (`start_ts`, `end_ts`)
- output file hashes and bytes
- schema and colmap versions
- code version (`git_commit` or `unknown`)
- determinism notes

## Hashing

- File hashes are SHA256 on raw file bytes.
- Parquet output tracks:
  - `parquet_bytes_sha256` (best effort)
  - `canonical_table_sha256` (source of truth)

`canonical_table_sha256` is computed from Arrow IPC stream serialization of the canon table with stable schema and row order.

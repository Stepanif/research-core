# Lineage Spec v1

## Purpose
Lineage v1 adds deterministic bidirectional lineage by combining:
- run-local lineage artifacts under each run directory, and
- dataset-catalog mirror links from dataset to run.

Dataset entries remain immutable and unchanged.

## Files
Run-local:
- `<run_dir>/lineage/lineage.json`
- `<run_dir>/lineage/lineage.manifest.json`

Catalog mirror:
- `<catalog_dir>/links/dataset_to_runs.index.json`

## Lineage Contract
Schema: `schemas/lineage.schema.v1.json`

Top-level fields:
- `lineage_version`: `"v1"`
- `created_utc`: required from `RESEARCH_CREATED_UTC`
- `run_ref`
- `inputs`
- `build`
- `artifacts`
- `lineage_canonical_sha256`

`run_ref`:
- `run_dir_ref` (stable non-absolute run identifier)
- `instrument`, `tf`
- `session_policy`, `tz`, `rth_start`, `rth_end`

`inputs`:
- `raw_dataset_id` (optional)
- `canon_dataset_id` (optional)
- `source_files_sha256` (from canonical `canon.manifest.json.input_files` listing)
- `schema_sha256`
- `colmap_sha256`

`build`:
- `git_commit`
- `tool_versions` (deterministic key order; include only present tools)

`artifacts`:
- `canon_table_sha256`
- `psa_table_sha256` (optional)
- `observe_summary_manifest_sha256` (optional canonical hash)
- `observe_profile_manifest_sha256` (optional canonical hash)

`lineage_canonical_sha256`:
- SHA256 over canonical JSON of `lineage.json` excluding `lineage_canonical_sha256`.

## Determinism
- Canonical JSON bytes are:
  `json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\\n"`
- No wall-clock timestamps; `RESEARCH_CREATED_UTC` required.
- Input file listing and all index maps are sorted deterministically.

## Immutability
- Existing `lineage.json` / `lineage.manifest.json` must match exactly on rerun; otherwise fail-loud.
- `dataset_to_runs.index.json` is append-only for new runs.
- If an existing `(dataset_id, canon_table_sha256)` pair appears with a different lineage hash, fail-loud.

## dataset_to_runs Index Contract
```
{
  "index_version": "v1",
  "created_utc": "...",
  "datasets": {
    "<dataset_id>": {
      "runs": [
        {
          "run_ref": "<stable string>",
          "run_lineage_canonical_sha256": "...",
          "canon_table_sha256": "...",
          "created_utc": "..."
        }
      ]
    }
  }
}
```

Ordering:
- dataset keys sorted
- each runs list sorted by `(canon_table_sha256, run_ref)`
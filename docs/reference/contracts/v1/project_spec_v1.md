# Project Spec v1

## Purpose
Project runner orchestrates experiment batches across an explicit run list. Project materialize provides a deterministic dataset-backed path that first produces run directories, then existing project run/report flows operate on explicit runs.

## Schema
File: `schemas/project.schema.v1.json`

Required fields:
- `project_version`: `"v1"`
- `name`: string
- `spec_dirs`: explicit list of spec directory paths
- `output_dir`: base output directory for project artifacts
- `policy.fail_fast`: must be `true`

Exactly one of:
- `runs`: explicit list of run directory paths
- `datasets`: list of dataset references for materialization

`datasets[]` fields:
- `dataset_id`
- `instrument`
- `tf`
- `session_policy` (`full|rth|eth`)
- `schema_path`
- `colmap_path`
- `rth_start`, `rth_end` required when `session_policy=rth`
- optional `note`

Optional fields:
- `created_utc`: ignored for outputs
- `policy.require_observe`: default `false`
- `notes`: optional string

## Determinism rules
- Output timestamps come only from `RESEARCH_CREATED_UTC`.
- Project ID is hash-based from canonical project payload and tool version.
- Batch ID is hash-based from run input hashes and spec listing hashes.
- Lists are sorted deterministically (`runs`, `spec_dirs`, entries in outputs).
- JSON output encoding is canonical bytes:
  `json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\\n"`

## Commands
- `project run --project <project.json>`
  - validates spec
  - executes/reuses deterministic per-run/per-spec-dir batches
  - writes:
    - `<output_dir>/<project_id>/project.summary.json`
    - `<output_dir>/<project_id>/project.manifest.json`
    - `<output_dir>/<project_id>/README_PROJECT.txt`

- `project report --project <project.json>`
  - read-only aggregation from existing batch and experiment report artifacts
  - writes:
    - `<output_dir>/<project_id>/project.report.json`
    - `<output_dir>/<project_id>/project.report.manifest.json`

- `project materialize --project <project.json> --catalog <catalog_dir> --runs-root <dir>`
  - requires project `datasets` mode
  - validates every referenced dataset is pre-registered
  - deterministically computes per-dataset run directory path from hash-derived run id
  - if run dir exists, requires `doctor run` PASS to reuse
  - if run dir does not exist, executes deterministic pipeline:
    - canon
    - psa
    - observe summary
    - observe profile
    - registry refresh
    - lineage build
  - writes:
    - `<output_dir>/<project_id>/materialize.summary.json`
    - `<output_dir>/<project_id>/materialize.manifest.json`

## Materialize determinism rules
- Run id input payload includes dataset reference parameters and file-byte hashes for schema/colmap contracts.
- Run directory naming is stable: `<runs_root>/runs/<run_id>`.
- Materialization iterates dataset refs sorted by `(dataset_id, tf)`.
- Materialize summary/manifest JSON outputs are canonical bytes.

## project.summary.json (v1)
- `project_id`, `project_version`, `name`, `created_utc`
- `runs`: sorted per run, each with sorted `batches`
- `totals`: deterministic counts

## project.manifest.json (v1)
- `manifest_version`, `created_utc`
- `inputs`: project spec + batch summary/manifest inputs used
- `outputs`: `project.summary.json` bytes + sha256 (and report output if present)
- `project_manifest_canonical_sha256`: canonical hash excluding self field

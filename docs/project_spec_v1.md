# Project Spec v1

## Purpose
Project runner orchestrates experiment batches across an explicit run list. It reuses existing experiment batch/report behavior and does not change core artifact semantics.

## Schema
File: `schemas/project.schema.v1.json`

Required fields:
- `project_version`: `"v1"`
- `name`: string
- `runs`: explicit list of run directory paths
- `spec_dirs`: explicit list of spec directory paths
- `output_dir`: base output directory for project artifacts
- `policy.fail_fast`: must be `true`

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

## project.summary.json (v1)
- `project_id`, `project_version`, `name`, `created_utc`
- `runs`: sorted per run, each with sorted `batches`
- `totals`: deterministic counts

## project.manifest.json (v1)
- `manifest_version`, `created_utc`
- `inputs`: project spec + batch summary/manifest inputs used
- `outputs`: `project.summary.json` bytes + sha256 (and report output if present)
- `project_manifest_canonical_sha256`: canonical hash excluding self field

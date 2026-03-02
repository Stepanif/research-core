# RunSet Spec v1

## Purpose
RunSet v1 introduces immutable cohort objects that reference both:
- `datasets` (dataset catalog IDs), and
- explicit `runs` references.

RunSets are content-addressed and catalog-local. They do not modify dataset catalog or lineage semantics.

## Storage layout
Under `<catalog_dir>/runsets/`:
- `runsets.index.json`
- `entries/<runset_id>.json`

`runsets.index.json` (v1):
- `index_version: "v1"`
- `created_utc` from `RESEARCH_CREATED_UTC`
- `runsets` mapping keyed by `runset_id`

Each record:
- `created_utc`
- `entry_path` (`entries/<runset_id>.json`)

## RunSet entry contract
Schema: `schemas/runset.schema.v1.json`

Entry fields:
- `runset_version`: `"v1"`
- `runset_id`: sha256 over canonical JSON of `fingerprint`
- `created_utc`: required from `RESEARCH_CREATED_UTC`
- `name`: optional
- `datasets`: sorted unique dataset IDs
- `runs`: sorted run refs by `(dataset_id or "", canon_table_sha256 or "", run_ref)`
- `policy`
- `fingerprint`
- `runset_entry_canonical_sha256`: canonical hash excluding self field

`runs[]` fields:
- `run_ref`: stable non-absolute string
- `dataset_id`: optional
- `canon_table_sha256`: optional
- `required_artifacts` defaults (v1):
  - `canon=true`
  - `psa=true`
  - `observe=true`
  - `experiments=false`

`policy` defaults (v1):
- `allow_materialize_missing=false`
- `require_lineage_links=true`
- `require_bidirectional=true`

`fingerprint` fields:
- `datasets_sha256`: canonical hash of sorted unique datasets list
- `runs_sha256`: canonical hash of sorted canonical runs list
- `policy_sha256`: canonical hash of canonical policy block

## Determinism rules
- Canonical JSON bytes are:
  `json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\\n"`
- No wall-clock timestamps; `RESEARCH_CREATED_UTC` is required.
- Index keys and listings are sorted deterministically.

## Immutability rules
- Existing `entries/<runset_id>.json` must match exactly; otherwise fail-loud.
- Existing index row for a `runset_id` must match exactly; otherwise fail-loud.
- No overwrite/delete semantics.

## CLI
- `runset create --catalog <catalog_dir> --spec <runset.json>`
- `runset list --catalog <catalog_dir>`
- `runset show --catalog <catalog_dir> --id <runset_id>`
- `runset validate --catalog <catalog_dir> --id <runset_id>`

## Validation behavior
`runset validate` checks:
- all dataset IDs exist in dataset catalog
- when `require_lineage_links=true`:
  - `links/dataset_to_runs.index.json` exists
  - each dataset has at least one linked run hash OR explicit run refs include `dataset_id+canon_table_sha256`
- when a run ref includes both `dataset_id` and `canon_table_sha256`:
  - that hash must exist in the dataset-to-runs index for that dataset

On-disk `run_ref` resolution is intentionally out of scope for v1 Step 1.

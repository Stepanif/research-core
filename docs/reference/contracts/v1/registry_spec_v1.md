# Research Registry Spec v1

## Dataset Registry

Command:

`python -m research_core.cli registry build --data-root <...> --out <...>`

Registry emits deterministic JSON containing one dataset record per discovered run manifest.
Ordering is stable and sorted by `(instrument, tf, source_path)`.

Required dataset fields:

- instrument
- tf
- source_path
- source_hash
- rowcount
- start_ts
- end_ts
- schema_version
- colmap_version
- session_policy
- output_hashes

## Run Index

Command:

`python -m research_core.cli registry index-runs --runs-root <...> --out <...>`

Index includes each run path with:

- manifest hash
- contract hash
- instrument
- tf

Duplicate manifest hashes are fail-loud.

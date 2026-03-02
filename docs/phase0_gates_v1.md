# Phase 0 Gates v1

## Command Gates

### Canonicalization

Required outputs per run:

- `canon.parquet`
- `canon.manifest.json`
- `canon.contract.json`
- `logs/canon.log`

Fail-loud on any parse, schema, ordering, timestamp, timezone, or invariant error.

### Validate Canon

Required output:

- `validate/canon_validate.json`

Validation fails on invariant violations or column contract drift.

### Registry Build

Required output:

- registry JSON with deterministic ordering and top-level hash.

### Run Index

Required output:

- runs index JSON with manifest and contract hashes.

Fails on duplicate manifest hashes or missing contracts.

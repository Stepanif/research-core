# Stage 0 Canon

Generated from docs/reference/artifacts/catalog.v1.yml by tools/docs/gen_artifact_catalog.py

- Stage Key: `stage0_canon`
- Tools:
  - `research canon`
  - `research validate canon`

## Outputs

| Output ID | Path Template | Type | Schema | Description |
|---|---|---|---|---|
| canon.contract.json | exec_outputs/runs/sample/canon.contract.json | json | TODO: schema link not yet confirmed | Canon contract output path from validate canon command. |
| canon.parquet | exec_outputs/runs/sample/canon.parquet | parquet | [../schemas/canon.schema.v1.md](../schemas/canon.schema.v1.md) | Canonicalized dataset output from canon command. |

## Invariants: canon.contract.json

- Contract path matches validate canon --contract target.

## Verification: canon.contract.json

- Check exec_outputs/runs/sample/canon.contract.json exists.

## Invariants: canon.parquet

- Required canon columns follow the canonical ordering contract.
- Timestamps are monotonic and duplicate timestamps are forbidden.

## Verification: canon.parquet

- Check exec_outputs/runs/sample/canon.parquet exists.

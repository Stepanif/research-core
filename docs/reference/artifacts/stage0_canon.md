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
| canon.log | <run_dir>/logs/canon.log | TODO: confirm type | TODO: not schema-driven | Canonicalization log file required by phase0 gates. |
| canon.manifest.json | <run_dir>/canon.manifest.json | json | TODO: schema link not yet confirmed | Canon generation manifest required by phase0 gates. |
| canon.parquet | exec_outputs/runs/sample/canon.parquet | parquet | [../schemas/canon.schema.v1.md](../schemas/canon.schema.v1.md) | Canonicalized dataset output from canon command. |
| canon_validate.json | <run_dir>/validate/canon_validate.json | json | TODO: schema link not yet confirmed | Validate canon report required by phase0 gates. |

## Invariants: canon.contract.json

- Contract path matches validate canon --contract target.

## Verification: canon.contract.json

- Check exec_outputs/runs/sample/canon.contract.json exists.

## Invariants: canon.log

- Canon gate requires logs/canon.log to exist per run.

## Verification: canon.log

- Check <run_dir>/logs/canon.log exists.

## Invariants: canon.manifest.json

- Canonicalization gate requires canon.manifest.json to exist per run.

## Verification: canon.manifest.json

- Check <run_dir>/canon.manifest.json exists.

## Invariants: canon.parquet

- Required canon columns follow the canonical ordering contract.
- Timestamps are monotonic and duplicate timestamps are forbidden.

## Verification: canon.parquet

- Check exec_outputs/runs/sample/canon.parquet exists.

## Invariants: canon_validate.json

- Validate gate requires validate/canon_validate.json to exist.

## Verification: canon_validate.json

- Check <run_dir>/validate/canon_validate.json exists.

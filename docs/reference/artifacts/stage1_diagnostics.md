# Stage 1 Diagnostics

Generated from docs/reference/artifacts/catalog.v1.yml by tools/docs/gen_artifact_catalog.py

- Stage Key: `stage1_diagnostics`
- Tools:
  - `research ci doctor`

## Outputs

| Output ID | Path Template | Type | Schema | Description |
|---|---|---|---|---|
| ci.doctor.summary.json | exec_outputs/analysis/es_5m/doctor/ci.doctor.summary.json | json | [../schemas/ci.doctor.summary.schema.v1.md](../schemas/ci.doctor.summary.schema.v1.md) | CI doctor summary listed as a primary ES5M analysis output. |

## Invariants: ci.doctor.summary.json

- File exists after ci doctor completes in the ES5M flow.

## Verification: ci.doctor.summary.json

- Check exec_outputs/analysis/es_5m/doctor/ci.doctor.summary.json exists.

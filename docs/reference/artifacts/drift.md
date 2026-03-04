# Drift

Generated from docs/reference/artifacts/catalog.v1.yml by tools/docs/gen_artifact_catalog.py

- Stage Key: `drift`
- Tools:
  - `TODO: confirm drift CLI command entrypoints`

## Outputs

| Output ID | Path Template | Type | Schema | Description |
|---|---|---|---|---|
| dashboard.summary.json | exec_outputs/analysis/es_5m/dashboard/dashboard.summary.json | json | [../schemas/dashboard.summary.schema.v1.md](../schemas/dashboard.summary.schema.v1.md) | Dashboard summary listed as primary ES5M analysis output. |

## Invariants: dashboard.summary.json

- File exists when dashboard verification reports success.

## Verification: dashboard.summary.json

- Run docs/scripts/verify_es5m_dashboard.ps1 and confirm DASHBOARD OK.

## TODO

- TODO: confirm dedicated drift.report output path for this workflow.

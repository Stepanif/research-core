# Risk

Generated from docs/reference/artifacts/catalog.v1.yml by tools/docs/gen_artifact_catalog.py

- Stage Key: `risk`
- Tools:
  - `research risk runset`

## Outputs

| Output ID | Path Template | Type | Schema | Description |
|---|---|---|---|---|
| risk.runset.summary.json | exec_outputs/analysis/es_5m/risk_runset/<runset_id>/risk.runset.summary.json | json | TODO: schema link not yet confirmed | Runset risk summary output listed in ES5M analysis docs. |

## Invariants: risk.runset.summary.json

- File exists for each analyzed runset_id.

## Verification: risk.runset.summary.json

- Check exec_outputs/analysis/es_5m/risk_runset/<runset_id>/risk.runset.summary.json exists.

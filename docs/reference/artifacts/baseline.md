# Baseline

Generated from docs/reference/artifacts/catalog.v1.yml by tools/docs/gen_artifact_catalog.py

- Stage Key: `baseline`
- Tools:
  - `TODO: confirm exact baseline CLI invocation from canonical user docs`

## Outputs

| Output ID | Path Template | Type | Schema | Description |
|---|---|---|---|---|
| baseline.card.json | baselines/prod/<runset_id>/baseline.card.json | json | TODO: schema link not yet confirmed | Baseline card produced by baseline promotion workflow. |

## Invariants: baseline.card.json

- File exists after promote_es5m_baseline workflow completes.

## Verification: baseline.card.json

- Check baselines/prod/<runset_id>/baseline.card.json exists.

## TODO

- TODO: confirm baseline diff/index/promotions artifact paths from contract sources.

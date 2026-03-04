# Baseline

Generated from docs/reference/artifacts/catalog.v1.yml by tools/docs/gen_artifact_catalog.py

- Stage Key: `baseline`
- Tools:
  - `python -m research_core.cli risk sweep --catalog exec_outputs/catalog --runset RUNSET_ID --out exec_outputs/pilot/risk`
  - `python -m research_core.cli baseline index refresh --root baselines/prod`
  - `python -m research_core.cli baseline promote --root baselines/prod --runset RUNSET_ID --baseline-id BASELINE_ID --label prod`
  - `python -m research_core.cli risk diff --a <baseline.card.json> --b <baseline.card.json> --out <dir>`

## Outputs

| Output ID | Path Template | Type | Schema | Description |
|---|---|---|---|---|
| baseline.card.json | baselines/prod/<runset_id>/baseline.card.json | json | TODO: schema link not yet confirmed | Baseline card produced by baseline promotion workflow. |
| baseline.diff.json | <out>/baseline.diff.json | json | TODO: schema link not yet confirmed | Deterministic baseline diff output from risk diff. |
| baseline.diff.manifest.json | <out>/baseline.diff.manifest.json | json | TODO: schema link not yet confirmed | Manifest for baseline.diff.json with input and output hashes. |

## Invariants: baseline.card.json

- File exists after promote_es5m_baseline workflow completes.

## Verification: baseline.card.json

- Check baselines/prod/<runset_id>/baseline.card.json exists.

## Invariants: baseline.diff.json

- Baseline diff classification uses fixed v1 instability thresholds.

## Verification: baseline.diff.json

- Check <out>/baseline.diff.json exists after risk diff.

## Invariants: baseline.diff.manifest.json

- Manifest includes byte hashes for both baseline card inputs and diff output.

## Verification: baseline.diff.manifest.json

- Check <out>/baseline.diff.manifest.json exists after risk diff.

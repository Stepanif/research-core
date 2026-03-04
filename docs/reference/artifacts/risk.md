# Risk

Generated from docs/reference/artifacts/catalog.v1.yml by tools/docs/gen_artifact_catalog.py

- Stage Key: `risk`
- Tools:
  - `research risk runset`

## Outputs

| Output ID | Path Template | Type | Schema | Description |
|---|---|---|---|---|
| risk.runset.manifest.json | <out>/<runset_id>/risk.runset.manifest.json | json | TODO: schema link not yet confirmed | Manifest for runset risk summary including runset and per-run inputs. |
| risk.runset.summary.json | <out>/<runset_id>/risk.runset.summary.json | json | TODO: schema link not yet confirmed | Deterministic runset-level risk summary from risk runset. |

## Invariants: risk.runset.manifest.json

- Manifest includes runset risk summary output hash and deterministic input list.

## Verification: risk.runset.manifest.json

- Check <out>/<runset_id>/risk.runset.manifest.json exists.

## Invariants: risk.runset.summary.json

- File exists for each analyzed runset_id.

## Verification: risk.runset.summary.json

- Check <out>/<runset_id>/risk.runset.summary.json exists.

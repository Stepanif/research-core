# Drift

Generated from docs/reference/artifacts/catalog.v1.yml by tools/docs/gen_artifact_catalog.py

- Stage Key: `drift`
- Tools:
  - `python -m research_core.cli risk drift --catalog exec_outputs/catalog --root baselines/prod --runset RUNSET_ID --label prod --out exec_outputs/pilot/drift`
  - `python -m research_core.cli risk dashboard --catalog exec_outputs/catalog --root baselines/prod --runsets configs/pilot/runsets.pilot.json --out exec_outputs/pilot/dashboard --label prod`

## Outputs

| Output ID | Path Template | Type | Schema | Description |
|---|---|---|---|---|
| dashboard.summary.json | <out>/dashboard.summary.json | json | [../schemas/dashboard.summary.schema.v1.md](../schemas/dashboard.summary.schema.v1.md) | Deterministic dashboard summary generated from runset drift reports. |
| dashboard.summary.manifest.json | <out>/dashboard.summary.manifest.json | json | TODO: schema link not yet confirmed | Manifest for dashboard summary with runsets and drift report inputs. |
| drift.report.json | <out>/drift/<runset_id>/drift.report.json | json | [../schemas/drift.report.schema.v1.md](../schemas/drift.report.schema.v1.md) | Deterministic drift classification report for one runset. |
| drift.report.manifest.json | <out>/drift/<runset_id>/drift.report.manifest.json | json | TODO: schema link not yet confirmed | Manifest for drift report with baseline, runset, and diff inputs. |

## Invariants: dashboard.summary.json

- Dashboard summary is written only when all listed runsets succeed.

## Verification: dashboard.summary.json

- Check <out>/dashboard.summary.json exists after risk dashboard.

## Invariants: dashboard.summary.manifest.json

- Manifest includes sorted input hashes and dashboard output hash.

## Verification: dashboard.summary.manifest.json

- Check <out>/dashboard.summary.manifest.json exists after risk dashboard.

## Invariants: drift.report.json

- Drift status is DRIFT iff abs(instability_mean_delta) >= 5.0 or worst5_jaccard <= 0.40.

## Verification: drift.report.json

- Check <out>/drift/<runset_id>/drift.report.json exists after risk dashboard.

## Invariants: drift.report.manifest.json

- Manifest includes drift report output hash and sorted input hashes.

## Verification: drift.report.manifest.json

- Check <out>/drift/<runset_id>/drift.report.manifest.json exists after risk dashboard.

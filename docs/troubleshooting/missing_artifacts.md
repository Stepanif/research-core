# Missing Artifacts

Use this page when expected output files are missing after a command/run.

## Quick checks

1. Confirm the command actually completed without failing fast.
	See also: [Run CI Locally](../how-to/run_ci_locally.md)
2. Confirm you are checking the expected path template from artifact reference pages.
	See also: [Artifacts Reference](../reference/artifacts/index.md)
3. Re-run the exact command from the relevant tutorial/how-to page.
4. If docs references are missing, run generated-doc checks.

PowerShell docs checks:

```powershell
python tools/docs/gen_cli_ref.py
python tools/docs/gen_schema_ref.py
python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
$env:NO_MKDOCS_2_WARNING = "1"
python -m mkdocs build
```

## Artifact path checks (examples)

PowerShell:

```powershell
Test-Path "exec_outputs/runs/sample/canon.manifest.json"
Test-Path "exec_outputs/registry/registry.json"
Test-Path "exec_outputs/analysis/es_5m/doctor/ci.doctor.summary.json"
Test-Path "baselines/prod/RUNSET_ID/baseline.card.json"
Test-Path "exec_outputs/pilot/dashboard/dashboard.summary.json"
```

Source path templates:

- [Stage 0 Canon](../reference/artifacts/stage0_canon.md)
- [Lineage Artifacts](../reference/artifacts/lineage.md)
- [Stage 1 Diagnostics](../reference/artifacts/stage1_diagnostics.md)
- [Baseline Artifacts](../reference/artifacts/baseline.md)
- [Drift Artifacts](../reference/artifacts/drift.md)

## Upstream cause map

| Missing artifact | Check upstream step |
|---|---|
| `canon.manifest.json` / `canon.parquet` | Re-run `canon` + `validate canon` flow from [Quickstart](../getting-started/quickstart.md) |
| `registry.json` / `index.json` | Re-run registry commands from [Quickstart](../getting-started/quickstart.md) and [Lineage Artifacts](../reference/artifacts/lineage.md) |
| `risk.runset.summary.json` | Re-run runset risk flow from [Risk Runset Analysis](../tutorials/risk_runset_analysis.md) |
| `drift.report.json` / `dashboard.summary.json` | Re-run drift/dashboard flow from [Drift Review Workflow](../tutorials/drift_review_workflow.md) |
| `baseline.card.json` / `baseline.index.json` / `baseline.promotions.json` | Re-run baseline workflow from [Baseline Promotion](../tutorials/baseline_promotion.md) |

## Related failure guides

- [Stale Goldens](stale_goldens.md)
- [Determinism Failures](determinism_failures.md)

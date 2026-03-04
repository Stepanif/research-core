# ES5M End to End

This tutorial runs the existing ES 5m pipeline scripts and validates the first outputs to inspect.

## Source of truth

- Main flow and script order: [README_ANALYSIS_ES5M](../README_ANALYSIS_ES5M.md)
- Operator command-level flow: [Pilot Cohort v1](../pilot_cohort_v1.md)
- Artifact interpretation: [Artifacts Reference](../reference/artifacts/index.md)
- Contract interpretation: [Contracts Reference](../reference/contracts/index.md)

## Prerequisites

- You are at repo root.
- Your Python environment is active.
- ES5m data registration requirements are satisfied per [README_ANALYSIS_ES5M](../README_ANALYSIS_ES5M.md).

## Step 1: Run the one-command ES5M pipeline

```powershell
./docs/scripts/run_full_es5m_pipeline.ps1
```

Per source docs, this runs in order:

1. `docs/scripts/register_es5m_dataset.ps1`
2. `docs/scripts/materialize_es5m_project.ps1`
3. `docs/scripts/create_es5m_runset.ps1`
4. `docs/scripts/promote_es5m_baseline.ps1`
5. `docs/scripts/run_analysis_es_5m.ps1`

## Step 2: Open first outputs

Open these files first (paths from [README_ANALYSIS_ES5M](../README_ANALYSIS_ES5M.md)):

- `exec_outputs/analysis/es_5m/doctor/ci.doctor.summary.json`
- `exec_outputs/analysis/es_5m/dashboard/dashboard.summary.json`
- `exec_outputs/analysis/es_5m/risk_runset/<runset_id>/risk.runset.summary.json`
- `baselines/prod/<runset_id>/baseline.card.json`

Interpretation references:

- CI doctor schema: [CI Doctor Summary Schema](../reference/schemas/ci.doctor.summary.schema.v1.md)
- Dashboard schema: [Dashboard Summary Schema](../reference/schemas/dashboard.summary.schema.v1.md)
- Risk contract: [Risk Spec v1](../reference/contracts/v1/risk_spec_v1.md)
- Baseline contract: [Baseline Card Spec v1](../reference/contracts/v1/baseline_card_spec_v1.md)

## Step 3: Run dashboard verification gate

```powershell
.\docs\scripts\verify_es5m_dashboard.ps1
```

Success criteria from source docs:

- Script prints `DASHBOARD OK`
- `exec_outputs/analysis/es_5m/dashboard/dashboard.summary.json` exists

## Step 4: Escalate to command-level flow when needed

If the one-command flow fails or you need finer control, run the explicit sequence in [Pilot Cohort v1](../pilot_cohort_v1.md), especially:

- `risk sweep`
- `baseline index refresh`
- `baseline promote`
- `risk drift`
- `risk dashboard`
- `ci run` / `ci doctor`

## Troubleshooting links

- [Missing Artifacts](../troubleshooting/missing_artifacts.md)
- [Determinism Failures](../troubleshooting/determinism_failures.md)
- [Stale Goldens](../troubleshooting/stale_goldens.md)

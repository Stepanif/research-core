# Drift Review Workflow

Use this workflow to generate drift artifacts for one runset and dashboard
summary across multiple runsets.

## What you will get

- Per-runset drift report + manifest:
	`drift.report.json`, `drift.report.manifest.json`
	([artifact ref](../reference/artifacts/drift.md)).
- Dashboard summary + manifest:
	`dashboard.summary.json`, `dashboard.summary.manifest.json`
	([artifact ref](../reference/artifacts/drift.md)).
- Contract-grounded interpretation rules for drift status:
	[Drift Report Spec v1](../reference/contracts/v1/drift_report_spec_v1.md),
	[Drift Dashboard Spec v1](../reference/contracts/v1/dashboard_spec_v1.md).
- Schema links:
	[Research Drift Report v1](../reference/schemas/drift.report.schema.v1.md),
	[Research Drift Dashboard Summary v1](../reference/schemas/dashboard.summary.schema.v1.md).

## Prereqs

- `RESEARCH_CREATED_UTC` is required for deterministic outputs.
- Catalog, baseline root, and runset IDs already exist.

!!! note "TODO: Environment bootstrap"
		This page assumes your Python environment is already active.

## Steps

### 1. Pin deterministic timestamp

```powershell
$env:RESEARCH_CREATED_UTC = "2026-03-02T00:00:00+00:00"
```

### 2. Run drift for one runset

```powershell
python -m research_core.cli risk drift --catalog exec_outputs/catalog --root baselines/prod --runset RUNSET_ID --label prod --out exec_outputs/pilot/drift
```

### 3. Run dashboard over a runset list

`--runsets` must be a strict JSON object with only `runset_ids`.

```json
{"runset_ids":["runset-a","runset-b"]}
```

```powershell
python -m research_core.cli risk dashboard --catalog exec_outputs/catalog --root baselines/prod --runsets configs/pilot/runsets.pilot.json --out exec_outputs/pilot/dashboard --label prod
```

## Verify outputs

Expected files:

- `exec_outputs/pilot/drift/RUNSET_ID/drift.report.json`
- `exec_outputs/pilot/drift/RUNSET_ID/drift.report.manifest.json`
- `exec_outputs/pilot/dashboard/dashboard.summary.json`
- `exec_outputs/pilot/dashboard/dashboard.summary.manifest.json`

References:

- [Drift Artifacts](../reference/artifacts/drift.md)
- [Drift Report Spec v1](../reference/contracts/v1/drift_report_spec_v1.md)
- [Drift Dashboard Spec v1](../reference/contracts/v1/dashboard_spec_v1.md)

## Common failures

| Failure | What to do |
|---|---|
| stale goldens | [Stale Goldens](../troubleshooting/stale_goldens.md) |
| determinism failures | [Determinism Failures](../troubleshooting/determinism_failures.md) |
| missing artifacts | [Missing Artifacts](../troubleshooting/missing_artifacts.md) |
| docs drift (if docs were regenerated during the same change) | [Run CI Locally](../how-to/run_ci_locally.md) |

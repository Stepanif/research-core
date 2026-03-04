# Risk Runset Analysis

Use this tutorial to run deterministic runset-level risk analysis and locate the
result artifacts.

## What you will get

- `risk.runset.summary.json`
	([artifact ref](../reference/artifacts/risk.md)).
- `risk.runset.manifest.json`
	([artifact ref](../reference/artifacts/risk.md)).
- A validated runset ID from RunSet v1 flow
	([RunSet Spec v1](../reference/contracts/v1/runset_spec_v1.md)).
- Contract/schemas for interpretation:
	[Risk Harness Spec v1](../reference/contracts/v1/risk_spec_v1.md),
	[Research Risk Harness v1 schema](../reference/schemas/risk.schema.v1.md),
	[Research RunSet v1 schema](../reference/schemas/runset.schema.v1.md).

## Prereqs

- `RESEARCH_CREATED_UTC` is required for risk outputs.
- A catalog directory and runset spec JSON are available.

!!! note "TODO: Environment bootstrap"
		This page assumes your Python environment is already active.

## Steps

### 1. Pin deterministic timestamp

```powershell
$env:RESEARCH_CREATED_UTC = "2026-03-02T00:00:00+00:00"
```

### 2. Create and validate a runset (or validate an existing one)

```powershell
python -m research_core.cli runset create --catalog exec_outputs/catalog --spec configs/pilot/runset.pilot.json
python -m research_core.cli runset validate --catalog exec_outputs/catalog --id RUNSET_ID
```

### 3. Run runset-level risk analysis

```powershell
python -m research_core.cli risk runset --catalog exec_outputs/catalog --id RUNSET_ID --out exec_outputs/pilot/risk_runset
```

### 4. Optional: generate baseline card from the same runset

```powershell
python -m research_core.cli risk sweep --catalog exec_outputs/catalog --runset RUNSET_ID --out exec_outputs/pilot/risk
```

## Verify outputs

Expected risk runset artifacts:

- `exec_outputs/pilot/risk_runset/RUNSET_ID/risk.runset.summary.json`
- `exec_outputs/pilot/risk_runset/RUNSET_ID/risk.runset.manifest.json`

References:

- [Risk Artifacts](../reference/artifacts/risk.md)
- [Risk Harness Spec v1](../reference/contracts/v1/risk_spec_v1.md)

## Common failures

| Failure | What to do |
|---|---|
| stale goldens | [Stale Goldens](../troubleshooting/stale_goldens.md) |
| determinism failures | [Determinism Failures](../troubleshooting/determinism_failures.md) |
| missing artifacts | [Missing Artifacts](../troubleshooting/missing_artifacts.md) |
| docs drift (if docs were regenerated during the same change) | [Run CI Locally](../how-to/run_ci_locally.md) |

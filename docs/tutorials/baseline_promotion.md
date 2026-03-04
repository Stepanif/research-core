# Baseline Promotion

Use this workflow to produce a baseline card, refresh baseline discovery index,
and promote a runset baseline to `label=prod`.

## What you will get

- Baseline card for a runset:
	`baselines/prod/<runset_id>/baseline.card.json`
	([artifact ref](../reference/artifacts/baseline.md)).
- Baseline discovery index and promotions files:
	`baseline.index.json`, `baseline.promotions.json`
	([Baseline Discovery Spec v1](../reference/contracts/v1/baseline_discovery_spec_v1.md)).
- Optional compare output via baseline diff:
	`baseline.diff.json`, `baseline.diff.manifest.json`
	([artifact ref](../reference/artifacts/baseline.md)).
- Schema references:
	[Research Baseline Card v1](../reference/schemas/baseline.card.schema.v1.md),
	[Research Baseline Index v1](../reference/schemas/baseline.index.schema.v1.md),
	[Research Baseline Promotions v1](../reference/schemas/baseline.promotions.schema.v1.md),
	[Research Baseline Diff v1](../reference/schemas/baseline.diff.schema.v1.md).

## Prereqs

- `RESEARCH_CREATED_UTC` pinned for deterministic artifacts.
- `RUNSET_ID` exists and validates.

!!! note "TODO: Environment bootstrap"
		This page assumes your Python environment is already active.

## Steps

### 1. Pin deterministic timestamp

```powershell
$env:RESEARCH_CREATED_UTC = "2026-03-02T00:00:00+00:00"
```

### 2. Validate runset

```powershell
python -m research_core.cli runset validate --catalog exec_outputs/catalog --id RUNSET_ID
```

### 3. Generate baseline card from runset

```powershell
python -m research_core.cli risk sweep --catalog exec_outputs/catalog --runset RUNSET_ID --out exec_outputs/pilot/risk
```

### 4. Refresh baseline index

```powershell
python -m research_core.cli baseline index refresh --root baselines/prod
```

### 5. Promote baseline to `prod`

```powershell
python -m research_core.cli baseline promote --root baselines/prod --runset RUNSET_ID --baseline-id BASELINE_ID --label prod
```

`BASELINE_ID` is the baseline checksum emitted by sweep/baseline card checksums.

### 6. Optional post-promotion gates from pilot flow

```powershell
python -m research_core.cli risk drift --catalog exec_outputs/catalog --root baselines/prod --runset RUNSET_ID --label prod --out exec_outputs/pilot/drift
python -m research_core.cli risk dashboard --catalog exec_outputs/catalog --root baselines/prod --runsets configs/pilot/runsets.pilot.json --out exec_outputs/pilot/dashboard --label prod
python -m research_core.cli ci run --config configs/pilot/ci.pilot.json
python -m research_core.cli ci doctor --config configs/pilot/doctor.pilot.json
```

## Verify outputs

Expected files:

- `baselines/prod/RUNSET_ID/baseline.card.json`
- `baselines/prod/baseline.index.json`
- `baselines/prod/baseline.promotions.json`

References:

- [Baseline Artifacts](../reference/artifacts/baseline.md)
- [Baseline Discovery Spec v1](../reference/contracts/v1/baseline_discovery_spec_v1.md)
- [Pilot Cohort v1](../pilot_cohort_v1.md)

## Common failures

| Failure | What to do |
|---|---|
| stale goldens | [Stale Goldens](../troubleshooting/stale_goldens.md) |
| determinism failures | [Determinism Failures](../troubleshooting/determinism_failures.md) |
| missing artifacts | [Missing Artifacts](../troubleshooting/missing_artifacts.md) |
| docs drift (if docs were regenerated during the same change) | [Run CI Locally](../how-to/run_ci_locally.md) |

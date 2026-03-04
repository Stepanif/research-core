# Run vs Run Compare

Use this workflow to compare two promoted runsets (often one run each) with the
repository's baseline diff path.

## What you will get

- A deterministic diff artifact: `baseline.diff.json`
	([artifact ref](../reference/artifacts/baseline.md)).
- A deterministic diff manifest: `baseline.diff.manifest.json`
	([artifact ref](../reference/artifacts/baseline.md)).
- A contract-backed compare method (`risk diff` / `risk diff-runset`)
	([Baseline Diff Spec v1](../reference/contracts/v1/baseline_diff_spec_v1.md),
	[Baseline Discovery Spec v1](../reference/contracts/v1/baseline_discovery_spec_v1.md)).
- Related references for lineage/runset/drift context:
	[RunSet Spec v1](../reference/contracts/v1/runset_spec_v1.md),
	[Lineage Spec v1](../reference/contracts/v1/lineage_spec_v1.md),
	[Drift Report Spec v1](../reference/contracts/v1/drift_report_spec_v1.md).

## Prereqs

- `RESEARCH_CREATED_UTC` is required for deterministic outputs in this workflow.
- Two promoted runsets must already exist in baseline root.

!!! note "TODO: Environment bootstrap"
		This page assumes your Python environment is already active. Use the
		project's standard local setup process before running commands.

## Steps

### 1. Pin deterministic timestamp

```powershell
$env:RESEARCH_CREATED_UTC = "2026-03-02T00:00:00+00:00"
```

### 2. Compare by runset IDs from baseline root

`risk diff-runset` is the repository's baseline-discovery compare wrapper.

```powershell
python -m research_core.cli risk diff-runset --root baselines/prod --a RUNSET_A --b RUNSET_B --out exec_outputs/compare
```

Optional label-resolved compare:

```powershell
python -m research_core.cli risk diff-runset --root baselines/prod --a RUNSET_A --b RUNSET_B --label-a prod --label-b prod --out exec_outputs/compare
```

### 3. Direct card-to-card compare (explicit file paths)

```powershell
python -m research_core.cli risk diff --a baselines/prod/RUNSET_A/baseline.card.json --b baselines/prod/RUNSET_B/baseline.card.json --out exec_outputs/compare
```

## Verify outputs

Expected outputs (from baseline artifact catalog + diff spec):

- `exec_outputs/compare/baseline.diff.json`
- `exec_outputs/compare/baseline.diff.manifest.json`

References:

- [Baseline Artifacts](../reference/artifacts/baseline.md)
- [Baseline Diff Spec v1](../reference/contracts/v1/baseline_diff_spec_v1.md)

## Common failures

| Failure | What to do |
|---|---|
| stale goldens | [Stale Goldens](../troubleshooting/stale_goldens.md) |
| determinism failures | [Determinism Failures](../troubleshooting/determinism_failures.md) |
| missing artifacts | [Missing Artifacts](../troubleshooting/missing_artifacts.md) |
| docs drift (if docs were regenerated during the same change) | [Run CI Locally](../how-to/run_ci_locally.md) |

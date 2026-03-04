# Concepts Map

This page is the operator spine: start here, then jump to the canonical reference or contract page for detail.

## Core terms

- **Run**: one materialized run directory with canon/validation outputs.
	- Reference: [Stage 0 Canon Artifacts](../reference/artifacts/stage0_canon.md)
	- Contract: [Phase 0 Gates v1](../reference/contracts/v1/phase0_gates_v1.md)

- **Runset**: deterministic grouping of runs for risk and drift analysis.
	- Contract: [Runset Spec v1](../reference/contracts/v1/runset_spec_v1.md)
	- Risk runset output: [Risk Artifacts](../reference/artifacts/risk.md)

- **Stage**: pipeline boundary with expected outputs.
	- Reference index: [Artifacts Reference](../reference/artifacts/index.md)
	- Canon stage contract: [Canon Spec v1](../reference/contracts/v1/canon_spec_v1.md)

- **Artifact**: file emitted by commands/stages, tracked in a deterministic catalog.
	- Catalog source: [Artifact Catalog Registry](../reference/artifacts/catalog.v1.yml)
	- Generated pages: [Artifacts Reference](../reference/artifacts/index.md)

- **Manifest**: hash-oriented metadata proving deterministic inputs/outputs.
	- Contract: [Manifest Spec v1](../reference/contracts/v1/manifest_spec_v1.md)
	- Examples: [Stage 0 Canon Artifacts](../reference/artifacts/stage0_canon.md), [Drift Artifacts](../reference/artifacts/drift.md)

- **Baseline**: promoted risk card snapshot used as reference for drift.
	- Reference: [Baseline Artifacts](../reference/artifacts/baseline.md)
	- Contracts: [Baseline Card Spec v1](../reference/contracts/v1/baseline_card_spec_v1.md), [Baseline Diff Spec v1](../reference/contracts/v1/baseline_diff_spec_v1.md)

- **Drift**: classification of runset change relative to baseline.
	- Reference: [Drift Artifacts](../reference/artifacts/drift.md)
	- Contracts: [Drift Report Spec v1](../reference/contracts/v1/drift_report_spec_v1.md), [Dashboard Spec v1](../reference/contracts/v1/dashboard_spec_v1.md)

- **Risk**: deterministic per-run and runset scoring outputs.
	- Reference: [Risk Artifacts](../reference/artifacts/risk.md)
	- Contract: [Risk Spec v1](../reference/contracts/v1/risk_spec_v1.md)

- **Golden**: approved baseline/expected outputs used for controlled comparisons and refreshes.
	- How-to: [Update Goldens Safely](../how-to/update_goldens_safely.md)
	- Troubleshooting: [Stale Goldens](../troubleshooting/stale_goldens.md)

## Suggested reading order

1. [Quickstart](quickstart.md)
2. [ES5M End to End](../tutorials/es5m_end_to_end.md)
3. [Artifacts Reference](../reference/artifacts/index.md)
4. [Contracts Reference](../reference/contracts/index.md)

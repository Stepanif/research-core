# Definitions

- **Artifact** — A file emitted by commands/stages and tracked in the artifact catalog.
	*See also:* [Artifacts Reference](../reference/artifacts/index.md), [Concepts Map](../getting-started/concepts-map.md)

- **Baseline** — A promoted reference snapshot used for drift and compare workflows.
	*See also:* [Baseline Discovery Spec v1](../reference/contracts/v1/baseline_discovery_spec_v1.md), [Baseline Artifacts](../reference/artifacts/baseline.md)

- **Baseline Card** — Deterministic summary output from `risk sweep` for a runset.
	*See also:* [Baseline Card Spec v1](../reference/contracts/v1/baseline_card_spec_v1.md), [Research Baseline Card v1](../reference/schemas/baseline.card.schema.v1.md)

- **Baseline Diff** — Deterministic comparator output between two baseline cards.
	*See also:* [Baseline Diff Spec v1](../reference/contracts/v1/baseline_diff_spec_v1.md), [Research Baseline Diff v1](../reference/schemas/baseline.diff.schema.v1.md)

- **Baseline Index** — `baseline.index.json` mapping runsets to discovered baseline metadata under a baseline root.
	*See also:* [Baseline Discovery Spec v1](../reference/contracts/v1/baseline_discovery_spec_v1.md), [Research Baseline Index v1](../reference/schemas/baseline.index.schema.v1.md)

- **Canon / Canonicalization** — Phase 0 process that normalizes raw input into deterministic canon outputs and validation artifacts.
	*See also:* [Canon Spec v1](../reference/contracts/v1/canon_spec_v1.md), [Stage 0 Canon](../reference/artifacts/stage0_canon.md)

- **CI Doctor** — Read-only integrity gate for baseline/runset promotion state that writes doctor summary artifacts.
	*See also:* [CI Doctor Spec v1](../reference/contracts/v1/ci_doctor_spec_v1.md), [Stage 1 Diagnostics](../reference/artifacts/stage1_diagnostics.md)

- **Contract** — Versioned spec page defining required behavior, output structure, and determinism rules.
	*See also:* [Contracts Reference](../reference/contracts/index.md)

- **Drift / Drift Report** — Deterministic classification of runset change versus baseline, written as drift report artifacts.
	*See also:* [Drift Report Spec v1](../reference/contracts/v1/drift_report_spec_v1.md), [Drift Artifacts](../reference/artifacts/drift.md)

- **Golden / Golden Fixture** — Approved expected output hashes in `tests/golden/*.sha256` used for regression checks.
	*See also:* [Update Goldens Safely](../how-to/update_goldens_safely.md), [Stale Goldens](../troubleshooting/stale_goldens.md)

- **Lineage** — Deterministic linkage between datasets and runs used by runset/risk workflows.
	*See also:* [Lineage Spec v1](../reference/contracts/v1/lineage_spec_v1.md), [Lineage Artifacts](../reference/artifacts/lineage.md)

- **Manifest** — Hash-oriented metadata proving deterministic inputs/outputs for an artifact-producing step.
	*See also:* [Manifest Spec v1](../reference/contracts/v1/manifest_spec_v1.md), [Stage 0 Canon](../reference/artifacts/stage0_canon.md)

- **Plan / `plan_sha256`** — A Plan is a deterministic task orchestration artifact; `plan_sha256` is the prune report confirmation token used for execute confirmation.
	*See also:* [Plan Spec v1](../reference/contracts/v1/plan_spec_v1.md), [Prune Spec v1](../reference/contracts/v1/prune_spec_v1.md)

- **Promotions (`baseline.promotions`)** — Label-to-runset baseline mapping in `baseline.promotions.json` with immutable remap rules.
	*See also:* [Baseline Discovery Spec v1](../reference/contracts/v1/baseline_discovery_spec_v1.md), [Research Baseline Promotions v1](../reference/schemas/baseline.promotions.schema.v1.md)

- **Prune Policy** — `policy.json` contract payload controlling prune protections, deletions, and safety guards.
	*See also:* [Prune Spec v1](../reference/contracts/v1/prune_spec_v1.md), [Research Prune Policy v1](../reference/schemas/prune.policy.schema.v1.md)

- **Run** — One materialized run with canon/psa/observe/risk outputs.
	*See also:* [Concepts Map](../getting-started/concepts-map.md), [Stage 0 Canon](../reference/artifacts/stage0_canon.md)

- **Run Directory** — A `<run_dir>` path that stores run-scoped artifacts such as manifests, logs, and stage outputs.
	*See also:* [Stage 0 Canon](../reference/artifacts/stage0_canon.md), [Phase 0 Gates v1](../reference/contracts/v1/phase0_gates_v1.md)

- **RunSet** — Deterministic, immutable grouping of datasets/runs for validation, risk, drift, and baseline workflows.
	*See also:* [RunSet Spec v1](../reference/contracts/v1/runset_spec_v1.md), [Research RunSet v1](../reference/schemas/runset.schema.v1.md)

- **Risk RunSet Summary** — Runset-level risk summary output written as `risk.runset.summary.json`.
	*See also:* [Risk Spec v1](../reference/contracts/v1/risk_spec_v1.md), [Risk Artifacts](../reference/artifacts/risk.md)

- **Risk Sweep** — Command path that computes runset risk outputs and writes baseline card/manifest artifacts.
	*See also:* [Baseline Card Spec v1](../reference/contracts/v1/baseline_card_spec_v1.md), [Baseline Promotion Tutorial](../tutorials/baseline_promotion.md)

- **Schema (v1)** — Versioned JSON schema reference page generated from `schemas/*schema*.json`.
	*See also:* [Schema Reference](../reference/schemas/index.md), [Add New Schema](../how-to/add_new_schema.md)

- **Stage (Stage0...Stage6)** — Named artifact boundary in the artifact catalog (`stage0_canon` through `stage6_observer`).
	*See also:* [Artifacts Reference](../reference/artifacts/index.md), [Add New Stage](../how-to/add_new_stage.md)

- **Verify Generated Docs Clean** — Docs drift guard command (`python tools/docs/verify_generated_docs_clean.py`) that regenerates refs and fails on generated-doc changes.
	*See also:* [Run CI Locally](../how-to/run_ci_locally.md), [Add New Artifact Catalog Entry](../how-to/add_new_artifact_catalog_entry.md)

# Research Platform Docs Hub

Research Core is a deterministic canonicalization and validation pipeline with
contracts-backed workflows and references. This docs hub organizes the wiki
around reproducible runs, deterministic artifacts, and contract-truth pages.
Use the sections below to start quickly, run operations, and extend safely.

## Start here

- [Quickstart](getting-started/quickstart.md) - Run the core canon + validation + registry flow.
- [ES5m End-to-End Tutorial](tutorials/es5m_end_to_end.md) - Walk the full ES5m pipeline and outputs.
- [Concepts Map](getting-started/concepts-map.md) - Learn core concepts and how artifacts relate.

## Search tips

- Try `baseline promotions` for promotion labels, baseline index, and promotion flows.
- Try `drift report` for `risk drift` outputs and dashboard-related docs.
- Try `verify_generated_docs_clean` for docs drift guard workflows.
- Try `prune policy` for prune safety rules and `plan_sha256` confirmation behavior.

## Run operations (tutorials)

- [Run vs Run Compare](tutorials/run_vs_run_compare.md) - Compare runsets via baseline diff workflows.
- [Risk Runset Analysis](tutorials/risk_runset_analysis.md) - Build/validate runsets and run risk runset analysis.
- [Drift Review Workflow](tutorials/drift_review_workflow.md) - Generate drift reports and dashboard summaries.
- [Baseline Promotion](tutorials/baseline_promotion.md) - Sweep, index, and promote baselines to `prod`.

## Reference (truth sources)

- [CLI Reference](reference/cli/index.md) - Generated command help pages.
- [Schema Reference](reference/schemas/index.md) - Generated schema pages from `schemas/*.json`.
- [Artifacts Reference](reference/artifacts/index.md) - Generated artifact catalog pages.
- [Contracts Reference](reference/contracts/index.md) - Vendored v1 contracts/specs.

## Extend the platform (how-to)

- [Add New CLI Command](how-to/add_new_cli_command.md)
- [Add New Schema](how-to/add_new_schema.md)
- [Add New Stage](how-to/add_new_stage.md)
- [Add New Artifact Writer](how-to/add_new_artifact_writer.md)
- [Add New Artifact Catalog Entry](how-to/add_new_artifact_catalog_entry.md)
- [Add New Test And Golden](how-to/add_new_test_and_golden.md)
- [Run CI Locally](how-to/run_ci_locally.md)
- [Prune Runs Safely](how-to/prune_runs_safely.md)

## When something breaks (troubleshooting)

- [Update Goldens Safely](how-to/update_goldens_safely.md)
- [Stale Goldens](troubleshooting/stale_goldens.md)
- [Determinism Failures](troubleshooting/determinism_failures.md)
- [Missing Artifacts](troubleshooting/missing_artifacts.md)

## Contributing / dev setup

- [Docs Style Guide](contributing/docs_style_guide.md)
- Bootstrap command:
	`powershell -ExecutionPolicy Bypass -File tools/dev/bootstrap.ps1`
- Enable hooks:
	`git config core.hooksPath .githooks`

## Docs are contracts-first

Generated refs stay in sync through `tools/docs` generators, the generated-docs
drift guard (`tools/docs/verify_generated_docs_clean.py`), and the pre-commit
hook.

# Repo Tour

Use this page as a quick map of where code, contracts, artifacts, and outputs live.

## Core folders

- `src/research_core/`
	Implementation for CLI commands and pipeline logic.
	See also: [CLI Reference](../reference/cli/index.md)

- `schemas/`
	JSON schema sources used for generated schema reference pages.
	See also: [Schema Reference](../reference/schemas/index.md)

- `docs/reference/contracts/v1/`
	Canonical v1 contract/spec pages.
	See also: [Contracts Reference](../reference/contracts/index.md)

- `docs/reference/artifacts/`
	Generated artifact catalog pages (from `catalog.v1.yml`).
	See also: [Artifacts Reference](../reference/artifacts/index.md)

- `tests/`
	Smoke, determinism, and golden regression test suites.
	See also: [Add New Test And Golden](../how-to/add_new_test_and_golden.md)

## Operational data folders

- `exec_outputs/`
	Runtime outputs from local/CI/tutorial runs.
	See also: [ES5m End-to-End Tutorial](../tutorials/es5m_end_to_end.md)

- `baselines/`
	Baseline roots used for index/promotions and drift comparison.
	See also: [Baseline Discovery Spec v1](../reference/contracts/v1/baseline_discovery_spec_v1.md)

- `configs/`
	Config inputs for analysis/pilot/CI flows.
	See also: [Pilot Cohort v1](../pilot_cohort_v1.md)

## Read in this order

1. [Quickstart](quickstart.md)
2. [Concepts Map](concepts-map.md)
3. [Artifacts Reference](../reference/artifacts/index.md)
4. [Contracts Reference](../reference/contracts/index.md)

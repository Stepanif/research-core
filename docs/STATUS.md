# Repository Status

## Summary
This repository contains a substantial implemented Python CLI and artifact pipeline under `src/research_core`, backed by schemas in `schemas/`, reference docs in `docs/`, and a large test suite in `tests/`. It is not just a four-command Phase 0 demo, but it is also not uniformly complete across every documented stage and reference surface.

## Implemented And Usable
- The CLI surface is implemented in [`src/research_core/cli.py`](../src/research_core/cli.py) with command groups for `canon`, `psa`, `validate`, `registry`, `observe`, `bundle`, `experiment`, `project`, `doctor`, `verify`, `plan`, `dataset`, `lineage`, `runset`, `risk`, `baseline`, `ci`, `release`, `prune`, and `pilot`.
- Core run processing is implemented:
  - Canonicalization and validation in [`src/research_core/canon`](../src/research_core/canon) and [`src/research_core/validate`](../src/research_core/validate).
  - PSA generation and PSA reporting in [`src/research_core/psa`](../src/research_core/psa).
  - Observe summary/profile generation in [`src/research_core/observe`](../src/research_core/observe).
- Catalog and lineage flows are implemented:
  - Dataset registration and validation in [`src/research_core/datasets`](../src/research_core/datasets).
  - Run lineage and dataset-to-runs indexing in [`src/research_core/lineage`](../src/research_core/lineage).
  - Registry/index views in [`src/research_core/registry`](../src/research_core/registry).
- Analysis/orchestration layers are implemented:
  - Experiment execution, batching, reporting, and promotions in [`src/research_core/experiments`](../src/research_core/experiments).
  - Project run/materialize/report/index/promotions in [`src/research_core/projects`](../src/research_core/projects).
  - Runset creation, validation, and materialization in [`src/research_core/runsets`](../src/research_core/runsets).
  - Plan build/execute in [`src/research_core/plan`](../src/research_core/plan).
- Risk/baseline/drift workflows are implemented in [`src/research_core/risk`](../src/research_core/risk) and [`src/research_core/baselines`](../src/research_core/baselines).
- CI, CI doctor, and pilot orchestration are implemented in [`src/research_core/ci`](../src/research_core/ci), [`src/research_core/ci_doctor`](../src/research_core/ci_doctor), and [`src/research_core/pilot`](../src/research_core/pilot).
- Operational support tooling is implemented for bundle export/verify, doctor checks, prune, and release drafting in [`src/research_core/bundle`](../src/research_core/bundle), [`src/research_core/doctor`](../src/research_core/doctor), [`src/research_core/prune`](../src/research_core/prune), and [`src/research_core/release`](../src/research_core/release).
- Usability is supported by broad automated coverage. `tests/` contains smoke, determinism, fail-loud, and golden-regression tests across canon, PSA, observe, dataset, lineage, experiment, runset, risk, project, plan, CI, pilot, bundle, prune, and release domains.
- CI automation exists in [`.github/workflows/research-ci.yml`](../.github/workflows/research-ci.yml) and docs generation/build automation exists in [`.github/workflows/docs.yml`](../.github/workflows/docs.yml).

## Scaffolded / Partial
- The front-door repository framing is narrower than the implemented code surface. [`README.md`](../README.md) still presents the repo as a Phase 0 canonicalization pipeline and shows only canon/validate/registry examples.
- Generated CLI reference coverage is partial. [`tools/docs/gen_cli_ref.py`](../tools/docs/gen_cli_ref.py) currently generates pages for overview, canon, risk, `risk run`, and `risk runset`, while the actual CLI surface in [`src/research_core/cli.py`](../src/research_core/cli.py) is much larger.
- Artifact reference coverage is partial. [`docs/reference/artifacts/catalog.v1.yml`](reference/artifacts/catalog.v1.yml) still contains multiple `TODO` schema/type placeholders, and several generated artifact pages expose those unresolved placeholders directly.
- Some implemented flows are intentionally constrained:
  - [`src/research_core/projects/materialize.py`](../src/research_core/projects/materialize.py) supports only `raw_vendor_v1` datasets and requires exactly one source file per dataset.
  - [`src/research_core/runsets/materialize.py`](../src/research_core/runsets/materialize.py) falls back to a temporary generated project spec with fixed defaults when auto-materialization is needed.
- `analysis_v1` is not a usable source package in its current state. [`src/research_core/analysis_v1`](../src/research_core/analysis_v1) contains only `__pycache__` files and no `.py` source files.

## Planned / Future
- Placeholder stage docs exist for:
  - [`docs/reference/artifacts/stage2_occupancy.md`](reference/artifacts/stage2_occupancy.md)
  - [`docs/reference/artifacts/stage3_streams.md`](reference/artifacts/stage3_streams.md)
  - [`docs/reference/artifacts/stage4_corridors.md`](reference/artifacts/stage4_corridors.md)
  - [`docs/reference/artifacts/stage5_flow_harness.md`](reference/artifacts/stage5_flow_harness.md)
  - [`docs/reference/artifacts/stage6_observer.md`](reference/artifacts/stage6_observer.md)
- Those pages do not define confirmed commands or outputs yet; the catalog source marks them as TODO in [`docs/reference/artifacts/catalog.v1.yml`](reference/artifacts/catalog.v1.yml).
- Some contract/reference organization decisions are still open. [`docs/reference/contracts/index.md`](reference/contracts/index.md) explicitly includes a TODO about whether `pilot_cohort_v1.md` should be treated as a formal contract source.

## What This Repo Is Not
- It is not a hosted service, web application, or networked control plane. The implemented runtime is a local CLI and filesystem pipeline.
- It is not limited to the four commands shown in [`README.md`](../README.md); the actual implemented surface is larger.
- It is not a uniformly complete multi-stage platform where every documented stage has confirmed commands and artifact definitions. Stage 2 through Stage 6 reference pages are still placeholder-driven.
- It is not a repo where every reference page is fully generated and fully complete. CLI reference coverage is partial, and artifact/schema references still expose unresolved TODOs in some places.
- It is not a universal hash-addressed storage system. Outputs are ordinary files written by explicit module writers, with canonical hashes and self-hash fields used where the relevant writer or manifest format defines them.
- It is not evidence that every conceptual package in `src/research_core` is currently usable as source. `analysis_v1` is present only as bytecode cache and should not be treated as a supported source module without follow-up cleanup.

## Practical Read
- If you need usable code today, the implemented CLI modules and their tests are the reliable ground truth.
- If you need complete public-facing documentation for every command/stage, the repo is not there yet.
- If you need a conservative repo description, “deterministic local CLI pipeline with implemented canon/PSA/observe/runset/risk/project/CI/pilot workflows, plus partial docs/reference coverage” matches the visible tree better than “Phase 0 only” or “fully complete research platform”.

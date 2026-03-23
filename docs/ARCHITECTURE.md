# Research Core Architecture

## 1. Overview
Research Core is a local, deterministic artifact pipeline implemented in Python under `src/research_core` and exposed through a Typer CLI in `src/research_core/cli.py`. The repo also includes contract/spec docs (`docs/reference/contracts/v1`), JSON schema sources (`schemas/*.json`), generated reference docs (`docs/reference/*`), and an extensive test suite (`tests/test_*.py`).

### Implemented now
- A multi-command CLI surface is wired in `src/research_core/cli.py` (command groups include `canon`, `psa`, `observe`, `experiment`, `project`, `runset`, `risk`, `baseline`, `ci`, `pilot`, `plan`, `prune`, `release`, `dataset`, `lineage`, `registry`, `doctor`, `verify`, `validate`).
- End-to-end run processing, cataloging, risk analysis, drift/dashboard, CI summaries, and pilot orchestration are implemented under `src/research_core/*` modules.
- Determinism, smoke, fail-loud, and golden-regression coverage exists across domains in `tests/` (for example `test_risk_*`, `test_project_*`, `test_plan_*`, `test_runset_*`, `test_ci_*`).

### Scaffolded / partial
- CLI docs generation currently includes only a subset of commands (`tools/docs/gen_cli_ref.py` `COMMANDS` list currently generates overview/canon/risk pages).
- Artifact catalog entries include multiple unresolved schema/type placeholders (`docs/reference/artifacts/catalog.v1.yml` contains many `TODO` values).
- `project materialize` is intentionally constrained in v1 to `raw_vendor_v1` datasets with exactly one source file (`src/research_core/projects/materialize.py`).
- `runset materialize` auto-materialization uses a temporary project spec with fixed defaults (for example fixed instrument/tf/schema paths and fixture spec dir) in `_build_temp_project_spec` (`src/research_core/runsets/materialize.py`).
- `src/research_core/analysis_v1` contains only `__pycache__` files and no `.py` sources. TODO: confirm whether this package is intentionally removed or should be restored/cleaned.

### Planned / future
- Stage placeholders are present but unresolved for `stage2_occupancy`, `stage3_streams`, `stage4_corridors`, `stage5_flow_harness`, and `stage6_observer` (`docs/reference/artifacts/stage*.md` and `docs/reference/artifacts/catalog.v1.yml`).
- TODO markers also exist for contract/doc organization details (for example `docs/reference/contracts/index.md` includes a TODO for `pilot_cohort_v1.md` naming).

## 2. Design Goals
Design goals are visible in module behavior, docs, and tests:

- Deterministic outputs and IDs.
  - Canonical JSON serialization helpers are reused across modules (`runsets/io.py`, `datasets/io.py`, `projects/contracts.py`, `plan/io.py`).
  - Canonical/self-hash fields are written and checked in many artifacts (for example `risk_summary_canonical_sha256`, `runset_entry_canonical_sha256`, `baseline_card_manifest_canonical_sha256`, `ci_manifest_canonical_sha256`).
  - Hash-derived IDs are used for core entities (dataset IDs in `datasets/catalog.py`, runset IDs in `runsets/ids.py`, experiment IDs in `experiments/ids.py`, project IDs in `projects/runner.py` and `projects/materialize.py`).

- Fail loud on integrity violations.
  - Validation errors are raised for missing/invalid artifacts and mismatched hashes across run, catalog, risk, drift, bundle, and doctor modules.
  - Immutability checks are explicit in index/entry writers (dataset/runset/project/experiment/baseline/promotion flows).

- Contract-first, artifact-first operation.
  - Contract/spec pages live under `docs/reference/contracts/v1`.
  - Artifact catalog source is `docs/reference/artifacts/catalog.v1.yml` and generated pages are produced by `tools/docs/gen_artifact_catalog.py`.
  - Schema pages are generated from `schemas/*.json` by `tools/docs/gen_schema_ref.py`.

- Reproducible operational workflows.
  - CI sets deterministic metadata (`RESEARCH_CREATED_UTC`, `RESEARCH_GIT_COMMIT`) in `.github/workflows/research-ci.yml`.
  - Many operations require `RESEARCH_CREATED_UTC` and fail if missing (for example in `risk`, `runsets`, `datasets`, `ci`, `ci_doctor`, `pilot`, `plan`, `project` modules).

## 3. Major Modules And Responsibilities
The main responsibilities are split by package under `src/research_core`:

- `canon`, `validate`:
  - Raw input parsing, canonicalization, session policy filtering, parquet writing, and canon invariant checks.
  - Key files: `canon/normalize.py`, `canon/writer.py`, `canon/manifest.py`, `validate/canon_checks.py`, `validate/invariants.py`.

- `psa`, `observe`:
  - PSA state/event derivation, PSA/report artifacts, and observe summary/profile artifacts plus manifests.
  - Key files: `psa/engine.py`, `psa/writer.py`, `psa/report.py`, `observe/summarize.py`, `observe/profile.py`, `observe/writer.py`.

- `datasets`, `lineage`, `registry`:
  - Dataset registration/validation/indexing, lineage building, dataset-to-runs links, and run registry/index views.
  - Key files: `datasets/catalog.py`, `lineage/build_lineage.py`, `lineage/writer.py`, `registry/observe_registry.py`, `registry/run_index.py`, `registry/dataset_registry.py`.

- `experiments`, `projects`, `runsets`, `plan`:
  - Experiment execution/reporting, project run/materialize/report/index/promotions, runset creation/validation/materialization, and parallel batch plan build/execute.
  - Key files: `experiments/runner.py`, `experiments/batch.py`, `projects/runner.py`, `projects/materialize.py`, `runsets/catalog.py`, `runsets/validate.py`, `runsets/materialize.py`, `plan/build.py`, `plan/execute.py`.

- `risk`, `baselines`:
  - Per-run risk, runset risk aggregation, sweep/baseline card generation, baseline diff, drift reports, dashboard summaries, baseline index/promotions/resolve.
  - Key files: `risk/writer.py`, `risk/runset_agg.py`, `risk/sweep.py`, `risk/diff_writer.py`, `risk/drift_writer.py`, `risk/dashboard_writer.py`, `baselines/index.py`, `baselines/promotions.py`, `baselines/resolve.py`.

- `ci`, `ci_doctor`, `pilot`:
  - CI drift/checksum gate artifacts, doctor integrity checks, and pilot orchestration that wires explicit runset generation + sweep + drift + doctor.
  - Key files: `ci/runner.py`, `ci/writer.py`, `ci_doctor/checks.py`, `ci_doctor/runner.py`, `pilot/runner.py`, `pilot/explicit.py`, `pilot/writer.py`.

- `doctor`, `bundle`, `prune`, `release`:
  - Artifact verification helpers, deterministic run bundle export/verify, guarded prune planning/execution, and git-based release helpers.
  - Key files: `doctor/run_doctor.py`, `doctor/project_doctor.py`, `bundle/exporter.py`, `prune/planner.py`, `prune/guards.py`, `release/notes.py`, `release/url.py`, `release/draft.py`.

## 4. Artifact Model
Artifacts are file-based outputs written by explicit module writers. Many artifacts also carry canonical hashes or self-hash fields, but the repo does not use a universal hash-path addressing scheme.

- Run-scoped artifacts:
  - Canon: `canon.parquet`, `canon.contract.json`, `canon.manifest.json`, `logs/canon.log`.
  - PSA: `psa.parquet`, `psa.log`, `psa.manifest.json`, optional `psa.report.json` + manifest.
  - Observe: `observe/observe.summary.json`, `observe/observe.profile.json` with per-artifact manifests.
  - Risk (per run): `risk/risk.summary.json` + manifest.
  - Experiments: `experiments/<exp_id>/transition_matrix.json`, `exp.manifest.json`, plus batch/report/index/promotions files.
  - Lineage: `lineage/lineage.json`, `lineage/lineage.manifest.json`.

- Catalog/index artifacts:
  - Dataset catalog: `datasets.index.json` + immutable `entries/<dataset_id>.json`.
  - Runset catalog: `runsets/runsets.index.json` + immutable `runsets/entries/<runset_id>.json`.
  - Dataset-to-runs linkage: `links/dataset_to_runs.index.json`.
  - Project index/promotions: `projects.index.json`, `projects.promotions.json`.
  - Baseline index/promotions: `baseline.index.json`, `baseline.promotions.json`.

- Comparison/report artifacts:
  - Runset risk: `<out>/<runset_id>/risk.runset.summary.json` + manifest.
  - Baseline card: `<out>/<runset_id>/baseline.card.json` + manifest.
  - Baseline diff: `<out>/baseline.diff.json` + manifest.
  - Drift report: `<out>/drift/<runset_id>/drift.report.json` + manifest.
  - Dashboard: `<out>/dashboard.summary.json` + manifest.
  - Some orchestration/report summaries also have paired manifest files, including CI, CI doctor, and pilot summary outputs.

- Determinism conventions:
  - Canonical JSON bytes are serialized with sorted keys and compact separators in many modules.
  - Many payloads carry self-hash fields (for example `*_canonical_sha256`) verified during read/check paths.
  - Parquet table truth hashes are recorded as `canonical_table_sha256`.

## 5. Execution Model
Execution is CLI-driven and file-system based.

- Core run pipeline:
  - `canon` creates canonical run artifacts.
  - `psa` consumes `canon.parquet` and writes PSA artifacts.
  - `observe summary` and `observe profile` consume canon+psa artifacts.
  - `registry refresh` and `lineage build` update run/cross-run indexes.

- Analysis and baseline pipeline:
  - `runset create/validate/materialize` manages runset selections.
  - `risk run` computes per-run metrics.
  - `risk runset` aggregates selected runs.
  - `risk sweep` derives baseline cards from runset risk.
  - `baseline index refresh/promote/resolve` governs baseline references.
  - `risk drift` compares current vs promoted baseline.
  - `risk dashboard` runs drift across runset lists and aggregates status.

- Orchestration layers:
  - `project materialize` can invoke canon/psa/observe/registry/lineage via subprocess for dataset-mode project specs.
  - `project run/report` orchestrates experiment batches and project summary/report manifests.
  - `plan build` emits deterministic task plans; `plan execute` runs tasks with thread pool parallelism, preflight checks, and stable logs.
  - `ci run` orchestrates baseline index refresh + risk dashboard + CI summary decision logic.
  - `ci doctor` performs integrity checks over baselines/promotions/runsets/bundles/dashboard depending on config flags.
  - `pilot run` orchestrates explicit runset generation from lineage index, baseline resolution, drift, and doctor checks.

## 6. Current System Boundary
Current boundaries visible in code/config/docs:

- Local filesystem boundary:
  - Core processing reads/writes local files and directories.
  - No service/database/network integration exists in runtime pipeline modules.

- Input boundary:
  - Canon raw parser expects tabular raw files with `Date`, `Time`, `Open`, `High`, `Low`, `Close`, `Up`, `Down` columns.
  - Canon timestamps are localized to `America/New_York`; canon dataset kind `canon_v1` enforces `tz=America/New_York`.

- Determinism boundary:
  - Many mutating commands require `RESEARCH_CREATED_UTC`.
  - Immutability checks prevent conflicting rewrites for key catalog/index/promotion artifacts.

- Risk scope boundary:
  - Risk metrics are derived from PSA dynamics only (`state_id`, `event_mask`) and fixed v1 weights/thresholds in `risk/contracts.py`.
  - PnL/execution modeling is not implemented in risk modules.

- Materialization boundary:
  - `project materialize` currently supports only `raw_vendor_v1` datasets and one source file per dataset.
  - `runset materialize` auto-materialization path is constrained by hard-coded temporary project defaults (see section 1 scaffolded/partial).

- Documentation boundary:
  - CLI/schema/artifact references are generator-driven (`tools/docs/*`), but CLI docs generation currently covers only a subset of commands.

## 7. Future Extension Points
Extension hooks already present in repo:

- Add/extend CLI commands in `src/research_core/cli.py`; update generated CLI docs via `tools/docs/gen_cli_ref.py`.
- Add/extend schemas in `schemas/`; regenerate schema docs via `tools/docs/gen_schema_ref.py`.
- Add/extend artifact stages/outputs in `docs/reference/artifacts/catalog.v1.yml`; regenerate pages via `tools/docs/gen_artifact_catalog.py`.
- Add new writers/manifests using existing canonical JSON + self-hash patterns (`risk/writer.py`, `ci/writer.py`, `observe/writer.py` are concrete patterns).
- Add orchestration gates/configs through `ci`, `ci_doctor`, `pilot`, `plan`, and `project` spec/config schemas.

Planned/future placeholders explicitly visible:

- TODO: define commands and artifact outputs for stage2-stage6 placeholder stages (`stage2_occupancy` to `stage6_observer` in artifact catalog/docs).
- TODO: resolve schema/type TODO markers in artifact catalog entries.
- TODO: decide final handling of `analysis_v1` (source absent; only bytecode cache present).

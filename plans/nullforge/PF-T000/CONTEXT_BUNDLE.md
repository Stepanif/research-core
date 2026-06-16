# PF-T000 Context Bundle

Pack name: NullForge M0 PF-T000 context bundle
Ticket: PF-T000 - Repo inventory and NullForge import plan
Milestone: M0 - Repo Source Import + Canonical Baseline
Created by: Context Curator pass only

## Curator Boundary

This bundle is context only. It does not plan implementation, import NullForge volumes, edit ResearchCore Engine docs, modify code, install dependencies, or run downstream PF-T001+ work.

## Repo State

- Repo root: `<repo-root>`
- Git repo exists: YES
- Clean before branch creation: YES (`git status --porcelain=v1` returned no files)
- Starting branch: `main`
- Ticket branch created/used: `docs/PF-T000-nullforge-import-plan`
- Branch existed before this pass: NO local branch found; NO remote branch found
- Current scoped output path: `plans/nullforge/PF-T000/`

## Incoming Package Discovery

- Incoming root: `<nullforge-incoming-root>`
- M0 package zip found: `<nullforge-incoming-root>\packages\NullForge_M0_Repo_Source_Import_v0_4_Package.zip`
- M0 package root used: `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package`
- Required M0 files found: YES
- Setup/volume package inputs are present as zips under `<nullforge-incoming-root>\packages` and remain outside the repo.

Setup/volume draft package paths:

- `<nullforge-incoming-root>\packages\NullForge_Setup_Package_v0_4.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_00_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_01_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_02_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_03_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_04_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_05_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_06_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_07_v0_4_Package.zip`

## Ticket Summary

PF-T000 is a docs/source-of-truth ticket. Its purpose is to inventory the existing `research-core` repo documentation and create a non-destructive import plan for NullForge planning sources. It may inspect repo docs, status files, README, architecture docs, prompts, and folder structure. It must not import generated volumes or rewrite engine docs.

Ticket outputs planned for the later Planner/Implementor loop:

- `docs/nullforge/import/PF-T000_REPO_INVENTORY.md`
- `docs/nullforge/import/PF-T000_IMPORT_PLAN.md`
- `docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md`
- `reports/nullforge/PF-T000/IMPLEMENTATION_REPORT.md`
- `audits/nullforge/PF-T000/AUDIT_REPORT.md`

This curator pass creates only:

- `plans/nullforge/PF-T000/CONTEXT_BUNDLE.md`
- `plans/nullforge/PF-T000/CONTEXT_BUNDLE_MANIFEST.md`

## Mission Slice

NullForge is a Windows-first local desktop research workbench for a solo research builder. It is intended to import market datasets, map lawful dataset capabilities, compile or generate candidate logic into auditable test specs, run the local ResearchCore Engine, inspect visual trade replays, and decide whether evidence should be promoted, repaired, archived, or quarantined.

## Active Source Docs

M0 package docs inspected:

- `prompts/nullforge/PF-T000/00_CONTEXT_CURATOR_PROMPT.md`
- `prompts/nullforge/PF-T000/01_PLANNER_PROMPT.md` (path verified only; not executed)
- `tickets/nullforge/PF-T000-repo-inventory-and-nullforge-import-plan.md`
- `milestones/nullforge/M0-repo-source-import/MILESTONE_BRIEF.md`
- `milestones/nullforge/M0-repo-source-import/TICKET_QUEUE.md`
- `milestones/nullforge/M0-repo-source-import/DEPENDENCY_MAP.md`
- `milestones/nullforge/M0-repo-source-import/CONTEXT_REFRESH_RULES.md`
- `milestones/nullforge/M0-repo-source-import/HUMAN_GATE_TRIGGERS.md`
- `milestones/nullforge/M0-repo-source-import/MILESTONE_ACCEPTANCE.md`

Repo docs/config inspected:

- `README.md`
- `docs/index.md`
- `docs/STATUS.md`
- `docs/ARCHITECTURE.md`
- `docs/getting-started/repo-tour.md`
- `docs/how-to/run_ci_locally.md`
- `docs/contributing/docs_style_guide.md`
- `docs/README_ANALYSIS_ES5M.md`
- `docs/dataset_catalog_spec_v1.md`
- `pyproject.toml`

## Dependency Status

PF-T000 has no prior ticket dependency. M0 is serial by doctrine: PF-T000 -> PF-T001 -> PF-T002 -> ADR-T001 -> ADR-T002 -> CX-T001 -> MB-T001. Do not parallelize downstream M0 tickets by default, because path and authority decisions compound.

## Relevant Existing Repo Files And Folders

Observed repo truth:

- `README.md` frames ResearchCore as a validation-first research lab and local artifact pipeline.
- `docs/STATUS.md` is an important current-state truth source. It says the repo has substantial implemented Python CLI/artifact pipeline code and broad tests, but also partial generated reference coverage and placeholders.
- `docs/ARCHITECTURE.md` describes the local Python CLI under `src/research_core`, Typer CLI surface, local filesystem boundary, deterministic artifacts, and current partial/scaffolded areas.
- `docs/index.md` is the docs hub for Research Core and points to generated references and tutorials.
- `docs/getting-started/repo-tour.md` maps core folders: `src/research_core/`, `schemas/`, `docs/reference/contracts/v1/`, `docs/reference/artifacts/`, `tests/`, `exec_outputs/`, `baselines/`, and `configs/`.
- `docs/contributing/docs_style_guide.md` requires repository-truth-only docs, generated/copy-from-source references, TODO markers for unknowns, and no guessed flags/paths/schema keys.
- `docs/README_ANALYSIS_ES5M.md` documents ES5m local analysis flows and says generated local pipeline artifacts go under `configs/analysis/local/` and remain ignored/stable.
- `docs/dataset_catalog_spec_v1.md` documents immutable dataset catalog entries and deterministic raw/canon registration.
- `pyproject.toml` identifies package name `research-core`, Python `>=3.11`, runtime dependencies (`pandas`, `pyarrow`, `typer`), dev extra (`pytest`), and pytest testpaths.

Observed proposed NullForge paths before this pass:

- `docs/nullforge`: absent
- `docs/nullforge/import`: absent
- `milestones/nullforge`: absent
- `tickets/nullforge`: absent
- `prompts/nullforge`: absent
- `plans/nullforge`: absent before creating this bundle path
- `reports/nullforge`: absent
- `audits/nullforge`: absent

## Source-Of-Truth Notes

- ResearchCore repo docs and implemented code are authoritative for the existing engine/repo state.
- Extracted M0 package docs are active instructions for M0 ticket execution.
- Generated setup/volume packages are draft/design inputs until reviewed, imported, and audited through M0.
- Chat output and old prompts are not source truth unless promoted through the M0 process.
- NullForge product truth must remain separate from ResearchCore Engine truth until imported under explicit docs/source-of-truth paths.

Potential non-blocking tension to preserve for the planner:

- `README.md` and `pyproject.toml` still use narrower or older ResearchCore framing in places, while `docs/STATUS.md` and `docs/ARCHITECTURE.md` describe a broader implemented CLI/artifact pipeline. PF-T000 should not rewrite these files, but the import plan should avoid creating contradictory active status language.
- Existing docs use both `ResearchCore` and `Research Core`. NullForge imports should preserve current engine naming unless a later ADR/human gate changes naming.

## Constraints And Forbidden Actions

Do not:

- Generate implementation code.
- Scaffold Tauri or any desktop app.
- Install dependencies.
- Modify `src/`, `tests/`, package files, CI, `pyproject.toml`, or engine internals.
- Import generated NullForge volumes in this pass.
- Rewrite or move existing ResearchCore Engine docs.
- Commit full `ES.zip`, raw/private data, or unsafe fixtures.
- Rename repo/package/app identity.
- Start M1 or PF-T001+.
- Run Planner, Implementor, or Auditor in this curator pass.
- Create broad build prompts.
- Mark generated volumes canonical before PF-T001 audit.

Allowed in this pass:

- Create PF-T000 context-curation artifacts under `plans/nullforge/PF-T000/`.
- Extract the required M0 package into incoming `01_extracts`, outside the repo.
- Record package paths and repo context for the next Planner prompt.

## Required Checks And Tests

PF-T000 ticket requires:

- `git status before and after`
- directory/file existence check for proposed target paths
- manual review that changed files are docs/plans only

Known repo verification commands discovered, but not run by this curator pass:

- `python tools/docs/gen_cli_ref.py`
- `python tools/docs/gen_schema_ref.py`
- `python tools/docs/gen_artifact_catalog.py`
- `python tools/docs/verify_generated_docs_clean.py`
- `python -m pytest -q`
- `python -m research_core.cli ci run --config .github/ci/ci.github.json` with required `RESEARCH_CREATED_UTC` and `RESEARCH_GIT_COMMIT`
- `python -m mkdocs build` after docs dependencies are available

Do not install dependencies during this curator pass.

## Human Gate Triggers

Stop before any action that would:

- overwrite, move, or rename existing ResearchCore Engine docs;
- change root README beyond a clearly scoped later link/summary;
- rename repo/package/CLI/public project identity;
- add dependencies, code, scripts, parsers, sidecar binaries, packaging configs, or CI/test behavior;
- commit full `ES.zip`, ES-derived fixtures without license/safety decision, or raw/private/local data;
- mark generated volumes canonical before PF-T001 audit;
- broaden into public release, legal/trademark naming, AI strategy activation, broker/live-trading, financial advice, auth, billing, cloud sync, marketplace, or mobile scope.

Human gates triggered in this curator pass: NONE.

## Required Outputs For Next Role

Next prompt to run after user confirmation:

`<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\prompts\nullforge\PF-T000\01_PLANNER_PROMPT.md`

The Planner should consume this bundle and produce planning artifacts only. It should not code, import volumes, or run implementation.

## Open Questions

- Should PF-T000 keep the M0 target layout from the milestone brief exactly, or adjust it after inventory if a safer non-conflicting location is found?
- Should any later root README change be limited to a link/summary, and does that require an explicit human gate?
- How should PF-T000 classify setup package docs versus volume docs when both are still draft inputs outside the repo?
- What license/safety decision is required before any ES-derived fixture can be committed later?
- Should existing ResearchCore status wording be left unchanged and cross-linked from NullForge docs, or should later docs propose a separate NullForge status without touching engine status?

## Ready For Planner

YES, subject to user confirmation and continued scope discipline.

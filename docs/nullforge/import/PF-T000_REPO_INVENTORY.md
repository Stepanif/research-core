# PF-T000 Repo Inventory

Ticket: PF-T000 - Repo inventory and NullForge import plan
Milestone: M0 - Repo Source Import + Canonical Baseline
Branch observed: `docs/PF-T000-nullforge-import-plan`
Repo root: `C:\Users\Filip\Desktop\Repos\research-core`

## Source Context

Repo-local PF-T000 context used:

- `plans/nullforge/PF-T000/CONTEXT_BUNDLE.md`
- `plans/nullforge/PF-T000/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/PF-T000/PLAN.md`
- `plans/nullforge/PF-T000/ACCEPTANCE.md`
- `plans/nullforge/PF-T000/IMPLEMENTOR_PROMPT.md`

Active incoming ticket source used:

- `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T000-repo-inventory-and-nullforge-import-plan.md`

The in-repo ticket path requested by the role prompt was checked and was absent during implementation:

- `tickets/nullforge/PF-T000-repo-inventory-and-nullforge-import-plan.md`

## Current ResearchCore Repo Truth

ResearchCore is the existing engine/repo. Its current truth remains the tracked repo docs and implemented code, not the generated NullForge planning packages.

Observed current-state summary:

- `README.md` frames ResearchCore as a validation-first research lab for pushing candidate logic through canonical data, artifact generation, validation, analysis, comparison, and downstream research workflows.
- `docs/index.md` is the current docs hub for Research Core. It organizes quickstart, tutorials, generated references, how-to pages, troubleshooting, and contributing setup.
- `docs/STATUS.md` is the clearest current-state summary. It says the repo has a substantial implemented Python CLI and artifact pipeline, broad tests, and partial generated reference coverage.
- `docs/ARCHITECTURE.md` describes a local deterministic Python artifact pipeline exposed through a Typer CLI under `src/research_core/cli.py`.
- `docs/getting-started/repo-tour.md` maps core code, schema, contract, artifact, test, output, baseline, and config folders.
- `docs/how-to/run_ci_locally.md` records the local CI/docs verification commands and notes dependency-installing setup commands.
- `docs/contributing/docs_style_guide.md` requires repo-truth-only docs, generated or copied reference pages, TODO markers for unknowns, and no guessed flags, paths, schema keys, or behaviors.
- `docs/README_ANALYSIS_ES5M.md` documents the ES5m local analysis flow and says generated local pipeline artifacts are written under `configs/analysis/local/`, which is ignored by git.
- `docs/dataset_catalog_spec_v1.md` documents deterministic immutable dataset catalog entries and local file-based registration.
- `pyproject.toml` identifies package name `research-core`, Python `>=3.11`, runtime dependencies `pandas`, `pyarrow`, `typer`, and dev dependency `pytest`.

## Existing Docs And Configs Likely To Host Or Conflict

| Path | Current role | PF-T000 read |
|---|---|---|
| `README.md` | Public/front-door project framing | Potential host for a future scoped link only; any root README change is a human gate. |
| `docs/index.md` | Docs hub/navigation | Potential future link host only after NullForge docs are imported and audited; not changed by PF-T000. |
| `docs/STATUS.md` | Current ResearchCore repo status truth | Must remain ResearchCore Engine truth; NullForge status should be separate. |
| `docs/ARCHITECTURE.md` | Current ResearchCore architecture truth | Must not be overwritten by NullForge desktop/product architecture. |
| `docs/getting-started/repo-tour.md` | Repo folder map | Useful context for future target paths; not a NullForge source doc. |
| `docs/how-to/run_ci_locally.md` | Verification commands | Useful for check planning; dependency installation remains out of PF-T000 scope. |
| `docs/contributing/docs_style_guide.md` | Docs truth/governance rules | Governs NullForge docs: use TODO for unknowns and avoid guessed details. |
| `docs/README_ANALYSIS_ES5M.md` | ES5m analysis workflow | Important data boundary; generated/local artifacts stay ignored and raw data must not enter repo. |
| `docs/dataset_catalog_spec_v1.md` | Dataset registration contract | Useful for later dataset-capability planning, but PF-T000 does not create data artifacts. |
| `pyproject.toml` | Package metadata and dependencies | Must not be changed by PF-T000. |

## Existing Or Absent NullForge Paths

Preflight checks during implementation found:

| Path | Exists before PF-T000 implementation? | Notes |
|---|---:|---|
| `docs/nullforge/` | No | Created only as needed to hold PF-T000 import docs. |
| `docs/nullforge/import/` | No | Created for PF-T000 import planning outputs. |
| `docs/nullforge/blueprint/volumes/` | No | Future PF-T001 target; not created by PF-T000. |
| `docs/nullforge/adr/` | No | Future ADR target; not created by PF-T000. |
| `docs/nullforge/codex/` | No | Future CX-T001 target; not created by PF-T000. |
| `milestones/nullforge/` | No | Future milestone handoff target; not created by PF-T000. |
| `tickets/nullforge/` | No | Future imported ticket target; not created by PF-T000. |
| `prompts/nullforge/` | No | Future imported prompt target; not created by PF-T000. |
| `plans/nullforge/` | Yes | Created by the PF-T000 context/planner passes. |
| `reports/nullforge/` | No | Created for PF-T000 implementation reports. |
| `audits/nullforge/` | No | Future auditor target; not created by PF-T000 implementor. |

## Confirmed Non-Conflicts

- No existing `docs/nullforge/` subtree was present before PF-T000 implementation.
- No existing `milestones/nullforge/`, `tickets/nullforge/`, `prompts/nullforge/`, `reports/nullforge/`, or `audits/nullforge/` subtree was present before PF-T000 implementation.
- PF-T000 can keep NullForge product/source-import material separated from ResearchCore Engine docs by using `docs/nullforge/` and related NullForge-only roots.

## Source-Of-Truth Separation

ResearchCore Engine truth:

- Existing tracked ResearchCore docs.
- Existing `src/research_core` implementation.
- Existing schemas, generated references, tests, and CI/docs workflows.

NullForge M0 execution truth:

- Extracted M0 package docs while they remain outside the repo.
- PF-T000 context, planner, implementation, and later audit artifacts.
- Future imported NullForge docs only after their owning ticket imports them and audit accepts them.

Draft/design memory only:

- NullForge setup and volume zip packages.
- Generated volumes before PF-T001 import and audit.
- Old chat or stale prompts unless explicitly promoted through M0.

## Inventory Conclusion

The current repo has no path collision with the proposed separated NullForge docs layout. PF-T000 should preserve the M0 target layout, keep NullForge status and product decisions under `docs/nullforge/`, and avoid changing ResearchCore Engine docs or package identity.

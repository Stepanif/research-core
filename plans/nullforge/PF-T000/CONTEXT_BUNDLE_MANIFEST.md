# PF-T000 Context Bundle Manifest

Pack name: NullForge M0 PF-T000 context bundle
Ticket: PF-T000 - Repo inventory and NullForge import plan
Purpose: Provide the smallest sufficient active context for the PF-T000 Planner without planning implementation or importing NullForge source docs.

## Included Files

| File | Truth status | Why included |
|---|---|---|
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\prompts\nullforge\PF-T000\00_CONTEXT_CURATOR_PROMPT.md` | Active M0 role prompt for this pass | Defines curator boundaries and required context bundle outputs. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\prompts\nullforge\PF-T000\01_PLANNER_PROMPT.md` | Next role prompt, verified only | Provides exact next prompt path; not executed in this pass. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T000-repo-inventory-and-nullforge-import-plan.md` | Active ticket source | Defines ticket purpose, scope, outputs, forbidden actions, checks, gates, and closeout requirements. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\MILESTONE_BRIEF.md` | Active milestone source | Defines M0 goal, doctrine, target layout, non-goals, and success definition. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\TICKET_QUEUE.md` | Active milestone queue | Defines required serial ticket order and stop conditions. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\DEPENDENCY_MAP.md` | Active dependency source | Confirms PF-T000 has no prior dependency and downstream ticket order must be serial. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\CONTEXT_REFRESH_RULES.md` | Active context policy | Defines refresh triggers and bundle include/exclude policy. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\HUMAN_GATE_TRIGGERS.md` | Active gate policy | Defines source-of-truth, technical, data, and product/legal human gates. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\MILESTONE_ACCEPTANCE.md` | Active milestone acceptance source | Defines M0 completion criteria and audit decision boundaries. |
| `<repo-root>\README.md` | Existing repo truth for public/project framing | Establishes ResearchCore identity, validation standard, repo structure, and typical verification commands. |
| `<repo-root>\docs\index.md` | Existing docs hub | Shows current docs organization and generated reference surfaces. |
| `<repo-root>\docs\STATUS.md` | Existing current-state truth source | Captures implemented/partial/planned repo status and non-goals. |
| `<repo-root>\docs\ARCHITECTURE.md` | Existing architecture truth source | Defines current local Python CLI/artifact architecture and extension boundaries. |
| `<repo-root>\docs\getting-started\repo-tour.md` | Existing repo map | Identifies core folders and operational data folders relevant to import planning. |
| `<repo-root>\docs\how-to\run_ci_locally.md` | Existing verification guide | Provides known local test/docs/CI commands. |
| `<repo-root>\docs\contributing\docs_style_guide.md` | Existing docs governance guide | Defines repo-truth-only docs rules and TODO-over-guessing policy. |
| `<repo-root>\docs\README_ANALYSIS_ES5M.md` | Existing ES5m workflow doc | Relevant to ES/fixture/data boundaries and local generated artifact handling. |
| `<repo-root>\docs\dataset_catalog_spec_v1.md` | Existing dataset contract doc | Relevant to dataset capability/import planning and immutable dataset registration concepts. |
| `<repo-root>\pyproject.toml` | Existing package/config truth | Provides package name, Python constraints, dependencies, and pytest config. |

## Included Package Inputs Without Full Text

These draft inputs were located and intentionally not expanded into the bundle text:

- `<nullforge-incoming-root>\packages\NullForge_Setup_Package_v0_4.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_00_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_01_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_02_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_03_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_04_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_05_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_06_v0_4_Package.zip`
- `<nullforge-incoming-root>\packages\NullForge_Volume_07_v0_4_Package.zip`

Truth status for package inputs: draft/design inputs only until reviewed, imported, and audited through M0.

## Excluded Files

| Excluded source | Reason |
|---|---|
| Full text of NullForge Volumes 0-7 | Too broad for PF-T000 context bundle; volumes remain draft inputs until import ticket PF-T001. |
| Full repo dump | Explicitly excluded by curator prompt and context refresh rules. |
| `src/`, `tests/`, engine internals | Not needed for docs/import-plan context and forbidden to modify in this pass. |
| Raw/full `ES.zip` or local data files | Explicit data gate; not needed for context and must not enter repo. |
| Old chat transcripts and stale prompts | Not source truth unless promoted through M0. |
| Tauri/Dataset Studio/Logic Factory/Visual Replay implementation detail | Out of scope for PF-T000 and this curator pass. |
| Dependency installation output or environment state | Installing dependencies is forbidden in this pass. |

## Truth Status Summary

- Existing `research-core` tracked docs/config: authoritative for current repo and engine state.
- Extracted M0 package docs: authoritative instructions for M0 execution until superseded by reviewed repo artifacts.
- Setup/volume zip packages: draft/design memory only.
- This context bundle: temporary working context for PF-T000 Planner; not canonical project documentation.

## Expiry

This bundle expires when any of the following changes:

- `main` changes;
- this branch changes outside `plans/nullforge/PF-T000/`;
- any M0 package file changes;
- any previous ticket output appears or changes;
- target paths change;
- a human gate is triggered;
- repo docs relevant to ResearchCore status, architecture, docs governance, ES/data handling, or test commands change.

## Refresh Rule

Refresh context before running the PF-T000 Planner if `git status` is dirty, if the branch is not `docs/PF-T000-nullforge-import-plan`, if the M0 package root moved, if setup/volume packages were extracted/changed, or if any proposed target path now exists.

## Context Risks

- Existing ResearchCore docs have active engine truth that must not be overwritten by NullForge product docs.
- Generated NullForge volumes are tempting to treat as canonical, but they are not canonical until imported and audited.
- Root README/package naming changes could trigger source-of-truth and public identity gates.
- Existing ES5m docs and future ES-derived fixtures require careful data/license/safety treatment.
- Repo docs currently contain some partial/TODO areas; the import plan should not imply the engine is more complete than repo truth says.

## Open Questions

- Should the Planner preserve the milestone target layout exactly or propose a safer adjusted layout after inventory?
- What minimal, human-approved root README touch is acceptable later, if any?
- Should setup package docs be imported in PF-T001 or only referenced as process support?
- What specific fixture/data policy is required before any ES-derived sample enters the repo?
- Should NullForge status live only under `docs/nullforge/` to avoid changing `docs/STATUS.md`?

## Human Gate Triggers

Human review is required before overwriting or moving ResearchCore docs, changing repo/package/CLI/public identity, adding dependencies/code/scripts/CI behavior, committing raw or ES-derived data without a safety decision, marking generated volumes canonical before audit, or broadening into public release/legal/financial/live trading/cloud/auth/billing/mobile scope.

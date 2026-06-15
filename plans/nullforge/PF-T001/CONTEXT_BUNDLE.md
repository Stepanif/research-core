# PF-T001 Context Bundle

Pack name: NullForge M0 PF-T001 context bundle
Ticket: PF-T001 - Import NullForge volumes into repo docs
Milestone: M0 - Repo Source Import + Canonical Baseline
Created by: Context Curator pass only

## Curator Boundary

This bundle is context only. It does not plan implementation, import volume content, edit ResearchCore Engine docs, modify code, install dependencies, or run downstream PF-T002+ work.

## Repo State

- Repo root: `C:\Users\Filip\Desktop\Repos\research-core`
- Current branch created for this pass: `docs/PF-T001-import-nullforge-volumes`
- Starting branch before creation: `main`
- `main` was clean and synced with `origin/main` before branch creation.
- PF-T000 has been committed, merged to `main`, and pushed.
- Current scoped output path: `plans/nullforge/PF-T001/`

## Ticket Summary

PF-T001 is a docs/source-of-truth ticket. Its purpose is to import reviewed NullForge Volumes 0-7 into a project-specific docs area without overwriting existing ResearchCore Engine docs.

Active ticket source says required outputs are:

- `docs/nullforge/blueprint/volumes/NullForge_Volume_00_...md through NullForge_Volume_07_...md`
- `docs/nullforge/blueprint/volumes/README.md`
- `docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md`
- `reports/nullforge/PF-T001/IMPLEMENTATION_REPORT.md`
- `audits/nullforge/PF-T001/AUDIT_REPORT.md`

Required role-loop artifacts:

- `plans/nullforge/PF-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/PF-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/PF-T001/PLAN.md`
- `plans/nullforge/PF-T001/ACCEPTANCE.md`
- `plans/nullforge/PF-T001/IMPLEMENTOR_PROMPT.md`
- `reports/nullforge/PF-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/PF-T001/CHANGED_FILES.md`
- `reports/nullforge/PF-T001/TEST_RESULTS.md`
- `reports/nullforge/PF-T001/AUDITOR_PROMPT.md`
- `audits/nullforge/PF-T001/AUDIT_REPORT.md`
- `audits/nullforge/PF-T001/FINDINGS.md`
- `audits/nullforge/PF-T001/REPAIR_PROMPT.md`

## Mission Slice

NullForge is a Windows-first local desktop research workbench that helps a solo research builder import market datasets, map lawful dataset capabilities, compile/generate candidate logic into auditable test specs, run the local ResearchCore Engine, inspect visual trade replays, and decide whether evidence should be promoted, repaired, archived, or quarantined.

## Active Source Docs

Incoming M0 package docs inspected:

- `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T001-import-nullforge-volumes-into-repo-docs.md`
- `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\MILESTONE_BRIEF.md`
- `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\TICKET_QUEUE.md`
- `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\DEPENDENCY_MAP.md`
- `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\HUMAN_GATE_TRIGGERS.md`

Prior dependency outputs inspected:

- `docs/nullforge/import/PF-T000_REPO_INVENTORY.md`
- `docs/nullforge/import/PF-T000_IMPORT_PLAN.md`
- `docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md`
- `audits/nullforge/PF-T000/AUDIT_REPORT.md`
- `reports/nullforge/PF-T000/TEST_RESULTS.md`

PF-T000 audit decision: PASS.

In-repo PF-T001 ticket path checked and absent:

- `tickets/nullforge/PF-T001-import-nullforge-volumes-into-repo-docs.md`

Use the incoming package ticket as the active PF-T001 ticket source until PF-T001 imports ticket docs or a later ticket creates repo-governed ticket paths.

## Dependency Status

PF-T001 depends on PF-T000.

Dependency result:

- PF-T000 audit decision: PASS.
- PF-T000 import plan approved target layout for PF-T001: `docs/nullforge/blueprint/volumes/`.
- PF-T000 found no conflict with the separated NullForge docs layout.

M0 remains serial:

```text
PF-T000 -> PF-T001 -> PF-T002 -> ADR-T001 -> ADR-T002 -> CX-T001 -> MB-T001
```

PF-T002 must not start until PF-T001 has implementation outputs and an independent audit disposition.

## Relevant Repo Files And Folders

Existing repo truth to preserve:

- `README.md` - ResearchCore public/front-door framing. Do not edit in PF-T001.
- `docs/index.md` - Research Core docs hub. Do not edit in PF-T001.
- `docs/STATUS.md` - ResearchCore current status. Do not edit in PF-T001.
- `docs/ARCHITECTURE.md` - ResearchCore architecture truth. Do not edit in PF-T001.
- `docs/contributing/docs_style_guide.md` - Repo-truth-only docs rules; use TODOs for unknowns.
- `docs/README_ANALYSIS_ES5M.md` - ES5m local analysis/data boundary.
- `docs/dataset_catalog_spec_v1.md` - Dataset catalog concepts relevant to later NullForge dataset docs but not to this import implementation.
- `pyproject.toml` - Package metadata and dependencies. Do not edit in PF-T001.

Existing NullForge paths from PF-T000:

- `docs/nullforge/import/` exists and contains PF-T000 import docs.
- `plans/nullforge/PF-T000/` exists.
- `reports/nullforge/PF-T000/` exists.
- `audits/nullforge/PF-T000/` exists.

PF-T001 target path status:

- `docs/nullforge/blueprint/` did not exist before this curator pass.
- `docs/nullforge/blueprint/volumes/` did not exist before this curator pass.
- `reports/nullforge/PF-T001/` did not exist before this curator pass.
- `audits/nullforge/PF-T001/` did not exist before this curator pass.

## Volume Package Inventory

The generated volume packages were inspected read-only from `C:\Users\Filip\Desktop\NullForge_Incoming\packages`. They were not extracted or copied into the repo during this curator pass.

| Volume | Package zip | Zip SHA256 | Artifact entry or entries observed |
|---|---|---|---|
| 00 | `NullForge_Volume_00_v0_4_Package.zip` | `48775665EB1F2EBAA00B2FD513F68B3A5152338AC7EAB800319A4E079672D3B3` | `artifacts/NullForge_Volume_00_North_Star_Doctrine_Claims_v0_4.md` and `artifacts/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md` |
| 01 | `NullForge_Volume_01_v0_4_Package.zip` | `69A09D04B563C5813F3C559AE0775A1351AE5C605371631C0E6841DD3C0DBD89` | `artifacts/NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md` |
| 02 | `NullForge_Volume_02_v0_4_Package.zip` | `8A392AD271641962C1DEBD4DF22745C657CD3A51AF03E328D3EA69ACEE0F9500` | `artifacts/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md` |
| 03 | `NullForge_Volume_03_v0_4_Package.zip` | `0C8E5730CBBAB35E5F80B496D291F2E34204A3363D218C8980DC2254B8AD297B` | `artifacts/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md` |
| 04 | `NullForge_Volume_04_v0_4_Package.zip` | `2C2783429B77016199B2F515C5CB95F6432C78CF12982DAA77557ACC9312715A` | `artifacts/NullForge_Volume_04_Dataset_Studio_ES_Intake_Fixture_Policy_DatasetCapabilityMap_Timeframe_Chart_Rules_v0_4.md` |
| 05 | `NullForge_Volume_05_v0_4_Package.zip` | `218387F5177999ED838A6985C35F18EC866C17AB21F957D5BB8557EDDCC17D45` | `artifacts/NullForge_Volume_05_Logic_Factory_LogicCard_Lifecycle_Compiler_Contract_Generator_Null_Ablation_TestPlan_Bridge_v0_4.md` |
| 06 | `NullForge_Volume_06_v0_4_Package.zip` | `C5B1609C022992194F8082F2050CE9BA97A6A71B81A0AFAE5D904952C5D0CAC2` | `artifacts/NullForge_Volume_06_Visual_Replay_Evidence_Cards_Audit_Decision_UX_Result_Interpretation_Boundaries_v0_4.md` |
| 07 | `NullForge_Volume_07_v0_4_Package.zip` | `B92C2210AA9C34869E1E3DBA044CA7626F30A46A28980888DB4AC9D6CDA42D03` | `artifacts/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` |

### Volume 00 Ambiguity

Volume 00 package manifest lists only:

- `artifacts/NullForge_Volume_00_North_Star_Doctrine_Claims_v0_4.md`

But the zip also contains:

- `artifacts/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md`

Both files have the same visible H1 topic. The second filename matches the PF-T001/M0 wording more fully. The context curator does not choose between them. The planner should explicitly decide whether to:

- import only the manifest-listed file;
- import the expanded filename file;
- import both with clear labels; or
- require human review before implementation.

## Observed Volume Headings And Status Snippets

Read-only heading/status inspection found:

- Volume 00: `# Volume 0 - NullForge North Star, Doctrine, Naming, Claims, MVP Cutline, Anti-Goals`; status variants include `DRAFT_FOR_PROMOTION` and `Draft canonical source, pending repo promotion`.
- Volume 01: `# Volume 1 - NullForge Workspace, Repo, Context, Source-of-Truth, Archive, and Quarantine System v0.4`; status says draft canonical project source after human review/promotion.
- Volume 02: `# NullForge Volume 2 - Planner / Implementor / Auditor Loop, QA Gates, Human Gates, and Codex Execution System v0.4`; status says `DRAFT_CANONICAL_PROJECT_SOURCE`.
- Volume 03: `# Volume 3 - NullForge Windows + Tauri Desktop Architecture, ResearchCore Engine Bridge, Sidecar Contract, and Packaging Spike Plan`; status says `DRAFT_CANONICAL_PROJECT_SOURCE`.
- Volume 04: `# Volume 4 - NullForge Dataset Studio, ES.zip Intake Boundary, Fixture Policy, DatasetCapabilityMap, Timeframe/Chart Capability Rules v0.4`; status says draft canonical project source.
- Volume 05: `# Volume 5 - NullForge Logic Factory, LogicCard Lifecycle, Compiler Contract, Generator/Null/Ablation Boundary, and Test-Plan Bridge v0.4`; status says `DRAFT_CANONICAL_SOURCE` and no implementation code generated.
- Volume 06: `# Volume 6 - NullForge Visual Replay, Evidence Cards, Audit Decision UX, and Result Interpretation Boundaries v0.4`; status says draft canonical project source.
- Volume 07: `# Volume 7 - NullForge Roadmap, Milestones, Ticket Backlog, Codex Prompt Packs, and First Execution Batch`; status says `DRAFT_CANONICAL_SOURCE_PENDING_REPO_IMPORT`.

## Constraints And Forbidden Actions

Do not:

- overwrite existing ResearchCore Engine docs;
- edit root `README.md`, `docs/index.md`, `docs/STATUS.md`, `docs/ARCHITECTURE.md`, package metadata, schemas, tests, CI, or code;
- create Tauri/app/sidecar/parser/compiler/visual replay/packaging code;
- install dependencies;
- import old chat logs wholesale;
- mark old prompts as active truth;
- import raw/full `ES.zip`, raw/private/local data, or ES-derived fixtures;
- broaden into public release, legal/trademark naming, AI strategy activation, broker/live-trading, financial advice, auth, billing, cloud sync, marketplace, or mobile scope;
- start PF-T002 or downstream M0 tickets.

PF-T001 may import reviewed volume docs into the agreed NullForge docs location, but the planner should keep prompts separate from canonical volume content unless a later scoped ticket imports prompts.

## Required Checks And Tests

PF-T001 ticket requires:

- all expected volume files exist;
- no source/implementation directories changed;
- manual check that imported docs do not overwrite engine docs.

Recommended implementor checks to plan:

- `git status --short --branch` before and after;
- `Test-Path -LiteralPath docs\nullforge\blueprint\volumes`;
- `Test-Path -LiteralPath` for every expected imported volume file, `README.md`, and `VOLUME_IMPORT_MANIFEST.md`;
- `git diff --name-only`;
- manual review that changed files are limited to:
  - `docs/nullforge/blueprint/volumes/`
  - `reports/nullforge/PF-T001/`
  - later `audits/nullforge/PF-T001/`
  - `plans/nullforge/PF-T001/`

Optional checks only if docs navigation or generated reference surfaces are changed:

- `python -m mkdocs build`
- `python tools/docs/verify_generated_docs_clean.py`

Do not install dependencies to satisfy optional checks.

## Human Gate Triggers

Human review is required before:

- overwriting existing ResearchCore Engine docs;
- renaming repo, package, CLI, or public project identity;
- moving existing docs;
- changing root README beyond a scoped link/summary;
- marking generated volumes canonical without PF-T001 audit;
- treating old chat as active source truth;
- adding dependencies, scripts, parsers, sidecar binaries, app code, packaging configs, tests, CI, or release/build changes;
- committing full `ES.zip`, ES-derived fixtures without a license/safety decision, or raw/private/local data;
- broadening into public release, legal/trademark claims, AI strategy generation activation, broker/live-trading integration, financial advice wording, auth, billing, cloud sync, marketplace, or mobile scope.

Potential gate to evaluate before implementation:

- Volume 00 contains two artifact markdown files, while its manifest lists only one. If the planner cannot resolve this from source documents, require human review.

Human gates triggered in this curator pass: NONE.

## Open Questions

- Which Volume 00 artifact should PF-T001 import, given the manifest/file mismatch?
- Should PF-T001 import prompt files at all, or only volume artifact markdown and manifest metadata? The ticket acceptance says prior prompts should be archived or referenced separately, not mixed into canonical volume content.
- Should imported volume files preserve original long filenames exactly, or normalize to stable `volume-00.md` through `volume-07.md` while preserving original source names in `VOLUME_IMPORT_MANIFEST.md`?
- Should each imported volume receive added front matter, or only a short import banner/title normalization? Ticket forbids content edits beyond path/front-matter/title normalization unless explicitly scoped.
- What exact import date should be used in `VOLUME_IMPORT_MANIFEST.md`: current execution date, git commit date, or `RESEARCH_CREATED_UTC` if available?

## Ready For Planner

YES, subject to the planner explicitly handling the Volume 00 source ambiguity and keeping PF-T001 docs-only.

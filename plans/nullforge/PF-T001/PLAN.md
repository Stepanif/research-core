# PF-T001 Plan

Ticket: PF-T001 - Import NullForge volumes into repo docs
Milestone: M0 - Repo Source Import + Canonical Baseline
Role: Planner

## Purpose

Produce a bounded, docs-only implementation plan for importing reviewed NullForge Volume 0-7 artifact markdown into the repo under the PF-T000-approved target path:

```text
docs/nullforge/blueprint/volumes/
```

PF-T001 must promote the selected volume docs from external generated package inputs into repo-managed NullForge project docs while preserving the boundary that they are NullForge product/workflow planning, not ResearchCore Engine implementation truth.

PF-T001 does not create implementation code, app scaffolds, scripts, parsers, sidecars, tests, schemas, package changes, CI changes, root docs navigation changes, or downstream PF-T002+ artifacts.

## Source Context Used

Repo-local context:

- `plans/nullforge/PF-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/PF-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/import/PF-T000_REPO_INVENTORY.md`
- `docs/nullforge/import/PF-T000_IMPORT_PLAN.md`
- `docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md`
- `audits/nullforge/PF-T000/AUDIT_REPORT.md`

Active ticket source from incoming package:

- `C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T001-import-nullforge-volumes-into-repo-docs.md`

The in-repo PF-T001 ticket path is absent at planner time:

- `tickets/nullforge/PF-T001-import-nullforge-volumes-into-repo-docs.md`

Volume package sources:

- `C:\Users\Filip\Desktop\NullForge_Incoming\packages\NullForge_Volume_00_v0_4_Package.zip`
- `C:\Users\Filip\Desktop\NullForge_Incoming\packages\NullForge_Volume_01_v0_4_Package.zip`
- `C:\Users\Filip\Desktop\NullForge_Incoming\packages\NullForge_Volume_02_v0_4_Package.zip`
- `C:\Users\Filip\Desktop\NullForge_Incoming\packages\NullForge_Volume_03_v0_4_Package.zip`
- `C:\Users\Filip\Desktop\NullForge_Incoming\packages\NullForge_Volume_04_v0_4_Package.zip`
- `C:\Users\Filip\Desktop\NullForge_Incoming\packages\NullForge_Volume_05_v0_4_Package.zip`
- `C:\Users\Filip\Desktop\NullForge_Incoming\packages\NullForge_Volume_06_v0_4_Package.zip`
- `C:\Users\Filip\Desktop\NullForge_Incoming\packages\NullForge_Volume_07_v0_4_Package.zip`

## Dependencies And Current Status

- PF-T001 depends on PF-T000.
- PF-T000 audit decision: PASS.
- PF-T000 approved `docs/nullforge/blueprint/volumes/` as the PF-T001 target area.
- Current branch: `docs/PF-T001-import-nullforge-volumes`.
- Current working tree contains only PF-T001 context bundle files under `plans/nullforge/PF-T001/`.
- M0 remains serial:

```text
PF-T000 -> PF-T001 -> PF-T002 -> ADR-T001 -> ADR-T002 -> CX-T001 -> MB-T001
```

PF-T002 must remain blocked until PF-T001 has implementation outputs and an independent audit disposition.

## Exact Scope

PF-T001 implementor may create:

```text
docs/nullforge/blueprint/volumes/README.md
docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md
docs/nullforge/blueprint/volumes/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_04_Dataset_Studio_ES_Intake_Fixture_Policy_DatasetCapabilityMap_Timeframe_Chart_Rules_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_05_Logic_Factory_LogicCard_Lifecycle_Compiler_Contract_Generator_Null_Ablation_TestPlan_Bridge_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_06_Visual_Replay_Evidence_Cards_Audit_Decision_UX_Result_Interpretation_Boundaries_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md
reports/nullforge/PF-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/PF-T001/CHANGED_FILES.md
reports/nullforge/PF-T001/TEST_RESULTS.md
reports/nullforge/PF-T001/AUDITOR_PROMPT.md
```

The later auditor may create:

```text
audits/nullforge/PF-T001/AUDIT_REPORT.md
audits/nullforge/PF-T001/FINDINGS.md
audits/nullforge/PF-T001/REPAIR_PROMPT.md
```

PF-T001 planner/implementor may also leave the existing PF-T001 planner files under:

```text
plans/nullforge/PF-T001/
```

No other files should change.

## Volume Import Decisions

### Volume 00

Human decision: import this expanded Volume 00 artifact:

```text
NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md
```

The `VOLUME_IMPORT_MANIFEST.md` must record that this was a human decision because the Volume 00 package manifest listed the shorter artifact:

```text
NullForge_Volume_00_North_Star_Doctrine_Claims_v0_4.md
```

### Prompts

Do not import prompt files as canonical volume content in PF-T001. Reference prompt files in `VOLUME_IMPORT_MANIFEST.md` only as non-imported package contents if needed.

### Filenames

Preserve original selected source artifact filenames for traceability. Do not normalize to `volume-00.md` through `volume-07.md` in PF-T001.

### Import Notice

Each imported volume file should receive a small standardized import notice at the top, then preserve the source artifact content below unchanged.

Required notice content:

- imported by PF-T001;
- source package zip name;
- source artifact path inside zip;
- source package SHA256;
- import date;
- authority status: repo-managed NullForge planning source after PF-T001 audit, not ResearchCore Engine implementation truth.

Use import date `2026-06-15` unless implementation occurs on a different date; if it does, use the actual implementation date and record it consistently in the manifest and imported volume notices.

## Forbidden Actions

- Do not modify existing ResearchCore Engine docs.
- Do not modify `README.md`, `docs/index.md`, `docs/STATUS.md`, `docs/ARCHITECTURE.md`, `docs/reference/`, `docs/contributing/`, or existing docs outside the allowed PF-T001 target paths.
- Do not modify `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, `pyproject.toml`, `mkdocs.yml`, `.github/`, package files, or CI files.
- Do not create implementation code, Tauri/app scaffold, sidecar, parser, compiler, visual replay, EvidenceCard, packaging, cloud, auth, billing, broker, or mobile artifacts.
- Do not install dependencies.
- Do not import raw/full `ES.zip`, raw/private/local data, or ES-derived fixtures.
- Do not import old chat logs.
- Do not mark old prompts as active truth.
- Do not start PF-T002 or downstream M0 tickets.
- Do not change repo/package/CLI/product identity.

## Likely Files Changed

Planner pass:

```text
plans/nullforge/PF-T001/PLAN.md
plans/nullforge/PF-T001/ACCEPTANCE.md
plans/nullforge/PF-T001/IMPLEMENTOR_PROMPT.md
```

Implementor pass:

```text
docs/nullforge/blueprint/volumes/README.md
docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md
docs/nullforge/blueprint/volumes/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_04_Dataset_Studio_ES_Intake_Fixture_Policy_DatasetCapabilityMap_Timeframe_Chart_Rules_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_05_Logic_Factory_LogicCard_Lifecycle_Compiler_Contract_Generator_Null_Ablation_TestPlan_Bridge_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_06_Visual_Replay_Evidence_Cards_Audit_Decision_UX_Result_Interpretation_Boundaries_v0_4.md
docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md
reports/nullforge/PF-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/PF-T001/CHANGED_FILES.md
reports/nullforge/PF-T001/TEST_RESULTS.md
reports/nullforge/PF-T001/AUDITOR_PROMPT.md
```

## Step-By-Step Docs/Source Update Plan

1. Preflight
   - Run `git status --short --branch`.
   - Confirm branch is `docs/PF-T001-import-nullforge-volumes`.
   - Confirm in-repo ticket path status:
     - `tickets/nullforge/PF-T001-import-nullforge-volumes-into-repo-docs.md`
   - Confirm expected target output paths do not already contain conflicting files.
   - Confirm PF-T000 audit PASS is present.

2. Source package verification
   - Compute or verify SHA256 for each source volume zip and compare to the hashes in `CONTEXT_BUNDLE.md`.
   - Confirm selected artifact entries exist inside each zip.
   - For Volume 00, confirm the selected expanded artifact exists and record the human decision in the import manifest.

3. Create target docs folder
   - Create `docs/nullforge/blueprint/volumes/`.

4. Import selected volume artifacts
   - Extract/copy only the selected artifact markdown files from the volume zips.
   - Preserve original source artifact filenames.
   - Add the standardized import notice at top of each imported file.
   - Preserve source content below the import notice.
   - Do not import prompt files.
   - Do not import package manifests as separate docs unless their metadata is represented in `VOLUME_IMPORT_MANIFEST.md`.

5. Create `README.md`
   - Explain the purpose of `docs/nullforge/blueprint/volumes/`.
   - State that files are NullForge planning/workflow docs, not ResearchCore Engine implementation truth.
   - List Volume 00-07 imported files.
   - Link to `VOLUME_IMPORT_MANIFEST.md`.
   - State prompts are not imported as canonical volume content.

6. Create `VOLUME_IMPORT_MANIFEST.md`
   - Record import date.
   - Record ticket `PF-T001`.
   - Record PF-T000 dependency PASS.
   - Record each source zip path, SHA256, selected source entry, destination path, and authority status.
   - Record prompt files as non-imported package contents if useful.
   - Record the Volume 00 human decision explicitly.
   - State generated packages remain design/source inputs until PF-T001 audit accepts the import.

7. Create implementation reports
   - `IMPLEMENTATION_REPORT.md`: actions, sources, decisions, gates, and remaining work.
   - `CHANGED_FILES.md`: every created/changed file and why.
   - `TEST_RESULTS.md`: exact commands/checks and outcomes.
   - `AUDITOR_PROMPT.md`: bounded PF-T001-only audit prompt.

8. Final verification
   - Run `git status --short --branch`.
   - Run `git status --short --untracked-files=all`.
   - Run `git diff --name-only`.
   - Run `Test-Path -LiteralPath` for every imported volume, `README.md`, `VOLUME_IMPORT_MANIFEST.md`, and report output.
   - Manually confirm changed paths are limited to PF-T001 docs/plans/reports and no forbidden paths changed.

## Tests And Checks Required

Required:

```text
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
Test-Path -LiteralPath <each expected imported volume file>
Test-Path -LiteralPath docs\nullforge\blueprint\volumes\README.md
Test-Path -LiteralPath docs\nullforge\blueprint\volumes\VOLUME_IMPORT_MANIFEST.md
Test-Path -LiteralPath reports\nullforge\PF-T001\IMPLEMENTATION_REPORT.md
Test-Path -LiteralPath reports\nullforge\PF-T001\CHANGED_FILES.md
Test-Path -LiteralPath reports\nullforge\PF-T001\TEST_RESULTS.md
Test-Path -LiteralPath reports\nullforge\PF-T001\AUDITOR_PROMPT.md
manual review that no implementation/source directories changed
manual review that imported docs do not overwrite engine docs
manual review that each imported volume is labeled as NullForge planning/workflow docs, not ResearchCore Engine implementation truth
```

Optional, only if docs navigation or generated docs surfaces are changed:

```text
python -m mkdocs build
python tools/docs/verify_generated_docs_clean.py
```

PF-T001 should not change docs navigation or generated docs surfaces, so those optional checks should normally be skipped with explanation. Do not install dependencies.

## Security, Privacy, And Data Considerations

- No raw/full ES data enters the repo.
- No ES-derived fixtures enter the repo.
- No private/local data enters the repo.
- Volume imports may mention ES.zip, Dataset Studio, Logic Factory, Tauri, sidecars, replay, or future product concepts, but they do not authorize implementation.
- Imported volume docs must be clearly scoped as NullForge planning/workflow docs, not ResearchCore Engine implementation truth or financial advice.
- Prompt files and old chats remain non-canonical unless separately imported by a scoped ticket and audit.

## Source-Of-Truth Risks

- Volume 00 package manifest differs from the selected artifact. This is resolved by a human decision and must be recorded in `VOLUME_IMPORT_MANIFEST.md`.
- Imported generated volumes could be mistaken for implemented engine behavior. Mitigate with import notices, README wording, and manifest authority status.
- Volume docs may contain future product architecture or UX scope. Do not let import imply implementation authorization.
- Root README/docs navigation changes could blur ResearchCore and NullForge truth. Do not change them in PF-T001.
- Prompt files inside packages could be mistaken for canonical source. Do not import prompts as canonical volume content.

## Rollback And Repair Route

If PF-T001 implementation goes out of scope:

1. Stop before further edits.
2. Identify changed files with `git status --short --untracked-files=all` and `git diff --name-only`.
3. Repair or remove only PF-T001-added files under:

```text
docs/nullforge/blueprint/volumes/
reports/nullforge/PF-T001/
plans/nullforge/PF-T001/
```

4. Do not revert unrelated user changes.
5. If engine docs, code, tests, schemas, package files, CI, raw data, or generated references changed, mark HOLD or REJECT for audit and require human review.

## Human Gate Triggers

Human review is required before:

- overwriting, moving, renaming, or materially editing existing ResearchCore Engine docs;
- changing root README or docs navigation beyond the PF-T001 target folder;
- changing repo, package, CLI, product, or public identity;
- adding dependencies, code, scripts, parsers, sidecar binaries, packaging configs, tests, schemas, or CI behavior;
- importing raw/full `ES.zip`, raw/private/local data, or ES-derived fixtures;
- marking generated volumes canonical without PF-T001 audit;
- treating old chats or prompts as active canonical source;
- broadening into public release, legal/trademark naming, AI strategy activation, broker/live trading, financial advice, auth, billing, cloud sync, marketplace, or mobile scope;
- starting PF-T002 or downstream M0 tickets before PF-T001 audit disposition.

Planner-detected human gates: NONE, because the Volume 00 ambiguity was resolved by human decision before this planner pass.

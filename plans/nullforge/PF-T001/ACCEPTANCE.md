# PF-T001 Acceptance

Ticket: PF-T001 - Import NullForge volumes into repo docs

## Testable Acceptance Criteria

- `docs/nullforge/blueprint/volumes/README.md` exists.
- `docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md` exists.
- The selected Volume 00 file exists:
  - `docs/nullforge/blueprint/volumes/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md`
- Volume 01 through Volume 07 files exist:
  - `docs/nullforge/blueprint/volumes/NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md`
  - `docs/nullforge/blueprint/volumes/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md`
  - `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md`
  - `docs/nullforge/blueprint/volumes/NullForge_Volume_04_Dataset_Studio_ES_Intake_Fixture_Policy_DatasetCapabilityMap_Timeframe_Chart_Rules_v0_4.md`
  - `docs/nullforge/blueprint/volumes/NullForge_Volume_05_Logic_Factory_LogicCard_Lifecycle_Compiler_Contract_Generator_Null_Ablation_TestPlan_Bridge_v0_4.md`
  - `docs/nullforge/blueprint/volumes/NullForge_Volume_06_Visual_Replay_Evidence_Cards_Audit_Decision_UX_Result_Interpretation_Boundaries_v0_4.md`
  - `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`
- `VOLUME_IMPORT_MANIFEST.md` records:
  - import date;
  - ticket `PF-T001`;
  - PF-T000 dependency PASS;
  - source package names;
  - source package SHA256 values;
  - selected artifact paths inside zips;
  - destination paths;
  - authority status;
  - prompt files as non-imported package contents if referenced;
  - the human decision selecting the expanded Volume 00 artifact over the manifest-listed shorter artifact.
- Each imported volume has a clear import notice stating it is NullForge product/workflow planning, not ResearchCore Engine implementation truth.
- Imported volume source content is preserved below the import notice.
- Prompt files are not imported as canonical volume content.
- `reports/nullforge/PF-T001/IMPLEMENTATION_REPORT.md` exists.
- `reports/nullforge/PF-T001/CHANGED_FILES.md` exists.
- `reports/nullforge/PF-T001/TEST_RESULTS.md` exists.
- `reports/nullforge/PF-T001/AUDITOR_PROMPT.md` exists.
- No implementation files are changed.
- No existing ResearchCore Engine docs are overwritten or modified.
- No raw/full ES data, private data, local data, or ES-derived fixtures are imported.
- No downstream PF-T002+ artifacts are created.

## Required Checks And Commands

Run and record:

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
```

Run and record `Test-Path -LiteralPath` checks for:

```text
docs\nullforge\blueprint\volumes\README.md
docs\nullforge\blueprint\volumes\VOLUME_IMPORT_MANIFEST.md
docs\nullforge\blueprint\volumes\NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md
docs\nullforge\blueprint\volumes\NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md
docs\nullforge\blueprint\volumes\NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md
docs\nullforge\blueprint\volumes\NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md
docs\nullforge\blueprint\volumes\NullForge_Volume_04_Dataset_Studio_ES_Intake_Fixture_Policy_DatasetCapabilityMap_Timeframe_Chart_Rules_v0_4.md
docs\nullforge\blueprint\volumes\NullForge_Volume_05_Logic_Factory_LogicCard_Lifecycle_Compiler_Contract_Generator_Null_Ablation_TestPlan_Bridge_v0_4.md
docs\nullforge\blueprint\volumes\NullForge_Volume_06_Visual_Replay_Evidence_Cards_Audit_Decision_UX_Result_Interpretation_Boundaries_v0_4.md
docs\nullforge\blueprint\volumes\NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md
reports\nullforge\PF-T001\IMPLEMENTATION_REPORT.md
reports\nullforge\PF-T001\CHANGED_FILES.md
reports\nullforge\PF-T001\TEST_RESULTS.md
reports\nullforge\PF-T001\AUDITOR_PROMPT.md
```

Manual review required:

- Confirm changed files are limited to:
  - `plans/nullforge/PF-T001/`
  - `docs/nullforge/blueprint/volumes/`
  - `reports/nullforge/PF-T001/`
- Confirm no `src/`, `tests/`, `schemas/`, `configs/`, `tools/`, package files, CI files, generated reference docs, root README, or existing ResearchCore Engine docs changed.
- Confirm imported volumes are labeled as NullForge planning/workflow docs and not ResearchCore Engine implementation truth.
- Confirm Volume 00 human decision is recorded in `VOLUME_IMPORT_MANIFEST.md`.

Optional checks:

- `python -m mkdocs build` only if docs navigation or mkdocs-visible configuration is changed.
- `python tools/docs/verify_generated_docs_clean.py` only if generated docs tooling or generated reference files are changed.

Do not install dependencies. If optional checks are skipped, record why in `TEST_RESULTS.md`.

## Docs Update Expectations

- Use repo-truth-only language.
- Do not guess source paths, hashes, schema keys, commands, or implementation behavior.
- Preserve source artifact content below the standardized import notice.
- Keep prompts out of canonical volume content.
- Treat imported volumes as repo-managed NullForge planning source after PF-T001 audit, not as ResearchCore Engine implementation truth.
- Preserve ResearchCore Engine docs as authoritative for current engine status and architecture.

## Done Definition

PF-T001 implementation is ready for auditor when:

- All selected volume files are present.
- `README.md` and `VOLUME_IMPORT_MANIFEST.md` are present.
- Required reports are present.
- Required checks are recorded in `reports/nullforge/PF-T001/TEST_RESULTS.md`.
- Human gate status is explicitly reported.
- Changed files are scoped to PF-T001 docs/plans/reports.
- `reports/nullforge/PF-T001/AUDITOR_PROMPT.md` is ready for an independent auditor.

PF-T001 itself is not complete until an auditor returns PASS, HOLD, or REJECT and the result is recorded by the later M0 handoff workflow.

## Conditions That Force HOLD Or REJECT

Return HOLD or REJECT if any of these occur:

- Existing ResearchCore Engine docs are overwritten, moved, renamed, or materially edited.
- Repo/package/CLI/product identity is changed.
- Code, tests, schemas, scripts, package files, CI behavior, generated docs tooling, or dependencies are added or modified.
- Raw/full data, `ES.zip`, private data, local generated data, or ES-derived fixtures enter the repo.
- Prompt files or old chats are imported as canonical volume content.
- Generated volumes are described as ResearchCore Engine implementation truth.
- Volume 00 human decision is omitted from `VOLUME_IMPORT_MANIFEST.md`.
- Required volume files or reports are missing.
- Checks are skipped without explanation.
- Changed files cannot be bounded to PF-T001 docs/plans/reports.
- A human gate is triggered and work continues without approval.
- PF-T002 or downstream M0 work starts before PF-T001 audit disposition.

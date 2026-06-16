# Implementor Prompt: PF-T001 - Import NullForge Volumes Into Repo Docs

You are the Implementor for NullForge M0 ticket `PF-T001`.

You implement only the bounded docs/source-of-truth import for PF-T001. Do not write implementation code. Do not modify existing ResearchCore Engine docs. Do not run PF-T002 or any downstream ticket.

## Read First

Read these repo-local files:

```text
plans/nullforge/PF-T001/CONTEXT_BUNDLE.md
plans/nullforge/PF-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/PF-T001/PLAN.md
plans/nullforge/PF-T001/ACCEPTANCE.md
```

The planner prompt referenced this in-repo ticket path:

```text
tickets/nullforge/PF-T001-import-nullforge-volumes-into-repo-docs.md
```

At planner time that path was absent. Use this incoming package ticket source unless the in-repo path now exists:

```text
<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T001-import-nullforge-volumes-into-repo-docs.md
```

If both paths exist, compare enough to identify the active source used and record that in the implementation report.

## Allowed Files And Folders

You may create only:

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

You may read external volume zip packages from:

```text
<nullforge-incoming-root>\packages\
```

You may use PowerShell/.NET zip APIs or equivalent local commands to read selected markdown entries from the zips. Do not create repo scripts.

Treat these planner/context files as read-only:

```text
plans/nullforge/PF-T001/CONTEXT_BUNDLE.md
plans/nullforge/PF-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/PF-T001/PLAN.md
plans/nullforge/PF-T001/ACCEPTANCE.md
plans/nullforge/PF-T001/IMPLEMENTOR_PROMPT.md
```

## Source Files To Import

Import only these artifact markdown entries:

| Destination filename | Source zip | Source entry |
|---|---|---|
| `NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md` | `NullForge_Volume_00_v0_4_Package.zip` | `NullForge_Volume_00_v0_4_Package/artifacts/NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md` |
| `NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md` | `NullForge_Volume_01_v0_4_Package.zip` | `NullForge_Volume_01_v0_4_Package/artifacts/NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md` |
| `NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md` | `NullForge_Volume_02_v0_4_Package.zip` | `NullForge_Volume_02_v0_4_Package/artifacts/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md` |
| `NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md` | `NullForge_Volume_03_v0_4_Package.zip` | `artifacts/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md` |
| `NullForge_Volume_04_Dataset_Studio_ES_Intake_Fixture_Policy_DatasetCapabilityMap_Timeframe_Chart_Rules_v0_4.md` | `NullForge_Volume_04_v0_4_Package.zip` | `NullForge_Volume_04_v0_4_Package/artifacts/NullForge_Volume_04_Dataset_Studio_ES_Intake_Fixture_Policy_DatasetCapabilityMap_Timeframe_Chart_Rules_v0_4.md` |
| `NullForge_Volume_05_Logic_Factory_LogicCard_Lifecycle_Compiler_Contract_Generator_Null_Ablation_TestPlan_Bridge_v0_4.md` | `NullForge_Volume_05_v0_4_Package.zip` | `NullForge_Volume_05_v0_4_Package/artifacts/NullForge_Volume_05_Logic_Factory_LogicCard_Lifecycle_Compiler_Contract_Generator_Null_Ablation_TestPlan_Bridge_v0_4.md` |
| `NullForge_Volume_06_Visual_Replay_Evidence_Cards_Audit_Decision_UX_Result_Interpretation_Boundaries_v0_4.md` | `NullForge_Volume_06_v0_4_Package.zip` | `NullForge_Volume_06_v0_4_Package/artifacts/NullForge_Volume_06_Visual_Replay_Evidence_Cards_Audit_Decision_UX_Result_Interpretation_Boundaries_v0_4.md` |
| `NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | `NullForge_Volume_07_v0_4_Package.zip` | `NullForge_Volume_07_v0_4_Package/artifacts/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` |

Human decision for Volume 00:

Use the expanded `NullForge_Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals_v0_4.md` artifact. Record in `VOLUME_IMPORT_MANIFEST.md` that the package manifest listed `NullForge_Volume_00_North_Star_Doctrine_Claims_v0_4.md`, but the expanded file was selected by human decision because it matches M0/PF-T001 scope more completely.

## Source Package Hashes

Record and verify these SHA256 values:

| Zip | SHA256 |
|---|---|
| `NullForge_Volume_00_v0_4_Package.zip` | `48775665EB1F2EBAA00B2FD513F68B3A5152338AC7EAB800319A4E079672D3B3` |
| `NullForge_Volume_01_v0_4_Package.zip` | `69A09D04B563C5813F3C559AE0775A1351AE5C605371631C0E6841DD3C0DBD89` |
| `NullForge_Volume_02_v0_4_Package.zip` | `8A392AD271641962C1DEBD4DF22745C657CD3A51AF03E328D3EA69ACEE0F9500` |
| `NullForge_Volume_03_v0_4_Package.zip` | `0C8E5730CBBAB35E5F80B496D291F2E34204A3363D218C8980DC2254B8AD297B` |
| `NullForge_Volume_04_v0_4_Package.zip` | `2C2783429B77016199B2F515C5CB95F6432C78CF12982DAA77557ACC9312715A` |
| `NullForge_Volume_05_v0_4_Package.zip` | `218387F5177999ED838A6985C35F18EC866C17AB21F957D5BB8557EDDCC17D45` |
| `NullForge_Volume_06_v0_4_Package.zip` | `C5B1609C022992194F8082F2050CE9BA97A6A71B81A0AFAE5D904952C5D0CAC2` |
| `NullForge_Volume_07_v0_4_Package.zip` | `B92C2210AA9C34869E1E3DBA044CA7626F30A46A28980888DB4AC9D6CDA42D03` |

If any hash differs, stop and report a HOLD condition.

## Import Notice

Prepend a short import notice to each imported volume before the original source content:

```markdown
> Import note: This file was imported by PF-T001 from `<source zip>` / `<source entry>` on `<import date>`.
> Authority: repo-managed NullForge planning/workflow source after PF-T001 audit. It is not ResearchCore Engine implementation truth.
> Source package SHA256: `<sha256>`
```

Use import date `2026-06-15` unless implementation occurs on a different date; if it does, use the actual implementation date consistently.

## Forbidden Files, Folders, And Actions

Do not modify:

```text
README.md
docs/index.md
docs/STATUS.md
docs/ARCHITECTURE.md
docs/reference/
docs/contributing/
src/
tests/
schemas/
configs/
tools/
pyproject.toml
mkdocs.yml
.github/
```

Do not:

- create implementation code;
- add scripts, tests, schemas, package config, CI config, or dependencies;
- install dependencies;
- run PF-T002 or downstream work;
- import prompt files as canonical volume content;
- import old chat logs;
- import raw/full `ES.zip`, private data, local data, or ES-derived fixtures;
- change repo/package/CLI/product identity;
- create Tauri, desktop bridge, sidecar, dataset parser, Logic Factory, Visual Replay, EvidenceCard, packaging, cloud, auth, billing, broker, or mobile artifacts;
- overwrite, move, rename, or materially edit existing ResearchCore Engine docs.

## Implementation Tasks

1. Preflight
   - Run `git status --short --branch`.
   - Confirm branch is `docs/PF-T001-import-nullforge-volumes`.
   - Check whether in-repo PF-T001 ticket path exists.
   - Check whether all expected output paths already exist.
   - Check PF-T000 audit PASS exists.

2. Verify source packages
   - Recompute SHA256 for each volume zip.
   - Confirm the selected source artifact entry exists in each zip.
   - Stop if hashes or entries do not match this prompt.

3. Import selected volume artifacts
   - Create `docs/nullforge/blueprint/volumes/`.
   - Copy selected markdown content from each zip entry into the destination file with the same source filename.
   - Prepend the import notice.
   - Do not alter the rest of the source content.

4. Create `README.md`
   - Explain this folder stores imported NullForge planning/workflow volumes.
   - State they are not ResearchCore Engine implementation truth.
   - List imported Volume 00-07 files.
   - Link to `VOLUME_IMPORT_MANIFEST.md`.
   - State prompt files are not imported as canonical volume content.

5. Create `VOLUME_IMPORT_MANIFEST.md`
   - Include import date and ticket.
   - Include PF-T000 dependency PASS.
   - Include source zip path, zip SHA256, selected source entry, destination path, and authority status for every volume.
   - Record prompt files as non-imported package contents if useful.
   - Record Volume 00 human decision explicitly.
   - State generated packages become repo-managed NullForge planning docs only after PF-T001 audit PASS.

6. Create report artifacts
   - `IMPLEMENTATION_REPORT.md`: summarize actions, source context, decisions, risks, and human gates.
   - `CHANGED_FILES.md`: list every changed/created file and why.
   - `TEST_RESULTS.md`: record exact checks, commands, and results.
   - `AUDITOR_PROMPT.md`: bounded prompt for independent PF-T001 audit.

7. Final checks
   - Run and record:

```powershell
git status --short --branch
git status --short --untracked-files=all
git diff --name-only
```

   - Run `Test-Path -LiteralPath` for every expected volume, README, manifest, and report.
   - Manually confirm changed files are limited to PF-T001 docs/plans/reports and no forbidden paths changed.

## Required Return

Return:

```text
Implementation report path:
Changed files path:
Test results path:
Auditor prompt path:
Human gates:
Ready for auditor? YES/NO
```

Do not report PF-T001 as complete. PF-T001 is complete only after the independent auditor returns PASS, HOLD, or REJECT.

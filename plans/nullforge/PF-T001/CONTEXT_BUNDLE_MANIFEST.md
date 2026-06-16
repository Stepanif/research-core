# PF-T001 Context Bundle Manifest

Pack name: NullForge M0 PF-T001 context bundle
Ticket: PF-T001 - Import NullForge volumes into repo docs
Purpose: Provide the smallest sufficient active context for the PF-T001 Planner without importing volume content or planning implementation.

## Included Files

| File | Truth status | Why included |
|---|---|---|
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T001-import-nullforge-volumes-into-repo-docs.md` | Active PF-T001 ticket source | Defines purpose, scope, outputs, forbidden actions, checks, human gates, and closeout requirement. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\MILESTONE_BRIEF.md` | Active milestone source | Defines M0 goal, non-goals, generated volumes, target layout, and success definition. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\TICKET_QUEUE.md` | Active milestone queue | Defines serial ticket order, branch names, dependency expectations, and stop conditions. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\DEPENDENCY_MAP.md` | Active dependency source | Explains why PF-T001 depends on PF-T000 and why M0 should not be parallelized. |
| `<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\milestones\nullforge\M0-repo-source-import\HUMAN_GATE_TRIGGERS.md` | Active gate policy | Defines source-of-truth, technical, data, and product/legal gate triggers. |
| `docs/nullforge/import/PF-T000_REPO_INVENTORY.md` | Accepted dependency output | Identifies existing repo docs, target path status, and source-of-truth separation. |
| `docs/nullforge/import/PF-T000_IMPORT_PLAN.md` | Accepted dependency output | Names `docs/nullforge/blueprint/volumes/` as PF-T001 target and defines downstream sequence. |
| `docs/nullforge/import/PF-T000_CONFLICTS_AND_GATES.md` | Accepted dependency output | Lists gates and source-of-truth tensions PF-T001 must preserve. |
| `audits/nullforge/PF-T000/AUDIT_REPORT.md` | Dependency audit disposition | Confirms PF-T000 PASS and authorizes normal progression to PF-T001. |
| `reports/nullforge/PF-T000/TEST_RESULTS.md` | Dependency verification record | Shows PF-T000 path checks and target path state before PF-T001. |

## Included Package Inputs Without Full Text

The following package zips were inspected read-only for inventory, artifact names, package hashes, manifests, and headings. Their full volume contents were not copied into this context bundle and were not imported into the repo during this pass.

| Package | SHA256 | Why included |
|---|---|---|
| `<nullforge-incoming-root>\packages\NullForge_Volume_00_v0_4_Package.zip` | `48775665EB1F2EBAA00B2FD513F68B3A5152338AC7EAB800319A4E079672D3B3` | Source package for Volume 00; contains a manifest-listed artifact and an additional expanded artifact. |
| `<nullforge-incoming-root>\packages\NullForge_Volume_01_v0_4_Package.zip` | `69A09D04B563C5813F3C559AE0775A1351AE5C605371631C0E6841DD3C0DBD89` | Source package for Volume 01. |
| `<nullforge-incoming-root>\packages\NullForge_Volume_02_v0_4_Package.zip` | `8A392AD271641962C1DEBD4DF22745C657CD3A51AF03E328D3EA69ACEE0F9500` | Source package for Volume 02. |
| `<nullforge-incoming-root>\packages\NullForge_Volume_03_v0_4_Package.zip` | `0C8E5730CBBAB35E5F80B496D291F2E34204A3363D218C8980DC2254B8AD297B` | Source package for Volume 03. |
| `<nullforge-incoming-root>\packages\NullForge_Volume_04_v0_4_Package.zip` | `2C2783429B77016199B2F515C5CB95F6432C78CF12982DAA77557ACC9312715A` | Source package for Volume 04. |
| `<nullforge-incoming-root>\packages\NullForge_Volume_05_v0_4_Package.zip` | `218387F5177999ED838A6985C35F18EC866C17AB21F957D5BB8557EDDCC17D45` | Source package for Volume 05. |
| `<nullforge-incoming-root>\packages\NullForge_Volume_06_v0_4_Package.zip` | `C5B1609C022992194F8082F2050CE9BA97A6A71B81A0AFAE5D904952C5D0CAC2` | Source package for Volume 06. |
| `<nullforge-incoming-root>\packages\NullForge_Volume_07_v0_4_Package.zip` | `B92C2210AA9C34869E1E3DBA044CA7626F30A46A28980888DB4AC9D6CDA42D03` | Source package for Volume 07. |

## Excluded Files

| Excluded source | Reason |
|---|---|
| Full text of Volume 0-7 artifacts | PF-T001 planner needs source paths, hashes, and ambiguity notes; full import belongs to the implementor prompt, not the context bundle. |
| Prompt files inside volume packages | Ticket says prior prompts must be archived or referenced separately, not mixed into canonical volume content. Planner should decide whether to include prompt references in the import manifest only. |
| Full repo dump | Explicitly excluded by context policy. |
| `src/`, `tests/`, `schemas/`, `tools/`, package files, and CI files | Not needed for a docs/source import context and forbidden to modify. |
| Raw/full `ES.zip`, private data, local generated data | Explicit data gate. |
| Old chat transcripts and stale prompts | Not source truth unless promoted through M0. |
| Tauri/app/sidecar/parser/compiler/visual replay implementation details | Out of scope for PF-T001 implementation. |

## Truth Status Summary

- Existing `research-core` tracked docs/config/code remain authoritative for ResearchCore Engine truth.
- PF-T000 outputs and PASS audit are authoritative dependency context for PF-T001.
- Incoming M0 ticket/milestone docs are active instructions until superseded by repo-governed M0 artifacts.
- Volume packages are draft/generated design artifacts until PF-T001 imports reviewed content and PF-T001 audit accepts it.
- This PF-T001 context bundle is temporary planner context, not canonical project documentation.

## Expiry

This bundle expires if any of the following occur:

- `main` changes before PF-T001 planner starts;
- current branch changes outside `plans/nullforge/PF-T001/`;
- any volume package changes or is replaced;
- PF-T000 outputs are amended;
- `docs/nullforge/blueprint/volumes/` appears or changes before PF-T001 planner starts;
- a human gate is triggered;
- relevant ticket, milestone, dependency, or gate docs change.

## Refresh Rule

Refresh context before running the PF-T001 Planner if:

- `git status --short --branch` is dirty beyond `plans/nullforge/PF-T001/`;
- branch is not `docs/PF-T001-import-nullforge-volumes`;
- the in-repo PF-T001 ticket path now exists;
- volume package hashes differ from this manifest;
- the Volume 00 ambiguity is resolved by a human or source update;
- target paths change.

## Context Risks

- Volume 00 package has two artifact markdown files while its manifest lists only one.
- Importing volumes can accidentally promote generated text too broadly; PF-T001 must label imported volumes as NullForge product/workflow planning, not ResearchCore Engine implementation truth.
- Volume docs contain future desktop/Tauri/sidecar/dataset/logic/replay concepts; importing docs must not create implementation authority or code scope.
- Data claims around ES.zip and fixtures must preserve data/license/safety gates.
- Root README and existing engine docs must remain untouched.

## Open Questions

- Which Volume 00 markdown artifact should be imported?
- Should PF-T001 import prompt files, reference them only in `VOLUME_IMPORT_MANIFEST.md`, or exclude them entirely?
- Should imported volume filenames preserve original package filenames or use normalized stable names like `volume-00.md` through `volume-07.md`?
- Should imported volumes receive front matter/import banners, and what exact fields are allowed?
- What import date convention should `VOLUME_IMPORT_MANIFEST.md` use?

## Human Gate Triggers

Human review is required before overwriting ResearchCore Engine docs, changing repo/package/CLI/public identity, adding dependencies/code/scripts/CI behavior, committing raw or ES-derived data without a safety decision, marking generated volumes canonical before PF-T001 audit, or broadening into public release/legal/financial/live trading/cloud/auth/billing/mobile scope.

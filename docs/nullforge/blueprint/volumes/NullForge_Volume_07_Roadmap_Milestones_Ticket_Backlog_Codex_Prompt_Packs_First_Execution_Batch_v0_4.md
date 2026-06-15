> Import note: This file was imported by PF-T001 from `NullForge_Volume_07_v0_4_Package.zip` / `NullForge_Volume_07_v0_4_Package/artifacts/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` on `2026-06-15`.
> Authority: repo-managed NullForge planning/workflow source after PF-T001 audit. It is not ResearchCore Engine implementation truth.
> Source package SHA256: `B92C2210AA9C34869E1E3DBA044CA7626F30A46A28980888DB4AC9D6CDA42D03`

# Volume 7 — NullForge Roadmap, Milestones, Ticket Backlog, Codex Prompt Packs, and First Execution Batch

```text
Project: NullForge
Existing repo / engine: research-core
Internal engine label: ResearchCore Engine
Platform: Windows 11 x64 first
Desktop stack: Tauri + React + TypeScript
Engine strategy: Python ResearchCore Engine sidecar / scoped command bridge
Volume: 7 of 7 in the medium Project Factory pattern
Version: v0.4
Status: DRAFT_CANONICAL_SOURCE_PENDING_REPO_IMPORT
```

---

## 1. Volume purpose

Volume 7 converts Volumes 0–6 into a roadmap, milestone map, ticket backlog, role-loop prompt system, and first execution batch plan.

This volume does **not** start implementation. It defines how implementation should begin after the generated volumes are reviewed, promoted, and imported into the `research-core` repo as project-specific source-of-truth docs.

Volume 7 exists to prevent this failure pattern:

```text
"We have enough planning"
→ broad Codex prompt
→ app scaffold explosion
→ source-of-truth drift
→ unreviewed dependencies
→ unclear tests
→ fake progress
```

The correct pattern is:

```text
promoted volumes
→ repo-source import pass
→ current status / claim / decision / roadmap docs
→ milestone batch
→ one ticket at a time
→ context curator
→ planner
→ implementor
→ auditor
→ repair/human gate
→ milestone handoff
```

---

## 2. Relationship to Volumes 0–6

| Prior volume | Governs | Volume 7 uses it for |
|---|---|---|
| Volume 0 | North Star, naming, claims, MVP cutline, anti-goals | Roadmap spine, MVP proof loop, non-goal filtering |
| Volume 1 | Workspace, repo, source-of-truth, archive/quarantine | Repo import plan, canonical docs, context-bundle policy |
| Volume 2 | Planner / Implementor / Auditor loop, QA and human gates | Role-loop prompt packs, ticket artifact tree, PASS/HOLD/REJECT gates |
| Volume 3 | Windows + Tauri architecture and ResearchCore Engine bridge | Desktop bridge and packaging milestones |
| Volume 4 | Dataset Studio and DatasetCapabilityMap | Dataset intake and capability-proof milestones |
| Volume 5 | Logic Factory, LogicCard, compiler/generator boundary | Logic compiler and test-plan bridge milestones |
| Volume 6 | Visual Replay, Evidence Cards, audit-decision UX | Replay/evidence/audit UX milestones |

### Volume 7 interpretation rule

```text
Volumes 0–6 are draft canonical project sources until imported into the repo through an audited setup ticket.
```

They should guide the next step, but they are not yet executable truth inside `research-core`.

---

## 3. Roadmap philosophy

NullForge should advance by **vertical proof slices**, not by building whole layers in isolation.

The roadmap should prioritize:

1. **Source-of-truth import before code.**
2. **Bridge proof before feature expansion.**
3. **Dataset capability proof before chart/test generation.**
4. **Compiler contract before generator.**
5. **Replay fixture before replay claims.**
6. **Evidence Card before promotion UI.**
7. **Packaging spike before public distribution.**

### Roadmap anti-patterns to block

```text
- Build the whole desktop app at once.
- Add Tauri, frontend, dataset import, logic generation, replay, and packaging in one milestone.
- Treat the UI as source of truth.
- Let Codex invent strategy or acceptance criteria.
- Build visual charts before evidence boundaries.
- Generate strategy logic before compiler/quarantine rules.
- Commit raw ES.zip.
- Add live trading, broker APIs, cloud sync, auth, billing, marketplace, mobile, or public release as MVP work.
```

---

## 4. MVP vertical slice recap

The MVP vertical slice is:

```text
User opens NullForge on Windows 11 x64
→ creates or selects a local workspace
→ imports or uses a small ES-derived OHLCV fixture
→ sees a DatasetCapabilityMap
→ runs one ResearchCore Engine smoke command through the desktop bridge
→ views produced artifact metadata
→ opens one visual replay fixture with signal / entry / SL / TP / exit labels
→ sees an audit / decision placeholder
```

### MVP claim focus

The first implementation stream tests whether NullForge can become a real local desktop research workbench around the existing ResearchCore Engine.

It does **not** test:

```text
market edge
retention
commercial demand
public distribution
live trading readiness
AI strategy generation
multi-user collaboration
```

---

## 5. Active source-of-truth docs to create in repo

The first milestone should create or update these canonical docs without overwriting existing ResearchCore Engine docs silently.

| Doc | Proposed path | Purpose | First action |
|---|---|---|---|
| Current status | `docs/nullforge/CURRENT_STATUS.md` | One active status for NullForge work | Create |
| Mission brief | `docs/nullforge/MISSION_BRIEF.md` | Canonical NullForge thesis and MVP loop | Create from Volume 0 |
| Claim ledger | `docs/nullforge/CLAIM_LEDGER.md` | NullForge claim IDs, evidence status, kill conditions | Create from Volume 0 |
| Decision ledger | `docs/nullforge/DECISION_LEDGER.md` | Product/architecture decisions and reversal conditions | Create seed |
| Roadmap | `docs/nullforge/ROADMAP.md` | Milestones, dependencies, ticket sequence | Create from Volume 7 |
| Volume index | `docs/nullforge/blueprint/README.md` | Navigation for Volumes 0–7 | Create |
| Volumes | `docs/nullforge/blueprint/volumes/` | Canonical project planning volumes | Import reviewed copies |
| ADR directory | `docs/nullforge/adr/` | Stack, name, data, sidecar decisions | Create |
| Data policy | `docs/nullforge/data/DATA_POLICY.md` | ES.zip, fixture, raw/imported/canonical boundaries | Create from Volume 4 |
| Desktop architecture | `docs/nullforge/architecture/DESKTOP_ARCHITECTURE.md` | Tauri/Windows/bridge structure | Create from Volume 3 |
| Bridge contract | `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md` | Scoped command protocol | Create from Volume 3 |
| Dataset capability contract | `docs/nullforge/data/DATASET_CAPABILITY_MAP.md` | YES/NO/APPROXIMATE/AMBIGUOUS rules | Create from Volume 4 |
| Logic lifecycle | `docs/nullforge/logic/LOGIC_LIFECYCLE.md` | LogicCard → compile → TestPlan → EvidenceCard | Create from Volume 5 |
| Replay/evidence spec | `docs/nullforge/evidence/REPLAY_AND_EVIDENCE_BOUNDARY.md` | Visual Replay and Evidence Card rules | Create from Volume 6 |
| Codex workflow | `docs/nullforge/codex/CODEX_ROLE_LOOP.md` | NullForge-specific role-loop instructions | Create from Volume 2 |
| QA/human gates | `docs/nullforge/qa/HUMAN_GATES.md` | Stop conditions and sensitive change review | Create from Volume 2/3/4/5/6 |
| Prompt archive | `prompts/nullforge/ARCHIVE/` | Store used prompts as history, not truth | Create |
| Milestones | `milestones/nullforge/` | Milestone packs and handoffs | Create |
| Tickets | `tickets/nullforge/` | Ticket files | Create |

### Path note

Use `docs/nullforge/` unless repo inventory shows a better existing convention. The first repo import ticket should inspect `research-core` before deciding final paths.

---

## 6. Recommended milestone map

| Milestone | Name | Purpose | Ticket count target | Status |
|---|---|---|---:|---|
| `M0` | Repo Source Import + Canonical Baseline | Import reviewed NullForge volumes into repo docs and create source-of-truth skeleton. | 5–7 | NEXT |
| `M1` | Desktop Shell + ResearchCore Engine Bridge Proof | Prove Windows/Tauri shell can call a safe engine command and show artifact metadata. | 4–6 | PLANNED |
| `M2` | Dataset Studio Fixture + DatasetCapabilityMap Proof | Prove tiny/small OHLCV fixture intake and lawful capability map. | 5–7 | PLANNED |
| `M3` | Logic Factory Compiler Proof | Prove one handwritten LogicCard compiles to a test-plan-ready spec, without generator trust. | 5–7 | PLANNED |
| `M4` | Visual Replay Fixture Proof | Prove one replay fixture renders signal/entry/SL/TP/exit with known-at-time and ambiguity labels. | 4–6 | PLANNED |
| `M5` | Evidence Card + Audit Placeholder Proof | Prove one EvidenceCard links artifacts, null/baseline placeholders, limitations, and decision state. | 4–6 | PLANNED |
| `M6` | Windows Packaging Spike | Prove Windows 11 x64 package path and sidecar feasibility without public distribution. | 3–5 | PLANNED |
| `M7` | MVP Integration Polish | Connect M1–M5 into one narrow demo workflow. | 5–8 | DEFERRED |
| `M8` | Local User Trial | Run owner-facing local trial against MVP proof loop. | 3–5 | DEFERRED |

---

## 7. Milestone dependency order

```text
M0 Repo Source Import
  ↓
M1 Desktop Shell + Engine Bridge Proof
  ↓
M2 Dataset Studio Fixture + DatasetCapabilityMap Proof
  ↓
M3 Logic Factory Compiler Proof
  ↓
M4 Visual Replay Fixture Proof
  ↓
M5 Evidence Card + Audit Placeholder Proof
  ↓
M6 Windows Packaging Spike
  ↓
M7 MVP Integration Polish
  ↓
M8 Owner Trial / First Validation Pass
```

### Dependency rules

| Rule | Meaning |
|---|---|
| `M0` blocks all implementation | Repo truth must exist before Codex builds. |
| `M1` blocks most UI work | Bridge proof is the highest-risk technical path. |
| `M2` blocks real dataset tests | DatasetCapabilityMap must gate timeframe/chart/test claims. |
| `M3` blocks generator work | Compiler contract must exist before generated variants matter. |
| `M4` depends on M2/M3 fixtures | Replay needs lawful data and candidate/test metadata. |
| `M5` depends on evidence boundaries | Evidence Card must not imply proof from replay alone. |
| `M6` can begin after M1 | Packaging proof needs shell/sidecar baseline, not full product. |

---

## 8. Ticket namespace policy recap

| Prefix | Track | Examples |
|---|---|---|
| `PF` | Project Factory / source setup | `PF-T000` repo import, `PF-T001` status docs |
| `ADR` | Architecture/product decisions | `ADR-T001` name/stack, `ADR-T002` local-first |
| `CX` | Codex workflow | `CX-T001` role-loop docs, `CX-T002` prompt templates |
| `DA` | Desktop app / Tauri / sidecar | `DA-T001` bridge contract, `DA-T002` shell smoke |
| `WB` | Workbench shell / artifact cockpit | `WB-T001` artifact metadata viewer |
| `DS` | Dataset Studio | `DS-T001` fixture policy, `DS-T002` capability map |
| `DCM` | DatasetCapabilityMap | `DCM-T001` contract, `DCM-T002` tests |
| `LF` | Logic Factory | `LF-T001` LogicCard contract, `LF-T002` compiler dry-run |
| `VR` | Visual Replay | `VR-T001` replay fixture, `VR-T002` ambiguity display |
| `EV` | Evidence Cards / decisions | `EV-T001` EvidenceCard schema, `EV-T002` decision placeholder |
| `QA` | QA/security/gates | `QA-T001` test discovery, `QA-T002` security gates |
| `PKG` | Packaging / Windows installer | `PKG-T001` packaging spike |
| `MB` | Milestone batch/handoff | `MB-T001` M0 package, `MB-T002` M1 package |

Do not reuse unprefixed `T000`/`T001` labels. App Forge tickets and Project Factory tickets are different things.

---

## 9. First 38-ticket backlog

This is the seed backlog. It is **not** permission to run all tickets at once.

| Order | Ticket | Milestone | Title | Type | Purpose | Depends on | Human gate |
|---:|---|---|---|---|---|---|---|
| 1 | `PF-T000` | M0 | Repo inventory and NullForge import plan | Docs/audit | Inspect `research-core`, choose canonical paths, avoid overwrites. | Vol 0–7 | Yes |
| 2 | `PF-T001` | M0 | Import NullForge volumes into repo docs | Docs | Add reviewed Volumes 0–7 under project-specific docs. | PF-T000 | Yes |
| 3 | `PF-T002` | M0 | Create NullForge current status and source index | Docs | Create `CURRENT_STATUS`, volume index, source map. | PF-T001 | Yes |
| 4 | `ADR-T001` | M0 | Name/platform/stack/engine ADR | Docs | Record NullForge, Windows 11 x64, Tauri, ResearchCore Engine boundary. | PF-T001 | Yes |
| 5 | `ADR-T002` | M0 | Local-first/no-cloud MVP ADR | Docs | Record local-first MVP stance and anti-goals. | PF-T001 | Yes |
| 6 | `CX-T001` | M0 | NullForge Codex role-loop docs | Docs | Adapt context-curator → planner → implementor → auditor workflow to repo. | PF-T002 | Yes |
| 7 | `MB-T001` | M0 | M0 milestone handoff | Docs/audit | Summarize imported docs, decisions, next milestone readiness. | PF-T000–CX-T001 | Yes |
| 8 | `QA-T001` | M1 | Existing repo command and test discovery | Docs/audit | Discover test/run commands, Python env blockers, no code changes. | M0 PASS | Yes if blockers |
| 9 | `DA-T001` | M1 | Desktop bridge contract finalization | Docs | Convert Volume 3 bridge draft into scoped command contract. | M0 PASS | Yes |
| 10 | `DA-T002` | M1 | Tauri app scaffold plan | Planning | Plan minimal Windows/Tauri shell without implementing yet. | DA-T001 | Yes |
| 11 | `DA-T003` | M1 | Tauri shell smoke implementation | Implementation | Create minimal shell that opens locally. | DA-T002 | Dependency gate |
| 12 | `DA-T004` | M1 | Engine command bridge smoke | Implementation | Invoke one allowed ResearchCore Engine smoke command safely. | DA-T003 | Security gate |
| 13 | `WB-T001` | M1 | Artifact metadata read-only viewer | Implementation | Display bridge-produced artifact metadata read-only. | DA-T004 | No |
| 14 | `MB-T002` | M1 | Desktop bridge proof audit/handoff | Audit | Record bridge result, failures, next gates. | DA-T003–WB-T001 | Yes |
| 15 | `DS-T001` | M2 | Dataset Studio object and manifest contract | Docs | Define dataset manifest fields and fixture paths. | M1 PASS | Yes |
| 16 | `DS-T002` | M2 | ES.zip fixture policy and local exclusion check | Docs/audit | Confirm raw data stays local/outside repo; define fixture rules. | DS-T001 | Yes |
| 17 | `DS-T003` | M2 | Tiny OHLCV fixture selection or synthetic fallback | Data/test | Create or select tiny fixture if license-safe; synthetic fallback if not. | DS-T002 | Data gate |
| 18 | `DCM-T001` | M2 | DatasetCapabilityMap schema/contract | Docs/test | Define statuses and output shape. | DS-T001 | Yes |
| 19 | `DCM-T002` | M2 | DatasetCapabilityMap dry-run fixture | Implementation/test | Produce YES/NO/AMBIGUOUS/REQUIRES_CONFIRMATION outputs for fixture. | DCM-T001, DS-T003 | No |
| 20 | `MB-T003` | M2 | Dataset Studio proof audit/handoff | Audit | Record fixture/capability proof result. | DS/DCM tickets | Yes |
| 21 | `LF-T001` | M3 | LogicCard schema and lifecycle docs | Docs | Formalize raw idea → LogicCard states. | M2 PASS | Yes |
| 22 | `LF-T002` | M3 | Compiler validation contract | Docs | Define required fields, no-leakage checks, failure modes. | LF-T001 | Yes |
| 23 | `LF-T003` | M3 | Handwritten LogicCard fixture | Test/doc | Create one non-executable candidate spec fixture. | LF-T002, DCM-T002 | Yes if market claim risk |
| 24 | `LF-T004` | M3 | Compile dry-run report | Implementation/test | Compile fixture to CompiledLogicSpec or clear failure report. | LF-T003 | No |
| 25 | `LF-T005` | M3 | Null/ablation placeholder policy wiring | Docs/test | Ensure nulls/ablations are required in TestPlan, not optional decoration. | LF-T004 | No |
| 26 | `MB-T004` | M3 | Logic Factory proof audit/handoff | Audit | Record compiler proof status and generator deferrals. | LF tickets | Yes |
| 27 | `VR-T001` | M4 | Visual Replay object and fixture spec | Docs | Define replay fixture fields and labels. | M3 PASS | Yes |
| 28 | `VR-T002` | M4 | Replay fixture generation or static fixture | Test/data | Produce one replay fixture without claiming edge. | VR-T001 | No |
| 29 | `VR-T003` | M4 | Read-only Visual Replay screen | Implementation | Render fixture with signal/entry/SL/TP/exit labels. | VR-T002, DA/WB baseline | UI gate |
| 30 | `VR-T004` | M4 | Known-at-time and ambiguity labels | Implementation/test | Add labels that prevent future-data confusion. | VR-T003 | No |
| 31 | `MB-T005` | M4 | Visual Replay proof audit/handoff | Audit | Record replay proof and limitations. | VR tickets | Yes |
| 32 | `EV-T001` | M5 | EvidenceCard schema and decision states | Docs | Define aggregate/null/ablation/failure/decision fields. | M4 PASS | Yes |
| 33 | `EV-T002` | M5 | EvidenceCard fixture | Test/doc | Create one placeholder EvidenceCard linked to fixture artifacts. | EV-T001 | No |
| 34 | `EV-T003` | M5 | EvidenceCard read-only view | Implementation | Display evidence and decision placeholder without proof inflation. | EV-T002 | UI/trust gate |
| 35 | `MB-T006` | M5 | Evidence/audit proof handoff | Audit | Decide readiness for integration/polish. | EV tickets | Yes |
| 36 | `PKG-T001` | M6 | Windows packaging spike plan | Docs/spike | Plan package build and sidecar inclusion test. | M1 PASS | Yes |
| 37 | `PKG-T002` | M6 | Local unsigned Windows build spike | Implementation/spike | Prove local Windows build path; no public distribution. | PKG-T001 | Release gate |
| 38 | `PKG-T003` | M6 | Packaging spike audit/handoff | Audit | Record feasibility, blockers, signing/updater deferrals. | PKG-T002 | Yes |

---

## 10. Ticket acceptance template

~~~markdown
# [TICKET_ID] — [Title]

## Type

Docs / ADR / planning / implementation / test / audit / packaging spike

## Milestone

M# — [Name]

## Purpose

What this ticket proves or prepares.

## Inputs

- Active source docs:
- Prior tickets:
- Relevant repo files:
- Known constraints:

## Outputs

- Required files/artifacts:
- Updated status docs:
- Reports/audits:

## Scope

Allowed actions:

```text

```

Allowed files/folders:

```text

```

## Out of scope / forbidden actions

```text

```

## Acceptance criteria

- [ ] Criterion is observable.
- [ ] Required artifact exists.
- [ ] Source-of-truth update is included if needed.
- [ ] Human gate status is recorded.
- [ ] Tests/checks are run or skipped with reason.
- [ ] Next ticket is named.

## Required tests / checks

```text
[commands/checks or "docs review only"]
```

## Human gate triggers

```text

```

## Required role-loop artifacts

```text
prompts/[TICKET_ID]/00_CONTEXT_CURATOR_PROMPT.md
prompts/[TICKET_ID]/01_PLANNER_PROMPT.md
plans/[TICKET_ID]/CONTEXT_BUNDLE.md
plans/[TICKET_ID]/CONTEXT_BUNDLE_MANIFEST.md
plans/[TICKET_ID]/PLAN.md
plans/[TICKET_ID]/ACCEPTANCE.md
plans/[TICKET_ID]/IMPLEMENTOR_PROMPT.md
reports/[TICKET_ID]/IMPLEMENTATION_REPORT.md
reports/[TICKET_ID]/CHANGED_FILES.md
reports/[TICKET_ID]/TEST_RESULTS.md
audits/[TICKET_ID]/AUDIT_REPORT.md
audits/[TICKET_ID]/FINDINGS.md
audits/[TICKET_ID]/REPAIR_PROMPT.md
```

## Done definition

```text
PASS audit or human-approved deferral.
```
~~~

### Docs-only compression rule

Docs-only tickets may compress implementation artifacts into a single report, but must still preserve:

```text
context → plan → change/report → audit → decision
```

A docs-only ticket is still not done until it has acceptance criteria and an audit verdict.

---


## 11. Milestone batching policy

### Operating sentence

```text
Batch the prompts.
Execute tickets serially.
Audit every pass.
Return at milestone gates.
```

### Allowed batching

A milestone batch may include:

```text
MILESTONE_BRIEF.md
TICKET_QUEUE.md
DEPENDENCY_MAP.md
CONTEXT_REFRESH_RULES.md
HUMAN_GATE_TRIGGERS.md
MILESTONE_ACCEPTANCE.md
MILESTONE_HANDOFF_TEMPLATE.md
MILESTONE_AUDIT_PROMPT.md
Ticket files
Context Curator prompts
Planner prompts
Implementor prompt placeholders or planner-generated implementor prompts
Auditor prompt requirements or implementor-generated auditor prompts
```

### Not allowed

A milestone batch may not:

```text
execute implementation by itself
skip per-ticket branches
skip context curation
skip planning
skip acceptance criteria
skip audits
merge without human approval
auto-release
silently expand scope
```

---

## 12. M0 first milestone package plan

```text
M0 — Repo Source Import + Canonical Baseline
```

### Goal

Promote the generated NullForge planning volumes into the `research-core` repo as project-specific current docs without overwriting existing ResearchCore Engine truth.

### Tickets

```text
PF-T000 — Repo inventory and NullForge import plan
PF-T001 — Import NullForge volumes into repo docs
PF-T002 — Create NullForge current status and source index
ADR-T001 — Name/platform/stack/engine ADR
ADR-T002 — Local-first/no-cloud MVP ADR
CX-T001 — NullForge Codex role-loop docs
MB-T001 — M0 milestone handoff
```

### Explicit non-goals

```text
No Tauri app.
No engine changes.
No dataset parser.
No fixture creation.
No desktop bridge implementation.
No public release.
No repo rename.
```

### Acceptance

```text
- NullForge docs have canonical repo paths.
- Existing ResearchCore Engine docs are not silently overwritten.
- Current status points to active NullForge phase and next milestone.
- Decisions for name/platform/stack/local-first are recorded with reversal conditions.
- Codex role-loop docs exist or are mapped to existing project docs.
- M1 readiness is explicit.
```

---

## 13. M1 desktop bridge proof package plan

```text
M1 — Desktop Shell + ResearchCore Engine Bridge Proof
```

### Goal

Prove a minimal Windows/Tauri desktop shell can safely call one scoped ResearchCore Engine command and show read-only artifact metadata.

### Ticket candidates

```text
QA-T001 — Existing repo command and test discovery
DA-T001 — Desktop bridge contract finalization
DA-T002 — Tauri app scaffold plan
DA-T003 — Tauri shell smoke implementation
DA-T004 — Engine command bridge smoke
WB-T001 — Artifact metadata read-only viewer
MB-T002 — Desktop bridge proof audit/handoff
```

### Proof target

```text
Open app → run one allowed bridge command → produce/read artifact metadata → no arbitrary shell execution → audit result recorded.
```

---

## 14. M2 Dataset Studio fixture/capability proof package plan

```text
M2 — Dataset Studio Fixture + DatasetCapabilityMap Proof
```

### Goal

Prove NullForge can handle a tiny/small OHLCV fixture and generate a truthful DatasetCapabilityMap before any timeframe/chart/test generation.

### Ticket candidates

```text
DS-T001 — Dataset Studio object and manifest contract
DS-T002 — ES.zip fixture policy and local exclusion check
DS-T003 — Tiny OHLCV fixture selection or synthetic fallback
DCM-T001 — DatasetCapabilityMap schema/contract
DCM-T002 — DatasetCapabilityMap dry-run fixture
MB-T003 — Dataset Studio proof audit/handoff
```

### Proof target

```text
Fixture selected/imported → manifest exists → DatasetCapabilityMap reports YES/NO/APPROXIMATE/AMBIGUOUS/REQUIRES_CONFIRMATION/QUARANTINE honestly.
```

---

## 15. M3 Logic Factory compiler proof package plan

```text
M3 — Logic Factory Compiler Proof
```

### Goal

Prove one handwritten LogicCard can be compiled or rejected with a clear report, while generated logic remains quarantined.

### Ticket candidates

```text
LF-T001 — LogicCard schema and lifecycle docs
LF-T002 — Compiler validation contract
LF-T003 — Handwritten LogicCard fixture
LF-T004 — Compile dry-run report
LF-T005 — Null/ablation placeholder policy wiring
MB-T004 — Logic Factory proof audit/handoff
```

### Proof target

```text
Raw candidate idea → LogicCard fixture → compiler checks timing/no-leakage/capability dependency → CompiledLogicSpec or failure report → null/ablation requirements visible.
```

---

## 16. M4 Visual Replay fixture proof package plan

```text
M4 — Visual Replay Fixture Proof
```

### Goal

Prove one read-only Visual Replay fixture can display signal, known-at-time information, entry, SL, TP, exit, and ambiguity labels without implying strategy validity.

### Ticket candidates

```text
VR-T001 — Visual Replay object and fixture spec
VR-T002 — Replay fixture generation or static fixture
VR-T003 — Read-only Visual Replay screen
VR-T004 — Known-at-time and ambiguity labels
MB-T005 — Visual Replay proof audit/handoff
```

### Proof target

```text
Replay fixture opens → chart/path labels render → known_at and ambiguity labels visible → no result screen implies edge or financial advice.
```

---

## 17. M5 Evidence Card/audit placeholder proof package plan

```text
M5 — Evidence Card + Audit Placeholder Proof
```

### Goal

Prove one EvidenceCard can connect candidate/run/artifact/replay metadata with nulls, ablations, sample size, limitations, failure modes, and a decision placeholder.

### Ticket candidates

```text
EV-T001 — EvidenceCard schema and decision states
EV-T002 — EvidenceCard fixture
EV-T003 — EvidenceCard read-only view
MB-T006 — Evidence/audit proof handoff
```

### Proof target

```text
EvidenceCard opens → shows aggregate fields and limitations → decision state is placeholder/audit-gated → no replay-only promotion.
```

---

## 18. M6 Windows packaging spike package plan

```text
M6 — Windows Packaging Spike
```

### Goal

Prove the local Windows 11 x64 packaging path is feasible for the Tauri shell plus ResearchCore Engine bridge, without public release or installer signing as MVP requirements.

### Ticket candidates

```text
PKG-T001 — Windows packaging spike plan
PKG-T002 — Local unsigned Windows build spike
PKG-T003 — Packaging spike audit/handoff
```

### Proof target

```text
Local Windows package builds or fails with clear report → sidecar inclusion risk recorded → signing/updater/public release deferred.
```

---

## 19. Context Curator prompt pattern for NullForge tickets

~~~markdown
# Context Curator Prompt: [TICKET_ID] — [TITLE]

You are the Context Curator for this NullForge repo ticket.

Your job is to gather the smallest sufficient active context. You do not plan implementation. You do not code. You do not invent strategy.

## Repo

```text
Repo:
Current branch/main status:
Ticket file:
Current status doc:
Prior audit/repair state, if any:
```

## Active source docs to inspect

```text
Relevant NullForge volumes:
Relevant ADRs:
Relevant source docs:
```

## Relevant repo files/folders

```text
[List the minimum needed. Do not include repo swamp.]
```

## Known commands

```text
Test/check commands:
Run command, if relevant:
```

## Forbidden actions

```text
No coding.
No implementation planning.
No product strategy invention.
No broad context dump.
No stale prompt as active truth.
```

## Required outputs

```text
plans/[TICKET_ID]/CONTEXT_BUNDLE.md
plans/[TICKET_ID]/CONTEXT_BUNDLE_MANIFEST.md
```

## Context bundle must include

- ticket summary;
- mission slice;
- active source docs;
- relevant repo files/folders;
- current repo state summary;
- constraints and forbidden actions;
- required tests/checks;
- human gate triggers;
- open questions.

## Return

```text
Created files:
Included context:
Excluded context:
Open questions:
Ready for planner? YES/NO
```
~~~

---


## 20. Planner prompt pattern for NullForge tickets

~~~markdown
# Planner Prompt: [TICKET_ID] — [TITLE]

You are the Planner for this NullForge repo ticket.

Read:

```text
plans/[TICKET_ID]/CONTEXT_BUNDLE.md
plans/[TICKET_ID]/CONTEXT_BUNDLE_MANIFEST.md
```

You do not code. You produce a bounded plan, acceptance criteria, and implementor prompt.

## Required outputs

```text
plans/[TICKET_ID]/PLAN.md
plans/[TICKET_ID]/ACCEPTANCE.md
plans/[TICKET_ID]/IMPLEMENTOR_PROMPT.md
```

## Plan must include

- purpose;
- source context used;
- scope;
- forbidden actions;
- likely files changed;
- implementation or docs steps;
- tests/checks required;
- security/privacy/data/file-access considerations;
- rollback/repair route;
- human gate triggers.

## Acceptance must include

- testable criteria;
- required commands/checks;
- docs update expectations;
- done definition;
- auditor focus.

## Return

```text
Plan path:
Acceptance path:
Implementor prompt path:
Risks:
Ready for implementor? YES/NO
```
~~~

---


## 21. Implementor prompt pattern for NullForge tickets

~~~markdown
# Implementor Prompt: [TICKET_ID] — [TITLE]

You are the scoped implementor for this NullForge repo ticket.

Follow exactly:

```text
plans/[TICKET_ID]/PLAN.md
plans/[TICKET_ID]/ACCEPTANCE.md
```

Do not invent product strategy. Do not broaden scope. Do not modify unrelated files. Do not add dependencies without explicit approval. Do not commit secrets. Do not merge or release.

## Allowed files/folders

```text
[LIST]
```

## Forbidden files/folders/actions

```text
[LIST]
```

## Required outputs

```text
reports/[TICKET_ID]/IMPLEMENTATION_REPORT.md
reports/[TICKET_ID]/CHANGED_FILES.md
reports/[TICKET_ID]/TEST_RESULTS.md
reports/[TICKET_ID]/AUDITOR_PROMPT.md
```

## Tests/checks

```text
[COMMANDS OR REVIEW CHECKS]
```

If tests cannot be run, explain exactly why.

## Return

```text
Branch:
Files changed:
Commands/checks run:
Tests passed/failed/skipped:
Acceptance status:
Known issues:
Auditor prompt path:
Human gate triggered? YES/NO
```
~~~

---


## 22. Auditor prompt pattern for NullForge tickets

~~~markdown
# Auditor Prompt: [TICKET_ID] — [TITLE]

You are the Auditor for this NullForge ticket. Use a fresh pass/session when possible.

Read:

```text
plans/[TICKET_ID]/CONTEXT_BUNDLE.md
plans/[TICKET_ID]/PLAN.md
plans/[TICKET_ID]/ACCEPTANCE.md
reports/[TICKET_ID]/IMPLEMENTATION_REPORT.md
reports/[TICKET_ID]/CHANGED_FILES.md
reports/[TICKET_ID]/TEST_RESULTS.md
```

Audit the implementation against the ticket, source-of-truth doctrine, acceptance criteria, tests, and safety/security/data constraints.

## Required outputs

```text
audits/[TICKET_ID]/AUDIT_REPORT.md
audits/[TICKET_ID]/FINDINGS.md
audits/[TICKET_ID]/REPAIR_PROMPT.md
```

## Verdict

Return exactly one:

```text
PASS
HOLD
REJECT
```

## Check

- scope matched ticket;
- forbidden files/actions avoided;
- tests/checks run or skipped with reason;
- acceptance criteria satisfied;
- docs/source-of-truth updated if behavior changed;
- no secrets committed;
- no silent dependency/migration/auth/permission changes;
- no product strategy invention;
- human gate triggers identified.

## Return

```text
Verdict:
Blocking findings:
Non-blocking findings:
Repair prompt path, if needed:
Human decision needed:
```
~~~

---


## 23. Human gate and stop-condition matrix

| Trigger | Stop? | Required human action |
|---|---:|---|
| Dependency added or upgraded | Yes | Review package, reason, alternatives, risk. |
| New Tauri permission / file access broadened | Yes | Review least-privilege boundary. |
| Python sidecar command surface expanded | Yes | Review command allowlist and shell-execution risk. |
| Full ES.zip or large data added to repo | Yes | Block unless explicit approved exception. |
| Fixture derived from proprietary data | Yes | License/privacy/source review. |
| Public distribution / installer upload | Yes | Legal/name/release review. |
| Signing/updater changes | Yes | Release/security review. |
| Auth/cloud/sync/accounts introduced | Yes | Scope reset; likely new volume/ADR. |
| Broker/live trading integration | Yes | Explicitly out of MVP; requires new project phase. |
| AI strategy generation or executable AI output | Yes | Requires new AI boundary and eval plan. |
| Test failure alters architecture assumption | Yes | Audit and repair plan. |
| Source-of-truth conflict | Yes | Librarian repair pass. |
| Broad refactor requested by Codex | Yes | New ticket only. |
| Security/privacy concern | Yes | Security review. |
| Documentation-only typo | No | Can be fixed in scoped docs ticket. |

---

## 24. QA/test command discovery plan

Before implementation tickets, run `QA-T001` to discover actual repo commands.

### QA-T001 should identify

```text
Python version
package manager
virtual environment expectation
test command(s)
lint/type commands
existing CLI commands
existing smoke tests
whether pyarrow or other dependencies block local tests
where fixtures/samples currently live
how docs are organized
whether existing CI exists
```

### Initial command candidates to verify, not assume

```text
python --version
python -m pytest
python -m pip show research-core
python -m pip show pyarrow
python -m research_core --help
research-core --help
```

### QA-T001 output

```text
docs/nullforge/qa/COMMAND_DISCOVERY.md
reports/nullforge/QA-T001/TEST_RESULTS.md
```

No later ticket should invent test commands if QA-T001 has already established them.

---

## 25. First milestone handoff template

~~~markdown
# Milestone Handoff: M0 — Repo Source Import + Canonical Baseline

## Summary

```text
Goal:
Result:
Overall status: COMPLETE / PARTIAL / BLOCKED / REPAIR_NEEDED
```

## Tickets

| Ticket | Branch | Verdict | PR/commit | Notes |
|---|---|---|---|---|
| PF-T001 |  | PASS/HOLD/REJECT |  |  |
| PF-T002 |  | PASS/HOLD/REJECT |  |  |
| PF-T003 |  | PASS/HOLD/REJECT |  |  |
| PF-T004 |  | PASS/HOLD/REJECT |  |  |
| ADR-T001 |  | PASS/HOLD/REJECT |  |  |
| CX-T001 |  | PASS/HOLD/REJECT |  |  |
| QA-T001 |  | PASS/HOLD/REJECT |  |  |

## Artifacts produced

```text
Plans:
Reports:
Audits:
Docs updated:
Code changed:
```

## Tests/checks

```text
Commands run:
Passed:
Failed:
Skipped with reason:
```

## Scope drift

```text
Expected:
Actual:
Drift:
Action:
```

## Human decisions needed

```text
Decision:
Why:
Options:
Recommendation:
```

## Claims / risks / decisions updated

```text
Claims:
Risks:
Decisions:
Source-of-truth changes:
```

## Next recommended batch

```text
Next milestone:
Suggested tickets:
Known blockers:
```
~~~

---


## 26. What should happen before Codex implementation begins

Before any implementation ticket such as `DA-T003`, complete:

```text
1. Review Volume 7 package.
2. Generate M0 milestone batch package.
3. Import Volumes 0–7 into repo through M0 tickets.
4. Create/update docs/nullforge/CURRENT_STATUS.md.
5. Create initial ADRs for name/platform/stack/local-first.
6. Create NullForge Codex role-loop docs.
7. Discover actual repo test/run commands.
8. Confirm active ticket queue and human gates.
9. Start M1 only after M0 PASS or human-approved deferral.
```

### Important distinction

```text
Volume generation is planning.
Repo-source import is governance.
Implementation starts only after governance is in place.
```

---

## 27. What should not be automated

Do not automate:

```text
merge decisions
release decisions
public installer distribution
name/trademark/legal approval
license review for ES-derived fixtures
live trading or broker integration
AI strategy generation activation
cloud sync/auth/billing scope changes
security/privacy boundary expansion
claim promotion
financial advice statements
large refactors
raw data deletion
full ES.zip commit
```

---

## 28. Volume 7 closeout

```text
Volume 7 status: COMPLETE_DRAFT
Decision: PROMOTE_TO_M0_REPO_SOURCE_IMPORT_AFTER_REVIEW
Current project phase: PROJECT_FACTORY_SETUP → REPO_SOURCE_IMPORT_PENDING
Next artifact: M0 Repo Source Import + Canonical Baseline milestone package
Next prompt: NullForge Prompt for M0 Repo Source Import Pass v0.4
Implementation code generated: NO
Codex execution started: NO
```

### What survives into M0

```text
NullForge working name
Windows 11 x64 first
Tauri + React + TypeScript
ResearchCore Engine as scoped Python sidecar / bridge
local-first workspace
DatasetCapabilityMap before tests/charts
LogicCard compiler before generator
Visual Replay as explanatory, not proof
EvidenceCard as aggregate/audit boundary
context-curator → planner → implementor → auditor role loop
milestone batching with serial ticket execution
```

### What remains deferred

```text
public release
installer signing/updater
AI strategy generation
broker/live trading
cloud sync/auth/billing/mobile/marketplace
full ES.zip in repo
repo rename
```

---

## 29. Exact next prompt — M0 repo-source import pass

Save and run the companion file:

```text
prompts/NullForge_Prompt_For_M0_Repo_Source_Import_Pass_v0_4.md
```

That prompt should generate the first milestone package, not implementation code.

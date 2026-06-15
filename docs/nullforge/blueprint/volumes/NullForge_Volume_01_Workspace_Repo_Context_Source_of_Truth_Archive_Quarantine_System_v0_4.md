> Import note: This file was imported by PF-T001 from `NullForge_Volume_01_v0_4_Package.zip` / `NullForge_Volume_01_v0_4_Package/artifacts/NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md` on `2026-06-15`.
> Authority: repo-managed NullForge planning/workflow source after PF-T001 audit. It is not ResearchCore Engine implementation truth.
> Source package SHA256: `69A09D04B563C5813F3C559AE0775A1351AE5C605371631C0E6841DD3C0DBD89`

# Volume 1 — NullForge Workspace, Repo, Context, Source-of-Truth, Archive, and Quarantine System v0.4

**Project:** NullForge  
**Existing repo / engine:** `research-core`  
**Internal engine label:** ResearchCore Engine  
**First platform:** Windows 11 x64  
**Desktop stack:** Tauri + React + TypeScript  
**Engine boundary:** Existing Python ResearchCore Engine as local sidecar / command bridge  
**Volume status:** Draft canonical project source after human review / promotion  
**Generated:** 2026-06-14

---

## 0. Volume authority

This volume defines the workspace, repo, context, archive, and quarantine operating system for NullForge. It does **not** implement the desktop app, sidecar bridge, dataset importer, logic compiler, visual replay, or evidence card system.

```text
Volume 0 decides what NullForge is.
Volume 1 decides where truth lives, where old material goes, and what context is allowed into future work.
Volume 2 will decide how Codex roles execute tickets without context soup or self-auditing.
```

---

## 1. Volume purpose

Volume 1 exists to keep NullForge from becoming a fog bank of chat decisions, stale prompts, duplicated docs, raw datasets, and unbounded Codex context.

It defines:

1. repo and workspace philosophy;
2. the boundary between `research-core` and NullForge;
3. canonical doc locations;
4. local user workspace layout;
5. active source-of-truth rules;
6. archive and quarantine policy;
7. ES.zip and fixture data boundaries;
8. prompt and volume storage policy;
9. ADR / decision ledger policy;
10. claim ledger and validation report policy;
11. context pack types;
12. drift checks;
13. human gates for source-of-truth changes;
14. repair plan for conflicting existing docs;
15. handoff into Volume 2.

### Non-purpose

Volume 1 does not:

```text
write code;
create the Tauri app;
create Python sidecar packaging;
parse ES.zip;
create chart renderers;
write logic compiler schemas;
start Codex implementation;
rename the GitHub repo;
claim public brand availability for NullForge;
commit user datasets;
replace existing ResearchCore Engine docs without audit.
```

---

## 2. Relationship to Volume 0

Volume 0 established the project’s north star:

```text
NullForge is a Windows-first local desktop research workbench that helps a solo research builder import market datasets, map lawful dataset capabilities, compile/generate candidate logic into auditable test specs, run the local ResearchCore Engine, inspect visual trade replays, and decide whether evidence should be promoted, repaired, archived, or quarantined.
```

Volume 1 accepts the following Volume 0 decisions as active planning inputs:

| Volume 0 decision | Volume 1 treatment |
|---|---|
| NullForge is the working product name | Use in planning docs; do not rename repo yet. |
| `research-core` exists | Treat as current engine repo, not blank slate. |
| ResearchCore Engine is internal engine label | Preserve engine identity and avoid product/engine confusion. |
| Windows 11 x64 first | Workspace and packaging docs assume Windows-first. |
| Tauri + React + TypeScript | Store desktop planning docs without implementing yet. |
| Python engine sidecar / command bridge | Document bridge boundary; implementation belongs later. |
| ES.zip local dataset plan | Full raw data stays outside repo; fixtures require explicit policy. |
| DatasetCapabilityMap gates data transformations | Data docs must separate lawful/approximate/impossible capabilities. |
| Compiler before generator | Logic docs must separate draft/generated ideas from compiled specs. |
| Visual replay explains; evidence decides | Replay examples are design/evidence adjuncts, not proof. |
| Evidence before promotion | Claim/decision ledgers must record evidence before authority. |

Volume 1 does **not** treat all prior chat output as source-of-truth. Prior chat artifacts are design memory unless promoted into canonical docs.

---

## 3. Repo / workspace philosophy

### Core rule

```text
Repo = executable truth + current docs.
Workspace = local user data, generated artifacts, private datasets, and runtime state.
Archive = memory without authority.
Quarantine = unresolved/conflicting/risky material without governance power.
Chat = scratch unless promoted.
```

### Why this matters

NullForge will combine:

```text
existing Python engine behavior;
new Tauri desktop app behavior;
local user datasets;
generated capability maps;
generated logic drafts;
compiled logic specs;
test runs;
visual replay examples;
evidence cards;
audits;
Codex reports.
```

Those are not the same kind of truth. A repo doc, a local user dataset, an old prompt, a generated candidate, and a passing test report cannot all have equal authority.

### Operating hierarchy

| Layer | Authority | Can govern implementation? | Notes |
|---|---:|---:|---|
| Promoted repo docs | High | Yes | Current mission, Volume docs, ADRs, tickets, acceptance criteria. |
| Passing audits | High | Yes | Only for scoped artifact / ticket. |
| Source code + tests | High | Yes | Executable truth, subject to docs drift checks. |
| Current status doc | High | Yes | Points to active ticket/state. |
| Decision ledger / ADRs | High | Yes | Must include reversal conditions. |
| Claim ledger | Medium/High | Yes, when promoted | Untested claims cannot govern as truth. |
| Validation reports | Medium/High | Yes, scoped to test | Evidence strength must be recorded. |
| Workspace artifacts | Medium | Sometimes | Runtime artifacts inform, but must be indexed/cited. |
| Vault notes | Medium/Low | No direct authority | Design memory and thinking surface. |
| Graphify output | Medium/Low | No direct authority | Navigation/context map, not truth. |
| Chat | Low | No, unless promoted | Scratchpad and prompt generation surface. |
| Archive | Low | No | Memory only. |
| Quarantine | None | No | Must be reviewed before promotion. |

---

## 4. Existing `research-core` repo boundary

The existing `research-core` repo is not disposable. It is the current engine foundation.

### What `research-core` owns now

| Area | Authority |
|---|---|
| Existing Python package / CLI | Engine implementation truth. |
| Existing tests | Engine regression truth until superseded by audit. |
| Existing schemas/artifacts | Engine artifact contracts unless revised by ticket. |
| Existing README/status docs | Current engine docs, but may need alignment. |
| Existing generated reports | Historical evidence/artifacts, subject to archive/source rules. |

### What NullForge adds

| Area | Relationship to `research-core` |
|---|---|
| Desktop product docs | New product docs, not silent overwrite of engine docs. |
| Tauri app | New app surface; should call engine rather than rewrite it. |
| Desktop bridge | Contract layer between app and engine. |
| Dataset Studio | Product layer over dataset intake/capability mapping. |
| Logic Factory | Product layer over candidate logic lifecycle. |
| Visual Replay | Product layer over test examples/artifacts. |
| Evidence Cards | Product/evidence layer over engine outputs and audits. |
| Packaging | Product distribution layer, Windows-first. |

### Boundary statement

```text
ResearchCore Engine remains the internal artifact/validation engine.
NullForge is the desktop product/workbench that orchestrates and presents the engine.
```

### Non-overwrite rule

NullForge docs may **repair** stale `research-core` docs through tickets, but may not silently overwrite engine identity, public README claims, package names, or architecture status.

### Naming rule

| Name | Use |
|---|---|
| NullForge | User-facing desktop app / planning project name. |
| NullForge Workbench | Main desktop app surface. |
| ResearchCore Engine | Internal Python engine label. |
| `research-core` | Existing repo name until separate ADR approves rename. |

---

## 5. Proposed repo doc layout for NullForge planning docs

This layout is a planning target. It should be introduced through scoped docs tickets, not dumped into the repo all at once unless explicitly approved.

```text
research-core/
├── README.md
├── AGENTS.md                         # later, after Volume 2
├── docs/
│   ├── CURRENT_STATUS.md
│   ├── MISSION_BRIEF.md
│   ├── CLAIM_LEDGER.md
│   ├── RISK_REGISTER.md
│   ├── DECISION_LEDGER.md
│   ├── ROADMAP.md
│   ├── MVP_CUTLINE.md
│   ├── PRODUCT_SPEC.md               # later, after product/UX volumes
│   ├── TECHNICAL_ARCHITECTURE.md      # later, after architecture volumes
│   │
│   ├── nullforge/
│   │   ├── README.md
│   │   ├── NULLFORGE_SCOPE.md
│   │   ├── ENGINE_BOUNDARY.md
│   │   ├── DATASET_STUDIO_BOUNDARY.md
│   │   ├── LOGIC_FACTORY_BOUNDARY.md
│   │   ├── VISUAL_REPLAY_BOUNDARY.md
│   │   └── EVIDENCE_CARD_BOUNDARY.md
│   │
│   ├── blueprint/
│   │   ├── volumes/
│   │   │   ├── Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals.md
│   │   │   ├── Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine.md
│   │   │   └── ...
│   │   ├── setup/
│   │   └── maps/
│   │
│   ├── adr/
│   │   ├── ADR-0001-working-name-nullforge.md
│   │   ├── ADR-0002-windows-11-x64-first.md
│   │   ├── ADR-0003-tauri-react-typescript.md
│   │   └── ADR-0004-researchcore-engine-boundary.md
│   │
│   ├── validation/
│   │   ├── reports/
│   │   ├── experiments/
│   │   └── baselines/
│   │
│   ├── context/
│   │   ├── CONTEXT_PACK_POLICY.md
│   │   ├── CONTEXT_BUNDLE_TEMPLATE.md
│   │   └── CONTEXT_BUNDLE_MANIFEST_TEMPLATE.md
│   │
│   ├── archive/
│   │   ├── prompts/
│   │   ├── outputs/
│   │   ├── status/
│   │   ├── roadmaps/
│   │   ├── superseded-names/
│   │   └── mockups/
│   │
│   └── quarantine/
│       ├── README.md
│       ├── naming/
│       ├── data/
│       ├── generated-logic/
│       ├── legal-privacy/
│       └── conflicting-claims/
│
├── prompts/
│   ├── volumes/
│   ├── codex/
│   ├── milestones/
│   └── archive/
│
├── tickets/
├── milestones/
├── plans/
├── reports/
├── audits/
│
├── data/
│   ├── README.md
│   └── samples/                       # license-safe tiny fixtures only
│
└── design/
    ├── mockups/
    └── archive/
```

### Layout principle

```text
Docs should state whether they govern product, engine, desktop app, dataset, logic, replay, evidence, or Codex workflow.
```

Every NullForge doc should include a short authority header:

```text
Authority: ACTIVE_SOURCE / DRAFT / DESIGN_MEMORY / ARCHIVE_ONLY / QUARANTINE_REVIEW
Governs: product / engine / desktop / dataset / logic / replay / evidence / Codex workflow
Last reviewed:
Reversal condition:
```

---

## 6. Proposed app / workspace layout for local user data

The local user workspace is **not** the Git repo. It is where user/private/runtime state lives.

```text
NullForge_Workspace/
├── workspace.json
├── settings.json
├── README_LOCAL_WORKSPACE.md
│
├── datasets/
│   ├── raw/
│   ├── imported/
│   ├── canonical/
│   ├── fixtures/
│   ├── manifests/
│   └── quarantine/
│
├── capability_maps/
│   ├── active/
│   ├── archived/
│   └── quarantine/
│
├── logic/
│   ├── drafts/
│   ├── compiled/
│   ├── generated/
│   ├── nulls/
│   ├── ablations/
│   ├── manifests/
│   └── quarantined/
│
├── runs/
│   ├── active/
│   ├── completed/
│   ├── failed/
│   └── manifests/
│
├── artifacts/
│   ├── engine/
│   ├── imported/
│   ├── indexed/
│   └── archived/
│
├── evidence/
│   ├── cards/
│   ├── reports/
│   ├── decisions/
│   └── quarantine/
│
├── visual_replay/
│   ├── fixtures/
│   ├── examples/
│   ├── exports/
│   └── review/
│
├── logs/
│   ├── app/
│   ├── engine/
│   ├── bridge/
│   └── audit/
│
├── cache/
│   └── .gitkeep
│
└── backups/
```

### Local workspace rules

| Rule | Reason |
|---|---|
| Raw user datasets stay in workspace, not repo. | Avoid bloat, privacy, licensing issues. |
| Generated artifacts can stay in workspace until curated. | Not every run belongs in source control. |
| Workspace manifests should be hashable where possible. | Reproducibility and auditability. |
| Quarantine exists in workspace too. | Bad/ambiguous data should not enter active flows. |
| Cache is disposable. | Cache should not govern truth. |
| Exports must be explicit. | Prevent accidental publication of private data. |

### Workspace identity file

`workspace.json` should eventually record:

```json
{
  "workspace_id": "local-generated-id",
  "workspace_version": "0.1",
  "created_at": "ISO-8601",
  "app_name": "NullForge",
  "engine_label": "ResearchCore Engine",
  "platform_target": "Windows 11 x64",
  "data_policy": "local-first",
  "repo_link": "optional path or URL",
  "notes": "no secrets here"
}
```

This is a future contract seed, not implementation code.

---

## 7. Source-of-truth map

| Source | Role | Authority | Update trigger | Drift check |
|---|---|---:|---|---|
| Repo docs | Canonical current planning/build truth | High | Volume/ticket/audit/ADR updates | Current docs match status/roadmap/tickets. |
| Repo source code | Executable truth | High | Implementation ticket | Tests/audits pass; docs reflect behavior. |
| Repo tests | Regression truth | High | Code change/test update | Test suite represents current expectations. |
| `docs/CURRENT_STATUS.md` | Current state pointer | High | Every milestone/ticket closeout | Active ticket/artifact matches latest decision. |
| ADRs | Durable major decisions | High | Stack/platform/naming/architecture changes | Every major decision has reversal condition. |
| Claim ledger | Assumptions/evidence authority | Medium/High | Test/validation/audit | Claim statuses reflect evidence. |
| Validation reports | Evidence history | Medium/High | Experiment/test closeout | Claims cite reports. |
| Workspace manifests | Local runtime evidence | Medium | Dataset/run/evidence changes | Hashes/paths/states align. |
| Vault | Design memory | Medium/Low | Human note-making | Active docs cite only promoted material. |
| Graphify | Context/navigation | Medium/Low | Repo/vault graph refresh | Navigation matches actual current files. |
| Chat | Scratch | Low | Manual promotion | Nothing governs from chat alone. |
| Archive | Memory | Low | Supersession/deprecation | Not included in active packs unless requested. |
| Quarantine | Risk holding area | None | Ambiguity/conflict/risk | Cannot govern until reviewed/promoted. |

---

## 8. Active docs table

These are the canonical docs NullForge should converge toward.

| Object | Canonical location | Governs | Current status | Repair needed? |
|---|---|---|---:|---:|
| Current status | `docs/CURRENT_STATUS.md` | Project state | Missing / old engine status may exist | Yes |
| Mission | `docs/MISSION_BRIEF.md` | Product mission | Draft in Volume 0 | Yes: promote after review |
| MVP cutline | `docs/MVP_CUTLINE.md` or Volume 0 | MVP scope | Draft in Volume 0 | Yes: extract/link |
| Claim ledger | `docs/CLAIM_LEDGER.md` | Claims/evidence | Seed in Volume 0 | Yes |
| Risk register | `docs/RISK_REGISTER.md` | Risks/kill conditions | Seed in Volume 0 | Yes |
| Decision ledger | `docs/DECISION_LEDGER.md` | Decisions | Missing for NullForge | Yes |
| ADRs | `docs/adr/` | Major decisions | Missing | Yes |
| Roadmap | `docs/ROADMAP.md` | Build sequence | Setup plan draft | Yes |
| Volume docs | `docs/blueprint/volumes/` | Project doctrine | Vol 0/1 generated in chat | Yes: promote/import |
| Setup docs | `docs/blueprint/setup/` | Workflow setup | Setup package generated | Yes |
| Product boundary docs | `docs/nullforge/` | Track boundaries | Draft only | Yes |
| Technical architecture | `docs/TECHNICAL_ARCHITECTURE.md` | Architecture | Not yet generated | Later |
| Product spec | `docs/PRODUCT_SPEC.md` | UX/workflows | Not yet generated | Later |
| Validation reports | `docs/validation/reports/` | Evidence | Not yet for NullForge | Later |
| Codex workflow docs | `docs/codex/` or `docs/context/` | Role loop | Sources exist; project-specific missing | Volume 2 |
| Prompts | `prompts/` | Prompt provenance | Generated externally | Yes: import/archive |
| Tickets | `tickets/` | Work units | Draft table exists | Later formalization |
| Plans/reports/audits | `plans/`, `reports/`, `audits/` | Codex execution artifacts | Not underway | Later |

---

## 9. Archive policy

Archive preserves memory without authority.

### Archive by default

```text
old prompts;
old ChatGPT outputs;
superseded setup plans;
superseded names;
static mockups that are not target product;
stale roadmaps;
failed experiments;
old Codex reports after supersession;
old screenshots/logs;
dead MVP variants;
old dataset slices not used in tests;
old generated logic that is not compiled/promoted.
```

### Archive locations

| Material | Repo archive path | Workspace archive path |
|---|---|---|
| Old prompts | `prompts/archive/` | N/A |
| Old volume drafts | `docs/archive/volumes/` | N/A |
| Old setup outputs | `docs/archive/setup/` | N/A |
| Superseded names | `docs/archive/superseded-names/` | N/A |
| Static UI mockups | `docs/archive/mockups/` or `design/archive/` | N/A |
| Old status docs | `docs/archive/status/` | N/A |
| Old roadmaps | `docs/archive/roadmaps/` | N/A |
| Failed experiments | `docs/validation/reports/` with `ARCHIVED` status | `evidence/reports/archived/` |
| Old workspace artifacts | Not repo by default | `artifacts/archived/` |
| Old run outputs | Not repo by default | `runs/completed/` or `runs/failed/` |

### Archive record template

```markdown
# Archive Record — [Object]

Archived object:
Date:
Original location:
Archive location:
Reason:
Superseded by:
Authority after archive: ARCHIVE_ONLY
Can be revived if:
Reviewer:
```

### Archive rule

```text
Archived material may be cited as history but must not be used as active context unless an Archive Review Pack is created.
```

---

## 10. Quarantine policy

Quarantine holds unresolved, conflicting, risky, or untrusted material. It has no governance power.

### Quarantine by default

```text
unverified generated logic;
AI-proposed strategies;
ambiguous dataset transformations;
unverified data sources;
name/legal conflict notes;
conflicting claims;
possible leakage cases;
unclear chart/timeframe capabilities;
suspicious test outputs;
old outputs that conflict with current source docs;
mockups that imply unapproved features;
anything that could mislead Codex if included as active truth.
```

### Quarantine statuses

| Status | Meaning | Can govern? |
|---|---|---:|
| `QUARANTINE_REVIEW` | Needs review. | No |
| `QUARANTINE_DATA` | Data quality/access issue. | No |
| `QUARANTINE_LOGIC` | Candidate/generated logic untrusted. | No |
| `QUARANTINE_LEGAL` | Legal/privacy/name issue. | No |
| `QUARANTINE_CONFLICT` | Conflicts with active docs/evidence. | No |
| `QUARANTINE_SECURITY` | Security/privacy/file access risk. | No |
| `RELEASE_BLOCKER` | Cannot release until resolved. | No |

### Quarantine locations

```text
repo:
  docs/quarantine/
    naming/
    data/
    generated-logic/
    legal-privacy/
    conflicting-claims/
    security/

workspace:
  datasets/quarantine/
  logic/quarantined/
  evidence/quarantine/
  capability_maps/quarantine/
```

### Quarantine record template

```markdown
# Quarantine Record — [Object]

Quarantined object:
Date:
Concern:
Source:
Why it cannot govern:
Review needed:
Promotion blocked until:
Possible outcomes: PROMOTE / REPAIR / ARCHIVE / KILL
Reviewer:
```

### Promotion from quarantine

A quarantined object may move to active/promoted only when:

```text
review is complete;
source is known;
risk is resolved or bounded;
claim/evidence relationship is recorded;
decision ledger entry exists if major;
audit or human gate accepts it;
new active location is explicit.
```

---

## 11. Design memory policy for prior chat / mockups / prompts

### Prior chat

Prior chat is design memory unless explicitly promoted.

Use prior chat for:

```text
idea recovery;
reasoning trace summaries;
name history;
why decisions were considered;
future archive review;
reconstruction when a canonical doc is missing.
```

Do not use prior chat as:

```text
implementation law;
acceptance criteria;
architecture source;
Codex ticket scope;
claim evidence;
current status;
repo truth.
```

### Static UI mockups

Static HTML/mockup artifacts are classified as:

```text
DESIGN_MEMORY
```

They may inform future UX discussion, but they do not define the product target. NullForge is a downloadable Windows desktop app, not a thin HTML file or localhost demo.

### Old prompts

Old prompts are instructions that produced artifacts. They are not source truth.

Classification:

| Prompt type | Storage | Authority |
|---|---|---:|
| Setup prompt used | `prompts/archive/setup/` or `prompts/volumes/` | Provenance only |
| Volume prompt used | `prompts/volumes/` | Prompt provenance |
| Superseded prompt | `prompts/archive/` | Archive only |
| Codex implementation prompt | `prompts/codex/[ticket]/` | Active only for its ticket |
| Old chat prompt | Archive only if needed | None |

---

## 12. Data boundary policy for ES.zip and fixtures

### Core data rule

```text
Full 10-year ES.zip stays outside repo.
```

### Data classes

| Data class | Location | Repo allowed? | Notes |
|---|---|---:|---|
| Full `ES.zip` | Local workspace / external drive | No | User-provided raw source. |
| Extracted full ES data | Local workspace | No | Too large and likely rights-sensitive. |
| Small ES-derived fixture | `data/samples/` only if license-safe | Maybe | Requires explicit decision. |
| Synthetic OHLCV fixture | `data/samples/` | Yes | Best first fixture. |
| Generated canonical dataset | Workspace | No by default | May commit tiny sample only. |
| Dataset manifest | Repo or workspace | Yes, if no private paths/secrets | Good for reproducibility. |
| Capability map example | Repo if synthetic or safe | Yes | Must not leak full dataset. |
| User dataset metadata | Workspace | No by default | Can contain private paths. |

### Fixture admission rule

A fixture may be committed only if:

```text
it is tiny;
it is license-safe;
it contains no private account/user data;
it is intentionally selected;
it has a manifest;
it is needed for deterministic tests;
it has a human gate approval.
```

### ES-derived fixture rule

If an ES-derived fixture is used:

```text
slice the smallest useful window;
record date range;
record source file hash if allowed;
strip private/local path info;
include column schema;
state licensing uncertainty if any;
do not include the full source zip;
do not imply the fixture proves market edge.
```

### DatasetCapabilityMap dependency

DatasetCapabilityMap must be generated before:

```text
timeframe aggregation;
chart-type generation;
SL/TP first-hit evaluation;
logic test eligibility;
visual replay examples;
claim promotion based on dataset behavior.
```

---

## 13. Prompt storage policy

### Prompt directory structure

```text
prompts/
├── volumes/
│   ├── NullForge_Prompt_For_Volume_00_v0_4.md
│   ├── NullForge_Prompt_For_Volume_01_v0_4.md
│   └── NullForge_Prompt_For_Volume_02_v0_4.md
├── setup/
│   └── NullForge_PF_T000R_Workflow_Setup_Plan_v0_4_Prompt.md
├── codex/
│   └── [TICKET_ID]/
│       ├── 00_CONTEXT_CURATOR_PROMPT.md
│       ├── 01_PLANNER_PROMPT.md
│       ├── 02_IMPLEMENTOR_PROMPT.md
│       └── 03_AUDITOR_PROMPT.md
├── milestones/
└── archive/
```

### Prompt metadata header

Every prompt file should begin with:

```markdown
# Prompt — [Purpose]

Project: NullForge
Prompt ID:
Version:
Created:
Used for:
Expected output:
Authority: PROMPT_PROVENANCE
Status: ACTIVE / USED / SUPERSEDED / ARCHIVE_ONLY
Source docs:
```

### Prompt lifecycle

| Status | Meaning |
|---|---|
| `ACTIVE` | Next prompt to use. |
| `USED` | Prompt was run and produced an artifact. |
| `SUPERSEDED` | Replaced by later prompt. |
| `ARCHIVE_ONLY` | Retained for memory, not use. |

---

## 14. Volume storage policy

### Volume directory

```text
docs/blueprint/volumes/
├── Volume_00_North_Star_Doctrine_Naming_Claims_MVP_Cutline_Anti_Goals.md
├── Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine.md
├── Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates.md
├── Volume_03_Windows_Tauri_ResearchCore_Engine_Bridge.md
├── Volume_04_Dataset_Studio_DatasetCapabilityMap.md
├── Volume_05_Logic_Factory_Compiler_Generator_Boundary.md
├── Volume_06_Visual_Replay_Evidence_Cards.md
└── Volume_07_Roadmap_Milestones_Tickets_Codex_Prompts.md
```

### Volume header

Each volume should include:

```markdown
# Volume N — [Title]

Project: NullForge
Version:
Status: DRAFT / ACTIVE_SOURCE / SUPERSEDED / ARCHIVE_ONLY
Governs:
Depends on:
Next volume:
Last reviewed:
Human approved: YES/NO
```

### Volume promotion rule

A volume becomes `ACTIVE_SOURCE` only after:

```text
human review;
conflicts checked;
current status updated;
related prompts archived or marked USED;
source-of-truth map updated;
next action clear.
```

---

## 15. ADR / decision ledger policy

### Decision ledger

Canonical location:

```text
docs/DECISION_LEDGER.md
```

### ADR directory

```text
docs/adr/
├── ADR-0001-working-name-nullforge.md
├── ADR-0002-windows-11-x64-first.md
├── ADR-0003-tauri-react-typescript-desktop.md
├── ADR-0004-researchcore-engine-sidecar-boundary.md
├── ADR-0005-local-first-no-cloud-mvp.md
└── ADR-0006-es-zip-outside-repo.md
```

### ADR template

```markdown
# ADR-[ID] — [Decision]

Status: PROPOSED / ACCEPTED / SUPERSEDED / REVERSED
Date:
Owner:

## Context

## Decision

## Options considered

## Chosen option

## Evidence

## Risks

## Reversal condition

## Follow-up ticket
```

### Required ADRs before implementation

| ADR | Decision | Needed before |
|---|---|---|
| `ADR-0001` | NullForge working name | Public docs/packaging language |
| `ADR-0002` | Windows 11 x64 first | Desktop scaffold |
| `ADR-0003` | Tauri + React + TypeScript | App scaffold |
| `ADR-0004` | ResearchCore Engine sidecar/bridge boundary | Bridge implementation |
| `ADR-0005` | Local-first/no-cloud MVP | Workspace/app architecture |
| `ADR-0006` | Full ES.zip outside repo | Dataset Studio work |

---

## 16. Claim ledger and validation report policy

### Claim ledger

Canonical location:

```text
docs/CLAIM_LEDGER.md
```

### Claim statuses

```text
UNTESTED
WEAK_SIGNAL
SUPPORTED
CONTRADICTED
KILLED
DEFERRED
PROMOTED
```

### NullForge claim IDs

Use prefix:

```text
NF-C###
```

Examples:

| Claim | Type | Current status |
|---|---|---|
| `NF-C001` Desktop cockpit improves solo research workflow | workflow | `UNTESTED` |
| `NF-C002` Tauri can bridge to ResearchCore Engine reliably | technical | `UNTESTED` |
| `NF-C003` DatasetCapabilityMap prevents illegal data assumptions | data/trust | `UNTESTED` |
| `NF-C004` Visual Replay helps explanation without replacing evidence | trust/workflow | `UNTESTED` |
| `NF-C005` Logic compiler can turn ideas into auditable specs | technical/workflow | `UNTESTED` |

### Validation reports

Canonical directory:

```text
docs/validation/reports/
```

Report filename pattern:

```text
YYYYMMDD_[experiment-or-ticket-id]_[short-title]_Validation_Report.md
```

### Validation report must include

```text
claim tested;
artifact tested;
method;
dataset/source;
sample/window;
success threshold;
failure threshold;
result;
evidence strength;
limitations;
decision;
claim ledger updates;
next action.
```

### Evidence rule

```text
Generated logic is not evidence.
Visual replay is not evidence by itself.
A pretty chart is not a promoted claim.
Aggregate test results, nulls, ablations, and audit determine promotion.
```

---

## 17. Current status doc template

Canonical location:

```text
docs/CURRENT_STATUS.md
```

Template:

```markdown
# NullForge Current Status

Updated:
Reviewer:
Status version:

## Current phase

```text
PROJECT_FACTORY_SETUP / VOLUME_GENERATION / REPO_BOOTSTRAP / CODEX_TICKET_LOOP / MILESTONE_BATCH_EXECUTION / AUDIT_REPAIR
```

## Current mission

```text
NullForge is a Windows-first local desktop research workbench that helps a solo research builder import market datasets, map lawful dataset capabilities, compile/generate candidate logic into auditable test specs, run the local ResearchCore Engine, inspect visual trade replays, and decide whether evidence should be promoted, repaired, archived, or quarantined.
```

## Active source docs

| Doc | Status | Notes |
|---|---|---|
| Volume 0 | DRAFT / ACTIVE_SOURCE |  |
| Volume 1 | DRAFT / ACTIVE_SOURCE |  |

## Current ticket

```text
Ticket ID:
Title:
Phase:
Branch:
```

## Current artifact

```text
Artifact:
Location:
Status:
```

## Current claims under test

| Claim ID | Claim | Status | Next evidence |
|---|---|---|---|
|  |  |  |  |

## Current blockers

```text
- 
```

## Current decision needed

```text
Decision:
Options:
Recommendation:
Human gate? YES/NO
```

## Non-claims

The following are not proven yet:

```text
- NullForge improves retention/research productivity.
- Tauri packaging is reliable.
- Python sidecar is stable across machines.
- ES fixtures are license-safe for repo use.
- Visual replay reduces overconfidence.
- Logic generation produces useful candidates.
```

## Next action

```text
Next artifact:
Next prompt:
Next ticket:
```
```

---

## 18. Context pack types

### Context pack map

| Pack type | Purpose | Include | Exclude |
|---|---|---|---|
| Minimal Active Pack | General planning/review | Current status, mission, Volume 0, relevant current volume, claim/decision summaries | Archive, raw data, old prompts |
| Volume Generation Pack | Generate next volume | Setup plan, prior volumes, current prompt, relevant source docs | Codebase dump, run outputs, unrelated archive |
| Repo Inventory Pack | Inspect existing `research-core` state | README, status docs, pyproject, source tree summary, tests summary | Full raw datasets, old chats |
| Codex Ticket Pack | One implementation/docs ticket | Ticket, current status, relevant volumes/ADRs/files, tests, forbidden actions | Broad strategy docs not needed |
| Dataset Pack | Dataset intake/capability work | Dataset manifest, schema, sample rows, data policy, DCM contract | Full data unless explicitly needed locally |
| Logic Factory Pack | Logic compiler/generator work | Logic lifecycle, compiler contract, examples, claim rules | Unverified generated strategy dumps |
| Visual Replay Pack | Replay/evidence work | Replay spec, fixture spec, evidence card contract, ambiguity rules | Cherry-picked charts without aggregate context |
| Validation Pack | Run/evaluate proof loop | Claim ledger, experiment plan, artifact, evidence outputs | Implementation details unless needed |
| Legal/Privacy/Name Pack | Review risk | Data policy, naming notes, privacy/security boundaries | Unrelated product dreams |
| Archive Review Pack | Recover old context | Specific archive slice + reason for review | Active context not related to review |

### Pack expiry rule

Every context pack must include:

```text
expiry condition;
refresh triggers;
truth status;
excluded context list;
human gate if stale/conflicting.
```

---

## 19. Context bundle manifest rules

Every Codex or planning context bundle must include a manifest.

### Manifest template

```markdown
# Context Bundle Manifest — [Pack/Ticket]

Pack ID:
Purpose:
Created:
Created by:
Current status doc version:
Ticket / volume / artifact:

## Included files

| File | Why included | Truth status | Last reviewed |
|---|---|---|---|
|  |  |  |  |

## Excluded files

| File / category | Why excluded |
|---|---|
| Archive | Not active truth unless specifically reviewed. |
| Full ES.zip | Raw local data; not needed for this ticket. |
| Old prompts | Prompt provenance only. |

## Assumptions

```text
- 
```

## Risks

```text
- 
```

## Expiry / refresh rule

Refresh this bundle if:

```text
- main changes;
- current status changes;
- active ticket changes;
- relevant volume/ADR changes;
- previous ticket modifies shared files;
- tests/dependencies change;
- audit returns HOLD/REJECT;
- source-of-truth conflict appears.
```

## Ready for next role?

```text
YES / NO
Reason:
```
```

---

## 20. Drift checks

Run drift checks after every volume, ticket, audit, and milestone.

### Project truth drift

- [ ] Only one active mission exists.
- [ ] Current status points to the current phase/ticket/artifact.
- [ ] Roadmap matches current volume/ticket sequence.
- [ ] Decision ledger reflects major decisions.
- [ ] Claim ledger statuses reflect latest evidence.
- [ ] Volume docs do not contradict setup plan without ADR.
- [ ] Archived material is not referenced as active truth.
- [ ] Quarantined material is not used for implementation.

### Repo / engine drift

- [ ] NullForge docs do not silently overwrite ResearchCore Engine identity.
- [ ] README status matches current docs or clearly distinguishes engine vs product.
- [ ] Existing engine tests remain respected.
- [ ] New desktop docs do not imply implemented features.
- [ ] Package metadata is not changed without ticket/ADR.

### Data drift

- [ ] Full ES.zip is not in repo.
- [ ] Fixture policy is followed.
- [ ] Dataset manifests do not leak private paths unnecessarily.
- [ ] Capability maps match available columns/timeframes.
- [ ] Ambiguous intrabar assumptions are labeled.

### Codex context drift

- [ ] Context bundles are task-sized.
- [ ] Old prompts are archived or marked USED.
- [ ] Implementor prompts do not ask for broad build.
- [ ] Auditor is not the same role pass as implementor.
- [ ] Human gate triggers are recorded.

---

## 21. Human gate triggers for source-of-truth changes

Stop for human review before:

```text
renaming the repo;
renaming the package;
publicly distributing under NullForge;
committing ES-derived fixtures;
adding large datasets;
changing data retention policy;
changing file access scope;
changing source-of-truth locations;
deleting archive/quarantine;
reversing major ADRs;
modifying engine identity/docs materially;
adding dependencies;
adding cloud/auth/sync;
activating AI generation;
adding broker/live trading integration;
changing ticket role-loop discipline;
marking a claim PROMOTED;
merging release/signing/installer changes.
```

---

## 22. What must stay outside repo

| Object | Reason | Allowed location |
|---|---|---|
| Full 10-year `ES.zip` | Size/licensing/source/privacy risk | Local workspace / external storage |
| Extracted full ES dataset | Size/licensing risk | Local workspace |
| Private datasets | Privacy/data rights | Local workspace |
| Local absolute paths | Machine-specific | Workspace settings, not repo docs unless sanitized |
| Secrets/API keys | Security | User secret store / env, not repo |
| Personal account credentials | Security | Never repo |
| Cache files | Disposable | Workspace cache |
| Large run outputs | Bloat | Workspace / curated artifact export |
| Generated logic dumps | Trust risk | Workspace quarantine until curated |
| Broker/live credentials | Anti-goal/security | Not applicable in MVP |
| Installer signing keys | Security/release gate | Secure external store |

---

## 23. Repair plan for existing docs that conflict with NullForge

### Known likely conflicts

| Possible conflict | Example | Repair path |
|---|---|---|
| Engine docs describe only old phase | README/status says Phase 0 only | Inventory first; update only through docs ticket. |
| Product name mismatch | ResearchCore Workbench / Crucible Workbench | Archive superseded names; promote NullForge working name. |
| Dashboard/browser language | Localhost/browser app implied as target | Replace with desktop-first Tauri language in NullForge docs. |
| Old ticket namespace | T000/T001/T002 without track prefix | Introduce prefixed ticket taxonomy. |
| Data samples unclear | Sample vs raw data boundary missing | Add `data/README.md` and fixture policy. |
| Prompts mixed with docs | Prompts treated as source truth | Move prompts to `prompts/` with status headers. |
| Generated outputs used as authority | AI/Codex output not audited | Archive or quarantine until accepted. |

### Repair sequence

```text
1. Inventory existing repo docs and status surfaces.
2. Classify each as ACTIVE_SOURCE / DESIGN_MEMORY / ARCHIVE_ONLY / QUARANTINE_REVIEW / SUPERSEDED.
3. Add or update CURRENT_STATUS.md.
4. Add NullForge docs under explicit product namespace.
5. Preserve existing ResearchCore Engine docs unless ticket says otherwise.
6. Create decision ledger and ADRs before changing public framing.
7. Move old prompts into prompt archive/provenance locations.
8. Add data boundary README before adding any fixture.
9. Run drift check.
10. Audit the source-of-truth repair pass.
```

### No silent supersession rule

```text
A new NullForge doc may supersede an old planning artifact only if it states what it supersedes and where the old artifact is archived.
```

---

## 24. Volume 1 closeout

### Volume 1 decision

```text
Decision: PROMOTE_TO_VOLUME_2_AFTER_REVIEW
```

### What Volume 1 promotes

```text
Repo/workspace split.
ResearchCore Engine boundary.
Canonical doc layout.
Local workspace layout.
Archive/quarantine taxonomy.
ES.zip outside-repo rule.
Prompt/volume storage policy.
ADR/decision ledger policy.
Claim/validation report policy.
Context pack system.
Drift checks.
Source-of-truth human gates.
```

### What remains unproven

```text
The repo has not yet been repaired.
The docs have not yet been imported.
The Tauri app is not implemented.
The Python sidecar bridge is not proven.
DatasetCapabilityMap is not implemented.
Logic compiler is not implemented.
Visual Replay is not implemented.
Evidence Cards are not implemented.
No Codex implementation ticket has run.
```

### Next volume

```text
Volume 2 — NullForge Planner / Implementor / Auditor Loop, QA Gates, Human Gates, and Codex Execution System
```

Volume 2 should define the exact role chain, ticket artifact tree, gate rules, prompt templates, milestone batching rules, and stop conditions before any implementation work begins.

---

## 25. Prompt for Volume 2

````md
# Prompt for Volume 2 — NullForge Planner / Implementor / Auditor Loop, QA Gates, Human Gates, and Codex Execution System

You are my ForgeIT Project Factory volume writer, Codex role-loop architect, QA/security gate designer, ticket artifact-system designer, milestone-batch planner, source-of-truth guardian, and anti-context-soup auditor.

Use the uploaded App Forge + Project Factory + Autonomous Codex Role Loop sources as governing context.

Do not generate implementation code.
Do not generate all volumes.
Do not write Codex implementation tickets yet.
Do not create a broad “build the app” prompt.
Do not treat old chat output as source of truth unless explicitly promoted.
Do not collapse App Forge validation and Project Factory implementation.

## Project

Working product name:

```text
NullForge
```

Existing repo / engine:

```text
research-core
```

Internal engine label:

```text
ResearchCore Engine
```

First platform:

```text
Windows 11 x64
```

Desktop stack:

```text
Tauri + React + TypeScript
```

Engine boundary:

```text
Existing Python ResearchCore Engine as local sidecar / command bridge.
```

Volume 0 status:

```text
Volume 0 — NullForge North Star, Doctrine, Naming, Claims, MVP Cutline, Anti-Goals has been generated as draft canonical project source.
```

Volume 1 status:

```text
Volume 1 — NullForge Workspace, Repo, Context, Source-of-Truth, Archive, and Quarantine System has been generated as draft canonical project source.
```

One-sentence thesis:

```text
NullForge is a Windows-first local desktop research workbench that helps a solo research builder import market datasets, map lawful dataset capabilities, compile/generate candidate logic into auditable test specs, run the local ResearchCore Engine, inspect visual trade replays, and decide whether evidence should be promoted, repaired, archived, or quarantined.
```

First proof loop:

```text
User opens a Windows 11 x64 desktop app
→ creates/selects a local workspace
→ imports or uses a small ES-derived OHLCV fixture
→ sees a DatasetCapabilityMap
→ runs one ResearchCore Engine smoke command through the desktop bridge
→ views produced artifact metadata
→ opens one visual replay fixture with signal/entry/SL/TP/exit labels
→ sees an audit/decision placeholder.
```

Core doctrine to preserve:

```text
Repo is source of truth.
Vault is design memory.
Graphify is context/navigation.
Chat is scratch unless promoted.
Archive is memory without authority.
Quarantine is unresolved material without governance power.
Generated logic is not evidence.
Visual replay explains examples; aggregate evidence decides.
DatasetCapabilityMap gates chart/timeframe/test claims.
Compiler before generator.
Evidence before promotion.
Ticket before branch.
Acceptance before code.
Tests before audit pass.
Audit before merge.
Human approval before release.
No broad “build the app” prompts.
No role grades its own work.
```

## Mission

Generate Volume 2 only:

```text
Volume 2 — NullForge Planner / Implementor / Auditor Loop, QA Gates, Human Gates, and Codex Execution System
```

This volume should adapt the context-curator → planner → implementor → auditor role loop to NullForge before any code implementation begins.

## Required sections

Include:

1. Volume purpose.
2. Relationship to Volumes 0 and 1.
3. Why direct-to-Codex implementation is forbidden.
4. Role-loop overview.
5. Human / ChatGPT Architect responsibilities.
6. Context Curator role.
7. Planner role.
8. Implementor / Codex role.
9. Auditor role.
10. Repair loop.
11. Per-ticket artifact tree.
12. Ticket namespace policy.
13. Branch naming policy.
14. Required ticket template.
15. Context bundle requirements.
16. Planner output requirements.
17. Implementor report requirements.
18. Auditor report requirements.
19. PASS / HOLD / REJECT rules.
20. QA gate matrix.
21. Security/privacy/data/file-access gates.
22. Human gate triggers.
23. Milestone batching rules.
24. Stop conditions.
25. Docs-only ticket compression rule.
26. First milestone categories, without generating full implementation tickets.
27. What Codex may and may not automate.
28. Volume 2 closeout.
29. Prompt for Volume 3.

## Required boundaries

Preserve these boundaries:

```text
No role grades its own work.
Context Curator does not plan implementation.
Planner does not code.
Implementor does not invent strategy.
Auditor does not silently repair.
Codex does not merge or release.
No ticket starts without acceptance criteria.
No implementation starts from a broad app-building prompt.
No dependency, security, migration, installer, data-access, AI, broker, or public release change bypasses a human gate.
Milestone batching batches prompts, but tickets execute serially.
```

## Response rules

Return Volume 2 as structured Markdown content or downloadable Markdown files if files are requested.
Do not generate Volume 3.
Do not generate implementation code.
Do not create a broad build prompt.
Keep the output detailed enough to become a canonical project source.
End with the exact next prompt for Volume 3.
````

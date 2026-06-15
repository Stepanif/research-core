> Import note: This file was imported by PF-T001 from `NullForge_Volume_02_v0_4_Package.zip` / `NullForge_Volume_02_v0_4_Package/artifacts/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md` on `2026-06-15`.
> Authority: repo-managed NullForge planning/workflow source after PF-T001 audit. It is not ResearchCore Engine implementation truth.
> Source package SHA256: `8A392AD271641962C1DEBD4DF22745C657CD3A51AF03E328D3EA69ACEE0F9500`

# NullForge Volume 2 — Planner / Implementor / Auditor Loop, QA Gates, Human Gates, and Codex Execution System v0.4

```text
Artifact type: Project Factory volume
Project: NullForge
Existing repo / engine: research-core
Internal engine label: ResearchCore Engine
First platform: Windows 11 x64
Desktop stack: Tauri + React + TypeScript
Volume status: DRAFT_CANONICAL_PROJECT_SOURCE
Generated for: ForgeIT Project Factory setup
```

---

## 1. Volume purpose

This volume defines the **execution system** for NullForge before any implementation begins.

Its job is to prevent the project from sliding into:

```text
"here is the repo, build the app"
```

That is forbidden.

NullForge must instead move through a role-separated, artifact-producing build loop:

```text
Human / ChatGPT Architect
→ Context Curator
→ Planner
→ Implementor / Codex
→ Auditor
→ Repair if needed
→ Human gate
→ Next ticket
```

This volume defines:

1. the responsibilities and forbidden actions of each role;
2. the artifact tree every ticket must produce;
3. the ticket namespace and branch policies;
4. the required ticket template;
5. the context-bundle rules;
6. planner, implementor, and auditor output requirements;
7. PASS / HOLD / REJECT rules;
8. QA, security, privacy, data, dependency, and packaging gates;
9. milestone batching rules;
10. stop conditions;
11. docs-only compression rules;
12. first milestone categories, without generating implementation tickets yet;
13. the prompt for Volume 3.

Volume 2 does **not** build NullForge. It creates the rails that future implementation must stay inside.

---

## 2. Relationship to Volumes 0 and 1

### Volume 0 governs why NullForge exists

Volume 0 defines:

```text
mission
first user
first proof loop
MVP cutline
claim ledger seed
fatal claims
anti-goals
promotion / repair / archive / quarantine policy
```

Volume 2 must protect those decisions from being silently overwritten during implementation.

### Volume 1 governs where truth lives

Volume 1 defines:

```text
repo as source of truth
vault as design memory
Graphify as context/navigation
chat as scratch unless promoted
archive as memory without authority
quarantine as unresolved material without governance power
canonical docs
context packs
drift checks
data boundaries
prompt storage
volume storage
```

Volume 2 applies those rules to the Codex execution system.

### Volume 2 governs how implementation may happen

Volume 2 answers:

```text
Who gathers context?
Who plans?
Who implements?
Who audits?
What files must be produced?
When do we stop?
When does the human decide?
What can Codex never do?
```

---

## 3. Why direct-to-Codex implementation is forbidden

Direct implementation is forbidden because NullForge has multiple risk surfaces:

```text
desktop shell
Windows packaging
Tauri permissions
Python sidecar bridge
local filesystem workspaces
dataset import
raw ES.zip boundary
fixture generation
logic compiler/generator boundary
visual replay trust boundary
evidence/audit decisions
future AI and broker/live-trading temptation
```

A broad prompt such as:

```text
Build NullForge.
```

is not a ticket. It is a context soup generator.

Direct-to-Codex implementation is forbidden because it can cause:

| Failure | Why it matters |
|---|---|
| Product strategy invention | Codex may build what sounds useful instead of what Volume 0 promoted. |
| Scope explosion | Dataset Studio, Logic Factory, replay, evidence, and packaging can sprawl quickly. |
| Silent dependency changes | Tauri/React/Python packaging can invite extra dependencies without review. |
| Unsafe file access | Local data, zip imports, fixture generation, and workspace paths need explicit gates. |
| False validation | Visual replay can make weak evidence look strong. |
| Source-of-truth drift | Chat, old prompts, or design memory can accidentally become active truth. |
| Repo bloat | Full ES.zip or generated artifacts may be committed by mistake. |
| Unreviewed architecture reversal | Tauri, sidecar, or workspace decisions may be bypassed. |
| No independent audit | If the implementor grades itself, the audit layer becomes decoration. |

Therefore:

```text
No ticket starts without acceptance criteria.
No implementation starts from a broad app-building prompt.
No role grades its own work.
No generated output becomes truth without audit.
```

---

## 4. Role-loop overview

The NullForge role loop is:

```text
Human / ChatGPT Architect
→ Context Curator Prompt
→ Context Curator
→ CONTEXT_BUNDLE.md
→ CONTEXT_BUNDLE_MANIFEST.md
→ Planner Prompt
→ Planner
→ PLAN.md
→ ACCEPTANCE.md
→ IMPLEMENTOR_PROMPT.md
→ Implementor / Codex
→ IMPLEMENTATION_REPORT.md
→ CHANGED_FILES.md
→ TEST_RESULTS.md
→ AUDITOR_PROMPT.md
→ fresh Auditor
→ AUDIT_REPORT.md
→ FINDINGS.md
→ REPAIR_PROMPT.md
→ repair if needed
→ human gate
→ next ticket
```

This is a staged artifact factory, not an autonomous agent swarm.

---

## 5. Human / ChatGPT Architect responsibilities

The Human / ChatGPT Architect owns:

```text
mission
scope
phase selection
ticket selection
milestone intent
human gates
final merge/release decision
promote/repair/archive/quarantine decisions
architecture reversal approval
public distribution approval
```

### Human / ChatGPT Architect may

- choose the next milestone;
- approve or reject ticket scope;
- approve dependencies;
- approve public release gates;
- decide whether a ticket’s audit result is acceptable;
- decide whether a design memory artifact should be promoted;
- stop a batch when the plan no longer matches reality.

### Human / ChatGPT Architect must not

- treat unreviewed Codex output as active truth;
- skip audit because the output looks plausible;
- merge or release work that triggered unresolved human gates;
- keep old chat output active without promotion;
- let implementation outrun the current Volume / ADR / ticket state.

### Human / ChatGPT Architect closeout checklist

Before a ticket begins:

```text
[ ] Current ticket is named.
[ ] Current branch policy is known.
[ ] Source docs are known.
[ ] Human gate triggers are visible.
[ ] Scope is bounded.
[ ] Acceptance criteria exist.
[ ] Test expectations are known.
[ ] Forbidden actions are listed.
```

---

## 6. Context Curator role

The Context Curator creates the smallest sufficient active context for the ticket.

The Context Curator does **not** plan implementation and does **not** code.

### Context Curator owns

```text
ticket summary
mission slice
active source docs
relevant repo files/folders
current repo state summary
constraints
forbidden actions
known risks
test commands
human gate triggers
open questions
```

### Context Curator inputs

```text
Ticket file
Current status doc
Relevant volumes
Relevant ADRs
Relevant source-of-truth docs
Relevant repo files/folders
Current branch/main status
Known test commands
Known forbidden files/actions
Prior audit/repair state, if any
```

### Context Curator outputs

```text
plans/[TICKET_ID]/CONTEXT_BUNDLE.md
plans/[TICKET_ID]/CONTEXT_BUNDLE_MANIFEST.md
```

### `CONTEXT_BUNDLE.md` must include

```text
Ticket ID and title
Ticket purpose
Mission slice
Relevant doctrine
Relevant architecture/product docs
Relevant files/folders
Current repo state summary
Constraints
Forbidden actions
Required tests
Human gate triggers
Dependencies/blockers
Open questions
Ready-for-planner verdict
```

### `CONTEXT_BUNDLE_MANIFEST.md` must include

```text
Included files
Why each included file matters
Excluded files
Why excluded files were excluded
Archive/design-memory items referenced, if any
Truth status for each input
Expiry / refresh rule
Context risk notes
```

### Context Curator must not

```text
include the whole repo by default
include old prompts as active truth
include full raw ES.zip
invent product strategy
write implementation plans
code
modify files unrelated to the context bundle
promote design memory
```

---

## 7. Planner role

The Planner consumes the context bundle and creates a bounded implementation plan.

The Planner does **not** code.

### Planner owns

```text
PLAN.md
ACCEPTANCE.md
IMPLEMENTOR_PROMPT.md
```

### Planner inputs

```text
plans/[TICKET_ID]/CONTEXT_BUNDLE.md
plans/[TICKET_ID]/CONTEXT_BUNDLE_MANIFEST.md
ticket definition
relevant source docs
current status
human gate policy
```

### Planner outputs

```text
plans/[TICKET_ID]/PLAN.md
plans/[TICKET_ID]/ACCEPTANCE.md
plans/[TICKET_ID]/IMPLEMENTOR_PROMPT.md
```

### `PLAN.md` must include

```text
ticket goal
source context used
assumptions
planned file changes
step-by-step implementation plan
out-of-scope items
forbidden actions
tests to run
risks
security/privacy/data/file-access notes
rollback/repair route
human gate triggers
```

### `ACCEPTANCE.md` must include

```text
testable criteria
required commands
expected files/artifacts
docs update expectations
security/privacy checks, if relevant
source-of-truth update expectations
done definition
```

### `IMPLEMENTOR_PROMPT.md` must include

```text
ticket ID and title
mission slice
allowed files/folders
forbidden files/folders/actions
required outputs
acceptance criteria
tests to run
report format
human gate triggers
explicit instruction not to broaden scope
```

### Planner must not

```text
code
broaden the ticket
change product strategy
change acceptance criteria to make implementation easier
silently approve dependencies
silently approve migrations
silently approve file-access expansion
generate a broad build prompt
```

---

## 8. Implementor / Codex role

The Implementor / Codex executes only the scoped plan.

Codex is a build assistant, not the product owner.

### Implementor owns

```text
scoped code/docs changes
test execution
implementation report
changed files report
test results report
auditor prompt
```

### Implementor inputs

```text
plans/[TICKET_ID]/PLAN.md
plans/[TICKET_ID]/ACCEPTANCE.md
plans/[TICKET_ID]/IMPLEMENTOR_PROMPT.md
```

### Implementor outputs

```text
reports/[TICKET_ID]/IMPLEMENTATION_REPORT.md
reports/[TICKET_ID]/CHANGED_FILES.md
reports/[TICKET_ID]/TEST_RESULTS.md
reports/[TICKET_ID]/AUDITOR_PROMPT.md
```

### `IMPLEMENTATION_REPORT.md` must include

```text
branch
ticket ID
summary of changes
files changed
commands run
tests passed/failed/skipped
acceptance criteria status
deviations from plan
dependency/security/migration changes
known issues
human gate triggered? YES/NO
next recommended action
```

### `CHANGED_FILES.md` must include

```text
all changed files
why each file changed
whether each change was expected by PLAN.md
unexpected changes
forbidden-file check
```

### `TEST_RESULTS.md` must include

```text
commands run
result for each command
environment notes
skipped tests and reason
failures
warnings
manual checks, if any
```

### `AUDITOR_PROMPT.md` must include

```text
ticket ID
links/paths to plan, acceptance, reports, changed files, tests
audit focus
known risks
human gate triggers
requested verdict format
```

### Implementor may

- make scoped changes allowed by the ticket;
- run tests;
- report skipped tests with exact reason;
- flag blockers;
- request human approval when a gate triggers.

### Implementor must not

```text
invent product strategy
change acceptance criteria
modify unrelated files
edit forbidden files
add dependencies silently
change auth/permissions/migrations/deployment silently
commit secrets
merge
release
publicly distribute
claim production readiness
treat generated logic as evidence
commit full ES.zip
activate AI strategy generation
add broker/live trading integration
```

---

## 9. Auditor role

The Auditor independently checks the implemented ticket against the ticket, plan, acceptance criteria, source-of-truth doctrine, and safety gates.

The Auditor should run in a fresh pass/session whenever possible.

### Auditor owns

```text
AUDIT_REPORT.md
FINDINGS.md
REPAIR_PROMPT.md
```

### Auditor inputs

```text
plans/[TICKET_ID]/CONTEXT_BUNDLE.md
plans/[TICKET_ID]/CONTEXT_BUNDLE_MANIFEST.md
plans/[TICKET_ID]/PLAN.md
plans/[TICKET_ID]/ACCEPTANCE.md
reports/[TICKET_ID]/IMPLEMENTATION_REPORT.md
reports/[TICKET_ID]/CHANGED_FILES.md
reports/[TICKET_ID]/TEST_RESULTS.md
reports/[TICKET_ID]/AUDITOR_PROMPT.md
changed repo state
```

### Auditor outputs

```text
audits/[TICKET_ID]/AUDIT_REPORT.md
audits/[TICKET_ID]/FINDINGS.md
audits/[TICKET_ID]/REPAIR_PROMPT.md
```

### Auditor must check

```text
scope matched ticket
plan was followed
acceptance criteria were satisfied
tests were run or skipped with valid reason
forbidden files/actions were avoided
docs/source-of-truth updates were correct
no secrets were committed
no silent dependencies were added
no silent migrations/auth/permissions/deployment changes occurred
no product strategy was invented
human gates were correctly identified
source-of-truth drift did not occur
artifact paths were recorded
next action is justified
```

### Auditor must not

```text
grade its own implementation
silently repair
merge
release
change product strategy
promote weak evidence
ignore failed tests
ignore human gate triggers
```

---

## 10. Repair loop

If audit returns `HOLD` or `REJECT`, repair must stay bounded.

### Repair flow

```text
Auditor writes FINDINGS.md
→ Auditor writes REPAIR_PROMPT.md
→ Human / Architect approves repair path if needed
→ Repair Implementor fixes only listed findings
→ Repair report is written
→ Auditor re-audits
```

### Repair outputs

```text
reports/[TICKET_ID]/REPAIR_IMPLEMENTATION_REPORT.md
reports/[TICKET_ID]/REPAIR_CHANGED_FILES.md
reports/[TICKET_ID]/REPAIR_TEST_RESULTS.md
audits/[TICKET_ID]/REPAIR_AUDIT_REPORT.md
```

### Repair may

- fix blocking findings;
- update tests/docs required by the findings;
- clarify acceptance status.

### Repair must not

```text
expand scope
open unrelated refactors
add new features
change strategy
hide failures
skip re-audit
```

### Repair attempt limit

Default:

```text
One autonomous repair attempt per ticket.
```

After one failed repair:

```text
Return to Human / ChatGPT Architect.
```

---

## 11. Per-ticket artifact tree

Default artifact tree:

```text
prompts/[TICKET_ID]/
  00_CONTEXT_CURATOR_PROMPT.md
  01_PLANNER_PROMPT.md
  02_IMPLEMENTOR_PROMPT.md
  03_AUDITOR_PROMPT.md
  04_REPAIR_PROMPT.md        # only if needed

plans/[TICKET_ID]/
  CONTEXT_BUNDLE.md
  CONTEXT_BUNDLE_MANIFEST.md
  PLAN.md
  ACCEPTANCE.md
  IMPLEMENTOR_PROMPT.md

reports/[TICKET_ID]/
  IMPLEMENTATION_REPORT.md
  CHANGED_FILES.md
  TEST_RESULTS.md
  AUDITOR_PROMPT.md
  REPAIR_IMPLEMENTATION_REPORT.md   # only if needed
  REPAIR_CHANGED_FILES.md           # only if needed
  REPAIR_TEST_RESULTS.md            # only if needed

audits/[TICKET_ID]/
  AUDIT_REPORT.md
  FINDINGS.md
  REPAIR_PROMPT.md
  REPAIR_AUDIT_REPORT.md            # only if needed
```

### Artifact path rules

- Use the full ticket ID in every folder name.
- Do not reuse artifacts across tickets unless explicitly referenced.
- Do not edit old ticket artifacts to rewrite history.
- If a ticket is repaired, append repair artifacts instead of replacing original reports.
- Archive superseded prompts when the ticket closes.
- Link all artifacts from the ticket closeout.

---

## 12. Ticket namespace policy

NullForge uses prefixed ticket namespaces so App Forge, Project Factory, desktop, data, logic, replay, evidence, QA, and Codex workflow do not collide.

| Prefix | Track | Owns |
|---|---|---|
| `AF-T###` | App Forge | Discovery, mission, user/problem, access, claims, MVP, validation |
| `PF-T###` | Project Factory | Repo setup, source-of-truth, volumes, project doctrine |
| `ADR-T###` | Decisions | ADRs, decision ledger entries, reversal conditions |
| `DA-T###` | Desktop App | Tauri, Windows packaging, sidecar bridge |
| `WB-T###` | Workbench | Lab cockpit, artifact browser, dashboard shell |
| `DS-T###` | Dataset Studio | Dataset import, schema mapping, fixture handling |
| `DCM-T###` | DatasetCapabilityMap | Capability statuses and lawful transformation rules |
| `LF-T###` | Logic Factory | Logic cards, compiler, generator, nulls, ablations |
| `VR-T###` | Visual Replay | Signal/entry/SL/TP/exit views and replay fixtures |
| `EV-T###` | Evidence Cards | Aggregate results, nulls, ablations, decisions |
| `QA-T###` | QA/Security | Test gates, data gates, permission/security gates |
| `CX-T###` | Codex Workflow | Context curator, planner, implementor, auditor prompts |
| `MB-T###` | Milestones | Milestone batches, handoff templates, dependency maps |

### Rule

```text
Do not use bare T000/T001/T002 for NullForge Project Factory work.
```

Bare ticket numbers may appear only inside old App Forge examples or archived material.

---

## 13. Branch naming policy

Branch names should reflect the track and ticket.

### Default branch formats

```text
docs/PF-T000-promote-setup-package
docs/ADR-T001-name-platform-stack
task/DA-T001-desktop-bridge-contract
task/DS-T001-dataset-studio-boundary
task/LF-T001-logic-lifecycle-map
fix/QA-T002-drift-check-repair
```

### Branch prefix meanings

| Prefix | Use |
|---|---|
| `docs/` | Docs-only or planning/source-of-truth tickets |
| `task/` | Feature/scaffold/build ticket |
| `fix/` | Bug/repair ticket |
| `chore/` | Hygiene, tooling, non-feature maintenance |
| `spike/` | Timeboxed technical feasibility experiment |
| `audit/` | Audit-only branch, if needed |

### Branch rules

```text
Start from clean main.
One branch per ticket.
No unrelated cleanup.
No combined feature branches.
No merge without audit and human gate.
Pull/refresh main before next ticket.
```

---

## 14. Required ticket template

Every ticket must include:

```markdown
# [TICKET_ID] — [Title]

## Type

docs / decision / spike / scaffold / feature / test / audit / repair / release

## Phase

App Forge / Project Factory / Desktop / Dataset / Logic / Replay / Evidence / QA / Milestone

## Purpose

What this ticket exists to make true.

## Source docs

Which volumes, ADRs, status docs, or tickets govern this work.

## Inputs

What artifacts or files are required before starting.

## Outputs

What exact files/artifacts must exist at closeout.

## Scope

What is in scope.

## Out of scope

What is explicitly not in scope.

## Forbidden actions

What must not happen.

## Dependencies

Which prior tickets/artifacts must be PASS or accepted.

## Likely files/folders

Expected files/folders that may change.

## Required context bundle contents

What the Context Curator must include.

## Acceptance criteria

Testable done conditions.

## Tests required

Commands, manual checks, or doc review checks.

## QA/security/privacy/data gates

Relevant gate checks.

## Human decision gate

When the human must decide.

## Suggested branch

Branch name.

## Suggested implementor prompt source

Path or note.

## Suggested auditor focus

What the auditor should scrutinize.

## Done definition

How the ticket is closed.

## Rollback / repair route

What to do if it fails.

## Next ticket

Expected next ticket if PASS.
```

---

## 15. Context bundle requirements

A context bundle is valid only if it is:

```text
small enough for the ticket
complete enough for the planner
explicit about what was excluded
explicit about truth status
time-bounded by an expiry/refresh rule
```

### Required context bundle sections

```markdown
# CONTEXT_BUNDLE — [TICKET_ID]

## Ticket summary

## Mission slice

## Active source docs

## Relevant repo files/folders

## Current repo state

## Constraints

## Forbidden actions

## Required tests

## Human gate triggers

## Prior related tickets/audits

## Excluded context

## Open questions

## Ready for planner?

YES / NO
```

### Required manifest sections

```markdown
# CONTEXT_BUNDLE_MANIFEST — [TICKET_ID]

## Included sources

| Source | Truth status | Why included |
|---|---|---|

## Excluded sources

| Source | Why excluded |
|---|---|

## Archive/design-memory references

| Source | Why referenced | Authority |
|---|---|---|

## Expiry / refresh rule

## Context risks

## Curator verdict
```

### Refresh required if

```text
main changed
previous ticket changed shared files
current status changed
source docs changed
ticket dependencies changed
tests changed
audit repaired architecture/docs
human gate changed project direction
```

---

## 16. Planner output requirements

### `PLAN.md` template

```markdown
# PLAN — [TICKET_ID] — [Title]

## Goal

## Source context used

## Assumptions

## Scope

## Out of scope

## Planned file changes

## Steps

## Tests to run

## Security/privacy/data/file-access considerations

## Human gate triggers

## Rollback / repair route

## Planner verdict

READY_FOR_IMPLEMENTOR / BLOCKED
```

### `ACCEPTANCE.md` template

```markdown
# ACCEPTANCE — [TICKET_ID] — [Title]

## Acceptance criteria

- [ ] 
- [ ] 
- [ ] 

## Required outputs

- [ ] 
- [ ] 

## Required tests/checks

```text

```

## Source-of-truth updates required

## Forbidden-pass conditions

This ticket cannot pass if:

- [ ] 
- [ ] 

## Done definition
```

### `IMPLEMENTOR_PROMPT.md` template

```markdown
# Implementor Prompt — [TICKET_ID] — [Title]

You are the scoped implementation agent for this NullForge ticket.

Follow:

```text
plans/[TICKET_ID]/PLAN.md
plans/[TICKET_ID]/ACCEPTANCE.md
```

Do not invent product strategy.
Do not broaden scope.
Do not modify unrelated files.
Do not add dependencies without explicit approval.
Do not commit secrets.
Do not merge or release.

## Allowed files/folders

```text

```

## Forbidden files/folders/actions

```text

```

## Required outputs

```text
reports/[TICKET_ID]/IMPLEMENTATION_REPORT.md
reports/[TICKET_ID]/CHANGED_FILES.md
reports/[TICKET_ID]/TEST_RESULTS.md
reports/[TICKET_ID]/AUDITOR_PROMPT.md
```

## Tests

```text

```

If tests cannot be run, explain exactly why.

## Return

```text
Branch:
Files changed:
Commands run:
Tests passed/failed/skipped:
Acceptance status:
Known issues:
Human gate triggered? YES/NO
Auditor prompt path:
```
```

---

## 17. Implementor report requirements

### `IMPLEMENTATION_REPORT.md` template

```markdown
# IMPLEMENTATION_REPORT — [TICKET_ID] — [Title]

## Branch

## Summary

## Files changed

| File | Expected by plan? | Why changed |
|---|---:|---|

## Acceptance status

| Criterion | Status | Evidence |
|---|---:|---|

## Commands run

```text

```

## Tests

```text
Passed:
Failed:
Skipped:
Reason for skipped tests:
```

## Deviations from plan

## Dependency/security/migration/deployment changes

## Data/file-access changes

## Known issues

## Human gate triggered?

YES / NO

## Next recommended action
```

### `CHANGED_FILES.md` template

```markdown
# CHANGED_FILES — [TICKET_ID]

| File | Added/Modified/Deleted | Expected? | Notes |
|---|---|---:|---|

## Forbidden-file check

## Unexpected changes
```

### `TEST_RESULTS.md` template

```markdown
# TEST_RESULTS — [TICKET_ID]

## Commands run

| Command | Result | Notes |
|---|---|---|

## Passed checks

## Failed checks

## Skipped checks

## Environment notes

## Manual checks

## Test verdict
```

### `AUDITOR_PROMPT.md` template

```markdown
# AUDITOR_PROMPT — [TICKET_ID] — [Title]

You are the independent auditor for this NullForge ticket.

Read:

```text
plans/[TICKET_ID]/CONTEXT_BUNDLE.md
plans/[TICKET_ID]/CONTEXT_BUNDLE_MANIFEST.md
plans/[TICKET_ID]/PLAN.md
plans/[TICKET_ID]/ACCEPTANCE.md
reports/[TICKET_ID]/IMPLEMENTATION_REPORT.md
reports/[TICKET_ID]/CHANGED_FILES.md
reports/[TICKET_ID]/TEST_RESULTS.md
```

Return exactly one verdict:

```text
PASS
HOLD
REJECT
```

Check scope, acceptance, tests, forbidden actions, source-of-truth, security/privacy/data/file-access gates, and human gate triggers.

Create:

```text
audits/[TICKET_ID]/AUDIT_REPORT.md
audits/[TICKET_ID]/FINDINGS.md
audits/[TICKET_ID]/REPAIR_PROMPT.md
```
```

---

## 18. Auditor report requirements

### `AUDIT_REPORT.md` template

```markdown
# AUDIT_REPORT — [TICKET_ID] — [Title]

## Verdict

PASS / HOLD / REJECT

## Summary

## Scope audit

| Check | Status | Notes |
|---|---:|---|

## Acceptance audit

| Criterion | Status | Evidence |
|---|---:|---|

## Test audit

## Source-of-truth audit

## Security/privacy/data/file-access audit

## Dependency/migration/deployment audit

## Human gate audit

## Findings summary

## Required repair, if any

## Audit closeout
```

### `FINDINGS.md` template

```markdown
# FINDINGS — [TICKET_ID]

## Blocking findings

| ID | Finding | Evidence | Required repair |
|---|---|---|---|

## Non-blocking findings

| ID | Finding | Evidence | Recommended follow-up |
|---|---|---|---|

## Human decision needed
```

### `REPAIR_PROMPT.md` template

```markdown
# REPAIR_PROMPT — [TICKET_ID] — [Title]

The audit returned:

```text
PASS / HOLD / REJECT
```

Repair only the findings below. Do not broaden scope.

## Findings to repair

```text

```

## Allowed files/folders

```text

```

## Forbidden actions

```text

```

## Required outputs

```text
reports/[TICKET_ID]/REPAIR_IMPLEMENTATION_REPORT.md
reports/[TICKET_ID]/REPAIR_CHANGED_FILES.md
reports/[TICKET_ID]/REPAIR_TEST_RESULTS.md
audits/[TICKET_ID]/REPAIR_AUDIT_REPORT.md
```

## Return

```text
Repairs made:
Files changed:
Tests run:
Remaining issues:
Ready for re-audit? YES/NO
```
```

---

## 19. PASS / HOLD / REJECT rules

### PASS

A ticket may receive `PASS` only if:

```text
acceptance criteria are satisfied
required tests/checks passed or validly skipped
scope matched the ticket
forbidden files/actions were avoided
no blocking security/privacy/data/file-access issue exists
no unapproved dependency/migration/deployment change occurred
source-of-truth docs are updated if required
human gates are either not triggered or explicitly resolved
artifacts are written to expected paths
next action is clear
```

### HOLD

A ticket receives `HOLD` if:

```text
direction is mostly correct
scope is mostly intact
repair is likely bounded
one or more acceptance/docs/test/evidence issues block pass
human gate is triggered but not resolved
missing artifact prevents closeout
tests were skipped without enough explanation
```

### REJECT

A ticket receives `REJECT` if:

```text
wrong scope was implemented
product strategy was invented
forbidden files/actions occurred
security/privacy/data/file-access risk was introduced
dependency/migration/deployment changes bypassed gate
tests contradict claimed success
implementation cannot be repaired within ticket scope
source-of-truth was overwritten or corrupted
full ES.zip or prohibited data was committed
AI/broker/live-trading behavior was activated
```

### Auditor verdict format

The Auditor must return exactly one:

```text
PASS
HOLD
REJECT
```

Then explain:

```text
why
blocking findings
non-blocking findings
human decision needed
repair prompt path, if any
```

---

## 20. QA gate matrix

| Gate | Applies when | Required check | Human gate? |
|---|---|---|---:|
| Scope gate | Every ticket | Work matches ticket and plan. | If drift |
| Acceptance gate | Every ticket | Criteria satisfied with evidence. | If ambiguous |
| Test gate | Every ticket | Required tests/checks run or skipped with reason. | If failing |
| Source-of-truth gate | Docs/status/roadmap/claim changes | Current docs updated and archive preserved. | If active truth changes |
| Dependency gate | New/changed dependency | Justification, lockfile review, security consideration. | **Yes** |
| File-access gate | Workspace/import/export/storage behavior | Paths constrained, no destructive behavior. | **Yes** |
| Data boundary gate | Dataset/fixture/ES.zip changes | No raw full data committed; fixture policy followed. | **Yes** |
| Security gate | Secrets/auth/permissions/sandboxing | No secrets; permissions explicit. | **Yes** |
| Privacy gate | User data/logs/workspace metadata | Minimal local data; retention/export notes if relevant. | **Yes** |
| Packaging gate | Installer/signing/updater changes | Windows packaging behavior reviewed. | **Yes** |
| AI gate | AI proposal/generation behavior | Quarantine and non-evidence rules preserved. | **Yes** |
| Trading/broker gate | Broker/live trading/order behavior | Explicitly blocked for MVP. | **Yes / stop** |
| Evidence gate | Evidence Cards/replay/results | Visuals do not replace aggregate evidence. | If unclear |
| Audit gate | Every ticket closeout | Auditor returns PASS/HOLD/REJECT. | If HOLD/REJECT |
| Release gate | Any public distribution | Human approval required. | **Yes** |

---

## 21. Security / privacy / data / file-access gates

NullForge is local-first, but local-first does not mean risk-free.

### Always gated

Stop before changing:

```text
file import behavior
zip extraction behavior
workspace deletion behavior
raw data retention
fixture generation and commit policy
Tauri filesystem permissions
sidecar process permissions
external command execution
installer/signing/updater behavior
logging of dataset paths or user files
dependency chain
AI activation
broker/live-trading integration
```

### File-access baseline

Future implementation must respect:

```text
User-selected workspace only.
No scanning arbitrary directories by default.
No destructive operations without confirmation.
No automatic upload.
No cloud sync for MVP.
No hidden telemetry.
No full ES.zip committed to repo.
No raw data path leakage in public reports.
```

### Sidecar baseline

Future implementation must respect:

```text
Tauri shell calls only explicit allowed ResearchCore Engine commands.
No arbitrary shell execution.
Command inputs must be validated.
Outputs must be structured.
Errors must be surfaced.
Logs must avoid sensitive raw paths where possible.
```

---

## 22. Human gate triggers

Human approval is required before:

```text
dependency changes
installer/signing/public distribution changes
Tauri permission broadening
file access broadening
data deletion or overwrite behavior
full ES.zip import/retention policy changes
small fixture publication
external API/network access
auth/account/cloud sync
billing/payment
AI proposal/generator activation
broker/live trading/order execution
schema/contract reversal
architecture reversal
large refactor
source-of-truth replacement
claim promotion
release
merge, unless explicitly delegated later
```

### Human gate record

When triggered, create or update:

```text
docs/DECISION_LEDGER.md
docs/adr/ADR-XXX-[decision].md
reports/[TICKET_ID]/HUMAN_GATE_REQUEST.md
```

The request must include:

```text
decision needed
options
recommendation
risk
reversal condition
what happens if no decision is made
```

---

## 23. Milestone batching rules

Milestone batching is allowed **after** the roadmap/ticket volume exists and the first milestone pack is generated.

### Core rule

```text
Batch prompts.
Execute tickets serially.
Audit every pass.
Return at gates.
```

### Milestone batch may include

```text
MILESTONE_BRIEF.md
TICKET_QUEUE.md
DEPENDENCY_MAP.md
CONTEXT_REFRESH_RULES.md
HUMAN_GATE_TRIGGERS.md
MILESTONE_ACCEPTANCE.md
MILESTONE_HANDOFF_TEMPLATE.md
MILESTONE_AUDIT_PROMPT.md
tickets/
prompts/
```

### Milestone batch may not

```text
let Codex choose product strategy
skip context curator
skip planner
skip auditor
merge without human gate
release publicly
execute tickets in parallel when they touch shared state
continue after source-of-truth conflict
continue after repeated HOLD/REJECT
```

### Ticket execution inside batch

Each ticket still requires:

```text
one ticket
one branch
one context bundle
one plan
one implementation report
one audit
one human gate if triggered
```

### Return to Human / ChatGPT when

```text
milestone completes
ticket is blocked
audit returns repeated HOLD/REJECT after one repair
human gate triggers
source-of-truth conflict appears
dependency/security/packaging/data gate triggers
milestone goal no longer matches reality
```

---

## 24. Stop conditions

Stop immediately if:

```text
repo is dirty before ticket start
main cannot be pulled cleanly
ticket dependencies are not PASS or explicitly deferred
current status conflicts with ticket queue
source docs conflict
required context is missing
acceptance criteria are unclear
tests cannot be identified
scope must expand
new dependency seems necessary
Tauri permissions need broadening
Python sidecar execution model must change
dataset import needs raw/private data handling change
full ES.zip might be committed
security/privacy concern appears
AI strategy generation is requested
broker/live trading behavior appears
public release/distribution is requested
audit returns REJECT
repair would exceed ticket scope
```

Stop means:

```text
write blocker report
do not continue autonomous execution
return to Human / ChatGPT Architect
```

---

## 25. Docs-only ticket compression rule

Some early NullForge tickets will be docs-only. They may use compressed artifacts, but cannot skip plan → evidence → audit.

### Eligible for compression

```text
volume promotion
ADR creation
source-of-truth baseline
ticket template creation
prompt template creation
archive inventory
```

### Not eligible for compression

```text
code changes
dependency changes
Tauri permissions
Python sidecar bridge
dataset import
zip extraction
file deletion
fixture publication
visual replay implementation
logic compiler behavior
AI/broker/cloud/auth/payment behavior
```

### Compressed docs-only artifact set

For docs-only tickets, if the human explicitly allows compression:

```text
tickets/[TICKET_ID].md
reports/[TICKET_ID]/DOCS_CHANGE_REPORT.md
audits/[TICKET_ID]/DOCS_AUDIT.md
```

The docs audit must still check:

```text
scope
source-of-truth consistency
links/paths
conflicts with existing docs
archive/quarantine handling
next action
```

---

## 26. First milestone categories, without implementation tickets

Do not generate full implementation tickets yet. Those belong in Volume 7 / milestone packs.

The first milestone categories should be:

| Milestone | Category | Purpose | Ticket types |
|---|---|---|---|
| `M0` | Repo/source baseline | Promote current planning into repo docs and preserve old work safely. | docs, ADR, inventory, status |
| `M1` | Desktop bridge spike | Prove Windows/Tauri shell can call ResearchCore Engine smoke command. | spike, scaffold, QA |
| `M2` | Dataset Studio proof | Prove fixture import and DatasetCapabilityMap contract. | data, docs, UI, QA |
| `M3` | Logic compiler proof | Prove one LogicCard can compile to a test-ready spec. | logic, compiler, QA |
| `M4` | Visual Replay fixture | Prove one replay fixture can render known-at-time labels and trade annotations. | replay, UI, QA |
| `M5` | Evidence Card proof | Prove artifact metadata, nulls/ablations placeholders, and decision status can be shown together. | evidence, audit, UI |
| `M6` | Windows packaging proof | Prove local desktop app can be packaged for Windows 11 x64 for internal use. | packaging, QA, release gate |

### Dependency order

```text
M0 → M1 → M2 → M3 → M4 → M5 → M6
```

Possible later dependency refinement:

```text
M2 and M3 may proceed in parallel only if they do not share implementation files and each has its own branch/audit path.
```

Default remains serial.

---

## 27. What Codex may and may not automate

### Codex may automate

```text
scoped docs changes
scoped scaffold creation
test file creation when accepted
small fixture generation when fixture policy allows
local smoke scripts
Tauri shell scaffolding when ticketed
ResearchCore Engine command invocation when contract exists
artifact metadata parsing when ticketed
UI components when specified
reports and audit prompts
```

### Codex may not automate

```text
product strategy
claim promotion
public brand/trademark decisions
legal/privacy decisions
public release
merge
dependency approval
Tauri permission expansion
raw data publication
full ES.zip commit
data licensing decisions
AI-generated executable trading logic
broker/live trading integration
secret handling
billing/payment
auth/cloud sync
architecture reversals
```

---

## 28. Volume 2 closeout

### Generated artifact

```text
Volume 2 — NullForge Planner / Implementor / Auditor Loop, QA Gates, Human Gates, and Codex Execution System v0.4
```

### Decisions promoted in this volume

```text
Direct-to-Codex implementation is forbidden.
The role loop is mandatory before implementation.
Every implementation ticket must have context, plan, report, audit, and gate handling.
Ticket namespaces must be prefixed.
Milestone batching is allowed only with serial ticket execution and per-ticket audits.
Human gates are mandatory for dependency/security/data/file-access/AI/broker/release changes.
Docs-only tickets may use compressed artifacts only when explicitly allowed and still audited.
```

### Still not generated

```text
Volume 3
implementation code
implementation tickets
milestone packs
Tauri scaffold
sidecar bridge code
Dataset Studio code
Logic Factory code
Visual Replay code
Evidence Card code
```

### Current decision

```text
PROMOTE_TO_VOLUME_3_AFTER_REVIEW
```

### Next artifact

```text
Volume 3 — NullForge Windows + Tauri Desktop Architecture, ResearchCore Engine Bridge, Sidecar Contract, and Packaging Spike Plan
```

---

## 29. Prompt for Volume 3

The exact next prompt is stored separately as:

```text
prompts/NullForge_Prompt_For_Volume_03_v0_4.md
```

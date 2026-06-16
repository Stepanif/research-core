# NullForge Codex Role Loop

Date: `2026-06-16`

Status: Accepted for CX-T001 implementation review; not implementation proof.

## Context

CX-T001 adapts the repo-local NullForge role loop from Volume 02 into active workflow documentation for later tickets. ADR-T002 has audit decision `PASS`, and CX-T001 is the next M0 ticket before MB-T001.

Primary sources:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
- `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`
- `audits/nullforge/ADR-T002/AUDIT_REPORT.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_02_Planner_Implementor_Auditor_Loop_QA_Gates_Human_Gates_Codex_Execution_System_v0_4.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`

No NullForge implementation code has started.

This document is workflow/source documentation only. It does not prove app behavior, Tauri feasibility, packaging feasibility, bridge reliability, local workspace safety, telemetry enforcement, no-cloud technical enforcement, product validation, user validation, market validation, trading validity, financial advice safety, legal/trademark clearance, data licensing safety, public distribution safety, or implementation governance before audit.

## Role Loop

Every scoped NullForge ticket follows this loop:

```text
Human / ChatGPT Architect -> Context Curator -> Planner -> Implementor / Codex -> Auditor -> Repair if needed -> human gate -> Next ticket
```

The loop is serial by default. Batch prompts may prepare a milestone, but tickets execute one at a time and each ticket still needs scoped artifacts and independent audit.

Direct prompts such as `build NullForge` are forbidden. A ticket starts only when source context, scope, acceptance criteria, tests/checks, forbidden actions, and human gate triggers are clear.

## Human / ChatGPT Architect

The Human / ChatGPT Architect owns mission, scope, ticket selection, milestone intent, human gates, merge/release decisions, source promotion decisions, architecture reversals, and public distribution approval.

May:

- select the next ticket or milestone;
- approve dependencies and human-gated scope changes;
- accept, reject, or defer audit outcomes;
- decide whether archive, quarantine, prompt, or incoming package material should be promoted through a scoped ticket;
- stop a batch when reality no longer matches the plan.

Must not:

- treat unaudited Codex output as active truth;
- skip audit because output looks plausible;
- merge, release, publish, or distribute work that triggered unresolved human gates;
- let old chats, prompt files, or incoming package material become active truth without scoped promotion;
- let implementation outrun current ADR, status, and ticket boundaries.

## Context Curator

The Context Curator creates the smallest sufficient active context for one ticket. The Context Curator does not plan implementation and does not code.

Owns:

- ticket summary and mission slice;
- active source docs;
- relevant repo files/folders;
- current repo state summary;
- constraints, forbidden actions, known risks, required checks, and human gate triggers;
- dependencies, blockers, excluded context, and open questions.

Outputs:

```text
plans/nullforge/[TICKET_ID]/CONTEXT_BUNDLE.md
plans/nullforge/[TICKET_ID]/CONTEXT_BUNDLE_MANIFEST.md
```

Must not:

- include the whole repo by default;
- include old prompts, chats, or external packages as active truth;
- include raw/full ES.zip or private/local data;
- invent product strategy;
- write implementation plans;
- code;
- promote design memory.

## Planner

The Planner consumes the context bundle and produces a bounded implementation plan. The Planner does not code.

Owns:

```text
plans/nullforge/[TICKET_ID]/PLAN.md
plans/nullforge/[TICKET_ID]/ACCEPTANCE.md
plans/nullforge/[TICKET_ID]/IMPLEMENTOR_PROMPT.md
```

`PLAN.md` must include goal, source context used, assumptions, scope, out-of-scope items, planned file changes, steps, tests/checks, security/privacy/data/file-access considerations, human gate triggers, rollback/repair route, and planner verdict.

`ACCEPTANCE.md` must include testable criteria, required outputs, required tests/checks, source-of-truth update expectations, forbidden-pass conditions, and done definition.

`IMPLEMENTOR_PROMPT.md` must include ticket ID, mission slice, allowed files/folders, forbidden files/folders/actions, required outputs, acceptance criteria, tests/checks, report format, human gate triggers, and explicit instruction not to broaden scope.

Must not:

- code;
- broaden the ticket;
- change product strategy;
- weaken acceptance criteria to make implementation easier;
- approve dependencies, migrations, file-access expansion, or permissions silently;
- generate broad build prompts.

## Implementor / Codex

The Implementor executes only the scoped plan. Codex is a build assistant, not the product owner.

Owns:

```text
reports/nullforge/[TICKET_ID]/IMPLEMENTATION_REPORT.md
reports/nullforge/[TICKET_ID]/CHANGED_FILES.md
reports/nullforge/[TICKET_ID]/TEST_RESULTS.md
reports/nullforge/[TICKET_ID]/AUDITOR_PROMPT.md
```

May:

- make only scoped changes allowed by the ticket;
- run required checks;
- record skipped checks with exact reasons;
- report blockers;
- stop and request human review when a gate triggers.

Must not:

- invent product strategy;
- change acceptance criteria;
- modify unrelated or forbidden files;
- add dependencies silently;
- change auth, permissions, migrations, deployment, CI, package files, generated docs, or schemas without explicit scope and human approval where required;
- commit secrets;
- merge, push, release, or publicly distribute unless explicitly requested in a later scoped workflow;
- claim production readiness;
- treat generated logic, visual replay, or weak evidence as proof;
- commit raw/full ES.zip, private/local data, generated datasets, or ES-derived fixtures;
- activate AI strategy generation, broker/live trading, cloud sync, auth, billing, marketplace, mobile, telemetry, or public release behavior.

## Auditor

The Auditor independently checks implementation against the ticket, plan, acceptance criteria, active source docs, and safety gates. The Auditor should run in a fresh pass/session when possible.

Owns:

```text
audits/nullforge/[TICKET_ID]/AUDIT_REPORT.md
audits/nullforge/[TICKET_ID]/FINDINGS.md
audits/nullforge/[TICKET_ID]/REPAIR_PROMPT.md
```

Must check:

- scope matched ticket and plan;
- acceptance criteria were satisfied;
- required tests/checks passed or were validly skipped;
- forbidden files/actions were avoided;
- source-of-truth docs were updated correctly;
- no secrets, silent dependencies, migrations, auth, permissions, deployment, code, data, or release changes occurred outside scope;
- no product strategy was invented;
- human gate triggers were identified;
- next action is justified.

Must not:

- grade its own implementation;
- silently repair;
- merge, release, or change strategy;
- promote weak evidence;
- ignore failed checks or unresolved human gates.

## Repair Implementor

If audit returns HOLD or REJECT, repair stays bounded to the listed findings.

Repair may:

- fix blocking findings;
- update tests/docs required by the findings;
- clarify acceptance status.

Repair must not:

- expand scope;
- open unrelated refactors;
- add new features;
- hide failures;
- skip re-audit.

Default limit: one autonomous repair attempt per ticket. After one failed repair, return to the Human / ChatGPT Architect.

## Artifact Tree

Default per-ticket artifact tree:

```text
plans/nullforge/[TICKET_ID]/
  CONTEXT_BUNDLE.md
  CONTEXT_BUNDLE_MANIFEST.md
  PLAN.md
  ACCEPTANCE.md
  IMPLEMENTOR_PROMPT.md

reports/nullforge/[TICKET_ID]/
  IMPLEMENTATION_REPORT.md
  CHANGED_FILES.md
  TEST_RESULTS.md
  AUDITOR_PROMPT.md
  REPAIR_IMPLEMENTATION_REPORT.md   # only if needed
  REPAIR_CHANGED_FILES.md           # only if needed
  REPAIR_TEST_RESULTS.md            # only if needed

audits/nullforge/[TICKET_ID]/
  AUDIT_REPORT.md
  FINDINGS.md
  REPAIR_PROMPT.md
  REPAIR_AUDIT_REPORT.md            # only if needed
```

Prompt files and milestone/ticket files are not created by default. They require separate scoped tickets unless the current ticket explicitly allows them.

Artifact rules:

- use the full ticket ID in every folder name;
- do not rewrite prior ticket artifacts;
- append repair artifacts instead of replacing original reports;
- link artifacts from closeout/status/source docs only when files exist;
- preserve archive and quarantine boundaries.

## Required Sections

`CONTEXT_BUNDLE.md` should include ticket summary, mission slice, active source docs, relevant repo files/folders, current repo state, constraints, forbidden actions, required tests/checks, human gate triggers, prior related tickets/audits, excluded context, open questions, and ready-for-planner verdict.

`CONTEXT_BUNDLE_MANIFEST.md` should include included sources, excluded sources, archive/design-memory references, expiry/refresh rule, context risks, and curator verdict.

`PLAN.md` should include goal, source context used, assumptions, scope, out of scope, planned file changes, steps, tests/checks, security/privacy/data/file-access considerations, human gate triggers, rollback/repair route, and planner verdict.

`ACCEPTANCE.md` should include acceptance criteria, required outputs, required tests/checks, source-of-truth updates required, forbidden-pass conditions, and done definition.

`IMPLEMENTOR_PROMPT.md` should include allowed files/folders, forbidden files/folders/actions, required outputs, checks, report format, and human gate triggers.

`IMPLEMENTATION_REPORT.md` should include branch, ticket ID, summary, files changed, acceptance status, commands run, tests/checks passed/failed/skipped, deviations, dependency/security/migration/deployment changes, data/file-access changes, known issues, human gate status, and next recommended action.

`CHANGED_FILES.md` should include all changed files, why each file changed, whether it was expected by plan, forbidden-file check, and unexpected changes.

`TEST_RESULTS.md` should include commands run, result for each command, passed checks, failed checks, skipped checks, environment notes, manual checks, and test verdict.

`AUDITOR_PROMPT.md` should include the ticket ID, files to read, audit focus, known risks, human gate triggers, required auditor outputs, and requested PASS / HOLD / REJECT verdict format.

`AUDIT_REPORT.md`, `FINDINGS.md`, and `REPAIR_PROMPT.md` should record verdict, findings, required repair, and bounded repair instructions.

## PASS / HOLD / REJECT

PASS requires:

- acceptance criteria satisfied;
- required tests/checks passed or were validly skipped;
- scope matched the ticket;
- forbidden files/actions avoided;
- no blocking security/privacy/data/file-access issue;
- no unapproved dependency, migration, auth, permission, deployment, or release change;
- source-of-truth updates completed where required;
- human gates not triggered or explicitly resolved;
- artifacts written to expected paths;
- next action clear.

HOLD applies when:

- direction is mostly correct but acceptance, docs, test, artifact, or evidence issues block pass;
- a human gate is triggered but unresolved;
- checks were skipped without enough explanation;
- repair is likely bounded.

REJECT applies when:

- wrong scope was implemented;
- product strategy was invented;
- forbidden files/actions occurred;
- security/privacy/data/file-access risk was introduced;
- dependency/migration/deployment changes bypassed gates;
- checks contradict claimed success;
- source-of-truth was overwritten or corrupted;
- full ES.zip or prohibited data was committed;
- AI, broker/live trading, cloud/auth/billing, public release, or financial-advice behavior was activated.

## Human Gates

A human gate is required before:

- dependency changes;
- installer, signing, updater, or public distribution changes;
- Tauri permission broadening;
- file access broadening;
- data deletion, overwrite, import, extraction, retention, or fixture-publication changes;
- full ES.zip, private/local data, generated datasets, or ES-derived fixture handling;
- external API or network access;
- auth, accounts, cloud sync, hosted backend, billing, mobile, marketplace, telemetry, AI/model calls, broker/live trading, or live execution;
- schema/contract reversal;
- architecture reversal;
- large refactor;
- source-of-truth replacement;
- claim promotion;
- merge or release unless explicitly delegated later.

If a human gate triggers, stop and write the decision needed, options, recommendation, risk, reversal condition, and what happens if no decision is made. Do not continue autonomous execution.

## Stop Conditions

Stop immediately if a stop condition appears:

- repo is dirty outside the scoped ticket files before implementation starts;
- dependencies are missing, not PASS, or not explicitly deferred;
- current status conflicts with ticket queue;
- source docs conflict;
- required context is missing;
- acceptance criteria are unclear;
- tests/checks cannot be identified;
- scope must expand;
- a new dependency appears necessary;
- Tauri permissions, filesystem access, sidecar command surface, or external command execution need broadening;
- raw/private data handling or full ES.zip handling changes;
- security/privacy concern appears;
- AI strategy generation, broker/live trading, or public release is requested;
- audit returns REJECT;
- repair would exceed ticket scope.

## Docs-Only Tickets

Docs-only tickets may create or update bounded source docs and reports. They still require context, plan, acceptance criteria, implementor report, changed files, test/check results, auditor prompt, and independent audit.

Docs-only tickets must not use their documentation status to claim implementation proof. They must not modify implementation code, dependencies, CI, schemas, tests, package files, generated docs, raw data, fixtures, app scaffolds, bridge code, sidecars, or release behavior unless a later scoped ticket allows it.

## Branch And Ticket Hygiene

Default branch pattern:

```text
docs/[TICKET_ID]-short-title
task/[TICKET_ID]-short-title
fix/[TICKET_ID]-short-title
spike/[TICKET_ID]-short-title
```

Rules:

- one branch per ticket unless the human explicitly chooses otherwise;
- no unrelated cleanup;
- no combined feature branches;
- no merge without audit and human gate handling;
- pull/refresh main before the next ticket after branch closeout;
- do not push, merge, or delete branches unless explicitly asked.

## Source Truth, Archive, Quarantine, And Prompts

Active docs are repo-local files created or imported by scoped role-loop tickets and accepted by audit disposition.

Design memory can inform later work, but it does not authorize implementation or prove claims by itself.

Archive material is memory without authority. Older source packages, old chat logs, superseded prompts, and prior drafts remain outside active truth unless a later audited ticket promotes them.

Quarantine is for unresolved, conflicting, risky, private, local-only, or unreviewed material. Quarantined material has no governance power.

Prompt files are workflow instructions, not canonical product or architecture source by default. Prompt files, old chats, and incoming package prompts are not active truth unless a later scoped and audited ticket promotes them.

## ADR Boundaries To Preserve

ADR-T001 boundaries:

- `NullForge` is a working product name only;
- repo remains `research-core`;
- internal engine label remains `ResearchCore Engine`;
- first platform is Windows 11 x64;
- Tauri + React/TypeScript is a default direction only, pending bridge and packaging spikes;
- future engine boundary is a Python ResearchCore Engine sidecar / scoped command bridge;
- no public release, trademark/legal, Tauri, packaging, bridge, product, user, market, financial-advice, trading, or distribution proof is claimed.

ADR-T002 boundaries:

- MVP is local-first by default;
- one selected local workspace is the planning runtime boundary;
- local ResearchCore Engine execution remains future scoped sidecar / command bridge work;
- tiny/small fixtures require later approved fixture policy;
- full ES.zip, raw/private data, generated datasets, and ES-derived fixtures remain gated;
- cloud storage, cloud sync, hosted backend, account/auth, billing, telemetry/analytics, mobile, marketplace, broker-live integration, live execution, public distribution, updater/signing/release channel, and financial advice scope are outside MVP.

## CX-T001 Boundaries And Non-Decisions

CX-T001 creates role-loop workflow documentation and CX-T001 implementation reports only.

CX-T001 does not decide or create:

- implementation code;
- app files;
- Tauri scaffold;
- bridge command contract;
- sidecar implementation;
- dependencies;
- schemas;
- tests;
- generated docs;
- CI;
- tickets;
- milestones;
- prompt archive;
- QA docs;
- data import;
- fixtures;
- ES.zip parsing;
- telemetry enforcement;
- network controls;
- cloud/auth/billing/mobile/marketplace/broker/live/AI/updater/signing/public release scope;
- legal/trademark, financial-advice, trading, product, user, market, validation, or data-licensing proof;
- MB-T001, ADR-T003, M1, or downstream work.

## Next Action

After CX-T001 independent audit disposition, the next ticket is `MB-T001`.

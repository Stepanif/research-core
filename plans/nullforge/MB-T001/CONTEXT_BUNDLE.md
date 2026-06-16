# MB-T001 Context Bundle

Ticket: `MB-T001`

Role: Context Curator

Date: `2026-06-16`

Ready for planner: YES

## Ticket Summary

`MB-T001` is the NullForge M0 milestone handoff ticket. It should summarize the completed M0 repo source import and canonical baseline work, record readiness and limits, and prepare the repo-local handoff from M0 toward later scoped tickets.

This context bundle does not plan or implement `MB-T001`.

## M0 Mission Slice

M0 is `Repo Source Import + Canonical Baseline`.

The M0 goal from Volume 07 is to promote reviewed NullForge planning volumes into `research-core` as project-specific current docs without overwriting existing ResearchCore Engine truth.

The M0 ticket set for this handoff is:

- `PF-T000` - Repo inventory and NullForge import plan.
- `PF-T001` - Import NullForge volumes into repo docs.
- `PF-T002` - Create NullForge current status and source index.
- `ADR-T001` - Name/platform/stack/engine ADR.
- `ADR-T002` - Local-first/no-cloud MVP ADR.
- `CX-T001` - NullForge Codex role-loop docs.
- `MB-T001` - M0 milestone handoff.

M0 explicit non-goals remain:

- No Tauri app.
- No engine changes.
- No dataset parser.
- No fixture creation.
- No desktop bridge implementation.
- No public release.
- No repo rename.

## Completed Dependencies

| Ticket | Audit evidence | Status for MB-T001 |
|---|---|---|
| `PF-T000` | `audits/nullforge/PF-T000/AUDIT_REPORT.md` contains `Decision: PASS`. | Complete dependency. |
| `PF-T001` | `audits/nullforge/PF-T001/AUDIT_REPORT.md` contains `Decision: PASS`. | Complete dependency. |
| `PF-T002` | `audits/nullforge/PF-T002/AUDIT_REPORT.md` contains `Decision: PASS`. | Complete dependency. |
| `ADR-T001` | `audits/nullforge/ADR-T001/AUDIT_REPORT.md` contains `Decision: PASS`. | Complete dependency. |
| `ADR-T002` | `audits/nullforge/ADR-T002/AUDIT_REPORT.md` contains `Decision: PASS`. | Complete dependency. |
| `CX-T001` | `audits/nullforge/CX-T001/AUDIT_REPORT.md` contains `Decision: PASS`. | Complete dependency. |

`CURRENT_STATUS.md` says `MB-T001` is the next scoped ticket after CX-T001 closeout.

## Active Source Docs

| Source | Role in MB-T001 context |
|---|---|
| `docs/nullforge/CURRENT_STATUS.md` | Current M0 status, dependency statuses, gates, claim status, and out-of-scope boundaries. |
| `docs/nullforge/SOURCE_INDEX.md` | Repo-local source map, active docs, imported volumes, completed ticket artifacts, and pending downstream docs. |
| `docs/nullforge/DECISION_LEDGER.md` | Accepted decisions `NF-D0001` through `NF-D0005` and pending `NF-D0006`; confirms accepted entries do not authorize implementation code. |
| `docs/nullforge/ARCHIVE_POLICY.md` | Authority boundary for active docs, design memory, archive, quarantine, prompts, and source promotion. |
| `docs/nullforge/codex/CODEX_ROLE_LOOP.md` | NullForge role loop, artifact tree, PASS/HOLD/REJECT rules, docs-only ticket rules, human gates, and stop conditions. |
| `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` | Accepted working product name, first platform, desktop stack direction, and ResearchCore Engine boundary. |
| `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` | Accepted local-first/no-cloud MVP boundary and exclusions. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | M0 milestone package source, ticket sequence, milestone handoff template, and downstream sequence context. |

## Relevant Repo Files And Folders For Later MB-T001 Planning

Minimum likely inputs:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/README.md`
- `docs/nullforge/import/`
- `docs/nullforge/blueprint/volumes/`
- `docs/nullforge/adr/`
- `plans/nullforge/PF-T000/`
- `plans/nullforge/PF-T001/`
- `plans/nullforge/PF-T002/`
- `plans/nullforge/ADR-T001/`
- `plans/nullforge/ADR-T002/`
- `plans/nullforge/CX-T001/`
- `reports/nullforge/PF-T000/`
- `reports/nullforge/PF-T001/`
- `reports/nullforge/PF-T002/`
- `reports/nullforge/ADR-T001/`
- `reports/nullforge/ADR-T002/`
- `reports/nullforge/CX-T001/`
- `audits/nullforge/PF-T000/`
- `audits/nullforge/PF-T001/`
- `audits/nullforge/PF-T002/`
- `audits/nullforge/ADR-T001/`
- `audits/nullforge/ADR-T002/`
- `audits/nullforge/CX-T001/`
- `plans/nullforge/MB-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/MB-T001/CONTEXT_BUNDLE_MANIFEST.md`

Likely future MB-T001 outputs should be chosen by the planner. The curator notes that the role-loop default artifact tree normally expects plan, acceptance, implementor prompt, reports, audit artifacts, and any explicitly allowed milestone handoff doc paths.

## Explicitly Excluded Files And Folders

Excluded from MB-T001 context curation and not to be modified by this curator pass:

- `tickets/nullforge/`
- `milestones/nullforge/`
- `prompts/`
- `docs/nullforge/qa/`
- `reports/nullforge/MB-T001/`
- `audits/nullforge/MB-T001/`
- `plans/nullforge/MB-T001/PLAN.md`
- `plans/nullforge/MB-T001/ACCEPTANCE.md`
- `plans/nullforge/MB-T001/IMPLEMENTOR_PROMPT.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/adr/`
- `docs/nullforge/blueprint/volumes/`
- ResearchCore Engine docs and code.
- `src/`, `tests/`, `schemas/`, `fixtures/`, package files, CI config, generated docs, raw/private data, and ES-derived fixtures.

Excluded downstream work:

- M1.
- `QA-T001`.
- `ADR-T003`.
- Desktop shell or Tauri scaffold work.
- Bridge, sidecar, command, parser, data, schema, fixture, packaging, release, network, cloud, telemetry, auth, billing, broker/live, or public distribution work.

## Current Repo State

At curator start:

- Branch: `main`.
- Tracking: `main...origin/main`.
- Worktree: clean.
- Latest known NullForge closeout commit on `main`: `7b30ac0a005d0e8430368e792f8db8c1902e0e35`.
- NullForge active phase: `REPO_SOURCE_IMPORT_BASELINE`.
- Current status still names active ticket `CX-T001` and next action `MB-T001` after CX-T001 closeout.
- No NullForge implementation code has started.

After this curator pass, only these files should be uncommitted:

- `plans/nullforge/MB-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/MB-T001/CONTEXT_BUNDLE_MANIFEST.md`

## Known Gates And Stop Conditions

Human gate triggers:

- Any proposed overwrite or reinterpretation of existing ResearchCore Engine docs or code.
- Any attempt to import milestone docs, ticket files, prompt files, raw/private data, old chat logs, or full ES.zip contents into active repo-local paths without explicit scoped approval.
- Any move from M0 handoff into M1, `QA-T001`, `ADR-T003`, app/code implementation, tests, schemas, generated docs, fixtures, dependencies, package files, CI, release, network, cloud, telemetry, auth, billing, broker/live, or public distribution.
- Any legal/trademark/public naming claim, financial advice claim, product validation claim, market claim, trading validity claim, data licensing claim, or release-readiness claim.
- Any mismatch between source docs and audit evidence.

Stop conditions:

- Any prerequisite audit is missing or not `PASS`.
- The worktree contains unrelated uncommitted changes outside the allowed MB-T001 curator files.
- A later stage needs to modify files not explicitly allowed by its own prompt.
- A later stage would need to create `tickets/`, `milestones/`, `prompts/`, QA docs, code, tests, schemas, fixtures, package files, CI, generated docs, or downstream artifacts without explicit authorization.
- `No NullForge implementation code has started.` is removed or contradicted.

## Constraints And Forbidden Actions

For this curator pass:

- Do not plan `MB-T001`.
- Do not implement `MB-T001`.
- Do not create `PLAN.md`, `ACCEPTANCE.md`, `IMPLEMENTOR_PROMPT.md`, reports, audits, milestone docs, ticket files, prompts, QA docs, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, or downstream artifacts.
- Do not modify current status, source index, decision ledger, archive policy, ADR files, audit files, imported volume files, existing M0 artifacts, or ResearchCore Engine docs/code.
- Do not start M1, `QA-T001`, `ADR-T003`, or downstream work.

For later MB-T001 planning:

- Keep MB-T001 docs/audit handoff only unless the human prompt explicitly allows additional output paths.
- Preserve ResearchCore Engine as separate engine truth.
- Preserve ADR-T001 and ADR-T002 boundaries.
- Keep imported volume claims as planning/design memory unless promoted by audited scoped work.

## Required Checks For Later Stages

Recommended bounded checks for the MB-T001 planner:

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `rg -n "Decision: PASS" audits\nullforge\PF-T000\AUDIT_REPORT.md audits\nullforge\PF-T001\AUDIT_REPORT.md audits\nullforge\PF-T002\AUDIT_REPORT.md audits\nullforge\ADR-T001\AUDIT_REPORT.md audits\nullforge\ADR-T002\AUDIT_REPORT.md audits\nullforge\CX-T001\AUDIT_REPORT.md`
- `rg -n "MB-T001|M0|QA-T001|CX-T001|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md docs\nullforge\codex\CODEX_ROLE_LOOP.md`

Recommended bounded checks for later implementor/auditor stages should be chosen by the planner, but should include:

- verifying all six prerequisite audit reports still contain `Decision: PASS`;
- verifying any MB-T001 handoff docs link only to repo-local files that exist;
- verifying no forbidden paths are created;
- verifying ResearchCore Engine docs/code, package files, schemas, tests, CI, generated docs, raw/private data, and fixtures remain untouched;
- verifying `MB-T001`, `QA-T001`, `ADR-T003`, and M1 are mentioned only as status/next-action context unless explicitly in scope.

## Open Questions

No blocking open questions.

Non-blocking items for the planner to decide:

- The exact allowed output path for the M0 milestone handoff doc, if any, because `milestones/nullforge/` is still pending downstream and should not be created unless explicitly authorized.
- Whether the MB-T001 implementor should update `CURRENT_STATUS.md` and `SOURCE_INDEX.md` during closeout, or leave those updates to audit/commit closeout.
- Whether MB-T001 should recommend `QA-T001` as the first M1-scoped step or require a separate human decision after M0 PASS.

## Ready For Planner Verdict

YES.

The context is bounded, prerequisites have audit `PASS`, and no M1 or implementation work is needed to begin MB-T001 planning.

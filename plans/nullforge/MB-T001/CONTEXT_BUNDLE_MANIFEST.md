# MB-T001 Context Bundle Manifest

Ticket: `MB-T001`

Role: Context Curator

Date: `2026-06-16`

## Created Artifacts

- `plans/nullforge/MB-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/MB-T001/CONTEXT_BUNDLE_MANIFEST.md`

No other MB-T001 artifacts were created.

## Included Sources

| Source | Inclusion reason | Authority boundary |
|---|---|---|
| `docs/nullforge/CURRENT_STATUS.md` | Current phase, dependency status, gates, claim status, out-of-scope list, and MB-T001 next action. | Active status baseline; does not authorize implementation. |
| `docs/nullforge/SOURCE_INDEX.md` | Repo-local source map, active docs, imported volumes, existing ticket artifacts, and pending downstream docs. | Active source navigation; links only to repo-local files that exist. |
| `docs/nullforge/DECISION_LEDGER.md` | Accepted decision list and pending source import item. | Accepted entries do not authorize implementation code. |
| `docs/nullforge/ARCHIVE_POLICY.md` | Active docs, design memory, archive, quarantine, prompt, and promotion policy. | Governs source authority and promotion boundaries. |
| `docs/nullforge/codex/CODEX_ROLE_LOOP.md` | Context Curator role, artifact tree, PASS/HOLD/REJECT, human gates, stop conditions, docs-only rules, and next-action sequence. | Active workflow source after CX-T001 audit `PASS`; not implementation proof. |
| `audits/nullforge/PF-T000/AUDIT_REPORT.md` | Prerequisite audit evidence. | `Decision: PASS`. |
| `audits/nullforge/PF-T001/AUDIT_REPORT.md` | Prerequisite audit evidence. | `Decision: PASS`. |
| `audits/nullforge/PF-T002/AUDIT_REPORT.md` | Prerequisite audit evidence. | `Decision: PASS`. |
| `audits/nullforge/ADR-T001/AUDIT_REPORT.md` | Prerequisite audit evidence and ADR-T001 closeout state. | `Decision: PASS`. |
| `audits/nullforge/ADR-T002/AUDIT_REPORT.md` | Prerequisite audit evidence and ADR-T002 closeout state. | `Decision: PASS`. |
| `audits/nullforge/CX-T001/AUDIT_REPORT.md` | Prerequisite audit evidence and CX-T001 closeout state. | `Decision: PASS`. |
| `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` | Working name, platform, stack direction, and engine boundary constraints. | Accepted planning decision; not implementation proof. |
| `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` | Local-first/no-cloud MVP boundary and exclusions. | Accepted planning decision; not technical enforcement proof. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | M0 package plan, MB-T001 ticket row, milestone handoff template, and downstream sequence. | Planning source; downstream tickets still require scoped role-loop execution. |

## Included Source Slices

Volume 07 slices used:

- M0 first milestone package plan: M0 goal, tickets, non-goals, and acceptance.
- First 38-ticket backlog: `MB-T001` as ticket 7, `QA-T001` as first M1 downstream ticket.
- Context Curator prompt pattern.
- Milestone handoff template.
- M0 survival conditions before implementation tickets.

`CODEX_ROLE_LOOP.md` slices used:

- Context Curator role.
- Planner, Implementor, Auditor, and Repair Implementor role boundaries.
- Artifact tree and required sections.
- PASS/HOLD/REJECT rules.
- Human gates and stop conditions.
- Docs-only ticket rules.
- Source truth, archive, quarantine, and prompt-handling rules.
- Next action after CX-T001: `MB-T001`.

## Excluded Sources

| Source or area | Reason excluded |
|---|---|
| `tickets/nullforge/` | Pending downstream; not created or imported in this curator ticket. |
| `milestones/nullforge/` | Pending downstream; not created or imported in this curator ticket. |
| `prompts/` | Prompt files are not active truth unless promoted by scoped audited work. |
| `docs/nullforge/qa/` | QA docs are downstream and not part of MB-T001 context curation. |
| `reports/nullforge/MB-T001/` | Reports are implementation-stage artifacts, not curator outputs. |
| `audits/nullforge/MB-T001/` | Audit artifacts are downstream of implementation, not curator outputs. |
| `plans/nullforge/MB-T001/PLAN.md` | Planning is explicitly forbidden in this curator task. |
| `plans/nullforge/MB-T001/ACCEPTANCE.md` | Planning output is explicitly forbidden in this curator task. |
| `plans/nullforge/MB-T001/IMPLEMENTOR_PROMPT.md` | Planning output is explicitly forbidden in this curator task. |
| ResearchCore Engine docs/code | Existing engine truth; not needed for MB-T001 context curation and not to be modified. |
| `src/`, `tests/`, `schemas/`, `fixtures/`, package files, CI, generated docs | Implementation and verification infrastructure are out of scope for this docs-only curator task. |
| Raw/private data, ES.zip contents, ES-derived fixtures | Quarantined/gated material not needed for M0 handoff context curation. |
| M1, `QA-T001`, `ADR-T003`, downstream tickets | Mentioned only as downstream context; not started. |

## Current Repo State Recorded

- Branch: `main`.
- Upstream: `origin/main`.
- Starting worktree status: clean.
- Active phase: `REPO_SOURCE_IMPORT_BASELINE`.
- Next scoped ticket in status/source index: `MB-T001`.
- No NullForge implementation code has started.

## Checks To Run For This Curator Pass

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath plans\nullforge\MB-T001\CONTEXT_BUNDLE.md`
- `Test-Path -LiteralPath plans\nullforge\MB-T001\CONTEXT_BUNDLE_MANIFEST.md`
- `rg -n "Decision: PASS" audits\nullforge\PF-T000\AUDIT_REPORT.md audits\nullforge\PF-T001\AUDIT_REPORT.md audits\nullforge\PF-T002\AUDIT_REPORT.md audits\nullforge\ADR-T001\AUDIT_REPORT.md audits\nullforge\ADR-T002\AUDIT_REPORT.md audits\nullforge\CX-T001\AUDIT_REPORT.md`
- `rg -n "MB-T001|M0|QA-T001|CX-T001|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md docs\nullforge\codex\CODEX_ROLE_LOOP.md`

## Manifest Verdict

Ready for planner: YES.

The included context is sufficient for a bounded MB-T001 planner pass. The excluded context remains out of scope unless a later human prompt explicitly authorizes it.

# PF-T000 Import Plan

Ticket: PF-T000 - Repo inventory and NullForge import plan
Milestone: M0 - Repo Source Import + Canonical Baseline

## Recommendation

Preserve the M0 target layout. The inventory found no existing repo path collision for the NullForge-specific roots. Keeping NullForge material under separated `docs/nullforge/`, `tickets/nullforge/`, `prompts/nullforge/`, `milestones/nullforge/`, `plans/nullforge/`, `reports/nullforge/`, and `audits/nullforge/` paths reduces source-of-truth confusion with existing ResearchCore Engine docs.

PF-T000 should not edit root README, existing ResearchCore docs, package metadata, code, tests, schemas, tools, or CI.

## Proposed Target Folders

| Target folder | Owner ticket | Purpose | PF-T000 action |
|---|---|---|---|
| `docs/nullforge/` | PF-T002 | NullForge project docs root | Propose only. |
| `docs/nullforge/import/` | PF-T000+ | Import planning and import audit trail | Create PF-T000 docs here. |
| `docs/nullforge/blueprint/volumes/` | PF-T001 | Reviewed/imported NullForge Volume 0-7 material | Propose only. |
| `docs/nullforge/adr/` | ADR-T001, ADR-T002 | NullForge decisions and reversibility notes | Propose only. |
| `docs/nullforge/codex/` | CX-T001 | NullForge Codex role-loop docs | Propose only. |
| `milestones/nullforge/M0-repo-source-import/` | MB-T001 | M0 handoff and milestone closeout | Propose only. |
| `tickets/nullforge/` | PF-T001 or ticket-import step chosen by audit | Repo-governed ticket docs | Propose only. |
| `prompts/nullforge/` | CX-T001 or ticket-import step chosen by audit | Repo-governed role prompts | Propose only. |
| `plans/nullforge/<ticket-id>/` | Each ticket role loop | Context, plan, acceptance, implementor prompt | Existing PF-T000 plan path already in use. |
| `reports/nullforge/<ticket-id>/` | Each implementor pass | Implementation reports, changed files, test results, auditor prompt | Create PF-T000 reports here. |
| `audits/nullforge/<ticket-id>/` | Each auditor pass | Audit report, findings, repair prompt | Propose only for auditor. |

## Expected Future Source-Of-Truth Files

| File | Owner ticket | Purpose |
|---|---|---|
| `docs/nullforge/README.md` | PF-T002 | NullForge docs entry point after imported source exists. |
| `docs/nullforge/CURRENT_STATUS.md` | PF-T002 | NullForge current state, separate from `docs/STATUS.md`. |
| `docs/nullforge/SOURCE_INDEX.md` | PF-T002 | Index of active NullForge source docs and truth status. |
| `docs/nullforge/DECISION_LEDGER.md` | PF-T002 | Lightweight decision/history ledger until ADRs cover major decisions. |
| `docs/nullforge/blueprint/volumes/volume-00.md` through `volume-07.md` or equivalent reviewed names | PF-T001 | Imported reviewed volume content or references. Exact filenames should be chosen by PF-T001 after source review. |
| `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` | ADR-T001 | Name/platform/stack/engine boundary decision. |
| `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` | ADR-T002 | Local-first/no-cloud MVP decision. |
| `docs/nullforge/codex/` role-loop docs | CX-T001 | Context Curator, Planner, Implementor, Auditor, QA, and human-gate guidance. |
| `milestones/nullforge/M0-repo-source-import/MILESTONE_HANDOFF.md` | MB-T001 | M0 closeout after all prior tickets pass or are explicitly deferred. |

PF-T000 does not create any of these future files except its own `docs/nullforge/import/PF-T000_*` files.

## Ticket Sequence And Ownership

M0 remains serial:

```text
PF-T000 -> PF-T001 -> PF-T002 -> ADR-T001 -> ADR-T002 -> CX-T001 -> MB-T001
```

The dependency rationale is:

- PF-T001 needs PF-T000 paths and conflict findings before importing volumes.
- PF-T002 needs actual imported volume paths before creating current status and source index.
- ADR-T001 needs the active source index/current status.
- ADR-T002 should reference the name/platform/stack/engine boundary from ADR-T001.
- CX-T001 should reflect the local-first and human-gate posture from ADR-T002.
- MB-T001 should summarize all imported source and role-loop artifacts.

## Import Plan By Ticket

### PF-T001 - Import NullForge volumes into repo docs

- Use the PF-T000 target layout unless a new conflict appears.
- Review NullForge Volume 0-7 package material before import.
- Import reviewed material under `docs/nullforge/blueprint/volumes/`.
- Preserve truth status: imported and audited docs become repo-governed; unimported package material remains draft/design memory.
- Do not import full `ES.zip`, raw data, or unsafe fixtures.
- Stop at any license/safety/data gate before committing ES-derived samples.

### PF-T002 - Create NullForge current status and source index

- Create `docs/nullforge/README.md`.
- Create `docs/nullforge/CURRENT_STATUS.md`.
- Create `docs/nullforge/SOURCE_INDEX.md`.
- Create `docs/nullforge/DECISION_LEDGER.md`.
- Link to actual imported PF-T001 paths.
- Keep NullForge status separate from `docs/STATUS.md`.

### ADR-T001 - Name/platform/stack/engine ADR

- Create the ADR under `docs/nullforge/adr/`.
- Record the NullForge name/platform/stack/engine relationship without renaming `research-core` or ResearchCore Engine.
- Any repo/package/CLI/public identity change requires human approval.

### ADR-T002 - Local-first/no-cloud MVP ADR

- Create the ADR under `docs/nullforge/adr/`.
- State local-first/no-cloud MVP posture and explicit exclusions.
- Avoid auth, billing, cloud sync, broker/live trading, marketplace, or mobile scope.

### CX-T001 - NullForge Codex role-loop docs

- Create role-loop docs under `docs/nullforge/codex/`.
- Preserve the rule that no role grades its own work.
- Use context refresh, planner, implementor, auditor, repair, and human-gate rules from imported source.

### MB-T001 - M0 milestone handoff

- Create `milestones/nullforge/M0-repo-source-import/MILESTONE_HANDOFF.md`.
- Summarize ticket dispositions, imported docs, unresolved gates, and readiness for M1 generation decision.
- Return to ChatGPT/user for M0 audit and M1 decision.

## Root README And Docs Navigation

PF-T000 should not change root README or docs navigation.

A later minimal link from `README.md` or `docs/index.md` to `docs/nullforge/` may be useful after PF-T001/PF-T002, but this should be explicitly scoped and reviewed because root/front-door changes can blur ResearchCore Engine truth and NullForge product truth.

## Data And Fixture Policy For Later Tickets

- Full `ES.zip` must not enter the repo.
- Raw/private/local data must not enter the repo.
- ES-derived fixtures require a later explicit license/safety decision before commit.
- Existing ES5m generated pipeline artifacts are documented as local/ignored under `configs/analysis/local/`.
- Dataset capability claims should be grounded in imported docs and, later, dataset catalog or fixture policy docs.

## Verification Plan For PF-T000

PF-T000 verification is docs/path scope only:

- `git status --short --branch`
- `Test-Path -LiteralPath` checks for required PF-T000 outputs.
- `Test-Path -LiteralPath` checks for proposed future target roots.
- `git diff --name-only` plus untracked-file review.
- Manual review that changed files are limited to PF-T000 docs/plans/reports.

No dependency installation, pytest run, docs build, generated docs regeneration, or CI run is required because PF-T000 does not modify executable code, docs navigation, generated reference files, schemas, package files, or CI.

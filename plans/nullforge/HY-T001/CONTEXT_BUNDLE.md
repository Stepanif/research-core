# HY-T001 Context Bundle

Ticket: `HY-T001`

Title: Local-path hygiene planning for NullForge documentation artifacts

Status: Ready for planner and implementor handoff. Planning only; no cleanup was performed in this ticket stage.

## Ticket Summary

`HY-T001` is a docs-only hygiene ticket to sanitize local absolute provenance paths in tracked NullForge documentation, planning, report, and audit artifacts where doing so is safe and does not change source meaning.

The cleanup target is documentation/provenance leakage only. The prior read-only contamination scan found no other-project code contamination. No ResearchCore Engine or NullForge implementation code should be changed.

## Source Context Used

- `docs/nullforge/CURRENT_STATUS.md`: Current NullForge status, M0 baseline, QA-T001 closeout, and no-code boundary.
- `docs/nullforge/SOURCE_INDEX.md`: Active source index and incoming package provenance entries.
- `docs/nullforge/ARCHIVE_POLICY.md`: Archive, quarantine, prompt, and source-of-truth policy.
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`: Role loop, artifact boundaries, audit rules, human gates, and docs-only ticket rules.
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`: QA-T001 command discovery and recorded local editable install path.
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`: QA-T001 audit `PASS` and note that local path hygiene is non-blocking for QA-T001.
- `reports/nullforge/QA-T001/TEST_RESULTS.md`: QA-T001 bounded check output with local temp editable install path.

## Current Repo State

Pre-planning checks showed:

- `git status --short --branch`: `## main...origin/main`
- `git status --short --untracked-files=all`: no output before `HY-T001` planner files
- `git diff --name-only`: no output before `HY-T001` planner files
- `git diff --check`: no output before `HY-T001` planner files

## M1 Readiness Context

- M0 is complete through `MB-T001`.
- `QA-T001` is complete, pushed, and audit `PASS`.
- `No NullForge implementation code has started.`
- `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, and downstream work remain out of scope for this ticket.

## Exact Path Patterns To Sanitize

These are represented as escaped path patterns so this planning artifact does not add new plain absolute path instances.

- Incoming package root: `C:\\Users\\Filip\\Desktop\\NullForge_Incoming\\`
- Repo root path: `C:\\Users\\Filip\\Desktop\\Repos\\research-core`
- Temp editable install root: `C:\\Users\\Filip\\AppData\\Local\\Temp\\research-core-gha-clone`
- Supporting discovery tokens: `NullForge_Incoming`, `research-core-gha-clone`, `AppData\\Local\\Temp`

## Candidate File Set Discovered

The bounded discovery search was:

```powershell
rg -n "C:\\Users\\Filip|NullForge_Incoming|research-core-gha-clone|AppData\\Local\\Temp" docs\nullforge plans\nullforge reports\nullforge audits\nullforge
```

Pre-`HY-T001` candidate files:

- `audits/nullforge/ADR-T001/AUDIT_REPORT.md`
- `audits/nullforge/PF-T002/AUDIT_REPORT.md`
- `audits/nullforge/QA-T001/REPAIR_PROMPT.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md`
- `docs/nullforge/import/PF-T000_REPO_INVENTORY.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `plans/nullforge/ADR-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/ADR-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/ADR-T001/IMPLEMENTOR_PROMPT.md`
- `plans/nullforge/ADR-T001/PLAN.md`
- `plans/nullforge/MB-T001/IMPLEMENTOR_PROMPT.md`
- `plans/nullforge/PF-T000/CONTEXT_BUNDLE.md`
- `plans/nullforge/PF-T000/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/PF-T000/IMPLEMENTOR_PROMPT.md`
- `plans/nullforge/PF-T000/PLAN.md`
- `plans/nullforge/PF-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/PF-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/PF-T001/IMPLEMENTOR_PROMPT.md`
- `plans/nullforge/PF-T001/PLAN.md`
- `plans/nullforge/PF-T002/CONTEXT_BUNDLE.md`
- `plans/nullforge/PF-T002/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/PF-T002/IMPLEMENTOR_PROMPT.md`
- `plans/nullforge/PF-T002/PLAN.md`
- `plans/nullforge/QA-T001/IMPLEMENTOR_PROMPT.md`
- `reports/nullforge/ADR-T001/AUDITOR_PROMPT.md`
- `reports/nullforge/ADR-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/ADR-T001/TEST_RESULTS.md`
- `reports/nullforge/MB-T001/AUDITOR_PROMPT.md`
- `reports/nullforge/PF-T000/AUDITOR_PROMPT.md`
- `reports/nullforge/PF-T000/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/PF-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/PF-T002/AUDITOR_PROMPT.md`
- `reports/nullforge/PF-T002/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T001/AUDITOR_PROMPT.md`
- `reports/nullforge/QA-T001/TEST_RESULTS.md`

The post-planning search is expected to also match `plans/nullforge/HY-T001/*` because these planner artifacts intentionally document the search tokens and replacement policy.

## Proposed Replacement Policy

- Replace repo-root absolute path occurrences with `<repo-root>` when the absolute root itself matters.
- Prefer repo-relative paths when the referenced file is clearly inside this repository and the relative path preserves more meaning than `<repo-root>`.
- Replace the incoming package root with `<nullforge-incoming-root>`.
- Replace the temp editable install root with `<local-temp-editable-install>`.
- Preserve file basenames, ticket IDs, volume names, hash strings, command names, package names, and repo-relative paths when useful.
- Preserve whether a path was local, incoming, repo-local, or temp-derived.
- Do not rewrite command outputs in a way that implies a command succeeded, failed, or produced different evidence.
- Do not remove provenance entries; sanitize only owner- and machine-specific prefixes.

## Files And Folders Likely Relevant To Later Implementation

- Candidate files listed above.
- `docs/nullforge/CURRENT_STATUS.md`, only if the implementation closeout prompt allows a status update for `HY-T001`.
- `docs/nullforge/SOURCE_INDEX.md`, already a candidate and likely needed to document `HY-T001` artifacts.
- `reports/nullforge/HY-T001/`, if the later implementor prompt creates standard implementation reports.

## Files And Folders Explicitly Excluded

- `src/`
- `tests/`
- `schemas/`
- `fixtures/`
- `.github/`
- package and dependency files
- generated docs
- raw data and private data
- ResearchCore Engine docs outside the explicitly discovered NullForge candidate set
- tickets, milestones, prompts, app files, and downstream implementation artifacts

## Known Gates And Stop Conditions

Stop and ask for human approval if:

- Cleanup would require changing code, tests, schemas, fixtures, package files, CI, generated docs, raw data, or private data.
- A path appears to be part of an immutable source quote, imported volume content, hash input, or external evidence where sanitization could change meaning.
- A candidate appears outside `docs/nullforge`, `plans/nullforge`, `reports/nullforge`, or `audits/nullforge`.
- Cleanup would require changing decisions, audit dispositions, ticket status, command outcomes, or source authority.
- New local absolute paths are found outside the discovered candidate set.

## Required Checks For Later Stages

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- Before and after local-path search for the target patterns.
- Verify no changes under `src`, `tests`, `schemas`, `fixtures`, package files, `.github`, generated docs, raw data, or private data.
- Verify `No NullForge implementation code has started.` remains unchanged.
- Verify `SOURCE_INDEX.md` links remain repo-local and resolvable if it is edited.

## Open Questions

- Should the later implementor sanitize `HY-T001` planner artifacts themselves, or should those remain as intentional policy references to the path patterns?
- Should `docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md` be sanitized if it is considered source-import metadata rather than imported source content?

## Ready-For-Planner Verdict

Ready for planner and implementor handoff, with the human gate that cleanup must preserve source meaning and avoid implementation work.

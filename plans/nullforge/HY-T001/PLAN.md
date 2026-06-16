# HY-T001 Plan

Ticket: `HY-T001`

Title: Local-path hygiene cleanup for NullForge docs artifacts

Verdict: Ready for implementor handoff after human acceptance of the replacement policy.

## Goal

Sanitize local absolute path leakage in tracked NullForge docs, plans, reports, and audits where safe, while preserving source meaning, ticket evidence, command outcomes, artifact names, and repo-relative references.

## Non-Goals

- Do not change code, tests, schemas, fixtures, package files, CI, generated docs, raw data, or private data.
- Do not change audit decisions, report findings, command outcomes, ticket status, or accepted decisions.
- Do not rewrite git history.
- Do not import or promote archived, quarantined, prompt, raw, private, or downstream artifacts.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, or downstream work.

## Source Context Used

- `CURRENT_STATUS.md` confirms QA-T001 is complete, `REPO_SOURCE_IMPORT_BASELINE` remains the M0 baseline, and `No NullForge implementation code has started.`
- `SOURCE_INDEX.md` contains incoming package provenance paths and source-index rows.
- `ARCHIVE_POLICY.md` defines archive/quarantine/prompt source authority limits.
- `CODEX_ROLE_LOOP.md` defines role and artifact boundaries.
- `COMMAND_DISCOVERY.md` and QA-T001 reports contain local temp editable install evidence.
- QA-T001 audit report records `Decision: PASS`.

## Assumptions

- Local absolute path occurrences are documentation/provenance leakage only.
- The later implementor may edit only the explicitly allowed target files and reports named by its prompt.
- Sanitization should be textual and meaning-preserving, not semantic rewriting.
- Existing ticket IDs, file basenames, hashes, and repo-relative paths remain useful evidence and should be preserved.

## Exact Path Patterns

Represented as escaped patterns:

- `C:\\Users\\Filip\\Desktop\\NullForge_Incoming\\`
- `C:\\Users\\Filip\\Desktop\\Repos\\research-core`
- `C:\\Users\\Filip\\AppData\\Local\\Temp\\research-core-gha-clone`
- `NullForge_Incoming`
- `research-core-gha-clone`
- `AppData\\Local\\Temp`

## Candidate File Set

Use the pre-planning candidate list from `CONTEXT_BUNDLE.md` and `CONTEXT_BUNDLE_MANIFEST.md` as the initial cleanup target set. The later implementor should re-run the bounded search before editing and update the final target set only if new hits are still inside the allowed NullForge docs/plans/reports/audits scope.

## Implementation Scope For Later Implementor

The later implementor should:

- Re-run the bounded local-path search.
- Review each candidate file before editing.
- Replace local owner/machine-specific path prefixes with approved placeholders or repo-relative paths.
- Preserve command evidence, ticket IDs, basenames, hashes, and repo-relative paths.
- Create standard implementation reports if the later prompt allows them.
- Update `SOURCE_INDEX.md` only if needed and allowed.
- Update `CURRENT_STATUS.md` only if needed and allowed.

## Proposed Replacement Policy

- Repo root path to repo root concept: use `<repo-root>`.
- Repo root path to a specific file inside this repo: prefer the repo-relative path.
- Incoming package root: use `<nullforge-incoming-root>`.
- Temp editable install root: use `<local-temp-editable-install>`.
- Keep file basenames, ticket IDs, volume titles, package names, command names, hashes, and repo-relative paths.
- Keep enough context to distinguish local machine provenance from source artifact provenance.

## Files Explicitly Out Of Scope

- `src/`
- `tests/`
- `schemas/`
- `fixtures/`
- `.github/`
- `README.md`
- `docs/reference/`
- `tools/`
- package/dependency files
- generated docs
- raw data and private data
- downstream ticket, milestone, prompt, app, desktop, bridge, sidecar, and implementation paths

## Proposed Allowed Files For Later Implementor

Potential cleanup targets:

- All pre-planning candidate files listed in `CONTEXT_BUNDLE.md`.
- `docs/nullforge/CURRENT_STATUS.md`, only if a later prompt explicitly permits status update.
- `docs/nullforge/SOURCE_INDEX.md`, already a candidate and only if link/source-index updates are needed.

Potential implementation report outputs:

- `reports/nullforge/HY-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/HY-T001/CHANGED_FILES.md`
- `reports/nullforge/HY-T001/TEST_RESULTS.md`
- `reports/nullforge/HY-T001/AUDITOR_PROMPT.md`

Do not create `audits/nullforge/HY-T001/` during implementation.

## Acceptance Criteria

- Local absolute owner/machine-specific paths are sanitized in the approved target set.
- No source meaning is changed.
- `No NullForge implementation code has started.` remains unchanged.
- No forbidden files or folders are created or modified.
- Any remaining matches are documented as intentional policy references, immutable source context, or human-gated exceptions.
- Bounded checks pass.
- HY-T001 is ready for independent audit.

## Required Checks

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `rg -n "C:\\Users\\Filip|NullForge_Incoming|research-core-gha-clone|AppData\\Local\\Temp" docs\nullforge plans\nullforge reports\nullforge audits\nullforge`
- `rg -n "No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools`
- `Test-Path -LiteralPath tickets`
- `Test-Path -LiteralPath milestones`
- `Test-Path -LiteralPath prompts`
- `Test-Path -LiteralPath audits\nullforge\HY-T001`

## Human Gates And Stop Conditions

Stop if:

- Sanitization would alter command results, audit decisions, source authority, accepted decisions, or ticket status.
- A candidate path appears in immutable imported source content where rewriting could invalidate provenance.
- Cleanup requires any ResearchCore Engine code/doc changes outside the explicitly scoped NullForge target set.
- A needed change falls outside the later implementor prompt's allowed files.
- There is uncertainty about whether a path is safe to sanitize without changing meaning.

## Rollback And Repair Route

- If a cleanup edit is too broad, revert only the HY-T001 cleanup edits in the affected file and preserve unrelated user changes.
- If audit returns `HOLD`, create a bounded repair prompt under `audits/nullforge/HY-T001/REPAIR_PROMPT.md`.
- If audit returns `REJECT`, stop and ask for human direction before any further cleanup.

## Ready-For-Implementor Verdict

Ready for implementor handoff, provided the implementor prompt keeps cleanup docs-only and bounded to the allowed target files.

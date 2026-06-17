# QA-T005 Repair Prompt

Ticket: `QA-T005`

Audit decision: `PASS`

Repair required: No

No NullForge implementation code has started.

## Use Condition

Do not use this repair prompt for the current QA-T005 audit result. The audit passed and no repair is required.

Use this only if a later human review finds drift from the QA-T005 audit result and explicitly asks for a bounded QA-T005 repair.

## Bounded Repair Scope If Later Authorized

Allowed repair files would be limited to QA-T005 audit-approved documentation surfaces:

- `docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T005/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T005/CHANGED_FILES.md`
- `reports/nullforge/QA-T005/TEST_RESULTS.md`
- `reports/nullforge/QA-T005/AUDITOR_PROMPT.md`
- `audits/nullforge/QA-T005/AUDIT_REPORT.md`
- `audits/nullforge/QA-T005/FINDINGS.md`
- `audits/nullforge/QA-T005/REPAIR_PROMPT.md`

Do not modify planner artifacts unless a later human prompt explicitly scopes planner repair.

## Forbidden During Any Later Repair

- Do not run install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, environment repair, full tests, docs generation, docs build, quickstart, CI smoke, `python -m research_core --help`, or `research-core --help`.
- Do not modify `src/`, `tests/`, `schemas/`, `fixtures/`, `pyproject.toml`, `requirements-docs.txt`, package files, `.github/`, `README.md`, `docs/reference/`, `tools/`, generated docs, raw data, private data, or ResearchCore Engine code/docs.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, public distribution, or downstream work.
- Do not stage or commit `.venv-qa-t005/`, `.pytest_cache/`, or `__pycache__/`.

## Required Checks For Later Repair

- `git status --short --branch`
- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `rg -n "Decision: PASS" audits\nullforge\QA-T005\AUDIT_REPORT.md`
- `rg -n "QA-T005|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md docs\nullforge\qa\ENVIRONMENT_REPAIR_EXECUTION.md`
- `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools`

## Repair Verdict

No repair required for QA-T005 audit `PASS`.

# QA-T005 Auditor Prompt

You are Codex working in `<repo-root>`.

Task: independently audit `QA-T005` only.

Context:

- QA-T005 implementation is complete but uncommitted.
- QA-T005 is the human-approved isolated project-local Python environment repair/readiness execution ticket.
- QA-T001, HY-T001, QA-T002, QA-T003, and QA-T004 audit decisions are `PASS`.
- QA-T005 used `.venv-qa-t005` as an approved local side effect and must not stage or commit it.
- No NullForge implementation code has started.
- Do not implement fixes.
- Do not commit.
- Do not push or merge.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, package changes, dependency changes outside `.venv-qa-t005`, tests, docs generation, docs build, quickstart commands, CI smoke commands, or downstream work.

Read first:

- `plans/nullforge/QA-T005/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T005/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/QA-T005/PLAN.md`
- `plans/nullforge/QA-T005/ACCEPTANCE.md`
- `plans/nullforge/QA-T005/IMPLEMENTOR_PROMPT.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `audits/nullforge/HY-T001/AUDIT_REPORT.md`
- `audits/nullforge/QA-T002/AUDIT_REPORT.md`
- `audits/nullforge/QA-T003/AUDIT_REPORT.md`
- `audits/nullforge/QA-T004/AUDIT_REPORT.md`
- `reports/nullforge/QA-T005/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T005/CHANGED_FILES.md`
- `reports/nullforge/QA-T005/TEST_RESULTS.md`
- `reports/nullforge/QA-T005/AUDITOR_PROMPT.md`
- `pyproject.toml`
- `docs/how-to/run_ci_locally.md`
- `docs/reference/cli/overview.md`
- `src/research_core/cli.py`

Allowed outputs:

- `audits/nullforge/QA-T005/AUDIT_REPORT.md`
- `audits/nullforge/QA-T005/FINDINGS.md`
- `audits/nullforge/QA-T005/REPAIR_PROMPT.md`

Forbidden:

- Do not modify QA-T005 implementation files.
- Do not modify plans or reports.
- Do not create tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts.
- Do not modify ResearchCore Engine docs/code.
- Do not run install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, environment repair, full test, docs generation, docs build, quickstart, CI smoke, `python -m research_core --help`, or `research-core --help`.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

Audit checks:

1. Verify changed files are bounded to QA-T005 planner artifacts, allowed NullForge status/source-index/QA execution docs, QA-T005 reports, and this audit folder.
2. Confirm QA-T001, HY-T001, QA-T002, QA-T003, and QA-T004 audit reports contain `Decision: PASS`.
3. Confirm `docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md` exists and includes:
   - ticket ID `QA-T005`;
   - purpose and non-goals;
   - explicit human approval evidence;
   - QA-T001, HY-T001, QA-T002, QA-T003, and QA-T004 audit `PASS` evidence;
   - inherited QA-T002/QA-T004 blocker summary including `<local-temp-editable-install>`, `python -m research_core.cli`, and `No module named research_core.cli`;
   - package/CLI facts from `pyproject.toml`, `docs/reference/cli/overview.md`, `docs/how-to/run_ci_locally.md`, and `src/research_core/cli.py`;
   - approved command results for `.venv-qa-t005`;
   - clear distinction between project-local venv readiness and active/global environment state;
   - side-effect review for `.venv-qa-t005/`, `__pycache__/`, `.pytest_cache/`, `exec_outputs/`, generated docs, source, package, tests, schemas, fixtures, and CI;
   - exact sentence `No NullForge implementation code has started.`
4. Confirm `CURRENT_STATUS.md` names active ticket `QA-T005`, keeps `REPO_SOURCE_IMPORT_BASELINE`, and preserves the no-code sentence.
5. Confirm `SOURCE_INDEX.md` links only to repo-local files that exist, including QA-T005 planner artifacts, `ENVIRONMENT_REPAIR_EXECUTION.md`, and QA-T005 report artifacts.
6. Confirm `.venv-qa-t005/` is not staged and no forbidden tracked files were modified.
7. Run:
   - `git status --short --branch`
   - `git status --short --untracked-files=all`
   - `git diff --name-only`
   - `git diff --check`
   - `Test-Path -LiteralPath docs\nullforge\qa\ENVIRONMENT_REPAIR_EXECUTION.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T005\IMPLEMENTATION_REPORT.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T005\CHANGED_FILES.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T005\TEST_RESULTS.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T005\AUDITOR_PROMPT.md`
   - `rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md audits\nullforge\QA-T002\AUDIT_REPORT.md audits\nullforge\QA-T003\AUDIT_REPORT.md audits\nullforge\QA-T004\AUDIT_REPORT.md`
   - `rg -n "QA-T005|QA-T004|python -m research_core.cli|No module named research_core.cli|local-temp-editable-install|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\qa\ENVIRONMENT_REPAIR_EXECUTION.md docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md reports\nullforge\QA-T005\IMPLEMENTATION_REPORT.md reports\nullforge\QA-T005\TEST_RESULTS.md`
   - `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools`
   - `Test-Path -LiteralPath tickets`
   - `Test-Path -LiteralPath milestones`
   - `Test-Path -LiteralPath prompts`
   - `Test-Path -LiteralPath audits\nullforge\QA-T005`

Return exactly one verdict:

- `PASS`
- `HOLD`
- `REJECT`

Then create the three audit files and report:

- verdict
- blocking findings
- non-blocking findings
- human decision needed
- repair prompt path

Do not commit.

# QA-T003 Auditor Prompt

You are Codex working in `<repo-root>`.

Task: independently audit `QA-T003` only.

Context:

- QA-T003 implementation is complete but uncommitted.
- QA-T003 is docs-only local Python environment repair decisioning.
- QA-T001, HY-T001, and QA-T002 audit decisions are `PASS`.
- No NullForge implementation code has started.
- Do not implement fixes.
- Do not commit.
- Do not push or merge.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, package changes, dependency changes, install commands, environment repair, tests, docs generation, docs build, quickstart commands, CI smoke commands, or downstream work.

Read first:

- `plans/nullforge/QA-T003/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T003/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/QA-T003/PLAN.md`
- `plans/nullforge/QA-T003/ACCEPTANCE.md`
- `plans/nullforge/QA-T003/IMPLEMENTOR_PROMPT.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `audits/nullforge/HY-T001/AUDIT_REPORT.md`
- `audits/nullforge/QA-T002/AUDIT_REPORT.md`
- `reports/nullforge/QA-T002/TEST_RESULTS.md`
- `reports/nullforge/QA-T003/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T003/CHANGED_FILES.md`
- `reports/nullforge/QA-T003/TEST_RESULTS.md`
- `reports/nullforge/QA-T003/AUDITOR_PROMPT.md`
- `pyproject.toml`
- `docs/how-to/run_ci_locally.md`
- `docs/reference/cli/overview.md`
- `src/research_core/cli.py`

Allowed outputs:

- `audits/nullforge/QA-T003/AUDIT_REPORT.md`
- `audits/nullforge/QA-T003/FINDINGS.md`
- `audits/nullforge/QA-T003/REPAIR_PROMPT.md`

Forbidden:

- Do not modify QA-T003 implementation files.
- Do not modify plans or reports.
- Do not create tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts.
- Do not modify ResearchCore Engine docs or code.
- Do not run install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, environment repair, full test, docs generation, docs build, quickstart, or CI smoke commands.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

Audit checks:

1. Verify changed files are bounded to QA-T003 planner artifacts, allowed NullForge status/source-index/QA decision docs, QA-T003 reports, and this audit folder.
2. Confirm QA-T001, HY-T001, and QA-T002 audit reports contain `Decision: PASS`.
3. Confirm `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md` exists and includes:
   - ticket ID `QA-T003`;
   - purpose and non-goals;
   - QA-T001, HY-T001, and QA-T002 audit `PASS` evidence;
   - QA-T002 blocker summary;
   - relevant package/CLI facts;
   - distinction between source facts, local environment observations, expected unsupported command shapes, unresolved blockers, and candidate repair/readiness paths;
   - statement that no install, repair, test, docs build/generation, quickstart, or CI smoke commands were run;
   - candidate repair/readiness paths with tradeoffs and required human gates;
   - recommended human decision options;
   - side-effect and rollback considerations;
   - local-path sanitization policy;
   - exact sentence `No NullForge implementation code has started.`
4. Confirm `CURRENT_STATUS.md` names active ticket `QA-T003`, keeps `REPO_SOURCE_IMPORT_BASELINE`, and preserves the no-code sentence.
5. Confirm `SOURCE_INDEX.md` links only to repo-local files that exist, including QA-T003 planner artifacts, `ENVIRONMENT_REPAIR_DECISION.md`, and QA-T003 report artifacts.
6. Confirm no forbidden files or folders were created or modified.
7. Run:
   - `git status --short --branch`
   - `git status --short --untracked-files=all`
   - `git diff --name-only`
   - `git diff --check`
   - `Test-Path -LiteralPath docs\nullforge\qa\ENVIRONMENT_REPAIR_DECISION.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T003\IMPLEMENTATION_REPORT.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T003\CHANGED_FILES.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T003\TEST_RESULTS.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T003\AUDITOR_PROMPT.md`
   - `rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md audits\nullforge\QA-T002\AUDIT_REPORT.md`
   - `rg -n "QA-T003|QA-T002|python -m research_core.cli|No module named research_core.cli|local-temp-editable-install|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\qa\ENVIRONMENT_REPAIR_DECISION.md docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md reports\nullforge\QA-T003\IMPLEMENTATION_REPORT.md reports\nullforge\QA-T003\TEST_RESULTS.md`
   - `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools`
   - `Test-Path -LiteralPath tickets`
   - `Test-Path -LiteralPath milestones`
   - `Test-Path -LiteralPath prompts`
   - `Test-Path -LiteralPath audits\nullforge\QA-T003`

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

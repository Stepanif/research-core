# QA-T002 Auditor Prompt

You are Codex working in `<repo-root>`.

Task: independently audit `QA-T002` only.

Context:

- QA-T002 implementation is complete but uncommitted.
- QA-T002 is docs-only local Python environment and CLI/runtime blocker triage.
- QA-T001 and HY-T001 audit decisions are `PASS`.
- No NullForge implementation code has started.
- Do not implement fixes.
- Do not commit.
- Do not push or merge.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, package changes, dependency changes, install commands, tests, docs generation, docs build, quickstart commands, CI smoke commands, or downstream work.

Read first:

- `plans/nullforge/QA-T002/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T002/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/QA-T002/PLAN.md`
- `plans/nullforge/QA-T002/ACCEPTANCE.md`
- `plans/nullforge/QA-T002/IMPLEMENTOR_PROMPT.md`
- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `reports/nullforge/QA-T001/TEST_RESULTS.md`
- `audits/nullforge/HY-T001/AUDIT_REPORT.md`
- `reports/nullforge/HY-T001/TEST_RESULTS.md`
- `reports/nullforge/QA-T002/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T002/CHANGED_FILES.md`
- `reports/nullforge/QA-T002/TEST_RESULTS.md`
- `reports/nullforge/QA-T002/AUDITOR_PROMPT.md`
- `pyproject.toml`
- `docs/how-to/run_ci_locally.md`
- `docs/reference/cli/overview.md`
- `src/research_core/cli.py`

Allowed outputs:

- `audits/nullforge/QA-T002/AUDIT_REPORT.md`
- `audits/nullforge/QA-T002/FINDINGS.md`
- `audits/nullforge/QA-T002/REPAIR_PROMPT.md`

Forbidden:

- Do not modify QA-T002 implementation files.
- Do not modify plans or reports.
- Do not create tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts.
- Do not modify ResearchCore Engine docs/code.
- Do not run install, uninstall, editable install, dependency sync, package build, environment repair, full test, docs generation, docs build, quickstart, or CI smoke commands.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

Audit checks:

1. Verify changed files are bounded to QA-T002 planner artifacts, allowed NullForge status/source-index/QA triage docs, QA-T002 reports, and this audit folder.
2. Confirm QA-T001 and HY-T001 audit reports contain `Decision: PASS`.
3. Confirm `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md` exists and includes:
   - ticket ID `QA-T002`;
   - purpose and non-goals;
   - inherited QA-T001 blocker summary;
   - package/source facts from `pyproject.toml` and `src/research_core/cli.py`;
   - current observed package/module/CLI visibility;
   - distinction between source facts, environment observations, expected unsupported commands, and unresolved blockers;
   - side-effect review;
   - human gates and recommended next decision;
   - exact sentence `No NullForge implementation code has started.`
4. Confirm `CURRENT_STATUS.md` names active ticket `QA-T002`, keeps `REPO_SOURCE_IMPORT_BASELINE`, and preserves the no-code sentence.
5. Confirm `SOURCE_INDEX.md` links only to repo-local files that exist, including QA-T002 planner artifacts, `ENVIRONMENT_TRIAGE.md`, and QA-T002 report artifacts.
6. Confirm no forbidden files or folders were created or modified.
7. Run:
   - `git status --short --branch`
   - `git status --short --untracked-files=all`
   - `git diff --name-only`
   - `git diff --check`
   - `Test-Path -LiteralPath docs\nullforge\qa\ENVIRONMENT_TRIAGE.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T002\IMPLEMENTATION_REPORT.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T002\CHANGED_FILES.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T002\TEST_RESULTS.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T002\AUDITOR_PROMPT.md`
   - `rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md`
   - `rg -n "QA-T002|environment|CLI|python -m research_core.cli|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\qa\ENVIRONMENT_TRIAGE.md docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md reports\nullforge\QA-T002\IMPLEMENTATION_REPORT.md reports\nullforge\QA-T002\TEST_RESULTS.md`
   - `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools`
   - `Test-Path -LiteralPath tickets`
   - `Test-Path -LiteralPath milestones`
   - `Test-Path -LiteralPath prompts`
   - `Test-Path -LiteralPath audits\nullforge\QA-T002`

Return exactly one verdict:

- `PASS`
- `HOLD`
- `REJECT`

Then create the three audit files and report:

- verdict,
- blocking findings,
- non-blocking findings,
- human decision needed,
- repair prompt path.

Do not commit.

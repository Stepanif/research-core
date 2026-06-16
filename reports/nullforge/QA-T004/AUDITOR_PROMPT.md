# QA-T004 Auditor Prompt

You are Codex working in `C:\Users\Filip\Desktop\Repos\research-core`.

Task: independently audit `QA-T004` only.

Context:
- QA-T004 implementation is complete but uncommitted.
- QA-T004 is docs-only local Python environment repair/readiness path preparation.
- QA-T001, HY-T001, QA-T002, and QA-T003 audit decisions are `PASS`.
- No NullForge implementation code has started.
- Do not implement fixes.
- Do not commit.
- Do not push or merge.
- Do not start ADR-T003, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, package changes, dependency changes, install commands, tests, docs generation, docs build, quickstart commands, CI smoke commands, environment repair, or downstream work.

Read first:
- `plans/nullforge/QA-T004/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T004/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/QA-T004/PLAN.md`
- `plans/nullforge/QA-T004/ACCEPTANCE.md`
- `plans/nullforge/QA-T004/IMPLEMENTOR_PROMPT.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `audits/nullforge/HY-T001/AUDIT_REPORT.md`
- `audits/nullforge/QA-T002/AUDIT_REPORT.md`
- `audits/nullforge/QA-T003/AUDIT_REPORT.md`
- `reports/nullforge/QA-T003/TEST_RESULTS.md`
- `reports/nullforge/QA-T004/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T004/CHANGED_FILES.md`
- `reports/nullforge/QA-T004/TEST_RESULTS.md`
- `reports/nullforge/QA-T004/AUDITOR_PROMPT.md`
- `pyproject.toml`
- `docs/how-to/run_ci_locally.md`
- `docs/reference/cli/overview.md`
- `src/research_core/cli.py`

Allowed outputs:
- `audits/nullforge/QA-T004/AUDIT_REPORT.md`
- `audits/nullforge/QA-T004/FINDINGS.md`
- `audits/nullforge/QA-T004/REPAIR_PROMPT.md`

Forbidden:
- Do not modify QA-T004 implementation files.
- Do not modify plans or reports.
- Do not create tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts.
- Do not modify ResearchCore Engine docs/code.
- Do not run install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, environment repair, full test, docs generation, docs build, quickstart, CI smoke, or post-repair CLI validation commands.
- Do not start ADR-T003, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

Audit checks:
1. Verify changed files are bounded to QA-T004 planner artifacts, allowed NullForge status/source-index/QA path docs, QA-T004 reports, and this audit folder.
2. Confirm QA-T001, HY-T001, QA-T002, and QA-T003 audit reports contain `Decision: PASS`.
3. Confirm `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md` exists and includes:
   - ticket ID QA-T004
   - purpose and non-goals
   - QA-T001, HY-T001, QA-T002, and QA-T003 audit PASS evidence
   - QA-T003 decision packet summary
   - unresolved blocker summary
   - relevant package/CLI facts from pyproject.toml, docs/reference/cli/overview.md, docs/how-to/run_ci_locally.md, and src/research_core/cli.py
   - distinction between source facts, recorded local environment observations, expected unsupported command shapes, unresolved blockers, candidate repair/readiness paths, and recommended path
   - explicit statement that no install, uninstall, editable install, dependency sync, package build, virtual-environment work, environment repair, full tests, docs generation, docs build, quickstart, CI smoke, or post-repair CLI validation commands were run
   - candidate repair/readiness paths with tradeoffs and required human gates
   - recommended default path of isolated project-local virtual environment preparation
   - future command packet labeled `not run`
   - human decision options and stop conditions
   - side-effect, rollback, and cleanup considerations
   - local-path sanitization policy
   - exact sentence `No NullForge implementation code has started.`
4. Confirm CURRENT_STATUS.md names active ticket QA-T004, keeps REPO_SOURCE_IMPORT_BASELINE, and preserves the no-code sentence.
5. Confirm SOURCE_INDEX.md links only to repo-local files that exist, including QA-T004 planner artifacts, ENVIRONMENT_REPAIR_PATH.md, and QA-T004 report artifacts.
6. Confirm no forbidden files or folders were created or modified.
7. Run:
   - `git status --short --branch`
   - `git status --short --untracked-files=all`
   - `git diff --name-only`
   - `git diff --check`
   - `Test-Path -LiteralPath docs\nullforge\qa\ENVIRONMENT_REPAIR_PATH.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T004\IMPLEMENTATION_REPORT.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T004\CHANGED_FILES.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T004\TEST_RESULTS.md`
   - `Test-Path -LiteralPath reports\nullforge\QA-T004\AUDITOR_PROMPT.md`
   - `rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md audits\nullforge\QA-T002\AUDIT_REPORT.md audits\nullforge\QA-T003\AUDIT_REPORT.md`
   - `rg -n "QA-T004|QA-T003|python -m research_core.cli|No module named research_core.cli|local-temp-editable-install|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\qa\ENVIRONMENT_REPAIR_PATH.md docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md reports\nullforge\QA-T004\IMPLEMENTATION_REPORT.md reports\nullforge\QA-T004\TEST_RESULTS.md`
   - `git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools`
   - `Test-Path -LiteralPath tickets`
   - `Test-Path -LiteralPath milestones`
   - `Test-Path -LiteralPath prompts`
   - `Test-Path -LiteralPath audits\nullforge\QA-T004`

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

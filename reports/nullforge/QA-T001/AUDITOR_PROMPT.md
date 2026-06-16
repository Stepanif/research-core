# QA-T001 Auditor Prompt

You are Codex working in `<repo-root>`.

Task: independently audit `QA-T001` only.

Context:
- QA-T001 implementation is complete but uncommitted.
- Do not implement fixes.
- Do not commit.
- Do not push or merge.
- Do not start ADR-T003, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, or downstream work.
- No NullForge implementation code has started.

Read first:
- `plans/nullforge/QA-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/QA-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/QA-T001/PLAN.md`
- `plans/nullforge/QA-T001/ACCEPTANCE.md`
- `plans/nullforge/QA-T001/IMPLEMENTOR_PROMPT.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/M0_HANDOFF.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `audits/nullforge/MB-T001/AUDIT_REPORT.md`
- `reports/nullforge/QA-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T001/CHANGED_FILES.md`
- `reports/nullforge/QA-T001/TEST_RESULTS.md`
- `reports/nullforge/QA-T001/AUDITOR_PROMPT.md`
- `pyproject.toml`
- `requirements-docs.txt`
- `README.md`
- `.github/workflows/research-ci.yml`
- `.github/workflows/docs.yml`
- `docs/how-to/run_ci_locally.md`
- `docs/how-to/add_new_test_and_golden.md`
- `docs/how-to/add_new_cli_command.md`
- `docs/getting-started/quickstart.md`
- `docs/reference/cli/overview.md`
- `docs/reference/cli/index.md`

Allowed outputs:
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `audits/nullforge/QA-T001/FINDINGS.md`
- `audits/nullforge/QA-T001/REPAIR_PROMPT.md`

Forbidden:
- Do not modify QA-T001 implementation files.
- Do not modify plans or reports.
- Do not create tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, ES-derived fixtures, or downstream artifacts.
- Do not modify ResearchCore Engine docs or code.
- Do not update `docs/nullforge/DECISION_LEDGER.md`.
- Do not run install commands, full test commands, docs generation, docs build, quickstart commands, or CI smoke commands.
- Do not start ADR-T003, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

Audit checks:
1. Verify changed files are bounded to QA-T001 planner artifacts, allowed NullForge docs, QA-T001 reports, and this audit folder.
2. Confirm all seven prerequisite audit reports contain `Decision: PASS`.
3. Confirm `docs/nullforge/qa/COMMAND_DISCOVERY.md` exists and identifies:
   - `pyproject.toml` as package metadata source.
   - absence of root `package.json`, `pnpm-workspace.yaml`, and `pnpm-lock.yaml`.
   - Python version expectation from CI and bounded local query.
   - existing test command candidates.
   - existing docs-generation and docs-build command candidates.
   - CLI invocation evidence, especially `python -m research_core.cli`.
   - candidate commands from Volume 07 that fail or are unsupported, if observed.
   - existing fixtures/sample paths.
   - skipped commands and why.
   - side-effect review for `.pytest_cache/`, `exec_outputs/`, docs build output, and generated docs.
   - human gates and blockers.
4. Confirm `CURRENT_STATUS.md` names active ticket `QA-T001`, keeps `REPO_SOURCE_IMPORT_BASELINE` as source-import baseline context, and preserves `No NullForge implementation code has started.`
5. Confirm `SOURCE_INDEX.md` links only to repo-local files that exist, including QA-T001 command discovery, planner artifacts, and report artifacts.
6. Confirm no forbidden files/folders were created or modified.
7. Run bounded checks from `plans/nullforge/QA-T001/ACCEPTANCE.md` without running forbidden commands.

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

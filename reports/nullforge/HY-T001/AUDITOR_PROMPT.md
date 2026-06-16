# HY-T001 Auditor Prompt

You are Codex working in `<repo-root>` for this repository.

Task: independently audit `HY-T001` only.

Context:
- HY-T001 implementation is complete but uncommitted.
- HY-T001 is docs-only local-path hygiene.
- No NullForge implementation code has started.
- Do not implement fixes.
- Do not commit.
- Do not push or merge.
- Do not start ADR-T003, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, or downstream work.

Read first:
- `plans/nullforge/HY-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/HY-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/HY-T001/PLAN.md`
- `plans/nullforge/HY-T001/ACCEPTANCE.md`
- `plans/nullforge/HY-T001/IMPLEMENTOR_PROMPT.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `reports/nullforge/QA-T001/TEST_RESULTS.md`
- `reports/nullforge/HY-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/HY-T001/CHANGED_FILES.md`
- `reports/nullforge/HY-T001/TEST_RESULTS.md`
- `reports/nullforge/HY-T001/AUDITOR_PROMPT.md`

Allowed outputs:
- `audits/nullforge/HY-T001/AUDIT_REPORT.md`
- `audits/nullforge/HY-T001/FINDINGS.md`
- `audits/nullforge/HY-T001/REPAIR_PROMPT.md`

Forbidden:
- Do not modify HY-T001 implementation files.
- Do not modify HY-T001 planner artifacts or reports.
- Do not create tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, or downstream artifacts.
- Do not modify ResearchCore Engine docs or code.
- Do not run tests, installs, docs generation, docs build, quickstart commands, or CI smoke commands.
- Do not start ADR-T003, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.

Audit checks:
1. Verify changed files are bounded to approved NullForge docs/plans/reports/audits cleanup targets, `CURRENT_STATUS.md`, `SOURCE_INDEX.md`, HY-T001 planner artifacts, HY-T001 reports, and this audit folder.
2. Confirm QA-T001 audit report contains `Decision: PASS`.
3. Confirm local absolute path leakage was sanitized in the pre-HY candidate file set.
4. Confirm any remaining local-path search hits are limited to read-only HY-T001 planner artifacts that intentionally document search terms and replacement policy.
5. Confirm `CURRENT_STATUS.md` names active ticket `HY-T001`, keeps `REPO_SOURCE_IMPORT_BASELINE`, and preserves the exact no-code sentence.
6. Confirm `SOURCE_INDEX.md` links only to repo-local files that exist, including HY-T001 planner and report artifacts.
7. Confirm no forbidden files or folders were created or modified.
8. Run the required bounded checks from `plans/nullforge/HY-T001/ACCEPTANCE.md` and `reports/nullforge/HY-T001/TEST_RESULTS.md`.

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

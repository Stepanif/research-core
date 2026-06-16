# MB-T001 Auditor Prompt

You are Codex working in `<repo-root>`.

Task: independently audit `MB-T001` only.

Context:

- `MB-T001` implementation is complete but uncommitted.
- Do not implement fixes.
- Do not commit.
- Do not push or merge.
- Do not start M1, `QA-T001`, `ADR-T003`, or downstream work.

Read first:

- `plans/nullforge/MB-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/MB-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/MB-T001/PLAN.md`
- `plans/nullforge/MB-T001/ACCEPTANCE.md`
- `plans/nullforge/MB-T001/IMPLEMENTOR_PROMPT.md`
- `docs/nullforge/M0_HANDOFF.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `audits/nullforge/PF-T000/AUDIT_REPORT.md`
- `audits/nullforge/PF-T001/AUDIT_REPORT.md`
- `audits/nullforge/PF-T002/AUDIT_REPORT.md`
- `audits/nullforge/ADR-T001/AUDIT_REPORT.md`
- `audits/nullforge/ADR-T002/AUDIT_REPORT.md`
- `audits/nullforge/CX-T001/AUDIT_REPORT.md`
- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
- `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`
- `reports/nullforge/MB-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/MB-T001/CHANGED_FILES.md`
- `reports/nullforge/MB-T001/TEST_RESULTS.md`
- `reports/nullforge/MB-T001/AUDITOR_PROMPT.md`

Allowed outputs:

- `audits/nullforge/MB-T001/AUDIT_REPORT.md`
- `audits/nullforge/MB-T001/FINDINGS.md`
- `audits/nullforge/MB-T001/REPAIR_PROMPT.md`

Forbidden:

- Do not modify MB-T001 implementation files.
- Do not modify plans or reports.
- Do not create `tickets/`, `milestones/`, `prompts/`, QA docs, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, ES-derived fixtures, or downstream artifacts.
- Do not modify ResearchCore Engine docs/code.
- Do not update `docs/nullforge/DECISION_LEDGER.md`.
- Do not start M1, `QA-T001`, `ADR-T003`, desktop shell, bridge, sidecar, dataset, parser, fixture, packaging, release, cloud, telemetry, auth, billing, broker/live, mobile, marketplace, or public distribution work.

Audit checks:

1. Verify changed files are bounded to MB-T001 plans, allowed NullForge docs, MB-T001 reports, and this audit folder.
2. Confirm all six prerequisite audit reports contain `Decision: PASS`.
3. Confirm `docs/nullforge/M0_HANDOFF.md` exists and includes:
   - M0 title and goal;
   - completed ticket table for `PF-T000`, `PF-T001`, `PF-T002`, `ADR-T001`, `ADR-T002`, and `CX-T001` with audit `PASS` evidence;
   - `MB-T001` as pending independent audit, not audit `PASS`;
   - artifacts produced by M0;
   - accepted decisions `NF-D0001` through `NF-D0005`;
   - pending/deferred `NF-D0006`;
   - tests/checks summary;
   - scope drift section;
   - human decisions needed after audit;
   - claims, risks, and non-proofs;
   - M1 readiness statement naming `QA-T001` only as the recommended next scoped ticket after MB-T001 audit/closeout;
   - exact sentence `No NullForge implementation code has started.`
4. Confirm `CURRENT_STATUS.md` keeps `REPO_SOURCE_IMPORT_BASELINE`, names active ticket `MB-T001`, keeps the no-code sentence, and keeps M1, `QA-T001`, `ADR-T003`, and downstream work not started.
5. Confirm `SOURCE_INDEX.md` links only to repo-local files that exist, including `M0_HANDOFF.md`, MB-T001 planner artifacts, and MB-T001 report artifacts.
6. Confirm no forbidden files or folders were created or modified.
7. Run:
   - `git status --short --branch`
   - `git status --short --untracked-files=all`
   - `git diff --name-only`
   - `git diff --check`
   - `rg -n "Decision: PASS" audits\nullforge\PF-T000\AUDIT_REPORT.md audits\nullforge\PF-T001\AUDIT_REPORT.md audits\nullforge\PF-T002\AUDIT_REPORT.md audits\nullforge\ADR-T001\AUDIT_REPORT.md audits\nullforge\ADR-T002\AUDIT_REPORT.md audits\nullforge\CX-T001\AUDIT_REPORT.md`
   - `rg -n "M0|MB-T001|PF-T000|PF-T001|PF-T002|ADR-T001|ADR-T002|CX-T001|PASS|QA-T001|No NullForge implementation code has started|REPO_SOURCE_IMPORT_BASELINE" docs\nullforge\M0_HANDOFF.md docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md`

Return exactly one verdict:

- `PASS`
- `HOLD`
- `REJECT`

Then create the three audit files and report:

- verdict;
- blocking findings;
- non-blocking findings;
- human decision needed;
- repair prompt path.

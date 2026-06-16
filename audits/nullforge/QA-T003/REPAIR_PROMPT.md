# QA-T003 Repair Prompt

Ticket: `QA-T003`

Audit verdict: PASS

Date: `2026-06-16`

No repair is required.

## If Later Drift Is Found

Use this bounded repair prompt only if later review finds drift in the QA-T003 artifacts.

You are Codex working in `C:\Users\Filip\Desktop\Repos\research-core`.

Task: repair `QA-T003` documentation only, limited to the specific findings from the QA-T003 audit.

Allowed repair files:

- `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T003/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T003/CHANGED_FILES.md`
- `reports/nullforge/QA-T003/TEST_RESULTS.md`
- `reports/nullforge/QA-T003/AUDITOR_PROMPT.md`

Forbidden:

- Do not run install, uninstall, editable install, dependency sync, package build, virtual-environment creation or activation, environment repair, full tests, docs generation, docs build, quickstart commands, or CI smoke commands.
- Do not modify `pyproject.toml`, source files, tests, schemas, fixtures, CI, generated docs, README, dependencies, package metadata, ResearchCore Engine docs/code, tickets, milestones, prompts, raw data, private data, or downstream artifacts.
- Do not start `ADR-T003`, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, packaging, release, cloud, telemetry, auth, billing, broker/live, AI/model, or public distribution work.
- Do not commit, push, merge, or clean branches unless explicitly asked.

Required repair behavior:

1. Read `audits/nullforge/QA-T003/AUDIT_REPORT.md` and `audits/nullforge/QA-T003/FINDINGS.md`.
2. Repair only the listed QA-T003 documentation findings.
3. Preserve `No NullForge implementation code has started.`
4. Preserve `REPO_SOURCE_IMPORT_BASELINE` if `CURRENT_STATUS.md` or `SOURCE_INDEX.md` is touched.
5. Rerun the bounded QA-T003 checks from `plans/nullforge/QA-T003/ACCEPTANCE.md`.
6. Report changed files, checks run, remaining findings, and whether QA-T003 is ready for re-audit.

Current audit result: no repair required.

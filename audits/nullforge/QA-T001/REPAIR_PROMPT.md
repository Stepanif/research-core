# QA-T001 Repair Prompt

No repair is required for QA-T001 audit `PASS`.

If future drift is found before closeout, use this bounded repair prompt:

```text
You are Codex working in `<repo-root>`.

Task: repair QA-T001 only.

Context:
- QA-T001 independent audit returned PASS, so no repair is currently required.
- Use this prompt only if a concrete QA-T001 closeout issue is later found before commit.
- Do not start ADR-T003, desktop shell, bridge, sidecar, app scaffolding, M1 implementation, or downstream work.

Allowed files:
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/QA-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/QA-T001/CHANGED_FILES.md`
- `reports/nullforge/QA-T001/TEST_RESULTS.md`
- `reports/nullforge/QA-T001/AUDITOR_PROMPT.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `audits/nullforge/QA-T001/FINDINGS.md`
- `audits/nullforge/QA-T001/REPAIR_PROMPT.md`

Forbidden:
- Do not modify plans, prerequisite audits, ResearchCore Engine docs/code, tests, schemas, fixtures, package files, CI, generated docs, raw data, private data, or downstream artifacts.
- Do not run install commands, full test commands, docs generation, docs build, quickstart commands, or CI smoke commands.
- Do not create tickets, milestones, prompts, app files, code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, raw data, private data, ES-derived fixtures, or downstream artifacts.
- Do not commit, push, or merge.

Required work:
1. Identify the concrete QA-T001 closeout issue.
2. Make only the smallest bounded QA-T001 repair.
3. Run the QA-T001 bounded verification checks.
4. Report changed files, checks run, remaining findings, and whether QA-T001 is still ready for closeout.
```

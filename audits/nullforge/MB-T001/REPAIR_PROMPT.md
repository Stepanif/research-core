# MB-T001 Repair Prompt

Audit decision: PASS

No repair is required for MB-T001.

Do not run a repair for MB-T001 unless a later human review changes the audit disposition or identifies a concrete issue. If a repair is requested later, keep it bounded to MB-T001 audit findings only and do not start M1, `QA-T001`, `ADR-T003`, implementation code, tests, schemas, fixtures, dependencies, package files, CI, generated docs, ResearchCore Engine changes, `tickets/`, `milestones/`, `prompts/`, QA docs, raw/private data, ES-derived fixtures, or downstream work.

Required repair scope if later activated:

1. Read `audits/nullforge/MB-T001/AUDIT_REPORT.md` and `audits/nullforge/MB-T001/FINDINGS.md`.
2. Modify only the files explicitly named in blocking findings.
3. Preserve `No NullForge implementation code has started.`
4. Preserve `QA-T001`, `ADR-T003`, M1, and downstream work as not started unless a human-approved scoped ticket changes that state.
5. Re-run bounded MB-T001 checks and update only MB-T001 repair reports or audit artifacts allowed by the new human prompt.

# PF-T002 Auditor Prompt

You are the independent Auditor for NullForge M0 ticket `PF-T002`.

Audit only PF-T002. Do not implement fixes unless explicitly asked after the audit. Do not run `ADR-T001` or any downstream ticket.

## Read

```text
plans/nullforge/PF-T002/CONTEXT_BUNDLE.md
plans/nullforge/PF-T002/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/PF-T002/PLAN.md
plans/nullforge/PF-T002/ACCEPTANCE.md
plans/nullforge/PF-T002/IMPLEMENTOR_PROMPT.md
docs/nullforge/README.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/ARCHIVE_POLICY.md
docs/nullforge/blueprint/volumes/README.md
docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md
reports/nullforge/PF-T002/IMPLEMENTATION_REPORT.md
reports/nullforge/PF-T002/CHANGED_FILES.md
reports/nullforge/PF-T002/TEST_RESULTS.md
```

Use the incoming package PF-T002 ticket source unless `tickets/nullforge/PF-T002-create-nullforge-current-status-and-source-index.md` now exists:

```text
C:\Users\Filip\Desktop\NullForge_Incoming\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\PF-T002-create-nullforge-current-status-and-source-index.md
```

## Verify

- PF-T002 stayed docs-only.
- PF-T002 created only the allowed implementor files:
  - `docs/nullforge/README.md`
  - `docs/nullforge/CURRENT_STATUS.md`
  - `docs/nullforge/SOURCE_INDEX.md`
  - `docs/nullforge/DECISION_LEDGER.md`
  - `docs/nullforge/ARCHIVE_POLICY.md`
  - `reports/nullforge/PF-T002/IMPLEMENTATION_REPORT.md`
  - `reports/nullforge/PF-T002/CHANGED_FILES.md`
  - `reports/nullforge/PF-T002/TEST_RESULTS.md`
  - `reports/nullforge/PF-T002/AUDITOR_PROMPT.md`
- Existing ResearchCore Engine docs were not modified.
- `CURRENT_STATUS.md` uses exact active phase label `REPO_SOURCE_IMPORT_BASELINE`.
- `CURRENT_STATUS.md` contains the exact sentence `No NullForge implementation code has started.`
- `CURRENT_STATUS.md` names active ticket `PF-T002`, PF-T000/PF-T001 audit `PASS`, PF-T002 in progress until audit, blockers/gates, and next action `ADR-T001` after PF-T002 audit disposition.
- `SOURCE_INDEX.md` links only to repo-local files that exist.
- `SOURCE_INDEX.md` lists incoming package M0/PF-T002 sources as external active inputs in plain text and does not make broken repo-local Markdown links to absent tickets, milestones, or ADR files.
- `SOURCE_INDEX.md` separates Active docs, Imported volumes, Current ticket artifacts, Incoming package inputs, Design memory, Archive, Quarantine, Prompts, and Pending downstream docs.
- `DECISION_LEDGER.md` records accepted PF-T000/PF-T001/PF-T002 source baseline decisions and pending `ADR-T001`/`ADR-T002` without claiming ADR completion.
- `ARCHIVE_POLICY.md` references Volume 01 and defines active docs, design memory, archive, quarantine, prompts, and promotion rules.
- No M0 milestone docs, ticket files, prompt files, raw/full ES.zip contents, private/local data, ES-derived fixtures, implementation code, tests, schemas, dependencies, package files, CI files, generated reference docs, or downstream PF-T002+ artifacts were created.
- Required checks are recorded in `reports/nullforge/PF-T002/TEST_RESULTS.md`.
- Changed files are bounded to PF-T002 docs, plans, and reports.

## Create

```text
audits/nullforge/PF-T002/AUDIT_REPORT.md
audits/nullforge/PF-T002/FINDINGS.md
audits/nullforge/PF-T002/REPAIR_PROMPT.md
```

## Required Return

```text
Audit report path:
Findings path:
Repair prompt path:
Decision: PASS/HOLD/REJECT
Human gates:
Ready for ADR-T001? YES/NO
```

PF-T002 is not complete until this independent audit returns `PASS`, `HOLD`, or `REJECT`.

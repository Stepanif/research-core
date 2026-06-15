# Auditor Prompt: PF-T001 - Import NullForge Volumes Into Repo Docs

You are the independent Auditor for NullForge M0 ticket `PF-T001`.

Audit only PF-T001. Do not implement fixes unless explicitly asked after the audit. Do not run PF-T002 or any downstream ticket.

## Read

```text
plans/nullforge/PF-T001/CONTEXT_BUNDLE.md
plans/nullforge/PF-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/PF-T001/PLAN.md
plans/nullforge/PF-T001/ACCEPTANCE.md
plans/nullforge/PF-T001/IMPLEMENTOR_PROMPT.md
docs/nullforge/blueprint/volumes/README.md
docs/nullforge/blueprint/volumes/VOLUME_IMPORT_MANIFEST.md
reports/nullforge/PF-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/PF-T001/CHANGED_FILES.md
reports/nullforge/PF-T001/TEST_RESULTS.md
```

Also inspect the imported Volume 00-07 files under:

```text
docs/nullforge/blueprint/volumes/
```

Use the incoming package ticket source recorded in the implementation report unless `tickets/nullforge/PF-T001-import-nullforge-volumes-into-repo-docs.md` now exists.

## Audit Requirements

Verify:

- PF-T001 stayed docs-only.
- The selected Volume 00-07 artifact markdown files exist in `docs/nullforge/blueprint/volumes/`.
- Each imported volume has the required PF-T001 import notice.
- Imported volume content is preserved below the import notice.
- `README.md` and `VOLUME_IMPORT_MANIFEST.md` exist and describe authority boundaries.
- `VOLUME_IMPORT_MANIFEST.md` records source package names, hashes, selected zip entries, destination paths, prompt exclusion, PF-T000 PASS, and the Volume 00 human decision.
- Prompt files were not imported as canonical volume content.
- No existing ResearchCore Engine docs were modified.
- No implementation code, tests, schemas, dependencies, package files, CI files, generated reference docs, raw data, ES-derived fixtures, or downstream PF-T002+ artifacts were created.
- Required checks are recorded in `reports/nullforge/PF-T001/TEST_RESULTS.md`.
- Changed files are bounded to PF-T001 plans, docs, and reports.

## Create Audit Artifacts

Create:

```text
audits/nullforge/PF-T001/AUDIT_REPORT.md
audits/nullforge/PF-T001/FINDINGS.md
audits/nullforge/PF-T001/REPAIR_PROMPT.md
```

## Required Return

```text
Audit report path:
Findings path:
Repair prompt path:
Decision: PASS/HOLD/REJECT
Human gates:
Ready for PF-T002? YES/NO
```

PF-T001 is not complete until this independent audit returns PASS, HOLD, or REJECT.

# ADR-T001 Auditor Prompt

You are the independent Auditor for NullForge M0 ticket `ADR-T001`.

Audit only ADR-T001. Do not implement fixes unless explicitly asked after the audit. Do not run `ADR-T002` or any downstream ticket.

## Read

```text
plans/nullforge/ADR-T001/CONTEXT_BUNDLE.md
plans/nullforge/ADR-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/ADR-T001/PLAN.md
plans/nullforge/ADR-T001/ACCEPTANCE.md
plans/nullforge/ADR-T001/IMPLEMENTOR_PROMPT.md
docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
reports/nullforge/ADR-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/ADR-T001/CHANGED_FILES.md
reports/nullforge/ADR-T001/TEST_RESULTS.md
```

Use the incoming package ADR-T001 ticket source unless `tickets/nullforge/ADR-T001-name-platform-stack-engine-adr.md` now exists:

```text
<nullforge-incoming-root>\01_extracts\NullForge_M0_Repo_Source_Import_v0_4_Package\tickets\nullforge\ADR-T001-name-platform-stack-engine-adr.md
```

## Verify

- ADR-T001 stayed docs-only.
- ADR-T001 created or modified only the allowed files.
- Existing ResearchCore Engine docs were not modified.
- The ADR records `NullForge` as working product name only.
- The ADR states `NullForge` is not legally/trademark cleared and not safe/approved for public distribution.
- The ADR records repo remains `research-core`.
- The ADR records package names, CLI names, root README, existing ResearchCore docs, and public identity are unchanged.
- The ADR records internal engine label remains `ResearchCore Engine`.
- The ADR records existing ResearchCore Engine remains separate current engine truth.
- The ADR records Windows 11 x64 as first platform for future desktop proof work.
- The ADR records Tauri + React/TypeScript as accepted default desktop stack direction pending bridge/packaging spikes.
- The ADR records the intended engine boundary as Python ResearchCore Engine sidecar / scoped command bridge.
- The ADR records the bridge as narrow, allowlisted, and structured, not arbitrary shell execution.
- The ADR includes context, options considered, chosen decision, consequences, risks, unknowns, human gates, and reversal conditions.
- The ADR states no NullForge implementation code has started.
- The ADR does not claim Tauri feasibility, packaging feasibility, bridge reliability, product validation, user validation, market claims, trading validity, financial advice safety, legal clearance, or public distribution safety is proven.
- `docs/nullforge/DECISION_LEDGER.md` updates `NF-D0004` in place to reference ADR-T001 and does not add a duplicate same-decision row.
- `docs/nullforge/DECISION_LEDGER.md` keeps ADR-T002 pending.
- `docs/nullforge/CURRENT_STATUS.md` keeps active phase `REPO_SOURCE_IMPORT_BASELINE`, names active ticket `ADR-T001`, points next action to `ADR-T002` after ADR-T001 audit disposition, and includes `No NullForge implementation code has started.`
- `docs/nullforge/SOURCE_INDEX.md` links the new ADR-T001 file with a repo-local Markdown link that resolves.
- `docs/nullforge/SOURCE_INDEX.md` does not create broken links to missing ticket, milestone, prompt, or ADR-T002 files.
- No root README, docs index, docs status, docs architecture, docs navigation, generated reference docs, package files, CI files, code, tests, schemas, tools, milestones, tickets, prompts, raw data, ES-derived fixtures, or ADR-T002 files were created or modified.
- Required checks are recorded in `reports/nullforge/ADR-T001/TEST_RESULTS.md`.
- Changed files are bounded to ADR-T001 plans, allowed NullForge docs, reports, and this audit folder.

## Create

```text
audits/nullforge/ADR-T001/AUDIT_REPORT.md
audits/nullforge/ADR-T001/FINDINGS.md
audits/nullforge/ADR-T001/REPAIR_PROMPT.md
```

## Required Return

```text
Audit report path:
Findings path:
Repair prompt path:
Decision: PASS/HOLD/REJECT
Human gates:
Ready for ADR-T002? YES/NO
```

ADR-T001 is not complete until this independent audit returns `PASS`, `HOLD`, or `REJECT`.

# Auditor Prompt: ADR-T002 - Local-first/no-cloud MVP ADR

You are the independent Auditor for NullForge M0 ticket `ADR-T002`.

Audit only ADR-T002. Do not implement fixes. Do not start CX-T001, MB-T001, ADR-T003, M1, or downstream work.

## Read First

```text
plans/nullforge/ADR-T002/CONTEXT_BUNDLE.md
plans/nullforge/ADR-T002/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/ADR-T002/PLAN.md
plans/nullforge/ADR-T002/ACCEPTANCE.md
plans/nullforge/ADR-T002/IMPLEMENTOR_PROMPT.md
docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
reports/nullforge/ADR-T002/IMPLEMENTATION_REPORT.md
reports/nullforge/ADR-T002/CHANGED_FILES.md
reports/nullforge/ADR-T002/TEST_RESULTS.md
```

Dependency evidence:

```text
audits/nullforge/ADR-T001/AUDIT_REPORT.md
reports/nullforge/ADR-T001/TEST_RESULTS.md
```

## Audit Scope

Confirm ADR-T002 stayed docs-only and created or modified only:

```text
plans/nullforge/ADR-T002/
docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
docs/nullforge/DECISION_LEDGER.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
reports/nullforge/ADR-T002/
```

Planner artifacts under `plans/nullforge/ADR-T002/` may already exist and should be treated as read-only planner context.

## Required Audit Checks

Verify:

- ADR-T001 audit `PASS` is cited as prerequisite evidence.
- ADR records NullForge MVP as local-first by default.
- ADR records one selected local workspace as MVP runtime boundary.
- ADR records local files, manifests, logs, run/artifact metadata, evidence placeholders, and local ResearchCore Engine execution as MVP planning assumptions.
- ADR records local engine execution as future scoped sidecar/command bridge work and does not claim the bridge is implemented or proven.
- ADR records tiny/small fixtures are allowed only through later approved fixture policy.
- ADR records full ES.zip, raw/private data, generated datasets, and ES-derived fixtures remain gated and must not be committed by default.
- ADR excludes cloud storage, cloud sync, hosted backend, account/auth, billing, telemetry/analytics, mobile, marketplace, broker-live integration, live execution, and public distribution from MVP scope.
- ADR records no network behavior is required for MVP and future network access requires scoped ADR/ticket and human review.
- ADR states no NullForge implementation code has started.
- ADR does not claim legal/trademark clearance, public brand approval, public distribution safety, financial advice safety, trading validity, product validation, user validation, market validation, Tauri feasibility, bridge reliability, packaging feasibility, data licensing safety, cloud-security proof, telemetry enforcement, or no-cloud technical enforcement.
- ADR includes context, options considered, chosen decisions, consequences, risks and unknowns, human gates, reversal conditions, non-decisions, and next action.
- `DECISION_LEDGER.md` updates `NF-D0005` in place and does not add a duplicate local-first/no-cloud decision row.
- `CURRENT_STATUS.md` keeps active phase `REPO_SOURCE_IMPORT_BASELINE`, names active ticket `ADR-T002`, points next action to `CX-T001` after ADR-T002 audit disposition, and includes the exact no-code sentence.
- `SOURCE_INDEX.md` links only to repo-local files that exist.
- CX-T001, MB-T001, ADR-T003, and downstream work remain pending only.
- Required checks are recorded in `reports/nullforge/ADR-T002/TEST_RESULTS.md`.

## HOLD Or REJECT If

Return HOLD or REJECT if:

- existing ResearchCore Engine docs are overwritten, moved, renamed, or materially edited;
- root README, docs index, docs status, docs architecture, docs navigation, generated reference docs, package files, CI, code, tests, schemas, tools, milestones, tickets, prompts, raw data, generated data, ES-derived fixtures, ADR-T003, CX-T001, MB-T001, or downstream files are changed;
- implementation code, Tauri scaffold, bridge implementation, sidecar implementation, schemas, tests, package/dependency changes, telemetry implementation, cloud/auth/billing/mobile code, broker/live code, network code, fixtures, or dataset imports are created;
- repo/package/CLI/app/product/public identity is changed;
- ADR claims implementation proof, legal/trademark clearance, public distribution safety, Tauri feasibility proof, packaging proof, bridge proof, product/user/market validation, live-trading readiness, financial advice safety, data-licensing safety, cloud-security proof, telemetry enforcement, or no-cloud technical enforcement;
- decision ledger does not reference ADR-T002 or duplicates `NF-D0005`;
- `SOURCE_INDEX.md` contains broken repo-local Markdown links;
- incoming-only ticket/milestone/prompt sources are treated as repo-local files that already exist;
- prompt files or old chats are treated as active source truth;
- CX-T001, MB-T001, ADR-T003, or downstream M0/M1 work starts;
- checks are skipped without explanation;
- a human gate is triggered and work continues without approval.

## Required Outputs

Create only:

```text
audits/nullforge/ADR-T002/AUDIT_REPORT.md
audits/nullforge/ADR-T002/FINDINGS.md
audits/nullforge/ADR-T002/REPAIR_PROMPT.md
```

Return exactly one verdict:

```text
PASS
HOLD
REJECT
```

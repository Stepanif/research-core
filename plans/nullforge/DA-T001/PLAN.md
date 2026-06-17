# DA-T001 Plan

Date: `2026-06-17`

Ticket: `DA-T001`

Title: Desktop bridge contract finalization

Role: Planner

Status: Ready for implementor handoff

No NullForge implementation code has started.

## Goal

Plan a docs-only DA-T001 implementation pass that creates a repo-local desktop bridge contract source document from the Volume 3 bridge draft.

The intended implementation output is:

```text
docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md
```

The contract must define the future NullForge desktop bridge boundary as a narrow, allowlisted, structured command protocol. It must not implement the bridge, app, sidecar, Tauri shell, commands, package metadata, dependencies, tests, schemas, fixtures, CI, or generated docs.

## Source Context Used

- `plans/nullforge/DA-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/DA-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/DECISION_LEDGER.md`
- `docs/nullforge/ARCHIVE_POLICY.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
- `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`
- `docs/nullforge/qa/COMMAND_DISCOVERY.md`
- `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md`
- prior PASS audit reports through `audits/nullforge/QA-T005/AUDIT_REPORT.md`
- `pyproject.toml`
- `docs/reference/cli/overview.md`
- `docs/how-to/run_ci_locally.md`
- `src/research_core/cli.py`

## Assumptions

- The human has selected DA-T001 as the next scoped ticket.
- Prior required tickets through QA-T005 have audit `PASS`.
- The worktree was clean before DA-T001 planning.
- DA-T001 implementation is docs-only.
- `docs/nullforge/architecture/` does not need to exist before the DA-T001 implementor creates `ENGINE_BRIDGE_CONTRACT.md`.
- Existing ResearchCore Engine behavior remains authoritative and unchanged.
- QA-T005 proves only that this workspace can be installed editable inside `.venv-qa-t005`, `research_core.cli` is import-visible there, and `python -m research_core.cli --help` runs there.
- `python -m research_core --help` and `research-core --help` remain unsupported command shapes.
- Volume 3 bridge command IDs are planning candidates unless separately proven or implemented.

## Scope

DA-T001 implementor may:

- create `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`;
- update `docs/nullforge/CURRENT_STATUS.md` only to reflect DA-T001 docs implementation/audit-pending state and preserve the no-code claim;
- update `docs/nullforge/SOURCE_INDEX.md` only to link the new bridge contract and DA-T001 artifacts that exist;
- create standard DA-T001 reports under `reports/nullforge/DA-T001/`;
- run read-only documentation checks and Git scope checks;
- record skipped runtime/test/build checks with exact reasons.

The bridge contract document should include:

- title, date, authority, scope, non-goals, and no-code claim;
- relationship to ADR-T001, ADR-T002, Volume 3, Volume 7, and QA-T005;
- contract principles: allowlisted command IDs, structured inputs/outputs, workspace scope, bounded logs/errors, deny-by-default permissions;
- explicit distinction between planned bridge commands and current ResearchCore Engine behavior;
- request object field table;
- response object field table;
- error response field table;
- candidate command allowlist with implementation status such as `planned/not implemented`;
- first-proof command selection policy for later DA-T004;
- forbidden bridge behaviors;
- workspace path and artifact path rules;
- logging and stderr rules;
- permission boundary and human gates;
- security/privacy/data/file-access considerations;
- tests/checks expected for later implementation tickets;
- non-proofs and claim boundaries;
- open questions for DA-T002/DA-T004.

## Out Of Scope

DA-T001 must not:

- create or modify Tauri, Rust, React, TypeScript, JavaScript, Node, Python bridge, sidecar, app, package, dependency, schema, test, fixture, generated-doc, CI, README, docs/reference, or tools files;
- change `pyproject.toml`, package metadata, CLI entrypoints, source code, tests, schemas, fixtures, `.github`, root docs, or ResearchCore Engine docs;
- add `[project.scripts]`, `console_scripts`, or `src/research_core/__main__.py`;
- create `tickets`, `milestones`, or `prompts`;
- create audits;
- run install commands, environment repair, full tests, docs generation, docs build, quickstart commands, CI smoke, Tauri commands, Node/Rust commands, bridge commands, sidecar commands, or app commands;
- create or use raw/full ES.zip, private/local data, generated datasets, or ES-derived fixtures;
- broaden filesystem permissions, shell/process command surface, network behavior, updater/signing/release behavior, telemetry, cloud/auth/billing, broker/live, AI/model, or public distribution scope;
- start DA-T002, DA-T003, DA-T004, WB-T001, MB-T002, ADR-T003, packaging, or downstream implementation work.

## Planned File Changes

Allowed implementation changes:

```text
docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md
docs/nullforge/CURRENT_STATUS.md
docs/nullforge/SOURCE_INDEX.md
reports/nullforge/DA-T001/IMPLEMENTATION_REPORT.md
reports/nullforge/DA-T001/CHANGED_FILES.md
reports/nullforge/DA-T001/TEST_RESULTS.md
reports/nullforge/DA-T001/AUDITOR_PROMPT.md
```

Allowed planning changes already performed by this prompt:

```text
plans/nullforge/DA-T001/CONTEXT_BUNDLE.md
plans/nullforge/DA-T001/CONTEXT_BUNDLE_MANIFEST.md
plans/nullforge/DA-T001/PLAN.md
plans/nullforge/DA-T001/ACCEPTANCE.md
plans/nullforge/DA-T001/IMPLEMENTOR_PROMPT.md
```

## Implementation Steps For Later Implementor

1. Confirm the worktree has only allowed DA-T001 planning artifacts before implementation.
2. Read all DA-T001 planner artifacts and active source docs listed in the implementor prompt.
3. Confirm prerequisite audit `PASS` evidence through QA-T005.
4. Create `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md` as a docs-only source document.
5. In the contract, define bridge fields and allowlist policy without claiming runtime implementation.
6. Label candidate commands as planned/not implemented unless current repo evidence proves otherwise.
7. Add a first-proof selection rule that a later ticket must choose a single safe command and must not rely on unsupported command shapes.
8. Preserve the QA-T005 boundary that only `.venv-qa-t005` readiness for `python -m research_core.cli --help` has been proven.
9. Update `docs/nullforge/CURRENT_STATUS.md` for DA-T001 audit-pending state only, preserving `No NullForge implementation code has started.`
10. Update `docs/nullforge/SOURCE_INDEX.md` with links to the contract and DA-T001 reports that exist.
11. Create DA-T001 implementation reports.
12. Run required checks.
13. Stop before any runtime bridge/app/environment work.

## Required Checks

The implementor should run:

- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- `Test-Path -LiteralPath docs\nullforge\architecture\ENGINE_BRIDGE_CONTRACT.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T001\IMPLEMENTATION_REPORT.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T001\CHANGED_FILES.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T001\TEST_RESULTS.md`
- `Test-Path -LiteralPath reports\nullforge\DA-T001\AUDITOR_PROMPT.md`
- prerequisite `Decision: PASS` checks for prior audits through QA-T005
- content search for `DA-T001`, `ENGINE_BRIDGE_CONTRACT`, `No NullForge implementation code has started`, `allowlist`, `arbitrary shell`, `.venv-qa-t005`, `python -m research_core.cli --help`, `network`, `broker`, and `live`
- forbidden tracked-path diff check for `src`, `tests`, `schemas`, `fixtures`, package/dependency files, `.github`, `README.md`, `docs/reference`, and `tools`
- absence checks for `tickets`, `milestones`, and `prompts`

The implementor must not run runtime/app/build/test commands beyond read-only docs/Git checks unless a later scoped prompt explicitly authorizes them.

## Security, Privacy, Data, And File Access Considerations

The future bridge contract must make these constraints explicit:

- no arbitrary shell strings from UI or docs;
- no user-provided scripts;
- no command execution outside an allowlist;
- no silent dependency installs or environment mutation;
- no broad drive/folder scans;
- workspace-scoped read/write only;
- workspace-relative artifact paths by default;
- path normalization and traversal rejection;
- bounded stderr in UI and logs;
- no secrets in logs;
- no full ES.zip, raw/private data, generated datasets, or ES-derived fixtures;
- no network/cloud/auth/billing/telemetry/mobile/marketplace behavior;
- no broker/live trading or live execution;
- no AI/model calls;
- no updater/signing/public release.

## Human Gate Triggers

The implementor must stop before:

- changing source/package/test/schema/fixture/generated-doc/CI files;
- adding or changing dependencies;
- creating Tauri, Rust, React, TypeScript, JavaScript, Python bridge, sidecar, app, package, or build files;
- running environment-changing commands;
- running Tauri, Node, Rust, bridge, sidecar, app, full test, docs build, quickstart, or CI smoke commands;
- expanding command allowlist beyond documentation of planned candidates;
- adding filesystem, shell/process, network, telemetry, cloud, auth, billing, broker/live, AI/model, updater, signing, or public release behavior;
- changing ResearchCore Engine command behavior;
- promoting implementation, product, market, legal, trading, financial advice, packaging, telemetry, no-cloud enforcement, or public distribution claims.

## Rollback And Repair Route

Planner repair is limited to:

- `plans/nullforge/DA-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/DA-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/DA-T001/PLAN.md`
- `plans/nullforge/DA-T001/ACCEPTANCE.md`
- `plans/nullforge/DA-T001/IMPLEMENTOR_PROMPT.md`

Implementation repair, if later needed, should be bounded to DA-T001 docs/status/source-index/report files only. Any repair that requires code, dependencies, tests, environment mutation, package metadata, app scaffolding, bridge execution, or command behavior changes must stop for human direction and a new scoped ticket.

## Planner Verdict

Ready for implementor handoff.

The later implementor may create the bridge contract document and DA-T001 reports, with tightly scoped status/source-index updates. No implementation or runtime proof is authorized.

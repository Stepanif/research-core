# DA-T001 Implementor Prompt

Use this prompt only for DA-T001 implementation after the human approves implementation of the planned docs-only contract.

```text
You are Codex working in `<repo-root>`.

Task: implement DA-T001 only. Do not commit.

Ticket:
DA-T001 - Desktop bridge contract finalization

Mission:
Create a repo-local desktop bridge contract source document from the Volume 3 bridge draft. This is docs-only. Do not implement Tauri, Rust, React, Python bridge code, sidecar code, package config, tests, schemas, CI, dependencies, fixtures, generated docs, app files, or runtime bridge behavior.

Required claim boundary:
No NullForge implementation code has started.

Read first:
- plans/nullforge/DA-T001/CONTEXT_BUNDLE.md
- plans/nullforge/DA-T001/CONTEXT_BUNDLE_MANIFEST.md
- plans/nullforge/DA-T001/PLAN.md
- plans/nullforge/DA-T001/ACCEPTANCE.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- docs/nullforge/DECISION_LEDGER.md
- docs/nullforge/ARCHIVE_POLICY.md
- docs/nullforge/codex/CODEX_ROLE_LOOP.md
- docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md
- docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md
- docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md
- docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md
- docs/nullforge/qa/COMMAND_DISCOVERY.md
- docs/nullforge/qa/ENVIRONMENT_TRIAGE.md
- docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md
- docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md
- docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md
- audits/nullforge/PF-T000/AUDIT_REPORT.md
- audits/nullforge/PF-T001/AUDIT_REPORT.md
- audits/nullforge/PF-T002/AUDIT_REPORT.md
- audits/nullforge/ADR-T001/AUDIT_REPORT.md
- audits/nullforge/ADR-T002/AUDIT_REPORT.md
- audits/nullforge/CX-T001/AUDIT_REPORT.md
- audits/nullforge/MB-T001/AUDIT_REPORT.md
- audits/nullforge/QA-T001/AUDIT_REPORT.md
- audits/nullforge/HY-T001/AUDIT_REPORT.md
- audits/nullforge/QA-T002/AUDIT_REPORT.md
- audits/nullforge/QA-T003/AUDIT_REPORT.md
- audits/nullforge/QA-T004/AUDIT_REPORT.md
- audits/nullforge/QA-T005/AUDIT_REPORT.md
- pyproject.toml
- docs/reference/cli/overview.md
- docs/how-to/run_ci_locally.md
- src/research_core/cli.py

Allowed files/folders:
- docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- reports/nullforge/DA-T001/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T001/CHANGED_FILES.md
- reports/nullforge/DA-T001/TEST_RESULTS.md
- reports/nullforge/DA-T001/AUDITOR_PROMPT.md

Treat as read-only:
- plans/nullforge/DA-T001/*
- all prior plans, reports, and audits
- docs/nullforge/ARCHIVE_POLICY.md
- docs/nullforge/DECISION_LEDGER.md
- docs/nullforge/codex/CODEX_ROLE_LOOP.md
- docs/nullforge/adr/*
- docs/nullforge/blueprint/*
- docs/nullforge/qa/*
- pyproject.toml
- requirements-docs.txt
- docs/reference/*
- docs/how-to/*
- README.md
- .github/
- src/
- tests/
- schemas/
- fixtures/
- tools/
- package/dependency files
- generated docs
- ResearchCore Engine docs/code

Required bridge contract content:
- authority and non-proof statement;
- DA-T001 scope and non-goals;
- source context used;
- relationship to ADR-T001, ADR-T002, Volume 3, Volume 7, and QA-T005;
- structured request fields;
- structured response fields;
- structured error response fields;
- command allowlist policy;
- candidate command IDs marked planned/not implemented unless evidence proves otherwise;
- explicit statement that Volume 3 candidates such as engine.version, engine.doctor, workspace.inspect, fixture.smoke, and artifact.scan are contract candidates, not proven current behavior;
- first-proof command selection rule for DA-T004;
- QA-T005 limitation: only .venv-qa-t005 readiness for python -m research_core.cli --help is proven;
- unsupported command shapes remain unsupported: python -m research_core --help and research-core --help;
- no arbitrary shell execution;
- no user-provided script execution;
- no silent dependency install or environment mutation;
- workspace-scoped path rules;
- artifact path and log/stderr rules;
- deny-by-default permission boundary;
- cloud/network/telemetry/auth/billing/broker/live/AI/updater/signing/public release exclusions;
- human gates and stop conditions;
- tests/checks expected for later bridge implementation tickets;
- claim boundaries and non-proofs.

Required implementation reports:
- reports/nullforge/DA-T001/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T001/CHANGED_FILES.md
- reports/nullforge/DA-T001/TEST_RESULTS.md
- reports/nullforge/DA-T001/AUDITOR_PROMPT.md

Required checks:
- git status --short --untracked-files=all
- git diff --name-only
- git diff --check
- Test-Path -LiteralPath docs\nullforge\architecture\ENGINE_BRIDGE_CONTRACT.md
- Test-Path -LiteralPath reports\nullforge\DA-T001\IMPLEMENTATION_REPORT.md
- Test-Path -LiteralPath reports\nullforge\DA-T001\CHANGED_FILES.md
- Test-Path -LiteralPath reports\nullforge\DA-T001\TEST_RESULTS.md
- Test-Path -LiteralPath reports\nullforge\DA-T001\AUDITOR_PROMPT.md
- rg -n "Decision: PASS" audits\nullforge\PF-T000\AUDIT_REPORT.md audits\nullforge\PF-T001\AUDIT_REPORT.md audits\nullforge\PF-T002\AUDIT_REPORT.md audits\nullforge\ADR-T001\AUDIT_REPORT.md audits\nullforge\ADR-T002\AUDIT_REPORT.md audits\nullforge\CX-T001\AUDIT_REPORT.md audits\nullforge\MB-T001\AUDIT_REPORT.md audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md audits\nullforge\QA-T002\AUDIT_REPORT.md audits\nullforge\QA-T003\AUDIT_REPORT.md audits\nullforge\QA-T004\AUDIT_REPORT.md audits\nullforge\QA-T005\AUDIT_REPORT.md
- rg -n "DA-T001|ENGINE_BRIDGE_CONTRACT|No NullForge implementation code has started|allowlist|arbitrary shell|\\.venv-qa-t005|python -m research_core.cli --help|network|broker|live" docs\nullforge\architecture\ENGINE_BRIDGE_CONTRACT.md docs\nullforge\CURRENT_STATUS.md docs\nullforge\SOURCE_INDEX.md reports\nullforge\DA-T001\IMPLEMENTATION_REPORT.md reports\nullforge\DA-T001\TEST_RESULTS.md
- git diff --name-only -- src tests schemas fixtures pyproject.toml requirements-docs.txt package.json pnpm-lock.yaml pnpm-workspace.yaml .github README.md docs\reference tools
- Test-Path -LiteralPath tickets
- Test-Path -LiteralPath milestones
- Test-Path -LiteralPath prompts

Forbidden:
- creating or modifying Tauri, Rust, React, TypeScript, JavaScript, Python bridge, sidecar, app, source, package, dependency, schema, test, fixture, generated-doc, CI, README, docs/reference, or tool files;
- changing ResearchCore Engine command behavior, CLI entrypoints, package metadata, docs/reference docs, or source code;
- adding [project.scripts], console_scripts, or src/research_core/__main__.py;
- creating tickets, milestones, prompts, or audits;
- running install commands, environment repair, full tests, docs generation, docs build, quickstart, CI smoke, Tauri, Node, Rust, bridge, sidecar, app, or runtime validation commands;
- creating or using full ES.zip, raw/private data, generated datasets, or ES-derived fixtures;
- permitting arbitrary shell execution;
- broadening filesystem, shell/process, network, telemetry, cloud/auth/billing, broker/live, AI/model, updater, signing, public release, or financial advice scope;
- starting DA-T002, DA-T003, DA-T004, WB-T001, MB-T002, ADR-T003, packaging, or downstream work.

Human gate:
Stop and report the needed decision if the contract appears to require:
- any code or dependency change;
- any environment mutation;
- any command behavior change in ResearchCore Engine;
- any exact bridge command implementation choice that cannot be documented without running or changing code;
- any permission or file access expansion;
- any network/cloud/telemetry/auth/billing/broker/live/AI/updater/signing/public release scope;
- any data/fixture handling.

Report:
- changed files;
- checks run;
- checks skipped with exact reason;
- forbidden-path review;
- human gates triggered;
- known risks and open questions;
- whether DA-T001 is ready for independent audit.

Do not commit.
```

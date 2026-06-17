# NullForge Rust/Cargo Toolchain Decision

Date: `2026-06-17`

Ticket: `DA-T003R`

Status: Complete; audit `PASS`.

No NullForge implementation code has started.

## Purpose

This document records the human-gated decision path for resolving the DA-T003 `HOLD` caused by missing `rustc` and `cargo` on PATH.

DA-T003R is docs-only toolchain availability decisioning. It is not Rust/Cargo installation, PATH repair, environment repair, toolchain verification, app scaffold creation, package configuration, dependency resolution, Tauri launch proof, bridge implementation, sidecar work, or runtime behavior.

## Source Authority

This document is derived from:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `audits/nullforge/DA-T003/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003/FINDINGS.md`
- `audits/nullforge/DA-T003/REPAIR_PROMPT.md`
- `reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003/CHANGED_FILES.md`
- `reports/nullforge/DA-T003/TEST_RESULTS.md`
- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
- `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md`
- `audits/nullforge/QA-T005/AUDIT_REPORT.md`
- `audits/nullforge/DA-T001/AUDIT_REPORT.md`
- `audits/nullforge/DA-T002/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003R/AUDIT_REPORT.md`

`audits/nullforge/DA-T003/AUDIT_REPORT.md` and `audits/nullforge/DA-T003/FINDINGS.md` are the direct DA-T003 blocker authority.

`audits/nullforge/DA-T003R/AUDIT_REPORT.md` is the closeout audit authority for this decision source and records `Decision: PASS`.

## DA-T003 HOLD Summary

DA-T003 attempted the first minimal launch-only Windows/Tauri shell scaffold implementation, but stopped before scaffold creation at the required toolchain gate.

The blocker is:

- `rustc` is unavailable on PATH.
- `cargo` is unavailable on PATH.

The DA-T003 audit decision is `HOLD`.

DA-T003 did not create:

- `apps/`;
- `apps/nullforge-desktop/`;
- `src-tauri/`;
- package files;
- lockfiles;
- Rust files;
- React files;
- TypeScript files;
- JavaScript files;
- CSS files;
- HTML app files.

DA-T003 did not run:

- dependency install commands;
- package-manager install commands;
- Tauri commands;
- app launch commands;
- bridge commands;
- sidecar commands;
- ResearchCore Engine commands;
- environment repair commands;
- downstream work.

## Decision

DA-T003 remains blocked until one of these separately authorized paths occurs:

1. A human-approved action makes `rustc` and `cargo` available on PATH.
2. A separate scoped planning or ADR ticket changes the DA-T003 plan.

The recommended path is path 1: a separate human-approved Rust/Cargo availability action, followed by a separate DA-T003 resume ticket.

DA-T003R does not execute that human action and does not prove Rust/Cargo availability.

## Future Human-Gated Path

The human-gated Rust/Cargo availability action is outside DA-T003R.

That future action may involve local machine setup, PATH configuration, or other prerequisite work, but DA-T003R does not authorize Codex to perform that work.

After the human-approved action is complete, a separate DA-T003 resume prompt may check:

- `rustc --version`
- `cargo --version`

Those checks are future DA-T003 resume checks only. They were not run by DA-T003R and must not be treated as DA-T003R proof.

If either command is still unavailable during a later DA-T003 resume, that ticket must stop again and record renewed blocker evidence. It must not install or repair Rust/Cargo unless a separate scoped ticket explicitly permits that work.

## Alternative Path

If Rust/Cargo cannot be made available, or if a non-Rust desktop route is desired, the next step is a separate scoped planning or ADR ticket.

That separate ticket must decide whether to:

- change the DA-T003 prerequisite;
- change the desktop scaffold approach;
- revisit the ADR-T001 Tauri + React/TypeScript stack direction;
- defer the desktop scaffold until local prerequisites are ready.

DA-T003R does not change the desktop stack direction.

## Stop Conditions

Any DA-T003R implementor or follow-on repair attempt must stop if the work would require:

- Rust/Cargo installation;
- PATH repair;
- environment variable changes;
- `rustc --version`;
- `cargo --version`;
- Node, pnpm, Tauri, package-manager, dependency, install, build, app, bridge, sidecar, runtime, ResearchCore Engine, Python CLI, test, docs build, quickstart, or CI commands;
- app/package/Tauri/Rust/React/TypeScript/JavaScript/CSS/HTML file creation;
- root package/workspace/Cargo files;
- source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool changes;
- DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work.

## Preserved Claim Boundaries

QA-T005 proves only:

- `research-core` can be installed editable into `.venv-qa-t005`;
- `research_core` and `research_core.cli` are import-visible inside `.venv-qa-t005`;
- `python -m research_core.cli --help` runs inside `.venv-qa-t005`.

The following command shapes remain unsupported unless a later source/package ticket changes them:

- `python -m research_core --help`
- `research-core --help`

DA-T001 proves only a docs-only planned desktop bridge contract source document.

DA-T002 proves only a docs-only Tauri scaffold plan source document.

DA-T003 proves only a blocked pre-scaffold implementation attempt caused by missing `rustc` and `cargo` on PATH.

DA-T003R proves only a docs-only human-gated Rust/Cargo availability decision source. It does not prove Rust/Cargo availability, app scaffold creation, Tauri launch behavior, package/dependency readiness, Rust/React/TypeScript/JavaScript/CSS/HTML behavior, bridge command behavior, sidecar behavior, runtime behavior, or public release readiness.

## Excluded Scope

The following remain excluded:

- cloud storage;
- cloud sync;
- hosted backend;
- network behavior;
- telemetry/analytics;
- account/auth;
- billing;
- marketplace;
- mobile;
- broker/live trading;
- live execution;
- AI/model calls;
- updater;
- signing;
- installer or public release;
- legal/trademark claims;
- financial advice claims;
- raw/full ES.zip;
- private/local data import;
- generated datasets;
- ES-derived fixtures;
- product, market, trading, or validation claims.

## Next Action After Audit

After DA-T003R audit `PASS`, human direction is needed before any Rust/Cargo availability action, DA-T003 resume, app scaffold creation, dependency work, runtime command, bridge implementation, sidecar work, ADR-T003, DA-T004, WB-T001, MB-T002, or downstream M1 work.

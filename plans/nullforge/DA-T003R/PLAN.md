# DA-T003R Plan

Date: `2026-06-17`

Ticket: `DA-T003R - Rust/Cargo toolchain availability decision`

Role: Context Curator + Planner

No NullForge implementation code has started.

## Objective

Plan a docs-only source document that records the human-gated path for resolving the DA-T003 `HOLD` caused by missing `rustc` and `cargo` on PATH.

DA-T003R implementation, when separately authorized, should create a decision/repair path source document only. It must not install Rust/Cargo, repair PATH, rerun toolchain probes, create app files, modify package config, run dependency commands, run Tauri/Node/Rust app commands, or resume DA-T003 implementation.

## Planned Implementation Target

The DA-T003R implementor should create:

```text
docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md
```

This document should become the repo-local source for the DA-T003 toolchain availability decision. It should not be treated as toolchain availability proof.

## Planned Source Document Requirements

The DA-T003R source document should include:

- ticket ID `DA-T003R`;
- purpose and scope;
- source authority list;
- DA-T003 HOLD summary;
- exact blocker: `rustc` and `cargo` are unavailable on PATH;
- explicit no-code sentence: `No NullForge implementation code has started.`;
- no-scaffold boundary: no `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app file has been created;
- selected recommendation: keep DA-T003 blocked until a human-approved action makes `rustc` and `cargo` available on PATH, or a separate scoped plan changes DA-T003;
- future human action boundary: install/PATH repair is outside DA-T003R and must not be performed by the implementor;
- future DA-T003 resume boundary: `rustc --version` and `cargo --version` may be verified only in a later scoped DA-T003 resume prompt after the human action is complete;
- fallback path: if the human does not approve Rust/Cargo availability work, changing the desktop stack or DA-T003 approach requires a separate scoped decision or ADR;
- stop conditions;
- non-proofs and excluded scope;
- QA-T005, DA-T001, DA-T002, and DA-T003 claim boundaries.

## Selected Recommendation To Record

DA-T003R should recommend this path:

1. Keep DA-T003 in `HOLD`.
2. Record that the recommended unblock path is a separate human-approved Rust/Cargo availability action outside DA-T003R.
3. After the human action, run a separate DA-T003 resume ticket that first checks `rustc --version` and `cargo --version`.
4. Resume DA-T003 only if Rust/Cargo are already available and the DA-T003 allowed file/command boundary remains valid.
5. If Rust/Cargo cannot be made available or a non-Rust desktop route is desired, create a separate scoped planning/ADR ticket before changing the scaffold plan.

DA-T003R must not execute any step above. It only records the decision path.

## Allowed Implementor Changes

The DA-T003R implementor may create or update only:

- `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T003R/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003R/CHANGED_FILES.md`
- `reports/nullforge/DA-T003R/TEST_RESULTS.md`
- `reports/nullforge/DA-T003R/AUDITOR_PROMPT.md`

No other tracked files should change.

## Implementation Steps

1. Re-read the DA-T003R planner artifacts.
2. Re-read `docs/nullforge/CURRENT_STATUS.md`, `docs/nullforge/SOURCE_INDEX.md`, `audits/nullforge/DA-T003/AUDIT_REPORT.md`, `audits/nullforge/DA-T003/FINDINGS.md`, and `audits/nullforge/DA-T003/REPAIR_PROMPT.md`.
3. Confirm the worktree state with `git status --short --untracked-files=all`.
4. Create `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md` as a docs-only decision source.
5. Update `docs/nullforge/CURRENT_STATUS.md` to record DA-T003R implementation pending independent audit only.
6. Update `docs/nullforge/SOURCE_INDEX.md` to link the DA-T003R decision source and reports only after the files exist.
7. Create DA-T003R reports under `reports/nullforge/DA-T003R/`.
8. Run all required checks in `ACCEPTANCE.md`.
9. Do not commit unless separately instructed.

## Forbidden Work

The DA-T003R implementor must not:

- install Rust/Cargo;
- run `rustup`;
- run `cargo install`;
- repair PATH or environment variables;
- run `rustc --version`;
- run `cargo --version`;
- run `node`, `pnpm`, Tauri, package-manager, dependency, install, build, app, bridge, sidecar, runtime, ResearchCore Engine, or Python CLI commands;
- create `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package files, lockfiles, Rust files, React files, TypeScript files, JavaScript files, CSS files, or HTML files;
- modify root package/workspace/Cargo files;
- modify source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool files;
- create tickets, milestones, prompt packs, audits, fixtures, schemas, tests, CI, generated docs, README, docs/reference, or tools;
- implement or invoke bridge commands;
- invoke ResearchCore Engine;
- package or launch a sidecar;
- start DA-T003 resume, DA-T004, WB-T001, MB-T002, ADR-T003, or downstream work;
- add cloud, network, telemetry, auth, billing, broker/live, AI/model, updater, signing, public release, mobile, marketplace, legal/trademark, or financial advice scope.

## Status And Navigation Expectations

If DA-T003R implementation creates the decision source document, `CURRENT_STATUS.md` should:

- keep `No NullForge implementation code has started.`;
- record DA-T003R as implemented and pending independent audit;
- keep DA-T003 blocked until a separate human-approved action makes `rustc` and `cargo` available on PATH or changes the DA-T003 plan;
- preserve that no app scaffold or app files have been created.

`SOURCE_INDEX.md` should add links only for DA-T003R files that exist.

## Checks To Require

DA-T003R implementation must run:

- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- required path/content/forbidden-path checks from `ACCEPTANCE.md`

The implementor must not run Rust/Cargo, Node, pnpm, Tauri, package-manager, dependency, app, bridge, sidecar, runtime, ResearchCore Engine, Python CLI, install, or environment repair commands.

## Risk Controls

- Treat DA-T003 audit `HOLD` as the blocker authority.
- Keep DA-T003R docs-only.
- Keep app scaffold creation deferred.
- Keep Rust/Cargo installation and PATH repair outside Codex unless a later human-approved scoped ticket explicitly permits it.
- Do not convert a toolchain availability decision into a desktop stack change.
- Require separate human direction before DA-T003 resume.

## Done Definition

DA-T003R implementation is done when:

- `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md` exists and records the recommended human-gated Rust/Cargo availability path;
- status/source navigation is bounded and audit-pending;
- DA-T003R reports exist;
- required content checks pass;
- absent app/package/toolchain path checks pass;
- forbidden tracked-path diff check returns no output;
- no Rust/Cargo install, environment repair, app scaffold, dependency work, runtime command, bridge work, sidecar work, or downstream work is introduced;
- no broader proof is claimed.

# DA-T003H Plan

Date: `2026-06-17`

Ticket: `DA-T003H - Human Rust/Cargo availability gate`

Role: Context Curator + Planner

No NullForge implementation code has started.

## Objective

Plan a docs-only source document that records the human-gated Rust/Cargo availability action needed before DA-T003 can resume.

DA-T003H implementation, when separately authorized, should create a human action checklist/record source document only. It must not install Rust/Cargo, repair PATH, rerun toolchain probes, create app files, modify package config, run dependency commands, run Tauri/Node/Rust app commands, or resume DA-T003 implementation.

## Planned Implementation Target

The DA-T003H implementor should create:

```text
docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md
```

This document should become the repo-local source for the human-only availability gate. It should not be treated as toolchain availability proof, app scaffold proof, or DA-T003 resume proof.

## Planned Source Document Requirements

The DA-T003H source document should include:

- ticket ID `DA-T003H`;
- purpose and scope;
- source authority list;
- DA-T003 HOLD summary;
- DA-T003R decision summary;
- exact blocker: `rustc` and `cargo` are unavailable on PATH;
- explicit no-code sentence: `No NullForge implementation code has started.`;
- no-scaffold boundary: no `apps/`, `apps/nullforge-desktop/`, `src-tauri/`, package file, lockfile, Rust, React, TypeScript, JavaScript, CSS, or HTML app file has been created;
- selected recommendation: human performs Rust/Cargo availability setup outside Codex, or a separate scoped plan changes DA-T003;
- human-only checklist fields for date, human actor, method category, PATH visibility note, and observed `rustc --version` / `cargo --version` outputs;
- explicit statement that DA-T003H does not run `rustc --version` or `cargo --version`;
- future DA-T003 resume boundary: the later resume ticket may verify `rustc --version` and `cargo --version` only after the human action is complete;
- fallback path: if the human does not approve Rust/Cargo availability work, changing the desktop stack or DA-T003 approach requires a separate scoped decision or ADR;
- stop conditions;
- non-proofs and excluded scope;
- QA-T005, DA-T001, DA-T002, DA-T003, and DA-T003R claim boundaries.

## Selected Recommendation To Record

DA-T003H should recommend this path:

1. Keep DA-T003 in `HOLD`.
2. Record that Rust/Cargo availability work is a human-only action outside Codex unless a later prompt explicitly authorizes environment work.
3. Have the human make `rustc` and `cargo` available on PATH for the shell context that Codex will use.
4. Have the human manually confirm outside Codex that `rustc --version` and `cargo --version` return version output.
5. Have the human provide the observed outputs or a short confirmation in the DA-T003H source document.
6. After the human action, use a separate DA-T003 resume ticket that first checks `rustc --version` and `cargo --version`.
7. Resume DA-T003 only if Rust/Cargo are already available and the DA-T003 allowed file/command boundary remains valid.
8. If Rust/Cargo cannot be made available or a non-Rust desktop route is desired, create a separate scoped planning/ADR ticket before changing the scaffold plan.

DA-T003H must not execute any step above. It only records the gate and checklist.

## Allowed Implementor Changes

The DA-T003H implementor may create or update only:

- `docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T003H/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003H/CHANGED_FILES.md`
- `reports/nullforge/DA-T003H/TEST_RESULTS.md`
- `reports/nullforge/DA-T003H/AUDITOR_PROMPT.md`

No other tracked files should change.

## Implementation Steps

1. Re-read the DA-T003H planner artifacts.
2. Re-read `docs/nullforge/CURRENT_STATUS.md`, `docs/nullforge/SOURCE_INDEX.md`, `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md`, `audits/nullforge/DA-T003/AUDIT_REPORT.md`, `audits/nullforge/DA-T003/FINDINGS.md`, and `audits/nullforge/DA-T003R/AUDIT_REPORT.md`.
3. Confirm the worktree state with `git status --short --untracked-files=all`.
4. Create `docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md` as a docs-only human action gate source.
5. Update `docs/nullforge/CURRENT_STATUS.md` to record DA-T003H implementation pending independent audit only.
6. Update `docs/nullforge/SOURCE_INDEX.md` with DA-T003H source and report links only after the files exist.
7. Create DA-T003H reports under `reports/nullforge/DA-T003H/`.
8. Run all required checks in `ACCEPTANCE.md`.
9. Do not commit unless separately instructed.

## Forbidden Work

The DA-T003H implementor must not:

- install Rust/Cargo;
- run `rustup`;
- run `cargo install`;
- repair PATH or environment variables;
- run `rustc --version`;
- run `cargo --version`;
- run `node`, `pnpm`, Tauri, package-manager, dependency, install, build, app, bridge, sidecar, runtime, ResearchCore Engine, Python CLI, test, docs build, quickstart, or CI commands;
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

If DA-T003H implementation creates the human gate source document, `CURRENT_STATUS.md` should:

- keep `No NullForge implementation code has started.`;
- record DA-T003H as implemented and pending independent audit;
- keep DA-T003 blocked until a human-approved action makes `rustc` and `cargo` available on PATH or a separate scoped plan changes DA-T003;
- preserve that no app scaffold or app files have been created.

`SOURCE_INDEX.md` should add links only for DA-T003H files that exist.

## Checks To Require

DA-T003H implementation must run:

- `git status --short --untracked-files=all`
- `git diff --name-only`
- `git diff --check`
- required path/content/forbidden-path checks from `ACCEPTANCE.md`

The implementor must not run Rust/Cargo, Node, pnpm, Tauri, package-manager, dependency, app, bridge, sidecar, runtime, ResearchCore Engine, Python CLI, install, or environment repair commands.

## Risk Controls

- Treat DA-T003 audit `HOLD` as the blocker authority.
- Treat DA-T003R audit `PASS` as the decision-source authority.
- Keep DA-T003H docs-only.
- Keep app scaffold creation deferred.
- Keep Rust/Cargo installation and PATH repair outside Codex unless a later human-approved scoped ticket explicitly permits it.
- Do not convert a human gate record into toolchain availability proof.
- Require separate human direction before DA-T003 resume.

## Done Definition

DA-T003H implementation is done when:

- `docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md` exists and records the human-only Rust/Cargo availability gate;
- status/source navigation is bounded and audit-pending;
- DA-T003H reports exist;
- required content checks pass;
- absent app/package/toolchain path checks pass;
- forbidden tracked-path diff check returns no output;
- no Rust/Cargo install, PATH repair, environment repair, Rust/Cargo probe, app scaffold, dependency work, runtime command, bridge work, sidecar work, or downstream work is introduced;
- no broader proof is claimed.

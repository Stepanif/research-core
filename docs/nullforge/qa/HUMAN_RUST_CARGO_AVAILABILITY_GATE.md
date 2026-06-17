# NullForge Human Rust/Cargo Availability Gate

Date: `2026-06-17`

Ticket: `DA-T003H`

Status: Complete; audit `PASS`.

No NullForge implementation code has started.

## Purpose

This document records the human-only Rust/Cargo availability gate required before DA-T003 can resume.

DA-T003H is docs-only human gate recording. It is not Rust/Cargo installation, PATH repair, environment repair, toolchain verification, DA-T003 resume, app scaffold creation, package configuration, dependency resolution, Tauri launch proof, bridge implementation, sidecar work, or runtime behavior.

## Source Authority

This document is derived from:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md`
- `audits/nullforge/DA-T003/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003/FINDINGS.md`
- `audits/nullforge/DA-T003/REPAIR_PROMPT.md`
- `audits/nullforge/DA-T003R/AUDIT_REPORT.md`
- `audits/nullforge/DA-T003R/FINDINGS.md`
- `reports/nullforge/DA-T003/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T003/CHANGED_FILES.md`
- `reports/nullforge/DA-T003/TEST_RESULTS.md`
- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
- `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`
- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `docs/nullforge/architecture/TAURI_SCAFFOLD_PLAN.md`

`audits/nullforge/DA-T003/AUDIT_REPORT.md` and `audits/nullforge/DA-T003/FINDINGS.md` are the direct DA-T003 blocker authority.

`docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md` and `audits/nullforge/DA-T003R/AUDIT_REPORT.md` are the DA-T003R decision authority.

## DA-T003 HOLD Summary

DA-T003 attempted the first minimal launch-only Windows/Tauri shell scaffold implementation and stopped before scaffold creation at the required Rust/Cargo toolchain gate.

The blocker is:

- `rustc` is unavailable on PATH.
- `cargo` is unavailable on PATH.

DA-T003 audit decision is `HOLD`.

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

DA-T003 did not run dependency install, Tauri, app launch, bridge, sidecar, ResearchCore Engine, environment repair, or downstream implementation commands.

## DA-T003R Decision Summary

DA-T003R completed with audit `PASS` and created only a docs-only Rust/Cargo toolchain availability decision source.

DA-T003R did not install Rust/Cargo, repair PATH, repair environment state, rerun Rust/Cargo probes, prove Rust/Cargo availability, resume DA-T003, create an app scaffold, create package/dependency artifacts, or prove runtime behavior.

DA-T003R selected the path that DA-T003 remains blocked until one of these separately authorized paths occurs:

1. A human-approved action makes `rustc` and `cargo` available on PATH.
2. A separate scoped planning or ADR ticket changes the DA-T003 plan.

## Human-Only Gate Decision

The selected DA-T003H gate is:

1. Keep DA-T003 in `HOLD`.
2. Require a human-only Rust/Cargo availability action outside Codex before DA-T003 can resume, unless a separate scoped plan changes DA-T003.
3. Have the human make `rustc` and `cargo` available on PATH for the shell context that Codex will use.
4. Have the human manually confirm outside Codex that both commands return version output.
5. Record the human action evidence in this source document or a later bounded status update.
6. Start a separate DA-T003 resume ticket only after human confirmation exists.

DA-T003H does not execute the human action and does not prove Rust/Cargo availability.

## Human Action Checklist

This table is a record template. The DA-T003H implementation does not fill it with proof.

| Field | Human-provided value |
|---|---|
| Human action date | Not recorded by DA-T003H implementation. |
| Human actor or approver | Not recorded by DA-T003H implementation. |
| Method category | Not recorded by DA-T003H implementation. Expected categories: new Rust installation, existing local installation made visible, PATH visibility update, or separate plan change. |
| Trusted source or local toolchain note | Not recorded by DA-T003H implementation. |
| PATH visibility note for Codex shell | Not recorded by DA-T003H implementation. |
| Fresh shell/session note | Not recorded by DA-T003H implementation. |
| Human-observed `rustc --version` output | Not recorded by DA-T003H implementation. |
| Human-observed `cargo --version` output | Not recorded by DA-T003H implementation. |
| Human confirmation that no app scaffold was created by this action | Not recorded by DA-T003H implementation. |
| Human decision if Rust/Cargo cannot be made available | Not recorded by DA-T003H implementation. |

The `rustc --version` and `cargo --version` entries above are human-recorded external observations only. They are not commands run by DA-T003H and are not DA-T003H execution proof.

## DA-T003V Human Evidence Entry

Date/time of human action: `2026-06-17 2:28 PM ET`

Actor/approver: `Filip Stepanian / project owner / human approver`

Method category: Human local PowerShell verification on Windows 11 x64 from `C:\Users\Filip\Desktop\Repos\research-core`.

PATH visibility note for Codex shell:

```text
Human PowerShell could not resolve rustc or cargo via PATH. where.exe rustc and where.exe cargo returned "INFO: Could not find files for the given pattern(s)." rustc --version and cargo --version both failed because the commands were not recognized. Codex shell PATH visibility should not be assumed. DA-T003V should be treated as HOLD/BLOCKED for Rust toolchain verification until Rust/PATH setup is handled through an approved human-gated setup step or a scoped follow-up ticket. No install, dependency change, Tauri scaffold, package creation, or app setup is authorized by this verification record.
```

Human-observed `rustc --version` output:

```text
rustc : The term 'rustc' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:8 char:1
+ rustc --version
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (rustc:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

Human-observed `cargo --version` output:

```text
cargo : The term 'cargo' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:9 char:1
+ cargo --version
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (cargo:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

Human confirmation that no app scaffold/package files were created:

```text
Confirmed by human local PowerShell after DA-T003V verification commands: no app scaffold/package files were detected. The checked paths all returned False:

- src-tauri: False
- package.json: False
- package-lock.json: False
- pnpm-lock.yaml: False
- yarn.lock: False
- bun.lockb: False
- vite.config.ts: False
- vite.config.js: False
- apps\nullforge: False
- apps\desktop: False
- packages\nullforge: False
- packages\desktop: False

git status --short printed no changes before or after the verification commands, so the repo appeared clean from this PowerShell output.
```

DA-T003V records negative human evidence only. It does not prove Rust/Cargo availability and does not unblock DA-T003. DA-T003 remains blocked until a separate human-approved setup action makes `rustc` and `cargo` available on PATH and a later scoped DA-T003 resume ticket independently verifies `rustc --version` and `cargo --version`, or until a separate scoped plan changes DA-T003.

DA-T003V audit closeout status:

- `audits/nullforge/DA-T003V/AUDIT_REPORT.md` records `Decision: PASS`.
- DA-T003V remains historical negative human evidence from before DA-T003S setup.
- DA-T003S later setup evidence does not contradict DA-T003V and is not DA-T003 resume proof.

## Future DA-T003 Resume Boundary

A later DA-T003 resume ticket may check:

- `rustc --version`
- `cargo --version`

Those checks belong only to a later scoped DA-T003 resume prompt after the human action is complete. DA-T003H does not run them.

If either command is still unavailable during a later DA-T003 resume, that ticket must stop again and record renewed blocker evidence. It must not install or repair Rust/Cargo unless a separate scoped ticket explicitly permits that environment work.

## Alternative Path

If Rust/Cargo cannot be made available, or if a non-Rust desktop route is desired, the next step is a separate scoped planning or ADR ticket.

That later ticket must decide whether to:

- change the DA-T003 prerequisite;
- change the desktop scaffold approach;
- revisit the ADR-T001 Tauri + React/TypeScript stack direction;
- defer the desktop scaffold until local prerequisites are ready.

DA-T003H does not change the desktop stack direction.

## Stop Conditions

Any DA-T003H implementor or follow-on repair attempt must stop if the work would require:

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

DA-T003R proves only a docs-only Rust/Cargo toolchain availability decision source.

DA-T003H proves only a docs-only human Rust/Cargo availability gate source. It does not prove Rust/Cargo availability, PATH correctness, app scaffold creation, package/dependency readiness, Tauri launch behavior, bridge command behavior, sidecar behavior, runtime behavior, or public release readiness.

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

## Next Action After DA-T003V Audit PASS

After DA-T003V audit `PASS`, human direction is still needed before any DA-T003 resume, app scaffold creation, dependency work, runtime command, bridge implementation, sidecar work, ADR-T003, DA-T004, WB-T001, MB-T002, or downstream M1 work.

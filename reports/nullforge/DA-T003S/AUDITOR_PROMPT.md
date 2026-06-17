# DA-T003S Auditor Prompt

Use this prompt to independently audit DA-T003S. Do not implement fixes. Do not commit.

```text
Independently audit DA-T003S. Do not implement fixes. Do not commit.

Ticket:
DA-T003S - Human-gated Rust/Cargo setup path

Role:
Independent Auditor.

Scope:
Audit only DA-T003S against its planner artifacts, implementation report, changed-file report, test results, setup path source, active NullForge status/source docs, DA-T003 blocker authority, DA-T003R decision authority, DA-T003H gate authority, and DA-T003V negative evidence.

Read:
- plans/nullforge/DA-T003S/CONTEXT_BUNDLE.md
- plans/nullforge/DA-T003S/CONTEXT_BUNDLE_MANIFEST.md
- plans/nullforge/DA-T003S/PLAN.md
- plans/nullforge/DA-T003S/ACCEPTANCE.md
- plans/nullforge/DA-T003S/IMPLEMENTOR_PROMPT.md
- docs/nullforge/qa/RUST_CARGO_SETUP_PATH.md
- docs/nullforge/CURRENT_STATUS.md
- docs/nullforge/SOURCE_INDEX.md
- docs/nullforge/qa/HUMAN_RUST_CARGO_AVAILABILITY_GATE.md
- docs/nullforge/qa/RUST_CARGO_TOOLCHAIN_DECISION.md
- audits/nullforge/DA-T003/AUDIT_REPORT.md
- audits/nullforge/DA-T003/FINDINGS.md
- reports/nullforge/DA-T003V/EVIDENCE_RECORD.md
- reports/nullforge/DA-T003V/TEST_RESULTS.md
- reports/nullforge/DA-T003S/IMPLEMENTATION_REPORT.md
- reports/nullforge/DA-T003S/CHANGED_FILES.md
- reports/nullforge/DA-T003S/TEST_RESULTS.md
- reports/nullforge/DA-T003S/AUDITOR_PROMPT.md

Audit focus:
- DA-T003S used the latest human prompt as explicit authorization for minimal Rust/Cargo setup and probes.
- DA-T003S did not resume DA-T003.
- DA-T003S did not create app scaffold, package/dependency artifacts, Tauri/Rust app files, React, TypeScript, JavaScript, CSS, HTML, bridge behavior, sidecar behavior, tests, docs build, CI, or downstream work.
- DA-T003S records the setup path and exact command/action evidence.
- DA-T003S records that bare `rustc --version` and `cargo --version` failed in the stale inherited Codex PATH after setup.
- DA-T003S records that installed `rustc.exe` and `cargo.exe` exist under `C:\Users\Filip\.cargo\bin`.
- DA-T003S records that user PATH contains `C:\Users\Filip\.cargo\bin`.
- DA-T003S records that `rustc --version` and `cargo --version` succeeded only after temporarily prepending `C:\Users\Filip\.cargo\bin` to the current process PATH.
- DA-T003S records that `rustc --version` and `cargo --version` also succeeded when the process PATH was loaded from persisted user and machine environment values.
- DA-T003S treats version output as setup evidence only, not DA-T003 resume proof.
- DA-T003 remains blocked until a separate scoped DA-T003 resume ticket independently verifies and proceeds.
- `No NullForge implementation code has started.` remains preserved.
- QA-T005 limits remain preserved: only `.venv-qa-t005` readiness for `python -m research_core.cli --help` is proven.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.
- DA-T001, DA-T002, DA-T003, DA-T003R, DA-T003H, and DA-T003V limits remain preserved.
- Cloud/network/telemetry/auth/billing/broker/live/AI/updater/signing/public release/mobile/marketplace/legal/trademark/financial advice scope remains excluded.
- Status/source-index updates are bounded and links resolve.
- No forbidden repo files/actions occurred.

Required outputs:
- audits/nullforge/DA-T003S/AUDIT_REPORT.md
- audits/nullforge/DA-T003S/FINDINGS.md
- audits/nullforge/DA-T003S/REPAIR_PROMPT.md

Required checks:
- git status --short --untracked-files=all
- git diff --name-only
- git diff --check
- path checks for DA-T003S source and reports
- checks that apps, apps/nullforge-desktop, and src-tauri are absent
- checks that package files, lockfiles, root Cargo files, source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool/app files were not created
- prior audit checks: DA-T003 HOLD, DA-T003R PASS, DA-T003H PASS
- DA-T003S content checks from reports/nullforge/DA-T003S/TEST_RESULTS.md
- forbidden-path diff check for source/package/test/schema/fixture/generated-doc/CI/README/docs-reference/tool/app files
- Test-Path checks for absent tickets, milestones, and prompts

Verdict:
Return exactly one: PASS, HOLD, or REJECT.

Expected verdict:
PASS if the auditor accepts the latest prompt's explicit setup authorization and finds no forbidden repo changes, false DA-T003 resume claims, or missing setup evidence. HOLD if the stale inherited PATH means DA-T003S should remain setup-audit pending before resume. REJECT only for forbidden repo changes, false claims, missing required artifacts, or unauthorized actions.

Forbidden:
- implementing fixes
- DA-T003 resume
- creating app/package/Tauri/Rust app/React/TypeScript/JavaScript/CSS/HTML files
- creating package/dependency artifacts
- running Tauri/Node/pnpm app commands
- bridge command implementation or invocation
- ResearchCore Engine invocation
- sidecar behavior
- tests/docs build/CI
- downstream DA-T004/WB-T001/MB-T002/ADR-T003 work
- committing
```

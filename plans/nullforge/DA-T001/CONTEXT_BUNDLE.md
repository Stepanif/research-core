# DA-T001 Context Bundle

Date: `2026-06-17`

Ticket: `DA-T001`

Title: Desktop bridge contract finalization

Role: Context Curator

Status: Ready for planner

No NullForge implementation code has started.

## Ticket Summary

DA-T001 is the next human-selected scoped NullForge ticket after QA-T005 closeout.

The ticket prepares a docs-only implementation pass to convert the Volume 3 bridge draft into a repo-local desktop bridge contract source document. DA-T001 must not create Tauri, Rust, React, Python bridge, sidecar, package, dependency, schema, test, CI, fixture, generated-doc, or app implementation changes.

## Mission Slice

Create the minimum active context needed for a planner and later implementor to produce a bounded bridge contract document, likely:

```text
docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md
```

The future contract should define a narrow, allowlisted, structured command protocol for a future NullForge desktop bridge around ResearchCore Engine. It must distinguish planned bridge command IDs from currently proven engine commands and must not claim bridge behavior has been implemented.

## Current Repo State

- Branch baseline was clean after commit `b75de1a Close out QA-T005 environment readiness`.
- `docs/nullforge/CURRENT_STATUS.md` says QA-T005 is complete with audit `PASS` and human direction is required for the next scoped ticket.
- The human selected `DA-T001` in this prompt.
- M0 source import and readiness tickets through QA-T005 have audit `PASS`.
- No NullForge implementation code has started.

## Active Source Docs

| Source | Why It Matters |
|---|---|
| `docs/nullforge/CURRENT_STATUS.md` | Current phase, gates, no-code claim, QA-T005 readiness boundary. |
| `docs/nullforge/SOURCE_INDEX.md` | Active source navigation and existing artifact links. |
| `docs/nullforge/DECISION_LEDGER.md` | Accepted decisions NF-D0001 through NF-D0005; pending NF-D0006. |
| `docs/nullforge/ARCHIVE_POLICY.md` | Source authority, archive, quarantine, and prompt policy. |
| `docs/nullforge/codex/CODEX_ROLE_LOOP.md` | Required role-loop outputs, stop conditions, docs-only rules, human gates. |
| `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md` | Working name, Windows 11 x64 first, Tauri + React/TypeScript direction, ResearchCore Engine sidecar / scoped command bridge boundary. |
| `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md` | Local-first/no-cloud MVP boundary and human gates. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md` | Primary bridge contract draft, command protocol, allowlist, forbidden behaviors, workspace, logging, permissions, and bridge proof tests. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | DA-T001 backlog placement and M1 desktop bridge proof sequence. |
| `docs/nullforge/qa/COMMAND_DISCOVERY.md` | Existing command discovery and unsupported command shapes. |
| `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md` | Local package/CLI blocker context before repair execution. |
| `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md` | Human-gated repair options and non-goals. |
| `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md` | Recommended isolated venv readiness path. |
| `docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md` | QA-T005 isolated `.venv-qa-t005` execution proof and limits. |

## Prior Related Audits

The following audit reports were read as prior PASS evidence:

- `audits/nullforge/PF-T000/AUDIT_REPORT.md`
- `audits/nullforge/PF-T001/AUDIT_REPORT.md`
- `audits/nullforge/PF-T002/AUDIT_REPORT.md`
- `audits/nullforge/ADR-T001/AUDIT_REPORT.md`
- `audits/nullforge/ADR-T002/AUDIT_REPORT.md`
- `audits/nullforge/CX-T001/AUDIT_REPORT.md`
- `audits/nullforge/MB-T001/AUDIT_REPORT.md`
- `audits/nullforge/QA-T001/AUDIT_REPORT.md`
- `audits/nullforge/HY-T001/AUDIT_REPORT.md`
- `audits/nullforge/QA-T002/AUDIT_REPORT.md`
- `audits/nullforge/QA-T003/AUDIT_REPORT.md`
- `audits/nullforge/QA-T004/AUDIT_REPORT.md`
- `audits/nullforge/QA-T005/AUDIT_REPORT.md`

Relevant audit constraints:

- Existing ResearchCore Engine docs/code remain authoritative for current engine behavior.
- NullForge docs can plan the future bridge but cannot claim it exists.
- QA-T005 readiness proof is limited to `.venv-qa-t005`.
- `python -m research_core.cli --help` is the only validated command shape inside `.venv-qa-t005`.
- `python -m research_core --help` and `research-core --help` remain unsupported unless a later source/package ticket changes them.
- Additional environment repair, source/package entrypoint changes, full tests, docs build, CI smoke, desktop bridge/app work, and M1 implementation require separate scope and human approval.

## Relevant Repo Files And Folders

Read-only for DA-T001 planning:

- `pyproject.toml`
- `docs/reference/cli/overview.md`
- `docs/how-to/run_ci_locally.md`
- `src/research_core/cli.py`
- existing prior `plans/nullforge/*`, `reports/nullforge/*`, and `audits/nullforge/*`

Potential future implementor output paths:

- `docs/nullforge/architecture/ENGINE_BRIDGE_CONTRACT.md`
- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `reports/nullforge/DA-T001/IMPLEMENTATION_REPORT.md`
- `reports/nullforge/DA-T001/CHANGED_FILES.md`
- `reports/nullforge/DA-T001/TEST_RESULTS.md`
- `reports/nullforge/DA-T001/AUDITOR_PROMPT.md`

Planner outputs for this prompt:

- `plans/nullforge/DA-T001/CONTEXT_BUNDLE.md`
- `plans/nullforge/DA-T001/CONTEXT_BUNDLE_MANIFEST.md`
- `plans/nullforge/DA-T001/PLAN.md`
- `plans/nullforge/DA-T001/ACCEPTANCE.md`
- `plans/nullforge/DA-T001/IMPLEMENTOR_PROMPT.md`

## Bridge Contract Requirements From Volume 3

The future `ENGINE_BRIDGE_CONTRACT.md` should cover at least:

- contract authority and non-proof status;
- request object fields such as `request_id`, `bridge_version`, `command_id`, `workspace_path`, `inputs`, `output_mode`, `timeout_ms`, and `dry_run`;
- response object fields such as `status`, `exit_code`, `duration_ms`, `engine`, `artifacts`, `warnings`, and `errors`;
- bounded error response structure;
- required bridge fields and status values;
- candidate bridge command IDs from Volume 3, marked planned unless implementation evidence exists;
- explicit command allowlist policy;
- no arbitrary shell string acceptance;
- no user-provided script execution;
- no silent dependency install or environment mutation;
- no broad folder/drive scanning;
- selected workspace path validation and workspace-relative artifact paths;
- bounded stderr/UI error behavior and local log policy;
- Tauri permission stance: deny by default, expand only through scoped ticket/audit;
- network/cloud/updater/telemetry/broker/live/AI/public release exclusions;
- human gates and stop conditions for any later bridge expansion.

## M1 Sequence Context From Volume 7

Volume 7 places DA-T001 in M1 after QA-T001/readiness work and before any shell scaffold:

```text
DA-T001 - Desktop bridge contract finalization
DA-T002 - Tauri app scaffold plan
DA-T003 - Tauri shell smoke implementation
DA-T004 - Engine command bridge smoke
WB-T001 - Artifact metadata read-only viewer
MB-T002 - Desktop bridge proof audit/handoff
```

DA-T001 must therefore produce a contract suitable for DA-T002 and DA-T004, without implementing those later tickets.

## Constraints

- Preserve `No NullForge implementation code has started.`
- Keep DA-T001 docs-only.
- Do not edit ResearchCore Engine source, tests, schemas, package metadata, CLI docs, generated references, CI, tools, README, or dependencies.
- Do not run install commands, full tests, docs generation, docs build, quickstart commands, CI smoke, Tauri commands, Node/Rust commands, Python bridge execution, sidecar execution, or app commands.
- Do not create `tickets`, `milestones`, `prompts`, app scaffolds, bridge code, sidecar code, package files, fixtures, raw/private data, or generated docs.
- Do not create audits during planning.
- Do not claim Tauri feasibility, bridge reliability, packaging feasibility, no-cloud enforcement, telemetry blocking, product validation, trading validity, financial advice safety, public release safety, or legal/trademark clearance.

## Required Checks

For this planner pass:

- `git status --short --untracked-files=all`
- `git diff --check`
- path existence checks for the five DA-T001 planner artifacts
- prerequisite audit `Decision: PASS` checks through QA-T005
- content checks for DA-T001, bridge contract target, no-code sentence, allowlist boundary, arbitrary shell prohibition, and cloud/network/broker/live exclusions

Future implementor checks should be docs-only and should not execute bridge/app/runtime behavior.

## Human Gate Triggers

Stop and request human direction before:

- any code implementation;
- any Tauri/Rust/React/Node/Python bridge/sidecar/app scaffold;
- any dependency or package metadata change;
- any source/test/schema/fixture/generated-doc/CI change;
- any environment mutation or install command;
- any command allowlist expansion beyond the contract;
- any arbitrary shell, broad filesystem, network, updater, telemetry, broker/live, AI/model, cloud/auth/billing, public release, or signing scope;
- any attempt to change current ResearchCore Engine command behavior;
- any raw/full ES.zip, private/local data, generated dataset, or ES-derived fixture handling.

## Excluded Context

- External incoming package files remain non-authoritative unless later imported by scoped audit.
- Prompt files, old chats, and raw package prompts are not active truth.
- Full ES.zip, private/local data, generated datasets, and ES-derived fixtures are excluded.
- Broad engine internals beyond source facts needed for bridge contract wording are excluded.
- M2 and later product feature details are excluded except where they reinforce anti-goals and gates.

## Open Questions

- Which exact bridge command ID should DA-T004 use first if no structured `engine.version` or `engine.doctor` command exists yet?
- Should DA-T001 contract define a planned `engine.version` command, a planned `engine.doctor` command, or a temporary dev smoke adapter around the currently validated `python -m research_core.cli --help` shape?
- Should a later source/package ticket add a structured ResearchCore Engine doctor/version command before DA-T004?
- Should DA-T001 update status/source index during implementation, or should closeout handle that after audit? The planner should choose a bounded convention.

## Ready For Planner Verdict

Ready for planner.

DA-T001 has enough active context to plan a docs-only bridge contract implementation. The planner must keep implementation, runtime execution, dependencies, and environment changes out of scope.

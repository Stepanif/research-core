# NullForge Engine Bridge Contract

Date: `2026-06-17`

Ticket: `DA-T001`

Status: DA-T001 complete with independent audit `PASS`.

No NullForge implementation code has started.

## Authority And Scope

This document defines the planned NullForge desktop bridge contract for future M1 work.

It is a docs-only contract source derived from:

- `docs/nullforge/adr/ADR-T001-name-platform-stack-engine.md`
- `docs/nullforge/adr/ADR-T002-local-first-no-cloud-mvp.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_03_Windows_Tauri_Desktop_Architecture_ResearchCore_Engine_Bridge_Sidecar_Contract_Packaging_Spike_v0_4.md`
- `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_EXECUTION.md`
- `audits/nullforge/QA-T005/AUDIT_REPORT.md`

Existing ResearchCore Engine docs, code, package metadata, schemas, tests, CLI behavior, and generated references remain authoritative for current engine behavior.

DA-T001 does not implement a desktop shell, Tauri command, Rust bridge, React UI, Python bridge, sidecar, package config, dependency, test, schema, fixture, CI change, generated doc, or runtime behavior. It does not prove Tauri feasibility, bridge reliability, sidecar feasibility, packaging feasibility, no-cloud technical enforcement, telemetry blocking, product validation, market validation, trading validity, financial advice safety, legal/trademark clearance, or public distribution safety.

## Contract Purpose

The future bridge is the boundary between a local NullForge desktop shell and the existing ResearchCore Engine.

The bridge must be:

- allowlisted;
- structured;
- workspace-scoped;
- auditable;
- narrow enough for M1 proof work;
- explicit about failures and non-proofs;
- not arbitrary shell execution.

The bridge contract is a protocol for future implementation tickets. It is not a claim that any command, app, sidecar, or Tauri permission currently exists.

## Non-Goals

DA-T001 does not authorize:

- Tauri, Rust, React, TypeScript, JavaScript, Python bridge, sidecar, or app implementation;
- ResearchCore Engine command behavior changes;
- package metadata or CLI entrypoint changes;
- install, uninstall, dependency sync, package build, or environment mutation;
- full tests, docs generation, docs build, quickstart commands, CI smoke, bridge smoke, sidecar smoke, or app runtime commands;
- raw/full ES.zip handling, private/local data import, generated datasets, or ES-derived fixtures;
- network, cloud, telemetry, auth, billing, marketplace, mobile, broker/live, AI/model, updater, signing, public release, legal/trademark, or financial advice scope.

## Proven Local Readiness Boundary

QA-T005 proves only the following bounded readiness facts:

- `research-core` can be installed editable into `.venv-qa-t005`;
- `research_core` and `research_core.cli` are import-visible inside `.venv-qa-t005`;
- `python -m research_core.cli --help` runs inside `.venv-qa-t005`.

QA-T005 does not prove:

- active/global Python environment correctness;
- full test suite pass status;
- docs build success;
- CI smoke success;
- Tauri or sidecar behavior;
- bridge command behavior;
- packaged app behavior.

The command shapes below remain unsupported unless a later source/package ticket changes them:

- `python -m research_core --help`
- `research-core --help`

## Contract Principles

| Principle | Requirement |
|---|---|
| Allowlist first | A request must use a known `command_id`; raw shell strings are never accepted. |
| Structured inputs | UI input is converted into typed fields, not concatenated into commands. |
| Workspace scope | Reads and writes are limited to the selected local workspace unless a later human-gated ticket expands scope. |
| Bounded output | UI receives structured status, artifact metadata, warnings, and bounded error excerpts. |
| Local-first | The MVP bridge requires no cloud, hosted backend, account/auth, telemetry, billing, marketplace, mobile, broker/live, AI/model, or network behavior. |
| Deny by default | Filesystem, process, updater, network, and storage permissions begin closed and expand only through scoped ticket/audit. |
| Engine preservation | The bridge must not rewrite ResearchCore Engine internals for UI convenience. |
| No proof inflation | Planned command IDs and contract shapes must not be described as implemented behavior. |

## Request Object

A future bridge request should use a JSON-compatible object with these fields.

| Field | Required | Type | Rule |
|---|---:|---|---|
| `request_id` | Yes | string | Unique ID for correlating UI action, bridge log, engine run, and artifacts. |
| `bridge_version` | Yes | string | Contract version, starting at `0.1` for future proof tickets. |
| `command_id` | Yes | string | Must match the active allowlist. |
| `workspace_path` | Yes | string | Selected local workspace path, validated before command execution. |
| `inputs` | Yes | object | Structured arguments only; no shell fragments or executable scripts. |
| `output_mode` | Yes | string | Initial planned value: `json`. |
| `timeout_ms` | Yes | integer | Required timeout for any future process execution. |
| `dry_run` | Yes | boolean | Allows future validation without mutation where supported. |

Example contract shape:

```json
{
  "request_id": "run-or-ui-event-id",
  "bridge_version": "0.1",
  "command_id": "engine.doctor",
  "workspace_path": "<selected-workspace>",
  "inputs": {},
  "output_mode": "json",
  "timeout_ms": 30000,
  "dry_run": false
}
```

The example is a contract example only. It is not proof that `engine.doctor` currently exists.

## Response Object

A future successful or blocked bridge response should use a JSON-compatible object with these fields.

| Field | Required | Type | Rule |
|---|---:|---|---|
| `request_id` | Yes | string | Must match the request. |
| `bridge_version` | Yes | string | Contract version used by the bridge. |
| `status` | Yes | string | One of `OK`, `ERROR`, `TIMEOUT`, `CANCELLED`, or `BLOCKED`. |
| `command_id` | Yes | string | Echoes the allowlisted command ID. |
| `exit_code` | When process ran | integer or null | Captured only when a process is actually executed. |
| `duration_ms` | Yes | integer | Wall-clock duration for bridge handling. |
| `engine` | Yes | object | Engine label, version if known, and mode such as `dev` or `sidecar`. |
| `artifacts` | Yes | array | Workspace-relative artifact metadata; can be empty. |
| `warnings` | Yes | array | Structured warning strings or objects; can be empty. |
| `errors` | Yes | array | Structured errors; can be empty for `OK`. |

Example contract shape:

```json
{
  "request_id": "run-or-ui-event-id",
  "bridge_version": "0.1",
  "status": "OK",
  "command_id": "engine.doctor",
  "exit_code": 0,
  "duration_ms": 523,
  "engine": {
    "name": "ResearchCore Engine",
    "version": "unknown-until-implemented",
    "mode": "dev-or-sidecar"
  },
  "artifacts": [],
  "warnings": [],
  "errors": []
}
```

## Error Response Rules

Errors must be explicit and bounded.

| Field | Required | Rule |
|---|---:|---|
| `code` | Yes | Stable error code such as `COMMAND_NOT_ALLOWLISTED`, `ENGINE_UNAVAILABLE`, `TIMEOUT`, or `WORKSPACE_INVALID`. |
| `message` | Yes | Human-readable summary suitable for the UI. |
| `stderr_excerpt` | If available | Bounded excerpt only; never unbounded stderr in UI. |
| `repair_hint` | If useful | Safe next action; no automatic install or mutation. |
| `log_path` | If written | Workspace-relative path only. |

Example contract shape:

```json
{
  "request_id": "run-or-ui-event-id",
  "bridge_version": "0.1",
  "status": "ERROR",
  "command_id": "engine.doctor",
  "exit_code": 2,
  "duration_ms": 812,
  "errors": [
    {
      "code": "ENGINE_COMMAND_FAILED",
      "message": "ResearchCore Engine command failed.",
      "stderr_excerpt": "bounded stderr excerpt",
      "repair_hint": "Check the local engine environment selected for this workspace."
    }
  ],
  "artifacts": [],
  "warnings": []
}
```

## Candidate Command Allowlist

The initial allowlist is a planned contract surface. These command IDs are not implemented by DA-T001.

| Command ID | Status | Mutates Workspace | Purpose | Notes |
|---|---|---:|---|---|
| `engine.version` | Planned candidate, not implemented | No | Return engine label/version/environment metadata. | Requires later proof or source/package support. |
| `engine.doctor` | Planned candidate, not implemented | Optional report only | Check that the engine can run and report basic health. | Requires later proof or source/package support. |
| `workspace.inspect` | Planned candidate, not implemented | No | Confirm selected workspace manifest and expected folders. | May be app/bridge-owned rather than engine-owned. |
| `fixture.smoke` | Planned candidate, not implemented | Yes | Run one tiny approved fixture smoke and write a bounded report. | Requires later fixture policy and approved fixture. |
| `artifact.scan` | Planned candidate, not implemented | No | Return workspace-relative artifact metadata. | Must not scan outside selected workspace. |
| `engine.cli_help_smoke` | Optional DA-T004 candidate, not implemented | No | Wrap the currently proven `python -m research_core.cli --help` shape as a temporary dev smoke. | Requires later human approval because CLI help is not structured engine output. |

Any future command not listed here requires a later scoped ticket and human review before implementation.

## First-Proof Selection Rule

DA-T004 or another future implementation ticket must choose exactly one first proof command before any bridge implementation starts.

Valid options are:

- implement or expose a structured `engine.version` or `engine.doctor` path through a scoped ticket;
- use a temporary, clearly labeled dev-only adapter around `python -m research_core.cli --help` inside `.venv-qa-t005`;
- defer bridge execution until a source/package ticket creates a safer structured command.

The first proof must not rely on:

- `python -m research_core --help`;
- `research-core --help`;
- arbitrary shell strings;
- unvalidated active/global Python environment state;
- full tests, docs build, quickstart, CI smoke, or unapproved runtime commands.

## Forbidden Bridge Behaviors

The bridge must not:

- accept arbitrary shell strings from UI, config, docs, or user input;
- concatenate user input into a process command;
- execute user-provided scripts;
- run commands outside the allowlist;
- silently install dependencies;
- silently mutate Python environments;
- scan arbitrary folders, parent directories, drives, or the repo;
- delete files outside the selected workspace;
- mutate repo source files from app runtime;
- commit or import full ES.zip;
- handle raw/private data without later approved policy;
- send datasets or artifacts to cloud services;
- add network behavior;
- add telemetry/analytics;
- add account/auth, billing, mobile, marketplace, updater, signing, or public release behavior;
- activate AI/model calls;
- activate broker/live trading or live execution;
- hide stderr, failed checks, or blocked commands;
- promote claims automatically.

## Workspace And Path Rules

The future bridge must operate against one selected local workspace.

Minimum path rules:

- validate and normalize `workspace_path` before use;
- reject path traversal;
- avoid scanning parent directories;
- use workspace-relative artifact paths in responses;
- record absolute local paths only in local workspace config when a later ticket explicitly allows it;
- do not log secrets, full private paths, or raw dataset contents unless later security review permits a bounded exception;
- do not assume the repo path is the workspace path.

Initial planned workspace-owned areas:

| Area | Planned Use |
|---|---|
| `logs/` | Bridge/app/engine logs, bounded and local. |
| `runs/` | Future smoke/run records. |
| `artifacts/` | Future artifact metadata and output indexes. |
| `datasets/fixtures/` | Later tiny approved fixture only. |

## Logging And Stderr Rules

The future bridge must keep logs local and bounded.

| Log | Planned Location | Allowed Contents | Exclusions |
|---|---|---|---|
| App/bridge log | `logs/nullforge-app.log` | lifecycle, allowlist decisions, non-sensitive errors | raw dataset contents, secrets, unbounded paths |
| Engine log | `logs/researchcore-engine.log` | command ID, request ID, bounded stderr | secrets, full ES data dump |
| Run log | `runs/<run_id>/run.log` | future smoke/run result | secrets, unbounded stderr in UI |

The UI may show a bounded stderr excerpt. Full local logs, when safe, remain in the workspace and are referenced with workspace-relative paths.

## Permission Boundary

Future Tauri or desktop permissions must be deny-by-default.

Initial planned permission categories:

| Capability | Default | Expansion Gate |
|---|---|---|
| Filesystem | Selected workspace-scoped read/write only | Human gate for broader import/reference behavior. |
| Shell/process | Allowlisted bridge commands only | Human gate for any command implementation or expansion. |
| Network | Off / not required | Human gate plus privacy/security review. |
| Updater/signing/public release | Off | Post-MVP release decision and legal review. |
| Telemetry/analytics | Off | Separate scoped decision; not MVP default. |
| Credential storage | Off | Separate security review. |

## Security And Privacy Gates

Human review is required before:

- adding dependencies;
- changing package metadata or CLI entrypoints;
- changing ResearchCore Engine command behavior;
- implementing any bridge command;
- adding filesystem, shell/process, network, updater, signing, telemetry, credential, broker/live, or AI/model permissions;
- using real ES.zip;
- committing data fixtures derived from ES.zip;
- changing workspace deletion or cleanup behavior;
- adding installer, public release, legal/trademark, financial advice, or distribution claims.

Security review is required before:

- arbitrary file import;
- external binary execution beyond the allowlist;
- large dataset import;
- workspace cleanup/delete features;
- credential or token storage;
- network access;
- plugin systems;
- auto-update.

## Later Test Expectations

Future implementation tickets should define exact commands. DA-T001 only defines test categories.

| Test Category | Purpose |
|---|---|
| Contract review | Confirm request/response/error fields are followed. |
| Allowlist negative test | Confirm unknown command IDs are blocked. |
| Arbitrary shell negative test | Confirm raw shell strings cannot run. |
| Workspace path test | Confirm reads/writes stay inside selected workspace. |
| Error handling test | Confirm missing engine, bad command, timeout, and invalid workspace are explicit. |
| Artifact metadata test | Confirm responses use workspace-relative artifact metadata. |
| Full ES.zip exclusion test | Confirm no raw/full ES.zip is used or committed. |
| Permission review | Confirm no broad filesystem, network, updater, telemetry, broker/live, or AI scope. |

Skipped tests must include precise reasons and cannot be treated as proof.

## Claim Boundaries

This contract does not prove:

- a desktop app exists;
- Tauri can run locally;
- Rust can invoke the engine safely;
- a Python sidecar can be packaged;
- any bridge command is implemented;
- workspace permissions are enforced;
- network/cloud/telemetry absence is technically enforced;
- artifact metadata can be displayed;
- product, user, market, trading, or financial-advice claims;
- public distribution, legal/trademark clearance, signing, or updater readiness.

Imported volumes remain design memory until scoped tickets produce audited source docs or implementation evidence.

## Open Questions For Later Tickets

- Should DA-T004 use a structured `engine.version`, `engine.doctor`, or temporary `engine.cli_help_smoke` command first?
- Should a source/package ticket add a structured ResearchCore Engine doctor/version command before DA-T004?
- What exact workspace manifest fields are needed before workspace inspection can be implemented?
- Should the future bridge invoke `.venv-qa-t005`, a new DA-scoped venv, or a packaged sidecar path?
- What minimal artifact metadata shape should WB-T001 display after DA-T004?

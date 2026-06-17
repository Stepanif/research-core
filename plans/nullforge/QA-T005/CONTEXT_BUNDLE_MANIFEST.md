# QA-T005 Context Bundle Manifest

Date: `2026-06-16`

Ticket: `QA-T005`

Role: Context Curator

Status: Ready for planner

No NullForge implementation code has started.

## Included Sources

| Source | Role in context |
|---|---|
| `docs/nullforge/CURRENT_STATUS.md` | Current NullForge phase, QA-T004 audit `PASS`, baseline marker, blockers, and gates. |
| `docs/nullforge/SOURCE_INDEX.md` | Repo-local active source index and QA-T004 artifact links. |
| `docs/nullforge/ARCHIVE_POLICY.md` | Active/archive/quarantine/prompt promotion policy and source authority boundaries. |
| `docs/nullforge/codex/CODEX_ROLE_LOOP.md` | Role-loop artifact expectations, PASS/HOLD/REJECT rules, human gates, and stop conditions. |
| `docs/nullforge/qa/COMMAND_DISCOVERY.md` | QA-T001 command surface, package metadata, and original local environment blocker discovery. |
| `docs/nullforge/qa/ENVIRONMENT_TRIAGE.md` | QA-T002 local environment and CLI/runtime blocker triage. |
| `docs/nullforge/qa/ENVIRONMENT_REPAIR_DECISION.md` | QA-T003 human-gated repair/readiness decision packet. |
| `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md` | QA-T004 recommended repair/readiness path packet. |
| `audits/nullforge/QA-T004/AUDIT_REPORT.md` | QA-T004 independent audit `PASS` and no-repair disposition. |
| `audits/nullforge/QA-T004/FINDINGS.md` | QA-T004 non-blocking finding that environment repair remains unresolved and human-gated. |
| `reports/nullforge/QA-T004/TEST_RESULTS.md` | QA-T004 bounded check results and skipped command classes. |
| `pyproject.toml` | Package metadata, src layout, dependencies, pytest config, and absence of console script. |
| `docs/how-to/run_ci_locally.md` | Existing install/test/docs/CI smoke command references; commands are context only and remain forbidden for curation. |
| `docs/reference/cli/overview.md` | Documented `python -m research_core.cli` CLI invocation. |
| `src/research_core/cli.py` | Existing Typer CLI module facts from read-only source inspection. |

## Read-Only Discovery Commands Used

- `git status --short --branch`
- `Get-Content -LiteralPath ...` for the listed source documents
- `rg -n "Decision: PASS" audits\nullforge\QA-T001\AUDIT_REPORT.md audits\nullforge\HY-T001\AUDIT_REPORT.md audits\nullforge\QA-T002\AUDIT_REPORT.md audits\nullforge\QA-T003\AUDIT_REPORT.md audits\nullforge\QA-T004\AUDIT_REPORT.md`
- `Test-Path -LiteralPath plans\nullforge\QA-T005`

No install, uninstall, editable install, dependency sync, package build, virtual-environment creation/activation, environment repair, test, docs generation, docs build, quickstart, CI smoke, post-repair CLI validation, or environment-changing command was run.

## Excluded Sources

| Source or class | Reason excluded |
|---|---|
| Full repository scan beyond listed sources | Not needed for bounded QA-T005 context curation. |
| `src/` implementation editing | Out of scope; source is read-only context only. |
| `tests/`, `schemas/`, `fixtures/` | Out of scope; no test/schema/fixture creation or execution. |
| `pyproject.toml` edits | Out of scope; package metadata changes require later human-gated ticket. |
| `.github/`, `README.md`, `docs/reference/`, `tools/` edits | Out of scope; context only. |
| `reports/nullforge/QA-T005/` | Forbidden for context curator. |
| `audits/nullforge/QA-T005/` | Forbidden for context curator. |
| `tickets/`, `milestones/`, `prompts/` | Forbidden for context curator. |
| Raw/private data and ES-derived fixtures | Gated and irrelevant to environment repair execution path curation. |
| Old chats, prompt archives, incoming package prompt files | Not active truth unless promoted by later audited ticket. |
| `ADR-T003`, desktop bridge/app, sidecar, package/release/public distribution work | Downstream and forbidden. |

## Archive And Design-Memory Handling

Imported NullForge volumes and prior ticket artifacts are design memory and workflow context only. They do not authorize implementation, package changes, environment repair, dependency changes, tests, generated docs, or downstream M1 work.

## Expiry And Refresh Rule

Refresh this context before planning if any of the following changes:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/qa/ENVIRONMENT_REPAIR_PATH.md`
- `pyproject.toml`
- `src/research_core/cli.py`
- active Python environment or editable install state
- QA-T004 audit disposition
- branch status

Do not refresh by running install, repair, full test, docs generation, docs build, quickstart, CI smoke, post-repair CLI validation, or environment-changing commands.

## Context Risks

- QA-T001 and QA-T002 diagnostics are local-environment observations, not portable truth.
- QA-T004 recommends isolated project-local virtual environment preparation, but that recommendation is not execution approval.
- The active environment may change after this context is created; the planner must decide whether later diagnostics are allowed and under what human gate.
- A future repair ticket may produce local paths in command output; the planner should require sanitization in reports.
- `python -m research_core.cli` is documented but was blocked locally; `research-core --help` and `python -m research_core --help` are separate unsupported command shapes.
- A later execution ticket can easily drift into package/source changes, tests, docs build, or CI smoke; QA-T005 planning must keep those classes explicitly authorized or forbidden.

## Curator Verdict

Ready for planner.

The planner should create bounded QA-T005 planning artifacts only and preserve the human gate for any environment mutation, validation command, or source/package change.

# QA-T001 Context Bundle Manifest

Date: `2026-06-16`

Ticket: `QA-T001`

Role: Context Curator

Curator verdict: `READY_FOR_PLANNER`

## Included Active NullForge Sources

| Source | Included reason | Authority boundary |
|---|---|---|
| `docs/nullforge/CURRENT_STATUS.md` | Current NullForge phase, gates, no-code sentence, and QA-T001 next-ticket state. | Active status; does not authorize implementation. |
| `docs/nullforge/SOURCE_INDEX.md` | Repo-local NullForge source map and pending downstream entries. | Active source navigation; only existing links are authoritative. |
| `docs/nullforge/DECISION_LEDGER.md` | Accepted decisions and pending source import state. | Accepted entries do not authorize implementation code. |
| `docs/nullforge/ARCHIVE_POLICY.md` | Archive, quarantine, prompt, and source-promotion rules. | Governs source authority boundaries. |
| `docs/nullforge/M0_HANDOFF.md` | M0 closeout, completed ticket list, and M1 readiness statement. | Handoff source after MB-T001 audit `PASS`; not implementation proof. |
| `docs/nullforge/codex/CODEX_ROLE_LOOP.md` | Context curator responsibilities and later planner/implementor/auditor rules. | Workflow source; not product implementation proof. |
| `audits/nullforge/MB-T001/AUDIT_REPORT.md` | Latest prerequisite audit disposition and human gate context. | Audit evidence for MB-T001 only. |
| `docs/nullforge/blueprint/volumes/NullForge_Volume_07_Roadmap_Milestones_Ticket_Backlog_Codex_Prompt_Packs_First_Execution_Batch_v0_4.md` | Names QA-T001 purpose, dependencies, command candidates, outputs, and blockers. | Planning source; downstream work still requires scoped role-loop execution. |

## Included Prerequisite Audit Evidence

| Source | Use |
|---|---|
| `audits/nullforge/PF-T000/AUDIT_REPORT.md` | Verify prerequisite `Decision: PASS`. |
| `audits/nullforge/PF-T001/AUDIT_REPORT.md` | Verify prerequisite `Decision: PASS`. |
| `audits/nullforge/PF-T002/AUDIT_REPORT.md` | Verify prerequisite `Decision: PASS`. |
| `audits/nullforge/ADR-T001/AUDIT_REPORT.md` | Verify prerequisite `Decision: PASS`. |
| `audits/nullforge/ADR-T002/AUDIT_REPORT.md` | Verify prerequisite `Decision: PASS`. |
| `audits/nullforge/CX-T001/AUDIT_REPORT.md` | Verify prerequisite `Decision: PASS`. |
| `audits/nullforge/MB-T001/AUDIT_REPORT.md` | Verify prerequisite `Decision: PASS`. |

## Included Repo Discovery Sources

| Source | Included reason | Notes |
|---|---|---|
| `pyproject.toml` | Python project metadata, dependencies, optional dev dependency, pytest config. | Existing metadata only; not edited. |
| `requirements-docs.txt` | Docs dependency list. | Existing dependency list only; not installed. |
| `README.md` | Top-level verification commands and repo structure. | Existing ResearchCore source; not edited. |
| `.github/workflows/research-ci.yml` | Current CI install/test/smoke commands. | Existing CI truth; not edited. |
| `.github/workflows/docs.yml` | Current docs-generation/build commands. | Existing CI truth; not edited. |
| `.github/ci/ci.github.json` | CI smoke config path identified by workflow. | Candidate read-only source for later planner. |
| `docs/how-to/run_ci_locally.md` | Local command mirror for CI and docs checks. | Existing docs source; not edited. |
| `docs/how-to/add_new_test_and_golden.md` | Existing smoke/determinism/golden test patterns. | Existing docs source; not edited. |
| `docs/how-to/add_new_cli_command.md` | Existing CLI and test/doc generation conventions. | Existing docs source; not edited. |
| `docs/getting-started/quickstart.md` | Existing sample CLI command flow. | Existing docs source; not edited. |
| `docs/reference/cli/overview.md` | Generated CLI root command list and usage. | Existing generated docs; not edited. |
| `docs/reference/cli/index.md` | Generated CLI reference index. | Existing generated docs; not edited. |
| `src/research_core/cli.py` | Source CLI command registration surface. | Read-only discovery target. |
| `tests/` | Existing test suite and patterns. | Read-only discovery target; no new tests. |
| `tests/fixtures/` | Existing sample fixtures. | Read-only discovery target; no fixture edits. |
| `tests/golden/` | Existing golden hash fixtures. | Read-only discovery target; no golden updates. |
| `tools/docs/` | Existing docs-generation scripts. | Read-only discovery target. |
| `schemas/` | Existing schema surface referenced by docs/tests. | Read-only discovery target. |

## Requested But Absent Inputs

These files were requested by the QA-T001 curator prompt but are absent in the current repo root:

- `package.json`
- `pnpm-workspace.yaml`
- `pnpm-lock.yaml`

The absence is material context for QA-T001. The repo currently presents as Python project metadata through `pyproject.toml`, not a root pnpm workspace.

## Excluded Sources And Actions

Excluded from active context or changes:

- old chats, prompt files, and incoming package prompts;
- incoming package milestone/ticket files not promoted into repo-local truth;
- archive/quarantine/private/local/raw data;
- raw/full ES.zip contents and ES-derived fixtures;
- app, Tauri, bridge, sidecar, installer, release, package, and public distribution paths;
- implementation code changes;
- package metadata changes;
- tests, schemas, fixtures, goldens, generated docs, and CI edits;
- `ADR-T003`, `DA-T001`, M1 implementation, and downstream work;
- install/build/test command execution during curation.

## Read-Only Discovery Commands Used

- `git status --short --branch`
- `rg -n` searches over required NullForge docs, Volume 07, repo docs, workflows, and CLI source.
- `rg --files` discovery for package metadata and command/test-related repo files.
- `Get-Content -LiteralPath` for required docs and selected repo metadata/docs.

No install, build, or test commands were run. No implementation commands were run.

One read-only `rg --files ... | rg ...` query required escalation because the Windows sandbox helper failed. It enumerated existing files only and did not modify the repo.

## Context Risks

- Volume 07 includes candidate commands that must be verified rather than assumed, including `python -m research_core --help` and `research-core --help`.
- Current generated CLI docs support `python -m research_core.cli ...`; no console script entrypoint was found in `pyproject.toml`.
- Running pytest or docs generation later may create local caches or generated outputs if not bounded.
- Dependency checks may reveal missing local packages such as `pyarrow` or missing editable install state.
- The repo has extensive existing tests and goldens; QA-T001 must avoid broad churn or hash updates.
- Root Node/pnpm files are absent; a planner should not assume pnpm commands unless later evidence appears.

## Expiry And Refresh Rule

Refresh this context before QA-T001 planning if any of these change:

- `docs/nullforge/CURRENT_STATUS.md`
- `docs/nullforge/SOURCE_INDEX.md`
- `docs/nullforge/M0_HANDOFF.md`
- `docs/nullforge/codex/CODEX_ROLE_LOOP.md`
- any prerequisite audit report;
- `pyproject.toml`;
- `requirements-docs.txt`;
- `.github/workflows/research-ci.yml`;
- `.github/workflows/docs.yml`;
- `README.md`;
- `docs/how-to/run_ci_locally.md`;
- `docs/reference/cli/`;
- `src/research_core/cli.py`;
- `tests/`;
- new package manager files such as `package.json`, `pnpm-workspace.yaml`, or lock files.

## Ready-For-Planner Verdict

`READY_FOR_PLANNER`.

The next QA-T001 role should be Planner only. It should create bounded planner artifacts and decide, explicitly, whether the later QA-T001 implementor may run commands or only document discovered command candidates.

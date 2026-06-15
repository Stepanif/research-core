# PF-T000 Conflicts And Gates

Ticket: PF-T000 - Repo inventory and NullForge import plan

## Human Gate Status

Human gates triggered during PF-T000 implementation: NONE.

No existing ResearchCore Engine docs were overwritten, moved, renamed, or edited. No code, tests, dependencies, CI, package metadata, generated docs, schemas, raw data, or volume contents were changed or imported.

## Confirmed Non-Conflicts

- `docs/nullforge/` did not exist before PF-T000 implementation.
- `docs/nullforge/import/` did not exist before PF-T000 implementation.
- `milestones/nullforge/` did not exist before PF-T000 implementation.
- `tickets/nullforge/` did not exist before PF-T000 implementation.
- `prompts/nullforge/` did not exist before PF-T000 implementation.
- `reports/nullforge/` did not exist before PF-T000 implementation.
- `audits/nullforge/` did not exist before PF-T000 implementation.
- A separated NullForge docs root can coexist with current ResearchCore docs without overwriting them.

## Source-Of-Truth Tensions

| Tension | Risk | PF-T000 handling |
|---|---|---|
| ResearchCore Engine docs already define current engine truth. | NullForge product docs could accidentally overwrite or contradict engine status/architecture. | Keep NullForge docs under `docs/nullforge/` and do not edit existing engine docs. |
| The role prompt referenced `tickets/nullforge/...`, but that path is absent in-repo. | Implementor could treat a missing in-repo path as a missing ticket. | Use the incoming package ticket as active source and record path absence. |
| Generated NullForge volumes are available as packages but not yet imported/audited. | Draft generated material could be treated as canonical too early. | PF-T000 only plans import; PF-T001 owns reviewed import and audit. |
| README and `pyproject.toml` contain narrower or older framing than `docs/STATUS.md` and implemented code. | PF-T000 could drift into unrelated repo framing cleanup. | Do not edit README, package metadata, or engine status docs in PF-T000. |
| Existing generated reference docs contain TODO/partial areas. | NullForge docs could overstate ResearchCore platform completeness. | Use conservative language and preserve known partial-state notes. |

## Human Gates

Stop and request human review before any action that would:

- overwrite, move, rename, or materially edit existing ResearchCore Engine docs;
- change root README beyond a later explicitly scoped link/summary;
- rename repo, package, CLI, project, product, or public identity;
- add dependencies, scripts, parsers, sidecar binaries, packaging configs, code, tests, schemas, or CI behavior;
- run or require dependency installation;
- commit full `ES.zip`, raw/private/local data, or ES-derived fixtures without a license/safety decision;
- mark generated NullForge volumes as canonical before PF-T001 import and audit;
- treat old chat or stale prompts as active source truth without promotion through M0;
- broaden into public release, legal/trademark naming, AI strategy activation, broker/live-trading integration, financial advice, auth, billing, cloud sync, marketplace, or mobile scope;
- skip, reverse, or parallelize required M0 dependencies without explicit human deferral.

## Data And Privacy Gates

| Item | Gate |
|---|---|
| Full `ES.zip` | Must not enter repo. |
| Raw/private/local datasets | Must not enter repo. |
| ES-derived fixtures | Require explicit license/safety decision before commit. |
| Generated local analysis artifacts | Keep in ignored local paths such as `configs/analysis/local/` unless a later ticket explicitly approves otherwise. |
| Dataset capability claims | Must be grounded in imported docs and later dataset/catalog evidence, not guessed. |

## Dependency And Code Gates

PF-T000 is docs/source-of-truth only. Any need to add or change executable code, tests, package config, scripts, generated docs tooling, CI behavior, dependencies, or build configuration forces HOLD and human review.

## Identity And Branding Gates

PF-T000 does not decide public naming, trademark/domain posture, release status, repo rename, package rename, CLI rename, or public product claims. ADR-T001 may document name/platform/stack/engine boundaries later, but any actual identity change requires human approval.

## Downstream Sequence Gates

M0 must remain serial unless a human explicitly defers a dependency:

```text
PF-T000 -> PF-T001 -> PF-T002 -> ADR-T001 -> ADR-T002 -> CX-T001 -> MB-T001
```

PF-T001 must not start until PF-T000 has implementation outputs and an independent audit disposition.

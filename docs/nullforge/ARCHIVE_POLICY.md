# NullForge Archive Policy

Date: `2026-06-15`

This policy defines how NullForge sources are treated during M0. Volume 01 is the deeper planning source for workspace, source-of-truth, archive, and quarantine concepts: [Volume 01](blueprint/volumes/NullForge_Volume_01_Workspace_Repo_Context_Source_of_Truth_Archive_Quarantine_System_v0_4.md).

## Active Docs

Active docs are repo-local files that have been created or imported by scoped role-loop tickets and accepted by audit disposition. They may guide later tickets within their stated authority boundary.

Active NullForge docs do not override ResearchCore Engine implementation truth unless a later audited ticket explicitly changes that boundary.

## Design Memory

Design memory preserves planning context, rationale, examples, and generated source material. It may inform later work, but it does not authorize implementation or prove claims by itself.

Imported Volume 00-07 files are active planning/workflow source after PF-T001 audit `PASS`, but technical and product claims inside them remain proposed until promoted by later audited work.

## Archive

Archive material is memory without authority. Archived material can help explain history, but it does not govern current tickets, implementation, product claims, or repo changes.

Prior drafts, old chat logs, superseded package contents, and previous planning outputs remain archive material unless a later scoped ticket imports and promotes them.

## Quarantine

Quarantine is for unresolved, conflicting, risky, private, local-only, or unreviewed material. Quarantined material has no governance power.

Raw/full ES.zip contents, private/local data, ES-derived fixtures, broker-live material, unresolved platform identity claims, and any source with unclear provenance remain gated until a later ticket explicitly handles them.

## Prompts

Prompt files are workflow instructions, not canonical product or architecture source by default. Prior chat and prompt text are not active truth unless explicitly promoted by a scoped and audited ticket.

PF-T001 recorded prompt exclusions in the volume import manifest. PF-T002 does not import prompt files.

## Promotion Rule

A source can move from archive, quarantine, prompt memory, or incoming package input into active repo-local truth only through a bounded ticket with:

- explicit source path and destination path,
- documented authority boundary,
- changed-file inventory,
- recorded checks,
- human gate handling when required,
- independent audit disposition.

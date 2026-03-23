What Stands Out Immediately

The front door is underselling and confusing the actual scope. README.md presents a narrow “Phase 0 deterministic canonicalization” flow with 4 commands, while the codebase exposes a much larger platform surface (README.md, cli.py).
Repo identity is split across names:
“Research Core” in README.md
“Research Platform Docs Hub” in index.md
Phase-tag release narrative in CHANGELOG.md (phase9 through phase14).
First 60-second impression is “serious implementation, weak framing.” The code/test surface looks real; the top-level narrative does not match it.
What The Repo Appears To Be

A Python CLI platform for deterministic data pipeline execution across canon/validation, runset/risk/baseline workflows, CI doctoring, projects/plans, release drafting, and pruning.
Evidence: 20 command groups and 58 command decorators in cli.py; broad module layout under research_core (e.g., risk/, runsets/, projects/, ci/, pilot/, release/).
Strong Signals

Strong test coverage pattern with determinism and fail-loud focus:
test_ci_run_determinism.py
test_bundle_export_fail_loud.py
test_plan_env_fingerprint_mismatch_fail_loud.py
plus a large suite across tests.
CI exists and is not superficial:
double pytest gates and smoke run in research-ci.yml.
docs generation + drift check in docs.yml.
Contract/schema orientation is explicit and structured:
schemas/*.json, schemas, v1.
Weak Or Unclear Areas

README.md is too small for repo scale. It lacks:
clear product boundary (what this is and is not),
command map,
architecture/dataflow diagram or equivalent,
testing entrypoint (pytest/CI local flow),
pointer to docs as primary entry.
CLI docs are materially incomplete relative to code:
only 5 generated CLI pages configured in gen_cli_ref.py (overview, canon, risk, risk_run, risk_runset),
while CLI exposes far more commands in cli.py.
Docs contain large unresolved TODO surface (93 TODO/TBD/WIP matches across docs/**/*.md), including user-facing references and tutorials.
Artifact reference includes placeholder stages with zero outputs and TODO commands:
stage2_occupancy.md
stage3_streams.md
stage4_corridors.md
stage5_flow_harness.md
stage6_observer.md.
Risky Mismatches

Determinism claims vs dependency strategy:
repo repeatedly claims deterministic behavior (README.md, index.md, CI metadata pinning in research-ci.yml),
but runtime deps are minimum-bound only, no lock/constraints (pyproject.toml), which weakens reproducibility across time.
Documentation self-consistency gap:
artifact tooling emits explicit TODO placeholders by design (gen_artifact_catalog.py, catalog.v1.yml),
schema tooling emits fallback “TODO: Description not found...” when schema descriptions are missing (gen_schema_ref.py), and many generated schema pages contain that text.
Command naming drift in docs examples:
some artifact pages still show research ... commands while actual documented invocation pattern is python -m research_core.cli ... and no project.scripts entrypoint is defined in pyproject.toml.
Contract duplication with unclear sync mechanism:
same spec content exists in both docs/*_spec_v1.md and docs/reference/contracts/v1/*_spec_v1.md,
no visible generator/verification for that duplication in docs.
README And Front-Door Problems

README.md currently reads like a minimal phase0 demo, not the real platform.
It omits key onboarding decisions a hiring manager looks for:
“who should use this,”
“what’s production-ready vs roadmap,”
“where to start for full pipeline vs phase0-only.”
It does not acknowledge the much broader command/test/docs surface already present.
Docs-To-Code Drift

cli.py command breadth is far beyond generated CLI reference coverage (index.md, gen_cli_ref.py).
Artifact pages include incomplete staged sections marked TODO despite being in published reference nav (index.md and stage pages above).
Contracts are vendored/copy-based (v1) with no visible automated drift guard analogous to schema/artifact/CLI generators.
Questions A Serious Reviewer Would Ask

Is this repo “Phase 0 core” or a broader “research platform”? Which label is canonical?
Which commands are stable/public API vs experimental/internal?
Why are stages 2-6 in public artifact reference if outputs/commands are unresolved?
What is the reproducibility guarantee without pinned transitive deps/constraints?
What is the authoritative contract source: docs/*_spec_v1.md or docs/reference/contracts/v1/*?
Is there an intended console command (research) or only module invocation?
What To Fix First

Rewrite README.md to reflect actual scope, boundaries, and start paths (phase0 quickstart + full-platform path + test/CI path).
Expand gen_cli_ref.py to cover all public command groups (or explicitly mark partial coverage and why).
Remove or quarantine unresolved TODO-heavy reference pages from public nav until they are complete.
Define and document one canonical contract source and automate sync verification.
Decide and document command entrypoint policy (python -m ... only vs add project.scripts for research).
What Can Wait

Filling every schema description field (important, but second-order once front-door truth is fixed).
Changelog/version naming cleanup (phase tags vs semver) after identity and docs coverage are corrected.
Deeper docs style polish once structural truth and coverage are aligned.
If you want, I can next produce a concrete “public-ready README skeleton” and a prioritized docs debt checklist mapped file-by-file.
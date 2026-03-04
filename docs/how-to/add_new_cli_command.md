# Add New CLI Command

This guide uses the current CLI implementation and existing test/doc generation
patterns.

Primary truth sources:

- `src/research_core/cli.py`
- `docs/reference/contracts/v1/*`
- `tools/docs/gen_cli_ref.py`
- `docs/reference/cli/*.md`
- tests under `tests/`

## Where commands live

CLI entrypoint is:

- `src/research_core/cli.py`

Command registration pattern in this file:

1. Create a Typer app object (for groups), for example `ci_app = typer.Typer(...)`.
2. Attach it with `app.add_typer(ci_app, name="ci")`.
3. Add concrete commands with decorators such as `@ci_app.command("run")`.

Existing examples:

- top-level command: `@app.command("canon")`
- grouped command: `@ci_app.command("run")`
- nested group command: `@baseline_index_app.command("refresh")`

## Contract-first checklist

Before implementing the command, confirm these contract decisions.

### Output paths, manifests, and schema links

- Define deterministic output paths and manifest outputs in the owning contract
	page under `docs/reference/contracts/v1/`.
- If command outputs include manifests, align with existing manifest discipline:
	`docs/reference/contracts/v1/manifest_spec_v1.md`.
- If command has a JSON config/output schema, add/update a file under `schemas/`
	and ensure docs generation picks it up (`tools/docs/gen_schema_ref.py`).

Concrete contract examples:

- CI outputs and manifests: `docs/reference/contracts/v1/ci_spec_v1.md`
- CI doctor outputs and manifests: `docs/reference/contracts/v1/ci_doctor_spec_v1.md`
- Risk outputs and manifests: `docs/reference/contracts/v1/risk_spec_v1.md`

### Determinism requirements

- Use stable ordering for emitted lists/maps when contracts require it.
- Use canonical JSON bytes where contracts require it.
- Avoid wall-clock timestamps when contract requires deterministic metadata;
	prefer `RESEARCH_CREATED_UTC` when required.

Contract anchors:

- `docs/reference/contracts/v1/risk_spec_v1.md`
- `docs/reference/contracts/v1/dataset_catalog_spec_v1.md`
- `docs/reference/contracts/v1/ci_spec_v1.md`

### Fail-loud behavior

Follow existing CLI fail pattern in `src/research_core/cli.py`:

- return non-zero via `raise typer.Exit(code=1)` when status/checks fail
	(`ci run`, `ci doctor`, `doctor run`, `runset validate`, `pilot run`).
- raise `ResearchError` / `ValidationError` for invalid inputs or unsafe states
	(for example prune confirm mismatch in `_run_prune`).

## Update generated CLI docs

Generated CLI reference source is:

- `tools/docs/gen_cli_ref.py`

It only generates help pages for entries in `COMMANDS`.

When a new command should appear in `docs/reference/cli/`, add a new
`(title, slug, args)` entry to `COMMANDS`.

Then run:

```powershell
python tools/docs/gen_cli_ref.py
python tools/docs/verify_generated_docs_clean.py
```

## Testing checklist

Use the existing test style already present in this repo.

### 1. Smoke test

Pattern examples:

- `tests/test_cli_smoke.py`
- `tests/test_ci_run_smoke.py`

Goal: command executes and expected artifacts/fields exist.

### 2. Determinism test

Pattern examples:

- `tests/test_ci_run_determinism.py`
- `tests/test_manifest_determinism.py`

Goal: run twice with equivalent inputs and compare deterministic outputs/hashes.

### 3. Golden fixture regression test (if applicable)

Pattern examples:

- `tests/test_golden_fixture_regression.py`
- `tests/test_ci_golden_fixture_regression.py`

Goal: compare canonical output hash(es) to `tests/golden/*.sha256` fixtures.

## Local verification commands

PowerShell:

```powershell
python tools/docs/gen_cli_ref.py
python tools/docs/gen_schema_ref.py
python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
$env:NO_MKDOCS_2_WARNING = "1"
python -m mkdocs build
pytest -q tests/test_cli_smoke.py
pytest -q tests/test_manifest_determinism.py
```

Add command-specific smoke/determinism/golden tests to this verification list
before merging.

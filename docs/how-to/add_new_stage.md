# Add New Stage

In this repo, a "stage" is an artifact-producer layer registered in
`docs/reference/artifacts/catalog.v1.yml` and rendered to
`docs/reference/artifacts/*.md` by `tools/docs/gen_artifact_catalog.py`.

## Stage references in this repo

- [Stage 0 Canon](../reference/artifacts/stage0_canon.md)
- [Stage 1 Diagnostics](../reference/artifacts/stage1_diagnostics.md)
- [Stage 2 Occupancy](../reference/artifacts/stage2_occupancy.md)
- [Stage 3 Streams](../reference/artifacts/stage3_streams.md)
- [Stage 4 Corridors](../reference/artifacts/stage4_corridors.md)
- [Stage 5 Flow Harness](../reference/artifacts/stage5_flow_harness.md)
- [Stage 6 Observer](../reference/artifacts/stage6_observer.md)

## When to add a new stage vs extend vs observer utility

- Add a **new stage** when you need a new `stage:` block in
	`docs/reference/artifacts/catalog.v1.yml` with new output IDs/path templates.
- **Extend an existing stage** when your outputs fit an existing stage key and
	tool flow already described in artifact catalog truth.
- Add a **read-only observer utility** when you are deriving diagnostics from
	existing artifacts without mutating baseline/catalog state.

!!! note "TODO: observer boundary detail is not fully specified"
		`stage6_observer` is currently TODO-driven in artifact catalog docs. Use the
		closest contract for read-only deterministic behavior when designing
		observer-like features:
		[Risk Harness Spec v1 (Scope: read-only)](../reference/contracts/v1/risk_spec_v1.md).

## Contract-first checklist

### 1. Define artifacts

Define these fields first (contract + catalog truth):

- `id` (output ID)
- `path_template`
- `type`
- `schema` link (or explicit TODO if not confirmed)
- `description`, `invariants`, `verification`

Use existing catalog entries as examples:

- `stage0_canon` outputs in `docs/reference/artifacts/catalog.v1.yml`
- `stage1_diagnostics` output in `docs/reference/artifacts/catalog.v1.yml`

### 2. Update artifact registry truth source

Edit:

- `docs/reference/artifacts/catalog.v1.yml`

This file is the source for generated artifact pages.

### 3. Regenerate artifact docs and verify clean output

PowerShell:

```powershell
python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
```

### 4. If a new CLI entrypoint is required

Follow:

- [Add New CLI Command](add_new_cli_command.md)

To ensure docs coverage in `docs/reference/cli/`, add the new help target to
`tools/docs/gen_cli_ref.py` `COMMANDS`, then run:

```powershell
python tools/docs/gen_cli_ref.py
python tools/docs/verify_generated_docs_clean.py
```

### 5. If the stage introduces schemas

Follow:

- [Add New Schema](add_new_schema.md)

Then regenerate schema docs:

```powershell
python tools/docs/gen_schema_ref.py
python tools/docs/verify_generated_docs_clean.py
```

## Testing requirements

Use existing patterns already in `tests/`.

### Smoke test

Examples:

- `tests/test_cli_smoke.py`
- `tests/test_ci_run_smoke.py`

### Determinism test (run twice and compare)

Examples:

- `tests/test_ci_run_determinism.py`
- `tests/test_manifest_determinism.py`

### Golden fixture regression (if stage has stable hash fixtures)

Examples:

- `tests/test_golden_fixture_regression.py`
- `tests/test_ci_golden_fixture_regression.py`

## Local verification

The docs workflow truth in `.github/workflows/docs.yml` runs these commands.

PowerShell:

```powershell
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install -r requirements-docs.txt
python tools/docs/gen_cli_ref.py
python tools/docs/gen_schema_ref.py
python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
$env:NO_MKDOCS_2_WARNING = "1"
python -m mkdocs build
```

Optional test gates aligned with `.github/workflows/research-ci.yml`:

```powershell
pytest -q
pytest -q
```

Optional CI runner / bash:

```bash
python -m pip install --upgrade pip; python -m pip install -e .
python -m pip install -r requirements-docs.txt
python tools/docs/gen_cli_ref.py; python tools/docs/gen_schema_ref.py; python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
NO_MKDOCS_2_WARNING=1 python -m mkdocs build
pytest -q
pytest -q
```

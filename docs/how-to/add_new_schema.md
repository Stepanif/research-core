# Add New Schema

This guide is contract-first and repo-truth-only.

Primary truth sources:

- `docs/reference/contracts/v1/*`
- `schemas/*schema*.json`
- `tools/docs/gen_schema_ref.py`
- existing tests under `tests/`

## Naming and placement rules

Place new schemas under `schemas/` and follow the existing filename pattern:

- `<name>.schema.v1.json`

Real examples in this repo:

- `schemas/canon.schema.v1.json`
- `schemas/manifest.schema.v1.json`
- `schemas/ci.summary.schema.v1.json`
- `schemas/ci.doctor.config.schema.v1.json`
- `schemas/prune.policy.schema.v1.json`

Versioning pattern in filenames is explicit (`.v1.json`).

## Step-by-step workflow

### 1. Create the new schema file

Create a new file in `schemas/` using the established pattern:

```text
schemas/<name>.schema.v1.json
```

### 2. Ensure docs discovery picks it up

`tools/docs/gen_schema_ref.py` discovers schemas with this glob:

```text
*.schema*.json
```

Discovery is recursive from repo root and skips `.git`, `.venv`, `site`,
`node_modules`, and `__pycache__`.

Generated pages are written under:

- `docs/reference/schemas/`

### 3. Wire validation usage (only where a validator exists)

There is no single repo-wide `jsonschema`-based validator in `src/`.

Current pattern is domain-specific loaders/validators, for example:

- `src/research_core/canon/contracts.py` (`load_schema_contract`)
- `src/research_core/prune/policy.py` (`load_prune_policy`)

If your new schema belongs to an existing domain, extend that domain's loader
and fail-loud checks.

TODO: Introduce a shared schema-validation utility if you need cross-domain,
uniform validation behavior.

### 4. Add tests using existing repo patterns

Follow the established mix of smoke, determinism, and golden regression tests.

Concrete examples:

- Schema/contract input usage:
	- `tests/test_canon_parse_and_schema.py`
	- `tests/test_cli_smoke.py`
- Determinism pattern (run twice, compare stable outputs):
	- `tests/test_manifest_determinism.py`
	- `tests/test_ci_run_determinism.py`
- Golden fixture regression pattern (`tests/golden/*.sha256`):
	- `tests/test_golden_fixture_regression.py`
	- `tests/test_ci_golden_fixture_regression.py`

### 5. Run local verification

PowerShell:

```powershell
python tools/docs/gen_schema_ref.py
python tools/docs/gen_cli_ref.py
python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
$env:NO_MKDOCS_2_WARNING = "1"
python -m mkdocs build
pytest -q tests/test_canon_parse_and_schema.py
pytest -q tests/test_manifest_determinism.py
pytest -q tests/test_golden_fixture_regression.py
```

Use domain-specific tests instead when your schema is not canon-related.

## Common mistakes

- Using a non-standard filename that does not match `*.schema*.json`, so
	schema docs are not generated.
- Adding a schema but not adding/adjusting fail-loud validation logic in the
	owning domain.
- Introducing non-canonical JSON output behavior.

Determinism/canonicalization anchors to check:

- `docs/reference/contracts/v1/dataset_catalog_spec_v1.md`
	- canonical JSON bytes (`json.dumps(..., sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\\n"`)
	- no wall-clock timestamps (`RESEARCH_CREATED_UTC` required)
- `docs/reference/contracts/v1/risk_spec_v1.md`
	- canonical JSON bytes and deterministic ordering
- `docs/reference/contracts/v1/manifest_spec_v1.md`
	- stable manifest hashing and deterministic metadata

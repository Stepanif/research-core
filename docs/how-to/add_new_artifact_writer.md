# Add New Artifact Writer

In this repo, a "writer" is code that persists deterministic artifacts
(`*.json`, `*.manifest.json`, parquet/log outputs), including canonical hashes
and manifest metadata when required by contract.

## What a writer contract includes here

Use `manifest_spec_v1.md` plus domain contracts as the anchor:

- [Manifest Spec v1](../reference/contracts/v1/manifest_spec_v1.md)
- [Risk Harness Spec v1](../reference/contracts/v1/risk_spec_v1.md)
- [CI Runner Spec v1](../reference/contracts/v1/ci_spec_v1.md)

Concrete writer examples in code:

- `src/research_core/risk/writer.py`
	- writes `risk.summary.json` and `risk.summary.manifest.json`
	- computes `sha256` and canonical self-hashes.
- `src/research_core/ci/writer.py`
	- writes `ci.summary.json` and `ci.summary.manifest.json`
	- emits sorted manifest `inputs` with byte/hash metadata.
- `src/research_core/observe/writer.py`
	- writes canonical JSON payloads with trailing newline and manifest hashes.

## Writer contract checklist

### Stable ordering

- Sort deterministic collections before writing where contract requires it.
- Example pattern: sorted manifest `inputs` list in `src/research_core/ci/writer.py`.

### Newline normalization (LF)

- JSON writer paths in repo commonly serialize as canonical compact JSON with a
	trailing `"\n"`.
- Example pattern: `json.dumps(..., sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"`
	in `src/research_core/observe/writer.py`.

### Timestamp policy

- Do not use wall-clock timestamps for deterministic outputs when contract
	requires deterministic metadata.
- Use `RESEARCH_CREATED_UTC` where required by contract (for example risk/ci).

### Stable numeric formatting

!!! note "TODO: repo-wide numeric formatting rule is not explicitly centralized"
		Use the owning contract's output semantics. If numeric precision/rounding
		rules are needed for your artifact, add them explicitly to the relevant
		contract page under `docs/reference/contracts/v1/`.

### Manifest generation

- Include output hashes/sizes and deterministic input path list where spec
	requires it.
- Prefer canonical hash fields that exclude their own self-field, following
	existing patterns in risk/ci writers.

## Step-by-step workflow

### 1. Choose output location and naming pattern

Follow existing artifact patterns under:

- `docs/reference/artifacts/`
- source registry: `docs/reference/artifacts/catalog.v1.yml`

### 2. Implement deterministic `write()` behavior

Follow writer patterns in:

- `src/research_core/risk/writer.py`
- `src/research_core/ci/writer.py`
- `src/research_core/observe/writer.py`

### 3. Emit manifest + contract/schema anchors (when required)

- Align payload structure with relevant contract page(s).
- Ensure manifest/hash fields are present and deterministic.

### 4. Add/update schema files when applicable

- Add schema under `schemas/*.schema*.json`.
- Ensure docs generation discovers it via `tools/docs/gen_schema_ref.py`.
- See: [Add New Schema](add_new_schema.md).

### 5. Update artifact catalog and regenerate docs

- Update `docs/reference/artifacts/catalog.v1.yml`.
- Regenerate docs:

```powershell
python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
```

### 6. Add tests using existing patterns

Smoke examples:

- `tests/test_cli_smoke.py`
- `tests/test_ci_run_smoke.py`

Determinism examples:

- `tests/test_ci_run_determinism.py`
- `tests/test_manifest_determinism.py`

Golden fixture regression examples:

- `tests/test_golden_fixture_regression.py`
- `tests/test_ci_golden_fixture_regression.py`

## Local verification

Commands grounded in `.github/workflows/docs.yml`:

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

Optional CI runner / bash:

```bash
python -m pip install --upgrade pip; python -m pip install -e .
python -m pip install -r requirements-docs.txt
python tools/docs/gen_cli_ref.py; python tools/docs/gen_schema_ref.py; python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
NO_MKDOCS_2_WARNING=1 python -m mkdocs build
```

## Common failure modes

| Failure mode | Guide |
|---|---|
| Golden hash mismatches after writer changes | [Update Goldens Safely](update_goldens_safely.md) |
| Intermittent/non-reproducible output hashes | [Determinism Failures](../troubleshooting/determinism_failures.md) |
| Expected hash fixtures no longer match | [Stale Goldens](../troubleshooting/stale_goldens.md) |

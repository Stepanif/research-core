# Run CI Locally

This page mirrors what CI actually runs in `.github/workflows/research-ci.yml`
and `.github/workflows/docs.yml`, using PowerShell-first local commands.

## What CI runs

### `research-ci.yml`

Workflow command steps:

```bash
python --version
echo "RESEARCH_CREATED_UTC=${RESEARCH_CREATED_UTC}"
pip install -e .[dev]
pytest -q
pytest -q
mkdir -p exec_outputs/gha_smoke/{catalog,baseline_root,out}
python -m research_core.cli ci run --config .github/ci/ci.github.json
```

Notes from workflow behavior:

- CI sets `RESEARCH_GIT_COMMIT=${GITHUB_SHA}`.
- CI sets `RESEARCH_CREATED_UTC=$(git show -s --format=%cI "$GITHUB_SHA")`.

### `docs.yml`

Workflow command steps:

```bash
python -m pip install --upgrade pip; python -m pip install -e .
python -m pip install -r requirements-docs.txt
python tools/docs/gen_cli_ref.py; python tools/docs/gen_schema_ref.py; python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
python -m mkdocs build
```

## Run the docs checks locally

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

Optional bash equivalent:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install -r requirements-docs.txt
python tools/docs/gen_cli_ref.py
python tools/docs/gen_schema_ref.py
python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
NO_MKDOCS_2_WARNING=1 python -m mkdocs build
```

## Run the test suite locally

`research-ci.yml` runs this twice:

```powershell
pytest -q
pytest -q
```

## Reproduce CI smoke run locally

The workflow smoke command is:

```bash
python -m research_core.cli ci run --config .github/ci/ci.github.json
```

PowerShell setup equivalent for the workflow metadata env vars:

```powershell
$env:RESEARCH_GIT_COMMIT = (git rev-parse HEAD)
$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI $env:RESEARCH_GIT_COMMIT)
python -m research_core.cli ci run --config .github/ci/ci.github.json
```

`ci run` contract reference: `docs/reference/contracts/v1/ci_spec_v1.md`.
`ci doctor` contract reference: `docs/reference/contracts/v1/ci_doctor_spec_v1.md`.

## Common CI failures -> local reproduction

| Failure class | Local reproduction command(s) | Troubleshooting |
|---|---|---|
| Stale goldens | `pytest -q` (same gate command as CI) | [Stale Goldens](../troubleshooting/stale_goldens.md) |
| Determinism failures | `pytest -q` and rerun identical commands with pinned `RESEARCH_CREATED_UTC` | [Determinism Failures](../troubleshooting/determinism_failures.md) |
| Docs drift check failures | `python tools/docs/gen_cli_ref.py`<br>`python tools/docs/gen_schema_ref.py`<br>`python tools/docs/gen_artifact_catalog.py`<br>`python tools/docs/verify_generated_docs_clean.py` | [Missing Artifacts](../troubleshooting/missing_artifacts.md) |
| Link/build failures | `$env:NO_MKDOCS_2_WARNING = "1"`<br>`python -m mkdocs build` | [Missing Artifacts](../troubleshooting/missing_artifacts.md) |

## Environment notes

- Use the same Python version as workflows (`3.13`).
- `ci run` requires `RESEARCH_CREATED_UTC` (authoritative by contract).
- `docs.yml` sets `NO_MKDOCS_2_WARNING: "1"`; set this locally before
	`python -m mkdocs build` to mirror CI behavior.

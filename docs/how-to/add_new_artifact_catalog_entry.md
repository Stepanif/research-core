# Add New Artifact Catalog Entry

## What This Is

`docs/reference/artifacts/catalog.v1.yml` is the single truth source for generated artifact reference pages.

Key links:

- Artifacts index: [Artifacts Reference](../reference/artifacts/index.md)
- Catalog source file: `docs/reference/artifacts/catalog.v1.yml`
- Generator: `tools/docs/gen_artifact_catalog.py`

If you add a new output, update `docs/reference/artifacts/catalog.v1.yml` and regenerate docs.

## Step-by-step Recipe

### 1. Identify the new output(s)

For each output, define the same keys used in catalog entries today:

- `id`
- `path_template`
- `type`
- `schema`
- `description`
- `invariants`
- `verification`

### 2. Edit `docs/reference/artifacts/catalog.v1.yml`

Use the exact existing shape and key names.

Minimal example snippet (structure only, keys copied from catalog):

```yaml
stages:
  - stage: your_stage_key
    name: Your Stage Name
    tools:
      - cli: python -m research_core.cli your command
    outputs:
      - id: your.output.id
        path_template: <out>/<runset_id>/your.output.json
        type: json
        schema: "TODO: schema link not yet confirmed"
        description: Describe the artifact from contract truth.
        invariants:
          - Invariant sentence from contract/spec truth.
        verification:
          - Check <out>/<runset_id>/your.output.json exists.
```

### 3. Regenerate generated artifact docs

PowerShell:

```powershell
python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
```

`verify_generated_docs_clean.py` also runs:

- `python tools/docs/gen_cli_ref.py`
- `python tools/docs/gen_schema_ref.py`
- `python tools/docs/gen_artifact_catalog.py`

and fails if generated docs drift exists under:

- `docs/reference/cli`
- `docs/reference/schemas`
- `docs/reference/artifacts`

(excluding `docs/reference/artifacts/catalog.v1.yml`).

### 4. Validate documentation build

PowerShell:

```powershell
$env:NO_MKDOCS_2_WARNING = "1"
python -m mkdocs build
```

## Choosing `path_template`

Use only confirmed patterns already present in `docs/reference/artifacts/catalog.v1.yml`, for example:

- `baselines/prod/<runset_id>/baseline.card.json`
- `<out>/dashboard.summary.json`
- `<out>/drift/<runset_id>/drift.report.json`
- `<out>/<runset_id>/risk.runset.summary.json`
- `<run_dir>/canon.manifest.json`
- `exec_outputs/analysis/es_5m/doctor/ci.doctor.summary.json`
- `exec_outputs/registry/registry.json`

Do not introduce guessed directory shapes.

## Common mistakes

- [ ] Forgot to run `python tools/docs/gen_artifact_catalog.py`.
- [ ] Forgot to run `python tools/docs/verify_generated_docs_clean.py`.
- [ ] Used guessed `path_template` instead of an existing confirmed pattern.
- [ ] Added inconsistent `id`/`type` versus actual artifact behavior.
- [ ] Omitted schema/contract anchor in `schema`, `description`, or `invariants`.

## Verification Block

PowerShell:

```powershell
python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
$env:NO_MKDOCS_2_WARNING = "1"
python -m mkdocs build
```

Optional CI runner / bash:

```bash
python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
NO_MKDOCS_2_WARNING=1 python -m mkdocs build
```

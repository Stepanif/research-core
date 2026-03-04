# Update Goldens Safely

Use this playbook when a `*_golden_fixture_regression` test fails and you need to
decide whether `tests/golden/*.sha256` should be updated.

!!! tip "If you only do one thing"
    Read the **Decision gate** below. If you cannot answer "yes" to every
    item in the ALLOW column, stop and investigate before touching any golden
    hash file.

## Quick diagnosis

| What you see | Likely path |
|---|---|
| Hash mismatch after an intentional contract change | Follow the workflow below |
| Intermittent hash mismatch across identical runs | See [Determinism Failures](../troubleshooting/determinism_failures.md) |
| Hash mismatch with no code changes in your PR | See [Stale Goldens](../troubleshooting/stale_goldens.md) |

## Decision gate

??? success "ALLOW — all three must be true"
    1. You intentionally changed deterministic output behavior covered by a
       contract/spec in `docs/reference/contracts/v1/`.
    2. You can reproduce the change locally and the change is stable across
       repeated runs.
    3. Related checks pass after update (docs generation verification +
       relevant tests).

??? danger "STOP — any one of these means do NOT update"
    - Failure is nondeterministic between identical runs.
    - Failure is caused by environment drift only (for example missing/pinned
      `RESEARCH_CREATED_UTC`) rather than intentional behavior change.
    - Output diffs include unexplained ordering/newline/hash changes.

See also:

- [Troubleshooting: Stale Goldens](../troubleshooting/stale_goldens.md)
- [Troubleshooting: Determinism Failures](../troubleshooting/determinism_failures.md)

## Step-by-step workflow

### 1. Reproduce locally

Run the failing golden test directly first:

```bash
pytest tests/test_golden_fixture_regression.py -q
```

For broader sweep of golden fixture regressions:

```bash
pytest -k golden_fixture_regression -q
```

### 2. Isolate cause — behavior change vs nondeterminism

Ask two questions:

- **Is this a behavior change?**
    - contract/spec change in `docs/reference/contracts/v1/`
    - schema/canonicalization change
- **Or is it nondeterminism?**
    - run-to-run hash differences for same inputs
    - missing deterministic env pin (`RESEARCH_CREATED_UTC`)

Quick deterministic rerun check using the canon command from `README.md`:

```bash
python -m research_core.cli canon --in tests/fixtures/raw_small_sample.txt --out exec_outputs/tmp_run_a --instrument ES --tf 1min --schema schemas/canon.schema.v1.json --colmap schemas/colmap.raw_vendor_v1.json
python -m research_core.cli canon --in tests/fixtures/raw_small_sample.txt --out exec_outputs/tmp_run_b --instrument ES --tf 1min --schema schemas/canon.schema.v1.json --colmap schemas/colmap.raw_vendor_v1.json
```

Then compare canonical table hashes (source of truth in manifest contract):

```bash
python -c "import json, pathlib; a=json.loads(pathlib.Path('exec_outputs/tmp_run_a/canon.manifest.json').read_text(encoding='utf-8')); b=json.loads(pathlib.Path('exec_outputs/tmp_run_b/canon.manifest.json').read_text(encoding='utf-8')); print(a['output_files']['canon.parquet']['canonical_table_sha256']); print(b['output_files']['canon.parquet']['canonical_table_sha256'])"
```

### 3. Run verification commands before any golden update

Docs generation checks used in CI (`.github/workflows/docs.yml`):

```bash
python tools/docs/verify_generated_docs_clean.py
```

Run the relevant test subset again:

```bash
pytest -k "golden_fixture_regression or determinism" -q
```

### 4. Regenerate goldens (only if the decision gate allows it)

Current truth in this repo:

- Golden tests compare computed hashes to files in `tests/golden/*.sha256`.
- There is no single documented `regolden` command/script in repository docs.

!!! note "TODO"
    Add an official repo-level regolden script that rewrites all affected
    `tests/golden/*.sha256` files in one controlled command.

Until then, update only the specific `.sha256` files for the failing fixtures,
in the same PR as the intentional behavior change.

### 5. Sanity-check diffs before commit

**Expected** (safe to merge):

- Targeted files under `tests/golden/*.sha256` tied to the changed behavior.
- If docs references changed, generated docs under `docs/reference/` only.

**Suspicious** (investigate before merge):

- Unrelated golden hashes changing across multiple domains.
- Pure ordering/noise diffs without corresponding contract update.
- CRLF/LF-only churn in docs/reference files (see `.gitattributes`).

## Golden churn anti-patterns

Avoid these mistakes — each one has caused real review pain:

- Updating golden hashes without a linked contract/spec behavior change.
- Batch-updating many golden files without running focused repro tests first.
- Ignoring deterministic contracts around canonical JSON and sorted inputs.
- Mixing unrelated refactors with golden updates in the same commit.

## Contract links for deterministic outputs

- [Manifest Spec v1](../reference/contracts/v1/manifest_spec_v1.md)
- [CI Spec v1](../reference/contracts/v1/ci_spec_v1.md)
- [Baseline Diff Spec v1](../reference/contracts/v1/baseline_diff_spec_v1.md)
- [Dashboard Spec v1](../reference/contracts/v1/dashboard_spec_v1.md)
- [Dataset Catalog Spec v1](../reference/contracts/v1/dataset_catalog_spec_v1.md)

# Add New Test And Golden

Use this page to decide and implement smoke, determinism, and golden fixture regression tests using existing repo patterns.

## Decision Gate

Add a **smoke** test when you need to prove the command/path creates expected artifacts and exits successfully.

- Existing pattern examples:
  - `tests/test_cli_smoke.py`
  - `tests/test_ci_run_smoke.py`

Add a **determinism** test when repeated runs with identical inputs must produce stable output/hashes.

- Existing pattern examples:
  - `tests/test_ci_run_determinism.py`
  - `tests/test_manifest_determinism.py`

Add a **golden fixture regression** test when output hashes are intentionally locked to `tests/golden/*.sha256` fixtures.

- Existing pattern examples:
  - `tests/test_golden_fixture_regression.py`
  - `tests/test_ci_golden_fixture_regression.py`

## Related Guides

- [Update Goldens Safely](update_goldens_safely.md)
- [Troubleshooting: Stale Goldens](../troubleshooting/stale_goldens.md)
- [Troubleshooting: Determinism Failures](../troubleshooting/determinism_failures.md)

## Step-by-step Recipe

### 1. Add a smoke test

Naming/location pattern from current repo:

- `tests/test_*_smoke.py`

Typical assertions in existing smoke tests:

- `exit_code == 0`
- expected artifact files exist

### 2. Add a determinism test

Naming/location pattern from current repo:

- `tests/test_*_determinism.py`

Pattern used in existing tests:

- run the same command twice
- compare output bytes/hashes (or canonical self-hashes)

Reference file:

- `tests/test_ci_run_determinism.py`

### 3. Add a golden fixture regression test (when applicable)

Naming/location pattern from current repo:

- `tests/test_*_golden_fixture_regression.py`

Fixture pattern used in existing tests:

- expected hashes in `tests/golden/*.sha256`

Evidence examples:

- `tests/test_golden_fixture_regression.py` reads `tests/golden/canon_small_sample_v1.parquet.sha256`
- `tests/test_ci_golden_fixture_regression.py` reads `tests/golden/ci_small_sample_v1.summary.json.sha256`

### 4. Update or create goldens only via approved workflow

Use:

- [Update Goldens Safely](update_goldens_safely.md)

Do not batch-update fixtures without deterministic repro and contract-backed justification.

## How To Run Locally (CI Mirror)

Exact pytest invocation used by CI (`.github/workflows/research-ci.yml`):

```powershell
pytest -q
pytest -q
```

`RESEARCH_CREATED_UTC` behavior is confirmed in CI and contracts:

- CI sets `RESEARCH_CREATED_UTC=$(git show -s --format=%cI "$GITHUB_SHA")`.
- Deterministic contracts use `RESEARCH_CREATED_UTC` as authoritative metadata.

Reference: [CI Runner Spec v1](../reference/contracts/v1/ci_spec_v1.md)

Optional CI runner / bash:

```bash
pytest -q
pytest -q
```

## Diff Hygiene

Expected:

- targeted test file additions/edits
- targeted `tests/golden/*.sha256` updates tied to intentional behavior changes

Suspicious:

- broad unrelated golden churn across domains
- hash-only updates without corresponding contract/spec behavior change
- nondeterministic reruns producing different hashes

Use these guides when reviewing diffs:

- [Update Goldens Safely](update_goldens_safely.md)
- [Troubleshooting: Stale Goldens](../troubleshooting/stale_goldens.md)
- [Troubleshooting: Determinism Failures](../troubleshooting/determinism_failures.md)

!!! note "TODO: per-command targeted pytest invocation"
    CI truth currently documents only `pytest -q` (twice) in
    `.github/workflows/research-ci.yml`. For command-specific local subsets,
    follow existing test filename patterns and your changed scope.

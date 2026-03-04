# Stale Goldens

A **stale golden** means a test-computed hash no longer matches the expected hash
file in `tests/golden/*.sha256`.

Golden regression tests follow the pattern `test_*_golden_fixture_regression.py`
and compare live output hashes against expected values loaded from
`tests/golden/*.sha256`.

!!! tip "If you only do one thing"
    Run the repro commands below. If the failure is stable, walk through the
    cause table to find the matching fix.

## Quick diagnosis

| What you see | Go to |
|---|---|
| `assert <computed_hash> == <expected_hash>` after your change | Cause table below |
| Same failure with no code changes | Platform line endings (cause 5) |
| Intermittent pass/fail across runs | [Determinism Failures](determinism_failures.md) |

## Symptom pattern

- A `*_golden_fixture_regression` test fails at `assert <computed_hash> == <expected_hash>`.
- The expected value is read from `tests/golden/...*.sha256`.

Example repro commands:

```bash
pytest tests/test_golden_fixture_regression.py -q
pytest -k golden_fixture_regression -q
```

## Common causes and concrete fixes

### 1. Schema changed

- **Cause:** output schema or required fields changed.
- **Check:**

```bash
python tools/docs/gen_schema_ref.py
python tools/docs/verify_generated_docs_clean.py
```

- **Fix:** update behavior + schema docs together, then refresh only affected
  `tests/golden/*.sha256` values.

### 2. Formatting or canonicalization changed

- **Cause:** canonical JSON or hashing behavior changed (contracts require
  canonical JSON in multiple specs, for example baseline diff and dataset catalog).
- **Check** contract references:
    - `docs/reference/contracts/v1/baseline_diff_spec_v1.md`
    - `docs/reference/contracts/v1/dataset_catalog_spec_v1.md`
- **Fix:** confirm intentional contract change, then update affected golden hashes.

### 3. New fields added

- **Cause:** outputs/manifests gained fields; canonical hash changes by design.
- **Check:** confirm new fields are specified in the relevant contract page.
- **Fix:** land contract + implementation together, then refresh affected goldens.

### 4. Ordering changed

- **Cause:** sorted-key/sorted-input ordering rules changed or were violated.
- **Check** deterministic ordering contracts:
    - `docs/reference/contracts/v1/ci_spec_v1.md` (sorted inputs)
    - `docs/reference/contracts/v1/dashboard_spec_v1.md` (sorted entries/aggregates)
    - `docs/reference/contracts/v1/dataset_catalog_spec_v1.md` (sorted file listing)
- **Fix:** restore required ordering or intentionally update contract and goldens.

### 5. Platform line endings (LF/CRLF)

- **Cause:** line-ending conversion churn on Windows.
- **Check** repo policy in `.gitattributes` (LF enforced for docs and generated refs).
- **Fix:**

```bash
git add --renormalize -- docs tools/docs .githooks mkdocs.yml requirements-docs.txt .github/workflows
```

Then re-run tests.

## Resolution checklist

- [ ] Confirm this is an expected behavior change, not nondeterminism.
- [ ] Reproduce with focused failing test(s).
- [ ] Update golden hashes in a controlled, minimal scope.
- [ ] Re-run relevant tests:

```bash
pytest -k "golden_fixture_regression or determinism" -q
```

- [ ] Re-run docs generation verification:

```bash
python tools/docs/verify_generated_docs_clean.py
```

## If this keeps happening

Golden fixtures in this repo are already hash-based (`tests/golden/*.sha256`)
rather than storing large full-output snapshots, which limits churn surface.

!!! note "TODO"
    Define a documented, repo-level regolden workflow that updates only the
    minimal affected hash files and records which contract change required
    each update.

See also: [Update Goldens Safely](../how-to/update_goldens_safely.md).

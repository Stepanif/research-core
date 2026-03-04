# Determinism Failures

Use this page when identical inputs produce different outputs/hashes across runs
or between local and CI.

## Symptom patterns

- CI or local tests intermittently fail in deterministic/golden suites:
	- `test_*_golden_fixture_regression.py`
	- `test_*_determinism.py`
- Re-running the same command with same inputs yields different hashes.
- CI checks around manifest/hash invariants fail even though command exit codes
	are normally zero in local ad-hoc runs.

Quick repro sweep:

```bash
pytest -k "determinism or golden_fixture_regression" -q
```

## Determinism checklist (contract-derived)

1. Stable ordering

- Contracts require sorted/stable ordering in multiple places:
	- CI manifest sorted inputs: `docs/reference/contracts/v1/ci_spec_v1.md`
	- Dashboard entries/aggregates ordering: `docs/reference/contracts/v1/dashboard_spec_v1.md`
	- Dataset file listing sorted paths: `docs/reference/contracts/v1/dataset_catalog_spec_v1.md`

2. Newline normalization

- Generated docs writers normalize to `\n` and write with `newline="\n"` in:
	- `tools/docs/gen_cli_ref.py`
	- `tools/docs/gen_schema_ref.py`
	- `tools/docs/gen_artifact_catalog.py`
- Repository `.gitattributes` enforces LF for docs and generated refs.

3. No uncontrolled timestamps

- `RESEARCH_CREATED_UTC` is authoritative in CI-related contracts.
- Dataset catalog determinism explicitly disallows wall-clock timestamps.

4. Hash and manifest rules

- Manifest hashing/source-of-truth rules:
	- `docs/reference/contracts/v1/manifest_spec_v1.md`
	- `docs/reference/contracts/v1/ci_spec_v1.md`
	- `docs/reference/contracts/v1/baseline_diff_spec_v1.md`

5. Canonicalization rules

- Canonical JSON and deterministic bytes are required in contracts such as:
	- `docs/reference/contracts/v1/dataset_catalog_spec_v1.md`
	- `docs/reference/contracts/v1/baseline_diff_spec_v1.md`
	- `docs/reference/contracts/v1/experiment_spec_v1.md`

## Concrete debugging commands

1. Run exactly the same command twice and compare outputs

Canon command (from `README.md`) to two output directories:

```bash
python -m research_core.cli canon --in tests/fixtures/raw_small_sample.txt --out exec_outputs/tmp_det_a --instrument ES --tf 1min --schema schemas/canon.schema.v1.json --colmap schemas/colmap.raw_vendor_v1.json
python -m research_core.cli canon --in tests/fixtures/raw_small_sample.txt --out exec_outputs/tmp_det_b --instrument ES --tf 1min --schema schemas/canon.schema.v1.json --colmap schemas/colmap.raw_vendor_v1.json
```

Compare canonical table hashes from manifests:

```bash
python -c "import json, pathlib; a=json.loads(pathlib.Path('exec_outputs/tmp_det_a/canon.manifest.json').read_text(encoding='utf-8')); b=json.loads(pathlib.Path('exec_outputs/tmp_det_b/canon.manifest.json').read_text(encoding='utf-8')); print(a['output_files']['canon.parquet']['canonical_table_sha256']); print(b['output_files']['canon.parquet']['canonical_table_sha256'])"
```

2. Diff artifacts directly

```bash
git diff --no-index -- exec_outputs/tmp_det_a exec_outputs/tmp_det_b
```

3. Verify generated docs determinism and cleanliness

```bash
python tools/docs/gen_cli_ref.py
python tools/docs/gen_schema_ref.py
python tools/docs/gen_artifact_catalog.py
python tools/docs/verify_generated_docs_clean.py
```

## Identify nondeterministic inputs

- Environment variables:
	- Ensure `RESEARCH_CREATED_UTC` is pinned to a fixed value for reproducibility.
- Locale/time parsing:
	- Canon parsing uses fixed `MM/DD/YYYY` and `HH:MM`; timestamps are localized to
		`America/New_York` (see canon contract).
- Random seeds:
	- TODO: No contract-level random-seed controls are currently documented in
		`docs/reference/contracts/v1/`; add explicit guidance if stochastic components
		are introduced.

## Related pages

- [Manifest Spec v1](../reference/contracts/v1/manifest_spec_v1.md)
- [CI Spec v1](../reference/contracts/v1/ci_spec_v1.md)
- [Canon Spec v1](../reference/contracts/v1/canon_spec_v1.md)
- [Stale Goldens](stale_goldens.md)
- [Update Goldens Safely](../how-to/update_goldens_safely.md)

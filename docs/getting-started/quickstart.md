# Quickstart

## What you'll get

- Canon output parquet at `exec_outputs/runs/sample/canon.parquet`
- Canon contract JSON at `exec_outputs/runs/sample/canon.contract.json`
- Registry snapshot at `exec_outputs/registry/registry.json`
- Runs index at `exec_outputs/runs/index.json`

These outputs are based on commands currently documented in `README.md`.

## Run it

```text
pip install -e .[dev]

python -m research_core.cli canon \
	--in tests/fixtures/raw_small_sample.txt \
	--out exec_outputs/runs/sample \
	--instrument ES \
	--tf 1min \
	--schema schemas/canon.schema.v1.json \
	--colmap schemas/colmap.raw_vendor_v1.json

python -m research_core.cli validate canon \
	--input exec_outputs/runs/sample/canon.parquet \
	--schema schemas/canon.schema.v1.json \
	--contract exec_outputs/runs/sample/canon.contract.json

python -m research_core.cli registry build \
	--data-root exec_outputs/runs \
	--out exec_outputs/registry/registry.json

python -m research_core.cli registry index-runs \
	--runs-root exec_outputs/runs \
	--out exec_outputs/runs/index.json
```

TODO: Add minimal post-run verification checks linked to reference pages.

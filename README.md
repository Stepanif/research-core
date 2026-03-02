# Research Core

Phase 0 deterministic canonicalization and validation pipeline.

## Install

```bash
pip install -e .[dev]
```

## Canonicalize

```bash
python -m research_core.cli canon \
	--in tests/fixtures/raw_small_sample.txt \
	--out exec_outputs/runs/sample \
	--instrument ES \
	--tf 1min \
	--schema schemas/canon.schema.v1.json \
	--colmap schemas/colmap.raw_vendor_v1.json
```

## Validate canon

```bash
python -m research_core.cli validate canon \
	--input exec_outputs/runs/sample/canon.parquet \
	--schema schemas/canon.schema.v1.json \
	--contract exec_outputs/runs/sample/canon.contract.json
```

## Registry

```bash
python -m research_core.cli registry build \
	--data-root exec_outputs/runs \
	--out exec_outputs/registry/registry.json

python -m research_core.cli registry index-runs \
	--runs-root exec_outputs/runs \
	--out exec_outputs/runs/index.json
```


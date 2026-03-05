# Performance

This repo currently defines deterministic correctness contracts, but not a
formal performance contract/SLO section.

## Triage first

- Confirm the issue is not a determinism/correctness failure.
	See also: [Determinism Failures](determinism_failures.md)
- Reproduce with CI-equivalent commands before optimizing.
	See also: [Run CI Locally](../how-to/run_ci_locally.md)

PowerShell CI-equivalent gates:

```powershell
pytest -q
pytest -q
```

## Current boundary

- Contracts in this repo focus on artifact structure, hashing, determinism,
	and fail-loud behavior.
- No dedicated performance tuning/profiling contract page is currently listed in
	contracts reference.

Blocked by: [Contracts Reference](../reference/contracts/index.md)

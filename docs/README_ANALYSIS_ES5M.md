# ES 5m Analysis Runner

Run analysis gates from prebuilt artifacts (read-only analysis flow):

Runset discovery for ES 5m must be manifest-driven because `runs[].run_ref` values are hashed run references, not descriptive names.

First create/update the ES 5m runset list from canon manifests:

```powershell
./configs/analysis/make_es5m_runset.ps1
```

This helper reads seed runset `9e0fb70c502a553cdfe23a4ecb3d40e1d1e48d009cf70d99e2e2331e3163078e`, resolves each run ref to `canon.manifest.json`, filters by `instrument == "ES"` and `tf` matching `5m|300s|00:05`, then writes:

- `configs/analysis/runset.es_5m.json`
- `configs/analysis/runsets.es_5m.json`

```powershell
./docs/scripts/run_analysis_es_5m.ps1
```

What this executes:

1. `ci doctor` using `configs/analysis/doctor.es_5m.json`
2. `risk dashboard` across `configs/analysis/runsets.es_5m.json`
3. `risk runset` for each runset ID in that list

Open these outputs first:

- `exec_outputs/analysis/es_5m/doctor/ci.doctor.summary.json`
- `exec_outputs/analysis/es_5m/dashboard/dashboard.summary.json`
- `exec_outputs/analysis/es_5m/risk_runset/<runset_id>/risk.runset.summary.json`

Determinism note:

- The script pins `RESEARCH_CREATED_UTC` to `git show -s --format=%cI HEAD` to prevent timestamp churn across runs.
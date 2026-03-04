# ES 5m Build + Analysis Cohort

Use this flow when ES5m runs do not already exist and you need to materialize them, build a runset, promote a baseline, and run analysis gates.

Important:

- `runs[].run_ref` values are hashed paths; do not detect ES5m from run ref text.
- ES5m detection must be manifest-driven via each run's `canon.manifest.json` (`instrument == "ES"` and `tf` matching `5m|300s|00:05`).
- All scripts pin `RESEARCH_CREATED_UTC` to `git show -s --format=%cI HEAD` for deterministic timestamps.
- Generated pipeline artifacts are written to `configs/analysis/local/` (ignored by git), so tracked configs remain stable.

## One-command pipeline

```powershell
./docs/scripts/run_full_es5m_pipeline.ps1
```

This runs, in order:

1. `docs/scripts/register_es5m_dataset.ps1`
2. `docs/scripts/materialize_es5m_project.ps1`
3. `docs/scripts/create_es5m_runset.ps1`
4. `docs/scripts/promote_es5m_baseline.ps1`
5. `docs/scripts/run_analysis_es_5m.ps1`

## What each script produces

- `register_es5m_dataset.ps1`
	- Registers raw ES5m dataset and writes `configs/analysis/local/_es5m_dataset_id.txt`
	- Does not modify tracked configs
- `materialize_es5m_project.ps1`
	- Creates local generated project spec at `configs/analysis/local/project.es_5m.generated.json`
	- Materializes using `--runs-root exec_outputs/runs` (actual run dirs under `exec_outputs/runs/runs/<hash>`)
	- Prints ES5m run hashes created today based on `canon.manifest.json`
- `create_es5m_runset.ps1`
	- Generates explicit runset inputs from tracked template + local dataset id
	- Validates each run via `canon.manifest.json` for ES5m criteria
	- Writes `configs/analysis/local/runset.es_5m.generated.json`
	- Writes `configs/analysis/local/runsets.es_5m.generated.json`
- `promote_es5m_baseline.ps1`
	- Runs risk sweep for runset
	- Promotes baseline into `baselines/prod` with label `prod`
- `run_analysis_es_5m.ps1`
	- Accepts `-Runsets <path>` override
	- Defaults to `configs/analysis/local/runsets.es_5m.generated.json` when present
	- Runs `ci doctor`, `risk dashboard`, and per-runset `risk runset`

## Open these outputs first

- `exec_outputs/analysis/es_5m/doctor/ci.doctor.summary.json`
- `exec_outputs/analysis/es_5m/dashboard/dashboard.summary.json`
- `exec_outputs/analysis/es_5m/risk_runset/<runset_id>/risk.runset.summary.json`
- `baselines/prod/<runset_id>/baseline.card.json`

## Verify

Run explicit dashboard verification:

```powershell
.\docs\scripts\verify_es5m_dashboard.ps1
```

Success criteria:

- Script prints `DASHBOARD OK`
- `exec_outputs/analysis/es_5m/dashboard/dashboard.summary.json` exists

Open:

- `exec_outputs/analysis/es_5m/dashboard/dashboard.summary.json`
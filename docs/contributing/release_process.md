# Release Process

## Public release safety checklist

Use this checklist before cutting a public tag, release bundle, or docs snapshot.

### 1. Keep generated local outputs out of the release

- Do not publish anything from `exec_outputs/`.
- Do not publish anything from `site/`.
- Do not publish anything from `_tmp/`.
- Do not publish local virtual environments, caches, or packaging metadata such as `.venv/`, `__pycache__/`, `build/`, `dist/`, and `*.egg-info/`.

These paths are already ignored in `.gitignore`. The public-safe policy is: delete stale generated content before release, then regenerate only what you explicitly intend to ship.

### 2. Clean local artifacts before the final scan

PowerShell:

```powershell
Remove-Item -Recurse -Force exec_outputs, site, _tmp -ErrorAction SilentlyContinue
Get-ChildItem -Recurse -Directory -Filter __pycache__ | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force .venv, build, dist -ErrorAction SilentlyContinue
Get-ChildItem -Recurse -Directory -Include *.egg-info | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
```

### 3. Rescan tracked content for private-name regressions

PowerShell:

```powershell
git grep -n -I -E "ResearchCore|research_core|\bresearch\b|RESEARCH_[A-Z0-9_]+"
```

Expected result: no matches in tracked files.

### 4. Rescan the whole worktree, including ignored files

PowerShell:

```powershell
Get-ChildItem -Recurse -File -Force | Select-String -Pattern 'ResearchCore|research_core|\bresearch\b|RESEARCH_[A-Z0-9_]+' -CaseSensitive:$false
```

Expected result: any remaining matches should be confined to local-only paths you are about to delete or regenerate.

### 5. Re-run minimum sanity checks

PowerShell:

```powershell
python -m research_core.cli --help
pytest tests/test_cli_smoke.py -q
```

### 6. Watch for leak-prone environment metadata

Historically leak-prone names include:

- `RESEARCH_CREATED_UTC`
- `RESEARCH_GIT_COMMIT`
- other `RESEARCH_*` variables captured into generated manifests, plans, logs, or release notes

If local wrappers, CI jobs, or shell profiles still export old variable names, regenerated artifacts can reintroduce private strings even when tracked source files are clean.

### 7. External path warning

If the local workspace path itself still contains the old private name, absolute paths inside regenerated local artifacts can leak it. Rename the workspace path or regenerate artifacts from a neutral path before publishing any derived outputs.

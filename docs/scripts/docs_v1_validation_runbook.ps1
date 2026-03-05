# Run from repo root: G:\Research Core\Research Core
# Purpose: Docs-v1 <-> Reality validation bundle (no code/docs edits, no commits)

Set-Location "G:\Research Core\Research Core"

# 1) Sync + bootstrap
git checkout main
git pull
powershell -ExecutionPolicy Bypass -File tools/dev/bootstrap.ps1

# Deterministic timestamp from current commit (used throughout tutorial steps)
$createdUtc = (git show -s --format=%cI HEAD).Trim()
$env:RESEARCH_CREATED_UTC = $createdUtc

# 2) Dedicated validation workspace
$ts = Get-Date -Format "yyyyMMdd_HHmmss"
$valRoot = "_tmp/docs_v1_validation/$ts"
New-Item -ItemType Directory -Path $valRoot -Force | Out-Null

# Helpers
$failures = New-Object System.Collections.Generic.List[string]

function Invoke-LoggedStep {
  param(
    [Parameter(Mandatory=$true)][string]$Label,
    [Parameter(Mandatory=$true)][scriptblock]$Command,
    [Parameter(Mandatory=$true)][string]$LogFile
  )
  "=== $Label ===" | Tee-Object -FilePath $LogFile -Append
  $global:LASTEXITCODE = 0
  & $Command *>&1 | Tee-Object -FilePath $LogFile -Append
  if ($LASTEXITCODE -ne 0) {
    $msg = "FAILED: $Label (exit $LASTEXITCODE)"
    $msg | Tee-Object -FilePath $LogFile -Append
    $script:failures.Add($msg) | Out-Null
    return $false
  }
  return $true
}

function Capture-HelpIfExists {
  param(
    [Parameter(Mandatory=$true)][string]$Name,
    [Parameter(Mandatory=$true)][string]$CommandLine,
    [Parameter(Mandatory=$true)][string]$OutFile
  )
  "=== $Name ===" | Out-File -FilePath $OutFile -Encoding utf8
  $global:LASTEXITCODE = 0
  Invoke-Expression "$CommandLine *>&1" | Out-File -FilePath $OutFile -Append -Encoding utf8
  if ($LASTEXITCODE -ne 0) {
    "NOT AVAILABLE OR FAILED (exit $LASTEXITCODE): $CommandLine" | Out-File -FilePath $OutFile -Append -Encoding utf8
    $script:failures.Add("CLI help failed: $Name (exit $LASTEXITCODE)") | Out-Null
  }
}

function Get-RepoRelativePath {
  param(
    [Parameter(Mandatory=$true)][string]$FullPath,
    [Parameter(Mandatory=$true)][string]$RepoRoot
  )
  $root = [System.IO.Path]::GetFullPath($RepoRoot).TrimEnd('\\')
  $full = [System.IO.Path]::GetFullPath($FullPath)
  if ($full.StartsWith($root + "\\", [System.StringComparison]::OrdinalIgnoreCase)) {
    return $full.Substring($root.Length + 1)
  }
  return $full
}

# 3) Baseline truth capture
git rev-parse HEAD | Out-File -FilePath "$valRoot/git_commit.txt" -Encoding utf8
python --version 2>&1 | Out-File -FilePath "$valRoot/python_version.txt" -Encoding utf8

Capture-HelpIfExists -Name "root help"  -CommandLine "python -m research_core.cli --help"       -OutFile "$valRoot/cli_help_root.txt"
Capture-HelpIfExists -Name "canon help" -CommandLine "python -m research_core.cli canon --help" -OutFile "$valRoot/cli_help_canon.txt"
Capture-HelpIfExists -Name "risk help"  -CommandLine "python -m research_core.cli risk --help"  -OutFile "$valRoot/cli_help_risk.txt"
Capture-HelpIfExists -Name "ci help"    -CommandLine "python -m research_core.cli ci --help"    -OutFile "$valRoot/cli_help_ci.txt"

# 4A) docs/tutorials/es5m_end_to_end.md (exact tutorial commands)
$logEs5m = "$valRoot/runlog_es5m.txt"

Invoke-LoggedStep -Label "A1 & .\\docs\\scripts\\run_full_es5m_pipeline.ps1" -LogFile $logEs5m -Command {
  & .\docs\scripts\run_full_es5m_pipeline.ps1
} | Out-Null

Invoke-LoggedStep -Label "A2 & .\\docs\\scripts\\verify_es5m_dashboard.ps1" -LogFile $logEs5m -Command {
  & .\docs\scripts\verify_es5m_dashboard.ps1
} | Out-Null

# Extract values for later tutorial placeholders
$runsetsFile = "configs/analysis/local/runsets.es_5m.generated.json"
$RUNSET_ID = $null
if (Test-Path $runsetsFile) {
  try {
    $runsetPayload = Get-Content -Raw $runsetsFile | ConvertFrom-Json
    if ($runsetPayload.runset_ids.Count -gt 0) { $RUNSET_ID = [string]$runsetPayload.runset_ids[0] }
  } catch {
    $failures.Add("Unable to parse $runsetsFile for RUNSET_ID") | Out-Null
  }
}
if (-not $RUNSET_ID) {
  $failures.Add("RUNSET_ID not found from ES5m output; later tutorial commands that need RUNSET_ID may fail") | Out-Null
  $RUNSET_ID = "RUNSET_ID"
}

$baselineCard = "baselines/prod/$RUNSET_ID/baseline.card.json"
$BASELINE_ID = $null
if (Test-Path $baselineCard) {
  try {
    $bc = Get-Content -Raw $baselineCard | ConvertFrom-Json
    foreach ($k in @("baseline_id","baselineId","checksum","baseline_checksum","id")) {
      if ($bc.PSObject.Properties.Name -contains $k -and $bc.$k) { $BASELINE_ID = [string]$bc.$k; break }
    }
  } catch {
    $failures.Add("Unable to parse $baselineCard for BASELINE_ID") | Out-Null
  }
}
if (-not $BASELINE_ID) {
  $BASELINE_ID = "BASELINE_ID"
  $failures.Add("BASELINE_ID not found automatically; baseline promote may fail if placeholder is unresolved") | Out-Null
}

# 5) Snapshot after ES5m run
if (Test-Path "exec_outputs") {
  $repoRoot = (Get-Location).Path
  Get-ChildItem -Path "exec_outputs" -Recurse -File |
    ForEach-Object { Get-RepoRelativePath -FullPath $_.FullName -RepoRoot $repoRoot } |
    Sort-Object |
    Out-File -FilePath "$valRoot/exec_outputs_files_es5m.txt" -Encoding utf8
} else {
  "exec_outputs does not exist after ES5m run" | Out-File "$valRoot/exec_outputs_files_es5m.txt" -Encoding utf8
  $failures.Add("exec_outputs missing after ES5m run") | Out-Null
}

# 4B) baseline_promotion.md (exact tutorial commands)
$logBaseline = "$valRoot/runlog_baseline.txt"
Invoke-LoggedStep -Label 'B1 set RESEARCH_CREATED_UTC from git HEAD' -LogFile $logBaseline -Command { $env:RESEARCH_CREATED_UTC = $createdUtc } | Out-Null
Invoke-LoggedStep -Label "B2 runset validate"          -LogFile $logBaseline -Command { python -m research_core.cli runset validate --catalog exec_outputs/catalog --id $RUNSET_ID } | Out-Null
Invoke-LoggedStep -Label "B3 risk sweep"              -LogFile $logBaseline -Command { python -m research_core.cli risk sweep --catalog exec_outputs/catalog --runset $RUNSET_ID --out exec_outputs/pilot/risk } | Out-Null
Invoke-LoggedStep -Label "B4 baseline index refresh"  -LogFile $logBaseline -Command { python -m research_core.cli baseline index refresh --root baselines/prod } | Out-Null
Invoke-LoggedStep -Label "B5 baseline promote"        -LogFile $logBaseline -Command { python -m research_core.cli baseline promote --root baselines/prod --runset $RUNSET_ID --baseline-id $BASELINE_ID --label prod } | Out-Null
Invoke-LoggedStep -Label "B6 risk drift"              -LogFile $logBaseline -Command { python -m research_core.cli risk drift --catalog exec_outputs/catalog --root baselines/prod --runset $RUNSET_ID --label prod --out exec_outputs/pilot/drift } | Out-Null
Invoke-LoggedStep -Label "B7 risk dashboard"          -LogFile $logBaseline -Command { python -m research_core.cli risk dashboard --catalog exec_outputs/catalog --root baselines/prod --runsets configs/pilot/runsets.pilot.json --out exec_outputs/pilot/dashboard --label prod } | Out-Null
Invoke-LoggedStep -Label "B8 ci run"                  -LogFile $logBaseline -Command { python -m research_core.cli ci run --config ci.pilot.json } | Out-Null
Invoke-LoggedStep -Label "B9 ci doctor"               -LogFile $logBaseline -Command { python -m research_core.cli ci doctor --config configs/pilot/doctor.pilot.json } | Out-Null

# 4C) risk_runset_analysis.md
$logRisk = "$valRoot/runlog_risk.txt"
Invoke-LoggedStep -Label 'C1 set RESEARCH_CREATED_UTC from git HEAD' -LogFile $logRisk -Command { $env:RESEARCH_CREATED_UTC = $createdUtc } | Out-Null
Invoke-LoggedStep -Label "C2 runset create"           -LogFile $logRisk -Command { python -m research_core.cli runset create --catalog exec_outputs/catalog --spec configs/pilot/runset.pilot.json } | Out-Null
Invoke-LoggedStep -Label "C3 runset validate"         -LogFile $logRisk -Command { python -m research_core.cli runset validate --catalog exec_outputs/catalog --id $RUNSET_ID } | Out-Null
Invoke-LoggedStep -Label "C4 risk runset"             -LogFile $logRisk -Command { python -m research_core.cli risk runset --catalog exec_outputs/catalog --id $RUNSET_ID --out exec_outputs/pilot/risk_runset } | Out-Null
Invoke-LoggedStep -Label "C5 risk sweep (optional)"   -LogFile $logRisk -Command { python -m research_core.cli risk sweep --catalog exec_outputs/catalog --runset $RUNSET_ID --out exec_outputs/pilot/risk } | Out-Null

# 4D) drift_review_workflow.md
$logDrift = "$valRoot/runlog_drift.txt"
Invoke-LoggedStep -Label 'D1 set RESEARCH_CREATED_UTC from git HEAD' -LogFile $logDrift -Command { $env:RESEARCH_CREATED_UTC = $createdUtc } | Out-Null
Invoke-LoggedStep -Label "D2 risk drift"              -LogFile $logDrift -Command { python -m research_core.cli risk drift --catalog exec_outputs/catalog --root baselines/prod --runset $RUNSET_ID --label prod --out exec_outputs/pilot/drift } | Out-Null
Invoke-LoggedStep -Label "D3 risk dashboard"          -LogFile $logDrift -Command { python -m research_core.cli risk dashboard --catalog exec_outputs/catalog --root baselines/prod --runsets configs/pilot/runsets.pilot.json --out exec_outputs/pilot/dashboard --label prod } | Out-Null

# 4E) run_vs_run_compare.md
$logCompare = "$valRoot/runlog_compare.txt"
$RUNSET_A = $RUNSET_ID
$RUNSET_B = $RUNSET_A
if (Test-Path $runsetsFile) {
  try {
    $compareRunsetsPayload = Get-Content -Raw $runsetsFile | ConvertFrom-Json
    if ($compareRunsetsPayload.runset_ids.Count -ge 2) {
      $RUNSET_A = [string]$compareRunsetsPayload.runset_ids[0]
      $RUNSET_B = [string]$compareRunsetsPayload.runset_ids[1]
    }
  } catch {
    $failures.Add("Unable to parse $runsetsFile for compare runset_ids; falling back to RUNSET_B = RUNSET_A") | Out-Null
  }
}

Invoke-LoggedStep -Label 'E1 set RESEARCH_CREATED_UTC from git HEAD' -LogFile $logCompare -Command { $env:RESEARCH_CREATED_UTC = $createdUtc } | Out-Null
Invoke-LoggedStep -Label "E2 risk diff-runset"        -LogFile $logCompare -Command { python -m research_core.cli risk diff-runset --root baselines/prod --a $RUNSET_A --b $RUNSET_B --out exec_outputs/compare } | Out-Null
Invoke-LoggedStep -Label "E3 risk diff-runset labeled"-LogFile $logCompare -Command { python -m research_core.cli risk diff-runset --root baselines/prod --a $RUNSET_A --b $RUNSET_B --label-a prod --label-b prod --out exec_outputs/compare } | Out-Null
Invoke-LoggedStep -Label "E4 risk diff card-to-card"  -LogFile $logCompare -Command { python -m research_core.cli risk diff --a "baselines/prod/$RUNSET_A/baseline.card.json" --b "baselines/prod/$RUNSET_B/baseline.card.json" --out exec_outputs/compare } | Out-Null

# 6) Snapshot after all operational tutorials
if (Test-Path "exec_outputs") {
  $repoRoot = (Get-Location).Path
  Get-ChildItem -Path "exec_outputs" -Recurse -File |
    ForEach-Object { Get-RepoRelativePath -FullPath $_.FullName -RepoRoot $repoRoot } |
    Sort-Object |
    Out-File -FilePath "$valRoot/exec_outputs_files_after_ops.txt" -Encoding utf8
} else {
  "exec_outputs does not exist after ops run" | Out-File "$valRoot/exec_outputs_files_after_ops.txt" -Encoding utf8
  $failures.Add("exec_outputs missing after ops run") | Out-Null
}

# 7) Artifact presence scan
$patterns = @(
  "baseline.diff.json",
  "baseline.card.json",
  "baseline.promotions.json",
  "drift.report.json",
  "risk.runset.summary.json",
  "ci.summary.json"
)

$scan = New-Object System.Collections.Generic.List[string]
$scan.Add("=== scan in exec_outputs_files_es5m.txt ===") | Out-Null
$scan.AddRange((Select-String -Path "$valRoot/exec_outputs_files_es5m.txt" -Pattern $patterns -ErrorAction SilentlyContinue | ForEach-Object { $_.Line })) | Out-Null
$scan.Add("") | Out-Null
$scan.Add("=== scan in exec_outputs_files_after_ops.txt ===") | Out-Null
$scan.AddRange((Select-String -Path "$valRoot/exec_outputs_files_after_ops.txt" -Pattern $patterns -ErrorAction SilentlyContinue | ForEach-Object { $_.Line })) | Out-Null
$scan | Out-File -FilePath "$valRoot/scan_expected_artifacts.txt" -Encoding utf8

# Final status
$required = @(
  "git_commit.txt","python_version.txt","cli_help_root.txt",
  "runlog_es5m.txt","runlog_baseline.txt","runlog_risk.txt","runlog_drift.txt","runlog_compare.txt",
  "exec_outputs_files_es5m.txt","exec_outputs_files_after_ops.txt","scan_expected_artifacts.txt"
)

"Validation workspace: $valRoot"
"`nRequired files status:"
foreach ($f in $required) {
  $p = Join-Path $valRoot $f
  if (Test-Path $p) { "OK $f" } else { "MISSING $f" }
}

if ($failures.Count -gt 0) {
  "`nFailures captured (see run logs for details):"
  $failures | ForEach-Object { "- $_" }
} else {
  "`nNo command failures captured."
}

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$env:RESEARCH_CREATED_UTC = (git show -s --format=%cI HEAD).Trim()

$catalogDir = "exec_outputs/catalog"
$baselineRoot = "baselines/prod"
$runsetsPath = "configs/analysis/local/runsets.es_5m.generated.json"

if (-not (Test-Path $baselineRoot -PathType Container)) {
    Write-Host "ERROR: Missing baseline root '$baselineRoot'." -ForegroundColor Red
    Write-Host "Next action: create baseline root directory before promotion: New-Item -ItemType Directory -Path $baselineRoot" -ForegroundColor Yellow
    exit 2
}

if (-not (Test-Path $runsetsPath -PathType Leaf)) {
    Write-Host "ERROR: Missing runsets file '$runsetsPath'." -ForegroundColor Red
    Write-Host "Next action: run .\docs\scripts\create_es5m_runset.ps1 first." -ForegroundColor Yellow
    exit 2
}

$runsetsPayload = Get-Content -Raw $runsetsPath | ConvertFrom-Json
$runsetIds = @($runsetsPayload.runset_ids)
if ($runsetIds.Count -eq 0) {
    Write-Host "ERROR: No runset_ids in '$runsetsPath'." -ForegroundColor Red
    Write-Host "Next action: run .\docs\scripts\create_es5m_runset.ps1 first." -ForegroundColor Yellow
    exit 2
}

$runsetId = [string]$runsetIds[0]

$sweepOutput = python -m research_core.cli risk sweep --catalog $catalogDir --runset $runsetId --out $baselineRoot 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: risk sweep failed for runset '$runsetId'." -ForegroundColor Red
    $sweepOutput | ForEach-Object { Write-Host $_ }
    Write-Host "Next action: ensure runset exists and has valid linked run artifacts." -ForegroundColor Yellow
    exit 2
}

$cardPath = Join-Path (Join-Path $baselineRoot $runsetId) "baseline.card.json"
if (-not (Test-Path $cardPath -PathType Leaf)) {
    Write-Host "ERROR: Missing baseline card after sweep: '$cardPath'." -ForegroundColor Red
    Write-Host "Next action: inspect risk sweep output for failures and rerun." -ForegroundColor Yellow
    exit 2
}

$cardPayload = Get-Content -Raw $cardPath | ConvertFrom-Json
$baselineId = [string]$cardPayload.checksums.per_run_vector_sha256
if ([string]::IsNullOrWhiteSpace($baselineId) -or $baselineId -notmatch '^[a-f0-9]{64}$') {
    Write-Host "ERROR: Could not read baseline_id from '$cardPath' (checksums.per_run_vector_sha256)." -ForegroundColor Red
    Write-Host "Next action: verify baseline.card.json integrity and rerun risk sweep." -ForegroundColor Yellow
    exit 2
}

$promoteOutput = python -m research_core.cli baseline promote --root $baselineRoot --runset $runsetId --baseline-id $baselineId --label prod 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: baseline promote failed for runset '$runsetId'." -ForegroundColor Red
    $promoteOutput | ForEach-Object { Write-Host $_ }
    Write-Host "Next action: verify baseline root permissions and baseline_id/runset_id values." -ForegroundColor Yellow
    exit 2
}

$indexOutput = python -m research_core.cli baseline index refresh --root $baselineRoot 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: baseline index refresh failed for root '$baselineRoot'." -ForegroundColor Red
    $indexOutput | ForEach-Object { Write-Host $_ }
    Write-Host "Next action: verify '$baselineRoot' permissions and baseline card integrity, then rerun." -ForegroundColor Yellow
    exit 2
}

Write-Host "Promoted baseline for ES5m runset." -ForegroundColor Green
Write-Host "- runset_id: $runsetId"
Write-Host "- baseline_id: $baselineId"
Write-Host "- card: $cardPath"
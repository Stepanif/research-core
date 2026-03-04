Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Must be run from the repository root so relative paths are correct.
if (-not (Test-Path -LiteralPath '.githooks' -PathType Container) -or -not (Test-Path -LiteralPath 'mkdocs.yml' -PathType Leaf)) {
    throw "Run this script from the repository root (expected .githooks/ and mkdocs.yml)."
}

git config core.hooksPath .githooks

$pythonExe = $null
if (Test-Path -LiteralPath '.venv/Scripts/python.exe' -PathType Leaf) {
    $pythonExe = '.venv/Scripts/python.exe'
} else {
    $pythonCmd = Get-Command python -ErrorAction SilentlyContinue
    if ($null -ne $pythonCmd) {
        $pythonExe = $pythonCmd.Source
    }
}

if (-not $pythonExe) {
    throw 'Python interpreter not found. Create .venv or install python on PATH.'
}

if (Test-Path -LiteralPath 'requirements-docs.txt' -PathType Leaf) {
    & $pythonExe -m pip install -r requirements-docs.txt
    if ($LASTEXITCODE -ne 0) {
        throw "pip install failed with exit code $LASTEXITCODE"
    }
}

$hooksPath = git config --get core.hooksPath
Write-Host "[bootstrap] Success"
Write-Host "[bootstrap] hooksPath: $hooksPath"
Write-Host "[bootstrap] python: $pythonExe"
Write-Host '[bootstrap] Bypass once: RESEARCH_SKIP_DOCS_HOOK=1 git commit -m "<msg>"'

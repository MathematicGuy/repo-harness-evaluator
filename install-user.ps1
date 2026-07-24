$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$HomeDir = [Environment]::GetFolderPath("UserProfile")

function Copy-WithBackup {
    param([string]$Source, [string]$Destination)
    $Parent = Split-Path -Parent $Destination
    New-Item -ItemType Directory -Force -Path $Parent | Out-Null
    if (Test-Path $Destination) {
        Copy-Item -Recurse -Force $Destination "$Destination.bak-$Stamp"
    }
    Copy-Item -Recurse -Force $Source $Destination
}

Copy-WithBackup `
    (Join-Path $Root ".agents\skills\repo-harness-evaluator") `
    (Join-Path $HomeDir ".agents\skills\repo-harness-evaluator")

Get-ChildItem (Join-Path $Root ".codex\agents\*.toml") | ForEach-Object {
    Copy-WithBackup $_.FullName (Join-Path $HomeDir ".codex\agents\$($_.Name)")
}

Copy-WithBackup `
    (Join-Path $Root "profile\repo-harness-eval.config.toml") `
    (Join-Path $HomeDir ".codex\repo-harness-eval.config.toml")

Write-Host "Installed repo-harness-evaluator."
Write-Host "Run: codex --profile repo-harness-eval"
Write-Host 'Invoke: $repo-harness-evaluator evaluate the current repository'

# install-security-kit.ps1 - Instalador do Security Guardian & Web Audit Kit by Marcos Paulo
param (
    [string]$Destino = (Get-Location).Path,
    [switch]$Global
)

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "[*] Antigravity Security Guardian & Web Audit Kit" -ForegroundColor Green
Write-Host "    Criado por Marcos Paulo" -ForegroundColor DarkCyan
Write-Host "==========================================================" -ForegroundColor Cyan

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$origemAgent = Join-Path $scriptDir ".agent"
$origemAgents = Join-Path $scriptDir ".agents"

if (-not (Test-Path $origemAgent)) {
    Write-Host "[!] Pasta .agent nao encontrada em: $scriptDir" -ForegroundColor Red
    exit 1
}

if ($Global) {
    $targetBase = "$HOME\.gemini\config"
    Write-Host "[*] Instalando no escopo GLOBAL ($targetBase)..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Force -Path "$targetBase\agents", "$targetBase\skills", "$targetBase\workflows" | Out-Null
    
    Copy-Item "$origemAgent\agents\*" -Destination "$targetBase\agents\" -Recurse -Force
    Copy-Item "$origemAgent\skills\*" -Destination "$targetBase\skills\" -Recurse -Force
    Copy-Item "$origemAgent\workflows\*" -Destination "$targetBase\workflows\" -Recurse -Force
    
    Write-Host "[OK] Security Guardian Kit instalado GLOBALMENTE com sucesso!" -ForegroundColor Green
    Write-Host "[i] Agora qualquer projeto aberto nesta maquina pode usar @security-guardian!" -ForegroundColor Cyan
} else {
    Write-Host "[*] Instalando no projeto: $Destino..." -ForegroundColor Yellow
    $targetAgent = Join-Path $Destino ".agent"
    New-Item -ItemType Directory -Force -Path "$targetAgent\agents", "$targetAgent\skills", "$targetAgent\workflows" | Out-Null
    
    Copy-Item "$origemAgent\agents\*" -Destination "$targetAgent\agents\" -Recurse -Force
    Copy-Item "$origemAgent\skills\*" -Destination "$targetAgent\skills\" -Recurse -Force
    Copy-Item "$origemAgent\workflows\*" -Destination "$targetAgent\workflows\" -Recurse -Force
    
    if (Test-Path $origemAgents) {
        $targetAgents = Join-Path $Destino ".agents"
        New-Item -ItemType Directory -Force -Path "$targetAgents" | Out-Null
        Copy-Item "$origemAgents\*" -Destination "$targetAgents\" -Recurse -Force
    }

    Write-Host "[OK] Security Guardian Kit instalado no projeto com sucesso!" -ForegroundColor Green
    Write-Host "[i] Para testar agora, digite no chat: @security-guardian faca um scan de seguranca" -ForegroundColor Cyan
    Write-Host "    Ou execute no terminal: python .agent/skills/projeto-scan/scripts/scan_projeto.py ." -ForegroundColor Gray
}

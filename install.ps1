# install.ps1 - Instalador do Security Guardian & Web Audit Kit by Marcos Paulo
[CmdletBinding()]
param (
    [string]$Destino = (Get-Location).Path,
    [switch]$Global
)

$banner = @'
  ____                             _ _            ____                  _ _             
 / ___|  ___  ___ _   _ _ __(_) |_ _   _     / ___|_   _  __ _ _ __ __| (_) __ _ _ __  
 \___ \ / _ \/ __| | | | '__| | __| | | |   | |  _| | | |/ _` | '__/ _` | |/ _` | '_ \ 
  ___) |  __/ (__| |_| | |  | | |_| |_| |   | |_| | |_| | (_| | | | (_| | | (_| | | | |
 |____/ \___|\___|\__,_|_|  |_|\__|\__, |    \____|\__,_|\__,_|_|  \__,_|_|\__,_|_| |_|
                                    |___/                                                
               ============================================================
               [*] ANTIGRAVITY SECURITY GUARDIAN & WEB AUDIT KIT
                                Criado por Marcos Paulo
               ============================================================
'@

Write-Host ""
Write-Host $banner -ForegroundColor Cyan
Write-Host ""

$isRemote = $false
$scriptDir = $PSScriptRoot
if (-not $scriptDir -and $MyInvocation.MyCommand.Definition) {
    $scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
}

$origemAgent = $null
$origemAgents = $null
$tempExtract = $null

if ($scriptDir -and (Test-Path (Join-Path $scriptDir ".agent"))) {
    $origemAgent = Join-Path $scriptDir ".agent"
    $origemAgents = Join-Path $scriptDir ".agents"
} else {
    $isRemote = $true
    Write-Host "[*] Baixando a versao mais recente diretamente do GitHub..." -ForegroundColor Yellow
    $zipUrl = "https://github.com/marcospaulos23/security-guardian-kit/archive/refs/heads/main.zip"
    $tempZip = Join-Path $env:TEMP "security-guardian-kit-$(Get-Random).zip"
    $tempExtract = Join-Path $env:TEMP "security-guardian-kit-extract-$(Get-Random)"
    
    Invoke-WebRequest -Uri $zipUrl -OutFile $tempZip -UseBasicParsing
    Expand-Archive -Path $tempZip -DestinationPath $tempExtract -Force
    Remove-Item -Path $tempZip -Force -ErrorAction SilentlyContinue

    $repoRoot = Join-Path $tempExtract "security-guardian-kit-main"
    $origemAgent = Join-Path $repoRoot ".agent"
    $origemAgents = Join-Path $repoRoot ".agents"
}

if (-not (Test-Path $origemAgent)) {
    Write-Host "[!] Erro: Pasta .agent nao encontrada para instalacao." -ForegroundColor Red
    if ($tempExtract) { Remove-Item -Path $tempExtract -Recurse -Force -ErrorAction SilentlyContinue }
    exit 1
}

if ($Global) {
    $targetBase = "$HOME\.gemini\config"
    Write-Host "[*] Instalando no escopo GLOBAL ($targetBase)..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Force -Path "$targetBase\agents", "$targetBase\skills", "$targetBase\workflows" | Out-Null
    
    Copy-Item "$origemAgent\agents\*" -Destination "$targetBase\agents\" -Recurse -Force
    Copy-Item "$origemAgent\skills\*" -Destination "$targetBase\skills\" -Recurse -Force
    Copy-Item "$origemAgent\workflows\*" -Destination "$targetBase\workflows\" -Recurse -Force

    if (Test-Path $origemAgents) {
        $targetAgents = Join-Path $HOME ".agents"
        New-Item -ItemType Directory -Force -Path "$targetAgents" | Out-Null
        Copy-Item "$origemAgents\*" -Destination "$targetAgents\" -Recurse -Force
    }
    
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

if ($tempExtract) {
    Remove-Item -Path $tempExtract -Recurse -Force -ErrorAction SilentlyContinue
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor DarkCyan
Write-Host "[i] Repositorio: https://github.com/marcospaulos23/security-guardian-kit" -ForegroundColor DarkGray
Write-Host "============================================================" -ForegroundColor DarkCyan
Write-Host ""

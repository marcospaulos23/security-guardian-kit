#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scan_projeto.py - Scanner de Seguranca
Criado por: Seu Kit de Seguranca Pessoal
Detecta segredos expostos, API keys e padroes perigosos em projetos.
"""
import io
sys_stdout_backup = None

import os
import re
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

# Forca UTF-8 no terminal do Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ─── Paleta de cores no terminal ───────────────────────────────────────────────
RED    = "\033[91m"
ORANGE = "\033[93m"
YELLOW = "\033[33m"
BLUE   = "\033[94m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

# ─── Padroes de deteccao ────────────────────────────────────────────────────────
PADROES_SEGREDOS = [
    # AWS
    ("AWS Access Key ID",      r"AKIA[0-9A-Z]{16}",                                     "CRITICO"),
    ("AWS Secret Access Key",  r"(?i)aws.{0,20}secret.{0,20}['\"][0-9a-zA-Z/+]{40}['\"]", "CRITICO"),
    # GitHub
    ("GitHub Token",           r"gh[pousr]_[A-Za-z0-9_]{36,}",                          "CRITICO"),
    ("GitHub Classic Token",   r"github_pat_[A-Za-z0-9_]{82}",                          "CRITICO"),
    # Stripe
    ("Stripe Secret Key",      r"sk_live_[0-9a-zA-Z]{24,}",                             "CRITICO"),
    ("Stripe Publishable Key", r"pk_live_[0-9a-zA-Z]{24,}",                             "ALTO"),
    # Twilio
    ("Twilio Account SID",     r"AC[a-z0-9]{32}",                                       "ALTO"),
    ("Twilio Auth Token",      r"(?i)twilio.{0,20}['\"][a-z0-9]{32}['\"]",              "CRITICO"),
    # SendGrid
    ("SendGrid API Key",       r"SG\.[a-zA-Z0-9_-]{22}\.[a-zA-Z0-9_-]{43}",            "CRITICO"),
    # Google
    ("Google API Key",         r"AIza[0-9A-Za-z_-]{35}",                                "CRITICO"),
    ("Google OAuth",           r"[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com", "ALTO"),
    # JWT
    ("JWT Token hardcoded",    r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}", "CRITICO"),
    # Chaves privadas
    ("Chave Privada RSA",      r"-----BEGIN RSA PRIVATE KEY-----",                      "CRITICO"),
    ("Chave Privada SSH",      r"-----BEGIN OPENSSH PRIVATE KEY-----",                  "CRITICO"),
    ("Chave Privada EC",       r"-----BEGIN EC PRIVATE KEY-----",                       "CRITICO"),
    # Senhas hardcoded genericas
    ("Senha hardcoded",        r"(?i)(password|passwd|pwd|secret)\s*=\s*['\"][^'\"]{4,}['\"]", "ALTO"),
    ("API Key generica",       r"(?i)(api_key|apikey|api-key)\s*[=:]\s*['\"][^'\"]{8,}['\"]",   "ALTO"),
    ("Token generico",         r"(?i)(token|bearer)\s*[=:]\s*['\"][^'\"]{8,}['\"]",             "ALTO"),
    # URLs com credenciais
    ("URL com credenciais",    r"https?://[^:]+:[^@]+@[^\s\"']+",                       "CRITICO"),
    # Supabase
    ("Supabase Service Key",   r"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+", "CRITICO"),
]

PADROES_CODIGO_PERIGOSO = [
    ("eval() sem validacao",           r"\beval\s*\(",                                    "MEDIO"),
    ("exec() sem validacao",           r"\bexec\s*\(",                                    "MEDIO"),
    ("dangerouslySetInnerHTML",        r"dangerouslySetInnerHTML",                        "MEDIO"),
    ("innerHTML direto",               r"\.innerHTML\s*=\s*(?!['\"]\s*['\"])",            "MEDIO"),
    ("console.log com dados sensiveis",r"console\.log\s*\([^)]*(?:password|token|secret|key)[^)]*\)", "BAIXO"),
    ("TODO com seguranca",             r"(?i)#\s*todo.{0,30}(security|auth|password|token)", "BAIXO"),
    ("Chave de criptografia fraca",    r"(?i)(md5|sha1)\s*\(",                            "MEDIO"),
]

PADROES_DATABASE_SEGURANCA = [
    ("Possivel SQL Injection (raw query com interpolacao)", r"(?i)(\$queryRawUnsafe|\.queryUnsafe|\.raw)\s*\([^)]*(\+|`[^`]*\$\{)", "CRITICO"),
    ("SQL Injection em string concatenada",                 r"(?i)(SELECT|INSERT|UPDATE|DELETE)\s+[^;'\"]*['\"]\s*\+\s*[a-zA-Z0-9_]+", "CRITICO"),
    ("Conexao de Banco sem SSL exigido",                  r"(?i)(postgres|mysql):\/\/[^@]+@[^\/\s]+\/[^?\s]+(?:\?(?!.*sslmode=require)[^\s\"']*)?", "MEDIO"),
    ("Consulta expondo campo sensivel (password/token)",   r"(?i)(select|findMany|findUnique)\s*:\s*\{[^}]*(password|token|secret|hash)\s*:\s*true", "ALTO"),
    ("Supabase client com service_role exposto",          r"(?i)(supabaseKey|createClient)\s*\([^)]*service_role", "CRITICO"),
]


# Extensoes de arquivos para analisar
EXTENSOES_CODIGO = {
    ".js", ".jsx", ".ts", ".tsx", ".py", ".php", ".rb", ".go",
    ".java", ".cs", ".cpp", ".c", ".env", ".yaml", ".yml",
    ".json", ".toml", ".sh", ".bash", ".zsh",
}

# Pastas para ignorar
PASTAS_IGNORADAS = {
    "node_modules", ".git", "dist", "build", ".next", "__pycache__",
    "venv", ".venv", "vendor", "coverage", ".nyc_output", "out",
}

# Arquivos para sempre verificar
ARQUIVOS_SENSIVEIS = {".env", ".env.local", ".env.production", ".env.development"}


def ofuscar(texto: str, inicio: int = 4, fim: int = 4) -> str:
    """Ofusca um valor sensivel mostrando apenas inicio e fim."""
    if len(texto) <= inicio + fim + 3:
        return "*" * len(texto)
    return texto[:inicio] + "..." + texto[-fim:] if fim > 0 else texto[:inicio] + "..."


def cor_severidade(sev: str) -> str:
    mapa = {"CRITICO": RED, "ALTO": ORANGE, "MEDIO": YELLOW, "BAIXO": BLUE}
    return mapa.get(sev, RESET)


def emoji_severidade(sev: str) -> str:
    mapa = {"CRITICO": "🔴", "ALTO": "🟠", "MEDIO": "🟡", "BAIXO": "🔵"}
    return mapa.get(sev, "⚪")


def deve_ignorar(caminho: Path) -> bool:
    """Verifica se o arquivo/pasta deve ser ignorado."""
    for parte in caminho.parts:
        if parte in PASTAS_IGNORADAS:
            return True
    return False


def analisar_arquivo(caminho: Path, padroes: list) -> list:
    """Analisa um arquivo em busca dos padroes especificados."""
    achados = []
    try:
        conteudo = caminho.read_text(encoding="utf-8", errors="ignore")
        linhas = conteudo.splitlines()
        for nome, padrao, severidade in padroes:
            for num_linha, linha in enumerate(linhas, 1):
                matches = re.finditer(padrao, linha)
                for match in matches:
                    valor_encontrado = match.group(0)
                    achados.append({
                        "tipo": nome,
                        "severidade": severidade,
                        "arquivo": str(caminho),
                        "linha": num_linha,
                        "trecho": linha.strip()[:120],
                        "valor_ofuscado": ofuscar(valor_encontrado),
                    })
    except (PermissionError, OSError):
        pass
    return achados


def verificar_env_no_git(raiz: Path) -> list:
    """Verifica se .env esta sendo trackeado pelo Git."""
    alertas = []
    gitignore = raiz / ".gitignore"
    env_existe = (raiz / ".env").exists()

    if not env_existe:
        return alertas

    if not gitignore.exists():
        alertas.append({
            "tipo": ".env sem .gitignore",
            "severidade": "CRITICO",
            "arquivo": str(raiz / ".env"),
            "linha": 0,
            "trecho": "Arquivo .env existe mas nao ha .gitignore no projeto!",
            "valor_ofuscado": "N/A",
        })
        return alertas

    conteudo_gitignore = gitignore.read_text(encoding="utf-8", errors="ignore")
    padroes_env = [".env", ".env.*", "*.env"]
    coberto = any(p in conteudo_gitignore for p in padroes_env)

    if not coberto:
        alertas.append({
            "tipo": ".env nao coberto pelo .gitignore",
            "severidade": "CRITICO",
            "arquivo": str(gitignore),
            "linha": 0,
            "trecho": "O .env existe mas nao esta no .gitignore — pode ser commitado acidentalmente!",
            "valor_ofuscado": "N/A",
        })

    return alertas


def escanear_projeto(raiz_str: str) -> dict:
    """Escaneia o projeto completo e retorna todos os achados."""
    raiz = Path(raiz_str).resolve()
    todos_achados = []
    arquivos_analisados = 0
    arquivos_ignorados = 0

    print(f"\n{CYAN}{BOLD}[SCAN] Iniciando analise de seguranca em:{RESET} {raiz}")
    print(f"{CYAN}{'─' * 60}{RESET}")

    # Verifica .env no git
    alertas_env = verificar_env_no_git(raiz)
    todos_achados.extend(alertas_env)

    # Percorre todos os arquivos
    for caminho in raiz.rglob("*"):
        if not caminho.is_file():
            continue
        if deve_ignorar(caminho.relative_to(raiz)):
            arquivos_ignorados += 1
            continue
        if caminho.suffix.lower() not in EXTENSOES_CODIGO and caminho.name not in ARQUIVOS_SENSIVEIS:
            continue

        arquivos_analisados += 1

        # Scan de segredos
        achados_segredos = analisar_arquivo(caminho, PADROES_SEGREDOS)
        todos_achados.extend(achados_segredos)

        # Scan de codigo perigoso (apenas arquivos de codigo)
        achados_codigo = []
        if caminho.suffix.lower() in {".js", ".jsx", ".ts", ".tsx", ".py"}:
            achados_codigo = analisar_arquivo(caminho, PADROES_CODIGO_PERIGOSO)
            todos_achados.extend(achados_codigo)

        # Scan de seguranca de banco de dados
        achados_db = []
        if caminho.suffix.lower() in {".js", ".jsx", ".ts", ".tsx", ".py", ".sql", ".prisma", ".env"}:
            achados_db = analisar_arquivo(caminho, PADROES_DATABASE_SEGURANCA)
            todos_achados.extend(achados_db)

        achados_arquivo = achados_segredos + achados_codigo + achados_db
        if achados_arquivo:
            sev = achados_arquivo[0]["severidade"]
            cor = cor_severidade(sev)
            rel = caminho.relative_to(raiz)
            print(f"  {cor}[!] {sev}{RESET}  {rel}  ({len(achados_arquivo)} problema(s))")

    print(f"{CYAN}{'─' * 60}{RESET}")
    print(f"  Arquivos analisados : {BOLD}{arquivos_analisados}{RESET}")
    print(f"  Arquivos ignorados  : {arquivos_ignorados}")

    return {
        "raiz": str(raiz),
        "timestamp": datetime.now().isoformat(),
        "arquivos_analisados": arquivos_analisados,
        "achados": todos_achados,
    }


def gerar_relatorio_md(resultado: dict, caminho_saida: str = None) -> str:
    """Gera o relatório de segurança em Markdown."""
    achados = resultado["achados"]
    timestamp = datetime.fromisoformat(resultado["timestamp"]).strftime("%d/%m/%Y às %H:%M")

    # Contagem por severidade
    contagem = {"CRITICO": 0, "ALTO": 0, "MEDIO": 0, "BAIXO": 0}
    for a in achados:
        sev = a.get("severidade", "BAIXO")
        contagem[sev] = contagem.get(sev, 0) + 1

    total = sum(contagem.values())

    linhas = [
        "# 🛡️ Relatório de Segurança — Scan do Projeto",
        "",
        f"**Data:** {timestamp}",
        f"**Projeto:** `{resultado['raiz']}`",
        f"**Arquivos analisados:** {resultado['arquivos_analisados']}",
        "",
        "---",
        "",
        "## 📊 Resumo Executivo",
        "",
        "| Severidade | Quantidade | Status |",
        "|---|---|---|",
        f"| 🔴 CRÍTICO | {contagem['CRITICO']} | {'❌ Ação imediata!' if contagem['CRITICO'] > 0 else '✅ Limpo'} |",
        f"| 🟠 ALTO    | {contagem['ALTO']}    | {'⚠️ Corrigir antes do deploy' if contagem['ALTO'] > 0 else '✅ Limpo'} |",
        f"| 🟡 MÉDIO   | {contagem['MEDIO']}   | {'📋 Débito técnico' if contagem['MEDIO'] > 0 else '✅ Limpo'} |",
        f"| 🔵 BAIXO   | {contagem['BAIXO']}   | {'💡 Melhoria' if contagem['BAIXO'] > 0 else '✅ Limpo'} |",
        f"| **TOTAL**  | **{total}**  | |",
        "",
    ]

    if total == 0:
        linhas += [
            "---",
            "",
            "## ✅ Nenhum problema encontrado!",
            "",
            "O projeto passou na análise de segurança sem problemas detectados.",
            "Continue seguindo as boas práticas!",
            "",
        ]
    else:
        linhas += ["---", "", "## 🔍 Achados Detalhados", ""]

        # Agrupa por severidade
        ordem = ["CRITICO", "ALTO", "MEDIO", "BAIXO"]
        for sev in ordem:
            achados_sev = [a for a in achados if a["severidade"] == sev]
            if not achados_sev:
                continue

            emoji = emoji_severidade(sev)
            linhas += [f"### {emoji} {sev} ({len(achados_sev)} achado(s))", ""]

            for i, a in enumerate(achados_sev, 1):
                arquivo_rel = a["arquivo"].replace(resultado["raiz"], "").lstrip("/\\")
                linha_info = f"Linha {a['linha']}" if a["linha"] > 0 else "Configuração"

                linhas += [
                    f"**{i}. {a['tipo']}**",
                    "",
                    f"- 📁 **Arquivo:** `{arquivo_rel}`",
                    f"- 📍 **Localização:** {linha_info}",
                    f"- 🔎 **Valor detectado:** `{a['valor_ofuscado']}`",
                    f"- 💬 **Trecho:** `{a['trecho'][:100]}`",
                    "",
                ]

        # Plano de ação
        linhas += [
            "---",
            "",
            "## 🚨 Plano de Ação Prioritário",
            "",
        ]

        if contagem["CRITICO"] > 0:
            linhas += [
                "### 🔴 Ação Imediata (CRÍTICO)",
                "",
                "1. **Revogue** imediatamente todas as keys/tokens expostos nos provedores (AWS Console, GitHub Settings, etc.)",
                "2. **Gere novas credenciais** e mova para variáveis de ambiente",
                "3. **Verifique o histórico do Git** — se foi commitado, o dano já está feito:",
                "   ```bash",
                "   git log --all --full-history -- '*.env'",
                "   ```",
                "4. **Nunca** coloque credenciais diretamente no código",
                "",
            ]

        if contagem["ALTO"] > 0:
            linhas += [
                "### 🟠 Antes do Próximo Deploy (ALTO)",
                "",
                "1. Mova todos os valores sensíveis para `.env` (e garanta que está no `.gitignore`)",
                "2. Use `process.env.NOME_DA_VARIAVEL` no código",
                "3. No Vercel/Netlify, configure as variáveis no painel de controle",
                "",
            ]

        linhas += [
            "### 📋 Template de .env correto",
            "",
            "```bash",
            "# .env — NUNCA commite este arquivo!",
            "DATABASE_URL=sua_url_aqui",
            "API_KEY=sua_key_aqui",
            "SECRET_TOKEN=seu_token_aqui",
            "```",
            "",
            "```bash",
            "# .gitignore — garanta que isto está incluso",
            ".env",
            ".env.*",
            "*.env",
            "```",
            "",
            "---",
            f"*Relatório gerado em {timestamp} pelo Security Guardian*",
        ]

    relatorio = "\n".join(linhas)

    # Salva o arquivo
    if caminho_saida is None:
        caminho_saida = "relatorio-seguranca.md"

    Path(caminho_saida).write_text(relatorio, encoding="utf-8")
    return relatorio


def main():
    parser = argparse.ArgumentParser(
        description="🛡️ Scanner de Segurança — detecta segredos e padrões perigosos"
    )
    parser.add_argument(
        "caminho",
        nargs="?",
        default=".",
        help="Caminho do projeto a analisar (padrão: diretório atual)",
    )
    parser.add_argument(
        "--output", "-o",
        default="relatorio-seguranca.md",
        help="Arquivo de saída do relatório (padrão: relatorio-seguranca.md)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Exporta também um arquivo JSON com os dados brutos",
    )
    args = parser.parse_args()

    # Executa o scan
    resultado = escanear_projeto(args.caminho)
    achados = resultado["achados"]

    # Contagem final
    contagem = {"CRITICO": 0, "ALTO": 0, "MEDIO": 0, "BAIXO": 0}
    for a in achados:
        contagem[a.get("severidade", "BAIXO")] += 1

    # Gera o relatório
    print(f"\n{CYAN}{BOLD}[OK] Gerando relatorio...{RESET}")
    gerar_relatorio_md(resultado, args.output)

    if args.json:
        json_path = args.output.replace(".md", ".json")
        Path(json_path).write_text(
            json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"  JSON salvo em: {json_path}")

    # Sumário final no terminal
    total = sum(contagem.values())
    print(f"\n{BOLD}{'=' * 60}{RESET}")
    print(f"{BOLD}  RESULTADO DO SCAN{RESET}")
    print(f"{'=' * 60}")
    print(f"  {RED}[CRITICO] : {contagem['CRITICO']}{RESET}")
    print(f"  {ORANGE}[ALTO]    : {contagem['ALTO']}{RESET}")
    print(f"  {YELLOW}[MEDIO]   : {contagem['MEDIO']}{RESET}")
    print(f"  {BLUE}[BAIXO]   : {contagem['BAIXO']}{RESET}")
    print(f"{'─' * 60}")
    print(f"  Total de problemas: {BOLD}{total}{RESET}")
    print(f"{'=' * 60}")

    if contagem["CRITICO"] > 0:
        print(f"\n{RED}{BOLD}  [ATENCAO] {contagem['CRITICO']} problema(s) CRITICO(s) encontrado(s)!")
        print(f"  Revogue as credenciais IMEDIATAMENTE!{RESET}")
    elif total == 0:
        print(f"\n{GREEN}{BOLD}  [OK] Projeto limpo! Nenhum problema encontrado.{RESET}")
    else:
        print(f"\n{YELLOW}  [!] Verifique o relatorio para detalhes.{RESET}")

    print(f"\n  Relatorio salvo em: {BOLD}{args.output}{RESET}\n")

    # Retorna código de saída baseado na severidade
    if contagem["CRITICO"] > 0:
        sys.exit(2)  # CI/CD vai falhar
    elif contagem["ALTO"] > 0:
        sys.exit(1)  # Aviso
    else:
        sys.exit(0)  # Tudo ok


if __name__ == "__main__":
    main()

---
name: projeto-scan
description: >
  Análise completa de segurança de um projeto — detecta segredos expostos,
  API keys, tokens, senhas hardcoded, arquivos .env mal configurados e
  padrões de código perigosos. Gera relatório detalhado em Markdown.
triggers:
  - "analisa meu projeto"
  - "tem algum segredo exposto"
  - "verifica segurança"
  - "scan de segurança"
  - "api key exposta"
  - "roda o scan"
---

# 🔍 Skill: projeto-scan

Análise estática de segurança focada em **detecção de segredos expostos**
e padrões de código inseguro. Não requer ferramentas externas — usa apenas
Python puro.

## Quando Usar

Ative esta skill quando o usuário pedir:
- Análise de segurança do projeto
- Verificação de API keys ou tokens expostos
- Scan de senhas hardcoded
- Auditoria de arquivos .env
- Revisão de código por padrões perigosos

## Como Executar

```bash
# Na raiz do projeto
python .agent/skills/projeto-scan/scripts/scan_projeto.py .

# Em um diretório específico
python .agent/skills/projeto-scan/scripts/scan_projeto.py ./src

# Com saída em arquivo
python .agent/skills/projeto-scan/scripts/scan_projeto.py . --output relatorio-seguranca.md
```

## O Que o Script Detecta

### 🔑 Segredos e Credenciais (CRÍTICO)
- AWS Access Keys (`AKIA...`)
- API Keys genéricas (`api_key = "..."`)
- Tokens JWT hardcoded
- Tokens do GitHub, Stripe, Twilio, SendGrid
- Senhas em variáveis (`password = "..."`)
- Chaves privadas RSA/SSH

### 🌍 Variáveis de Ambiente (ALTO)
- Arquivo `.env` commitado no Git
- `.env` sem `.gitignore` cobrindo
- Valores reais em `.env.example`

### ⚠️ Código Perigoso (MÉDIO)
- Uso de `eval()` e `exec()`
- `dangerouslySetInnerHTML` sem sanitização
- URLs hardcoded com credenciais
- `console.log` com dados sensíveis

## Interpretando o Relatório

O script gera `relatorio-seguranca.md` com:

1. **Resumo executivo** — contagem por severidade
2. **Achados detalhados** — arquivo, linha, trecho ofuscado
3. **Plano de correção** — passos concretos para resolver

## Regras de Interpretação

- 🔴 **CRÍTICO** — pare o que está fazendo e corrija agora
- 🟠 **ALTO** — corrija antes do próximo deploy
- 🟡 **MÉDIO** — adicione à lista de débito técnico
- 🔵 **BAIXO** — corrija quando tiver tempo
- ✅ **LIMPO** — nenhum problema encontrado nessa categoria

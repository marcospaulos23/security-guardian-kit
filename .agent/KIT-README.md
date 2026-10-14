# 🛡️ Antigravity Security Guardian & Web Audit Kit — by Marcos Paulo

> Kit de elite para Auditoria de Segurança, Detecção de Segredos, Banco de Dados Seguro, Performance Web e Qualidade de Código para Antigravity IDE / Gemini AI.

[![Security: Hardened](https://img.shields.io/badge/Security-Hardened-red.svg)](#)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](#)
[![Vercel: 57 Rules](https://img.shields.io/badge/Vercel-57_Rules_Optimized-black.svg)](#)
[![Database: SQLi & RLS Protected](https://img.shields.io/badge/Database-SQLi_%26_RLS_Protected-green.svg)](#)

---

## ⚡ Instalação Rápida (1 Comando)

### Opção 1: Via Terminal do Antigravity (`npx skills add`)
Instale direto do GitHub sem precisar baixar nada manualmente:
```bash
npx skills add marcospaulos23/security-guardian-kit
```
*(Para instalar globalmente em todos os projetos da sua máquina: `npx skills add marcospaulos23/security-guardian-kit -g`)*

### Opção 2: Via PowerShell One-Liner (Nuvem / GitHub)
```powershell
irm https://raw.githubusercontent.com/marcospaulos23/security-guardian-kit/main/install.ps1 | iex
```

### Opção 3: No Computador Local
Se você já clonou este repositório:
```powershell
powershell -ExecutionPolicy Bypass -File .\install-security-kit.ps1
```
*(Ou passe `-Global` para instalar globalmente).*

---

## 🎯 Por Que Esse Kit É Especialista?

Desenvolvedores e empresas perdem dias e sofrem invasões por **chaves expostas no Git**, **queries sem sanitização (SQL Injection)**, **falta de Row Level Security (RLS)** e **deploys desprotegidos**.

Este Kit foi desenhado para agir como um **Especialista em Segurança & Auditoria Web**:
1. **Pensa como um atacante (Red Team)** para encontrar brechas.
2. **Protege como um defensor (Blue Team)** aplicando correções reais e objetivas.
3. **Audita banco de dados, performance Vercel e SEO técnico** antes do deploy.

---

## 📦 O Que Está Incluído no Kit

### 🛡️ Agentes Especialistas (18)

| Agente | Especialidade |
|---|---|
| `security-guardian` | **🆕 Guardião Principal**: Scanner de segredos, API keys, senhas hardcoded e código inseguro |
| `security-auditor` | Compliance de segurança, OWASP 2025, auditoria de código e arquitetura |
| `penetration-tester` | Mentalidade ofensiva, identificação de vetores de ataque e testes de intrusão |
| `database-architect` | **Novo Foco Seguro**: Prevenção de SQLi, Row Level Security (RLS), SSL pooling e migrações seguras |
| `performance-optimizer` | Otimização web, Core Web Vitals, bundle analyzer e carregamento ultrarrápido |
| `seo-specialist` | Auditoria de SEO técnico, E-E-A-T e otimização para motores de busca por IA (GEO) |
| `test-engineer` | Planejamento de suíte de testes, cobertura e automação de qualidade |
| `qa-automation-engineer` | Testes E2E com Playwright e validação contínua em CI |
| `debugger` | Investigação sistemática em 4 fases e análise de causa raiz |
| `devops-engineer` | DevSecOps, pipelines de CI/CD blindados e deploy seguro |
| `orchestrator` | Coordenação inteligente de múltiplos especialistas para missões complexas |
| `project-planner` | Quebra estratégica de tarefas e arquitetura antes da implementação |
| `code-archaeologist` | Auditoria de código legado, dependências obsoletas e refatoração segura |
| `explorer-agent` | Mapeamento completo e inteligência de repositórios |
| `documentation-writer` | Documentação técnica, manuais de segurança e changelogs |

---

### 🧩 Skills Modulares

#### 🔐 Segurança & Scanner
| Skill | Descrição |
|---|---|
| `projeto-scan` | **Motor Python nativo**: Detecta segredos expostos, senhas, SQL Injection e vazamentos |
| `vulnerability-scanner` | Mapeamento OWASP 2025, CVEs de dependências e supply chain security |
| `code-security` | Regras Semgrep para detecção de vulnerabilidades estáticas |
| `llm-security` | Proteção contra vulnerabilidades específicas de IA (OWASP LLM Top 10) |
| `red-team-tactics` | Táticas baseadas em MITRE ATT&CK para simulação de ataques |

#### 🗄️ Banco de Dados Seguro & Performance
| Skill | Descrição |
|---|---|
| `database-design` | **Hardened**: Prevenção de SQLi, RLS (Supabase/Postgres), SSL obrigatório, migrations seguras |
| `react-best-practices` | **Vercel Core**: 57 regras de ouro da engenharia da Vercel para performance e eliminação de waterfalls |
| `performance-profiling` | Métricas de Core Web Vitals, profiling de memória e bundle analysis |

#### 🧪 Testes & Qualidade
| Skill | Descrição |
|---|---|
| `testing-patterns` | Padrões de teste unitário, integração e mocking limpo |
| `webapp-testing` | Playwright E2E, testes de fluxo crítico e tolerância a falhas |
| `tdd-workflow` | Ciclo RED-GREEN-REFACTOR focado em confiabilidade |
| `code-review-checklist` | Checklist rigoroso de revisão de código e boas práticas |
| `lint-and-validate` | Verificação estática de tipos, sintaxe e formatação |
| `systematic-debugging` | 4 fases científicas de depuração de bugs |

#### 🌐 SEO & Infraestrutura
| Skill | Descrição |
|---|---|
| `seo-fundamentals` | Auditoria técnica de SEO, semântica e visibilidade orgânica |
| `geo-fundamentals` | Otimização para buscadores de IA (ChatGPT, Claude, Perplexity) |
| `deployment-procedures` | **DevSecOps**: Checklist pré-deploy com 5 categorias de verificação e rollback rápido |

---

### 🐍 Motor de Scan em Python (`scan_projeto.py`)

O kit inclui um scanner autônomo em Python sem dependências externas:

```bash
# Scan de segurança completo no projeto
python .agent/skills/projeto-scan/scripts/scan_projeto.py .

# Salvar relatório customizado em Markdown
python .agent/skills/projeto-scan/scripts/scan_projeto.py . --output auditoria.md

# Checklist rápido geral
python .agent/scripts/checklist.py .
```

#### O que o Scanner Detecta Automaticamente:
- 🔴 **CRÍTICO:** Chaves AWS, Tokens GitHub, Chaves Secret Stripe, Service Keys do Supabase, Chaves Privadas SSH/RSA, URLs com senha, SQL Injection via raw query interpolada.
- 🟠 **ALTO:** Senhas hardcoded em código, `.env` sem proteção no `.gitignore`, consultas expondo dados sensíveis (password/token).
- 🟡 **MÉDIO:** Conexões de banco sem SSL (`sslmode=require`), `eval()`, `exec()`, `dangerouslySetInnerHTML`, hashing fraco (MD5/SHA1).
- 🔵 **BAIXO:** `console.log` vazando credenciais em produção, TODOs críticos de segurança esquecidos.

---

### 🔄 Workflows & Slash Commands

| Comando | O Que Faz |
|---|---|
| `/test` | Gera rotas de teste e testes automatizados para seu código |
| `/debug` | Inicia o modo de investigação sistemática de bugs |
| `/deploy` | Executa o checklist DevSecOps antes de subir para produção |
| `/plan` | Cria o plano arquitetural completo antes de alterar código |
| `/orchestrate` | Aciona o comitê de múltiplos agentes para tarefas complexas |
| `/brainstorm` | Conduz descoberta guiada de requisitos com perguntas socráticas |

---

## 🎨 Procurando pelo Kit de UI & Design?

Para manter este kit 100% focado e cirúrgico em **Segurança, Auditoria e Qualidade**, os componentes de design visual, paletas de cores, tipografia e estilos foram organizados no:
👉 **[Antigravity UI/UX & Design Kit](./kits/design-kit/README.md)** (inclui `/ui-ux-pro-max`, `frontend-specialist`, paletas premium e design systems).

---

## 🚀 Como Usar no Dia a Dia

```
# Pedir uma auditoria completa de segurança
@security-guardian faça uma varredura de segurança no meu projeto

# Verificar vulnerabilidades em banco de dados
@database-architect verifique se há risco de SQL Injection ou falta de RLS nas minhas queries

# Gerar testes para uma rota ou função
/test crie testes unitários para a rota de autenticação

# Validar antes do deploy
/deploy verifique pré-requisitos de segurança para produção
```

---

*Criado e mantido por Marcos Paulo — Antigravity Agent Kit*

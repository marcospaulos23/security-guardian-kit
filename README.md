# 🛡️ Antigravity Security Guardian & Web Audit Kit — by Marcos Paulo

> Kit de elite para Auditoria de Segurança, Detecção de Segredos, Banco de Dados Seguro, Performance Web e Qualidade de Código para Antigravity IDE / Gemini AI.

[![Security: Hardened](https://img.shields.io/badge/Security-Hardened-red.svg)](#)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](#)
[![Vercel: 57 Rules](https://img.shields.io/badge/Vercel-57_Rules_Optimized-black.svg)](#)
[![Database: SQLi & RLS Protected](https://img.shields.io/badge/Database-SQLi_%26_RLS_Protected-green.svg)](#)

---

## ⚡ Instalação Rápida (1 Comando)

### Opção 1: Via Terminal do Antigravity (`npx skills add`)
Instale direto sem precisar baixar nada manualmente:
```bash
npx skills add security-guardian-kit
```
*(Para instalar globalmente em todos os projetos da sua máquina: `npx skills add security-guardian-kit -g`)*

### Opção 2: Via PowerShell One-Liner (Nuvem / GitHub)
```powershell
irm https://raw.githubusercontent.com/marcospaulos23/security-guardian-kit/main/install.ps1 | iex
```

### Opção 3: No Computador Local
Se você já clonou este repositório:
```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
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

### 🛡️ Agentes Especialistas & Skills Conectadas

| Agente | Especialidade | Skills que ele ativa automaticamente |
|---|---|---|
| `security-guardian` | **🆕 Guardião Principal**: Scanner de segredos, API keys e código inseguro | `projeto-scan`, `vulnerability-scanner`, `clean-code` |
| `security-auditor` | Compliance OWASP 2025, auditoria de código e arquitetura | `vulnerability-scanner`, `red-team-tactics`, `api-patterns` |
| `penetration-tester` | Mentalidade ofensiva, vetores de ataque e testes de intrusão | `vulnerability-scanner`, `red-team-tactics`, `api-patterns` |
| `database-architect` | **Banco Seguro**: Prevenção de SQLi, RLS, SSL pooling e migrations | `database-design`, `projeto-scan`, `vulnerability-scanner` |
| `performance-optimizer` | Core Web Vitals, bundle analyzer e carregamento ultrarrápido | `performance-profiling`, `clean-code` |
| `seo-specialist` | SEO técnico, E-E-A-T e otimização para buscas por IA (GEO) | `seo-fundamentals`, `geo-fundamentals` |
| `test-engineer` | Planejamento de testes, cobertura e automação de qualidade | `testing-patterns`, `tdd-workflow`, `webapp-testing` |
| `qa-automation-engineer` | Testes E2E com Playwright e validação contínua em CI | `webapp-testing`, `testing-patterns`, `lint-and-validate` |
| `debugger` | Investigação sistemática em 4 fases e análise de causa raiz | `systematic-debugging`, `clean-code` |
| `devops-engineer` | DevSecOps, pipelines de CI/CD blindados e deploy seguro | `deployment-procedures`, `server-management`, `powershell-windows`, `bash-linux` |
| `orchestrator` | Coordenação multi-agente para missões complexas | `parallel-agents`, `behavioral-modes`, `architecture`, `plan-writing` |
| `project-planner` | Quebra estratégica de tarefas e arquitetura pré-código | `app-builder`, `plan-writing`, `brainstorming` |
| `code-archaeologist` | Código legado, dependências obsoletas e refatoração | `clean-code`, `code-review-checklist` |
| `explorer-agent` | Mapeamento completo e inteligência de repositórios | `architecture`, `plan-writing`, `systematic-debugging` |
| `documentation-writer` | Documentação técnica, manuais de segurança e changelogs | `documentation-templates`, `clean-code` |
| `backend-specialist` | APIs REST/GraphQL, Node.js, Python e microsserviços | `api-patterns`, `nodejs-best-practices`, `python-patterns`, `database-design` |


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

# 🚀 Guia Prático: Como Subir os Kits de Agentes para o GitHub
*Passo a passo completo e à prova de erros para publicar o `security-guardian-kit` e o `design-pro-max-kit`*

---

## 📌 Visão Geral

Você tem as duas pastas prontas na sua pasta **Downloads**:
1. `C:\Users\Gamer\Downloads\security-guardian-kit`
2. `C:\Users\Gamer\Downloads\design-pro-max-kit`

Abaixo está o tutorial exato de como criar os repositórios no site do GitHub e subir cada pasta com comandos simples no terminal.

---

## 🛡️ PARTE 1: Subindo o Kit de Segurança (`security-guardian-kit`)

### Passo 1: Criar o Repositório no GitHub (No Navegador)
1. Acesse: **[github.com/new](https://github.com/new)**
2. Em **Repository name**, digite: `security-guardian-kit`
3. Em **Description** (opcional): `Antigravity Agent Kit para Auditoria de Segurança, Detecção de Segredos e Web Quality`
4. Deixe como **Public** (Público).
5. ⚠️ **IMPORTANTE:** **NÃO** marque as caixas *"Add a README file"*, *"Add .gitignore"* nem *"Choose a license"* (nós já criamos todos esses arquivos na sua pasta).
6. Clique no botão verde **Create repository**.
7. Copie a URL do seu repositório (exemplo: `https://github.com/SEU_USUARIO/security-guardian-kit.git`).

---

### Passo 2: Executar os Comandos no Terminal (PowerShell)
Abra o **PowerShell** no seu computador e execute os comandos abaixo, um por um:

```powershell
# 1. Entrar na pasta do kit de segurança em Downloads
cd C:\Users\Gamer\Downloads\security-guardian-kit

# 2. Inicializar o Git nesta pasta
git init

# 3. Adicionar todos os arquivos
git add .

# 4. Fazer o primeiro commit
git commit -m "feat: lancamento inicial do security-guardian-kit"

# 5. Definir a branch principal como 'main'
git branch -M main

# 6. Conectar ao repositório do GitHub (Substitua SEU_USUARIO pelo seu username do GitHub)
git remote add origin https://github.com/SEU_USUARIO/security-guardian-kit.git

# 7. Enviar os arquivos para o GitHub
git push -u origin main
```

*(Se o Git pedir login na primeira vez, basta autorizar na janela do navegador que abrir).*

---

## 🎨 PARTE 2: Subindo o Kit de Design (`design-pro-max-kit`)

### Passo 1: Criar o Repositório no GitHub (No Navegador)
1. Acesse novamente: **[github.com/new](https://github.com/new)**
2. Em **Repository name**, digite: `design-pro-max-kit`
3. Em **Description** (opcional): `Antigravity Agent Kit para UI/UX, Design Systems, Paletas Premium e Micro-animações`
4. Deixe como **Public** (Público).
5. ⚠️ **IMPORTANTE:** Também **NÃO** marque nenhuma caixinha de README/license.
6. Clique em **Create repository**.
7. Copie a URL gerada (exemplo: `https://github.com/SEU_USUARIO/design-pro-max-kit.git`).

---

### Passo 2: Executar os Comandos no Terminal (PowerShell)
No mesmo terminal PowerShell, execute:

```powershell
# 1. Entrar na pasta do kit de design em Downloads
cd C:\Users\Gamer\Downloads\design-pro-max-kit

# 2. Inicializar o Git nesta pasta
git init

# 3. Adicionar todos os arquivos
git add .

# 4. Fazer o primeiro commit
git commit -m "feat: lancamento inicial do design-pro-max-kit"

# 5. Definir a branch principal como 'main'
git branch -M main

# 6. Conectar ao repositório do GitHub (Substitua SEU_USUARIO pelo seu username do GitHub)
git remote add origin https://github.com/SEU_USUARIO/design-pro-max-kit.git

# 7. Enviar os arquivos para o GitHub
git push -u origin main
```

---

## 🔄 Como Atualizar os Repositórios no Futuro

Sempre que você criar novas skills, adicionar scripts ou modificar algo nos agentes e quiser enviar a atualização para o GitHub, basta abrir o terminal na pasta correspondente e rodar apenas estes 3 comandos:

```powershell
# 1. Adicionar o que mudou
git add .

# 2. Salvar com uma mensagem explicando a melhoria
git commit -m "feat: adicionada nova regra de seguranca"

# 3. Enviar para o GitHub
git push
```

---

## 💡 Dica Bônus: Se o Git pedir Senha/Token no Terminal

Se ao rodar `git push` o terminal pedir senha e não aceitar a senha normal da sua conta do GitHub, o GitHub exige um **Personal Access Token**:

1. No GitHub, vá em: **Settings** (no seu avatar) → **Developer settings** (no final do menu à esquerda) → **Personal access tokens** → **Tokens (classic)**.
2. Clique em **Generate new token (classic)**.
3. Marque a caixinha **`repo`** (dá permissão de enviar código).
4. Clique em **Generate token** no final da página e copie o token gerado.
5. Quando o terminal pedir **Password**, cole esse token!

---

*Guia gerado por Marcos Paulo para o Antigravity Agent Kit*

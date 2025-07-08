# DashboardsPython
Este repositório contém códigos desenvolvidos para a disciplina de Dashboards em Python do MBA em Ciência de Dados

## Setup
Aplicação Streamlit com dependências gerenciadas pelo [uv](https://github.com/astral-sh/uv).

---

## ✅ Pré-requisitos

- **Python >= 3.12**
- [uv instalado](https://github.com/astral-sh/uv)

Instalação do uv via pip:

```bash
pip install uv
````

Ou via script oficial:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

---

## ⚡️ Setup do projeto

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

2. **Crie o ambiente virtual com uv**

```bash
uv venv
```

3. **Instale as dependências**

```bash
uv pip install
```

Ou, para instalar e gerar o lockfile:

```bash
uv pip install --create-lockfile
```

---

## ▶️ Execução da aplicação

### **Ativando o venv**

No Linux/macOS:

```bash
source .venv/bin/activate
streamlit run app.py
```

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
streamlit run app.py
```

---

### **Ou executando diretamente sem ativar**

```bash
./.venv/bin/streamlit run app.py
```

---

## Gerando lockfile (opcional)

Para atualizar ou criar o `uv.lock`:

```bash
uv pip install --relock
```

---

## Estrutura principal

* `pyproject.toml` – definição de dependências do projeto
* `uv.lock` – lockfile gerado (versões exatas)
* `app.py` – script Streamlit principal

---

## Notas

* Para instalar geopandas corretamente, certifique-se que GDAL, GEOS e PROJ estão disponíveis no sistema.
* uv é ultrarrápido e substitui pip/pip-tools para builds consistentes.

---

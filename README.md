# 📌 PROJETO – DASHBOARD COM DADOS DO RECLAME AQUI
## MBA em Ciência de Dados – Disciplina: Dashboards em Python
* Prof. Túlio Ribeiro
## Alunos
* Igor Florentino
* Rodrigo Galba
* João Paulo

### **Descrição**

* O objetivo é criar um painel interativo com **Streamlit** utilizando dados de reclamações do Reclame Aqui.

### **O painel deve conter**

* **Série temporal** do número de reclamações.
* **Frequência de reclamações por estado.**
* **Frequência por tipo de** `STATUS`.
* **Distribuição do tamanho dos textos** das reclamações (coluna `DESCRIÇÃO`).
* **WordCloud** com as palavras mais frequentes nos textos das descrições.
* **Mapa do Brasil com heatmap** mostrando a quantidade de reclamações por **ano**, com granularidade por **estado ou município**.

  > O mapa **deve conter um seletor para o ano** que será visualizado.

### **Os gráficos devem ser interativos e filtráveis com seletores de:**

* Estado
* Status
* Faixa de tamanho do texto da reclamação

# DashboardsPython
Este repositório contém códigos desenvolvidos para a disciplina de Dashboards em Python do MBA em Ciência de Dados

[Acesse a aplicação aqui](https://dashboardspython-ulegbeppwubxo4fmj9jvyj.streamlit.app/)

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

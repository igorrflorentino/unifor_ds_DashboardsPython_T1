# DashboardsPython
Este repositório contém códigos desenvolvidos para a disciplina de Dashboards em Python do MBA em Ciência de Dados da Unifor.

## 📊 Sobre o Projeto
Dashboard interativo desenvolvido com **Streamlit** para análise de dados do Reclame Aqui sobre a empresa Ibyte, incluindo:
- 📈 Séries temporais de reclamações
- 🗺️ Mapas geográficos do Brasil
- ☁️ Nuvens de palavras das descrições
- 📊 Gráficos de distribuição e frequência

---

## ✅ Pré-requisitos

- **Python >= 3.12**
- **Conda** (Miniconda ou Anaconda)
- **uv** (gerenciador de pacotes moderno)

### Instalação do uv

```bash
# Via Homebrew (macOS)
brew install uv

# Via pip
pip install uv

# Via script oficial (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 🚀 Setup do Projeto

### **Método 1: Conda + uv (Recomendado)**

Combina o melhor dos dois mundos: Conda para dependências do sistema e uv para pacotes Python.

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/DashboardsPython.git
cd DashboardsPython

# 2. Crie o ambiente conda com dependências do sistema
conda env create -f environment.yml

# 3. Ative o ambiente
conda activate unifor_df_dashboards-python_T1

# 4. Instale o projeto e dependências Python com uv
uv pip install -e .

# 5. Execute a aplicação
cd dashboards
streamlit run app.py
```

### **Método 2: Somente uv (Alternativo)**

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/DashboardsPython.git
cd DashboardsPython

# 2. Crie ambiente virtual
uv venv --python 3.12

# 3. Ative o ambiente
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate.bat  # Windows

# 4. Instale dependências
uv pip install -e .

# 5. Execute a aplicação
cd dashboards
streamlit run app.py
```

### **Método 3: Somente Conda (Tradicional)**

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/DashboardsPython.git
cd DashboardsPython

# 2. Crie ambiente conda
conda env create -f environment.yml

# 3. Ative o ambiente
conda activate unifor_df_dashboards-python_T1

# 4. Execute a aplicação
cd dashboards
streamlit run app.py
```

---

## ⚡️ Execução Rápida

### **Com ambiente conda ativo:**
```bash
conda activate unifor_df_dashboards-python_T1
cd dashboards
streamlit run app.py
```

### **Com uv (sem ativar ambiente):**
```bash
cd dashboards
uv run streamlit run app.py
```

### **Executar em porta específica:**
```bash
streamlit run app.py --server.port 8502
```

---

## 📁 Estrutura do Projeto

```
DashboardsPython/
├── dashboards/
│   └── app.py              # Aplicação Streamlit principal
├── datasets/
│   ├── RECLAMEAQUI_IBYTE.csv    # Dados das reclamações
│   └── brazil-states.geojson    # Dados geográficos do Brasil
├── notebook/
│   └── Projeto.ipynb      # Notebook de análise exploratória
├── referencias/
│   ├── aula1.ipynb        # Material de referência
│   └── aula2.ipynb
├── pyproject.toml         # Configuração do projeto Python
├── environment.yml        # Configuração do ambiente Conda
├── requirements.txt       # Lista de dependências
└── README.md             # Este arquivo
```

---

## 🔧 Gerenciamento de Dependências

### **Adicionar nova dependência:**
```bash
# Edite pyproject.toml na seção [project.dependencies]
# Depois execute:
uv pip install -e .
```

### **Atualizar dependências:**
```bash
uv pip install --upgrade -e .
```

### **Instalar dependências de desenvolvimento:**
```bash
uv pip install -e ".[dev]"
```

---

## 🏗️ Arquitetura Moderna

Este projeto utiliza uma arquitetura moderna de desenvolvimento Python:

- **`pyproject.toml`**: Configuração central do projeto (PEP 518)
- **`environment.yml`**: Gerencia dependências do sistema via Conda
- **`uv`**: Gerenciador de pacotes Python ultrarrápido
- **Conda + uv**: Combo poderoso para ambientes reproduzíveis

### **Por que esta combinação?**

1. **Conda**: Excelente para dependências do sistema (GDAL, GEOS, PROJ para GeoPandas)
2. **uv**: 10-100x mais rápido que pip para dependências Python
3. **pyproject.toml**: Padrão moderno para configuração de projetos Python

---

## 📝 Comandos Úteis

```bash
# Listar ambientes conda
conda env list

# Exportar ambiente atual
conda env export > environment.yml

# Remover ambiente
conda env remove -n unifor_df_dashboards-python_T1

# Verificar dependências instaladas
uv pip list

# Executar sem instalar
uv run --with streamlit streamlit run dashboards/app.py
```

---

## 🐛 Troubleshooting

### **Erro com GeoPandas:**
```bash
# Instale dependências do sistema primeiro
conda install gdal geos proj fiona
```

### **Erro de porta ocupada:**
```bash
# Use porta diferente
streamlit run app.py --server.port 8502
```

### **Ambiente não encontrado:**
```bash
# Recrie o ambiente
conda env remove -n unifor_df_dashboards-python_T1
conda env create -f environment.yml
```

---

## 📋 Notas Importantes

- ⚠️ **GeoPandas**: Requer dependências do sistema (GDAL, GEOS, PROJ)
- 🔄 **uv**: Substituto moderno e ultrarrápido do pip
- 🐍 **Python 3.12+**: Versão mínima requerida
- 📦 **Conda**: Recomendado para dependências do sistema
- ⚡ **Performance**: uv é 10-100x mais rápido que pip para instalação

---

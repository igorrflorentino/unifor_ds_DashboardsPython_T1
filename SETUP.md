# Configuração do Ambiente de Desenvolvimento

Este projeto utiliza **pyenv** para gerenciamento de versões do Python e **uv** para gerenciamento de dependências e ambientes virtuais.

## Pré-requisitos

Certifique-se de ter instalado:
- [pyenv](https://github.com/pyenv/pyenv#installation)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Configuração do Ambiente

### 1. Instalar Python 3.12.11 (se não estiver instalado)

```bash
pyenv install 3.12.11
```

### 2. Configurar Python para o projeto

```bash
pyenv local 3.12.11
```

### 3. Sincronizar dependências e criar ambiente virtual

O comando `uv sync` automaticamente cria o ambiente virtual e instala todas as dependências:
```bash
uv sync
```

Este comando:
- Cria automaticamente um ambiente virtual em `.venv/` se não existir
- Instala todas as dependências definidas em `pyproject.toml`
- Usa o arquivo `uv.lock` para garantir versões exatas
- Não requer ativação manual do ambiente

### 4. Verificar instalação

```bash
uv pip list
```

## Executar o Dashboard

### Método 1: No navegador do VS Code (Simple Browser)

1. **Execute o Streamlit em modo headless:**
```bash
uv run streamlit run dashboards/app.py --server.headless true --server.port 8501
```

### Método 2: No navegador externo

```bash
uv run streamlit run dashboards/app.py
```

### Método 3: Com ambiente ativado manualmente

```bash
source .venv/bin/activate
streamlit run dashboards/app.py
```

## Ferramentas de Desenvolvimento

### Formatação de código
```bash
uv run black .
```

### Linting
```bash
uv run ruff check .
```

### Executar testes
```bash
uv run pytest
```

### Jupyter Lab
```bash
uv run jupyter lab
```

## Estrutura do Projeto

```
DashboardsPython/
├── dashboards/         # Código principal do dashboard
├── datasets/           # Datasets para análise
├── notebook/           # Notebooks Jupyter
├── referencias/        # Material de referência
├── pyproject.toml     # Configuração do projeto e dependências
├── uv.lock           # Lock file para reprodutibilidade
└── .python-version   # Versão do Python para pyenv
```

## Vantagens desta Configuração

- **pyenv**: Gerencia múltiplas versões do Python
- **uv**: Instalação ultra-rápida de dependências
- **Reprodutibilidade**: arquivo `.python-version` e `uv.lock` garantem que todos usem a mesma configuração
- **Isolamento**: Ambiente virtual separado para o projeto

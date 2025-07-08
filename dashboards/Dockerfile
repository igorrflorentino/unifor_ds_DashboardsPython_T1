# Usa Python 3.12 slim
FROM python:3.12-slim

# Instala dependências do sistema para geopandas e outros pacotes
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    gdal-bin \
    libgdal-dev \
    libproj-dev \
    proj-data \
    && rm -rf /var/lib/apt/lists/*

# Instala uv via pip
RUN pip install uv

# Define diretório de trabalho
WORKDIR /app

# Copia pyproject.toml
COPY dashboards/pyproject.toml ./

# Cria venv e instala dependências com uv
RUN uv venv && uv pip install -r pyproject.toml

# Dentro do seu Dockerfile
COPY datasets ./datasets


# Copia o restante do projeto
COPY dashboards .

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Comando default para rodar o app Streamlit (ajuste conforme seu script)
CMD ["./.venv/bin/streamlit", "run", "app.py"]

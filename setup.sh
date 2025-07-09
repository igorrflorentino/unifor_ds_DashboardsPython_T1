#!/bin/bash
# Setup script para o projeto DashboardsPython

set -e

echo "🚀 Configurando ambiente para DashboardsPython..."

# Verificar se conda está instalado
if ! command -v conda &> /dev/null; then
    echo "❌ Conda não encontrado. Instale Miniconda ou Anaconda primeiro."
    exit 1
fi

# Verificar se uv está instalado
if ! command -v uv &> /dev/null; then
    echo "📦 Instalando uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source ~/.bashrc || source ~/.zshrc || true
fi

echo "🐍 Criando ambiente conda..."
conda env create -f environment.yml -y

echo "✅ Ativando ambiente..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate unifor_df_dashboards-python_T1

echo "📦 Instalando dependências Python com uv..."
uv pip install -e .

echo "🎉 Setup concluído! Para usar:"
echo ""
echo "  conda activate unifor_df_dashboards-python_T1"
echo "  cd dashboards" 
echo "  streamlit run app.py"
echo ""

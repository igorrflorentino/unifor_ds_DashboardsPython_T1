import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud
import geopandas as gpd
import json

# Carregue os dados
df = pd.read_csv('datasets/RECLAMEAQUI_IBYTE.csv')
df['TEMPO'] = pd.to_datetime(df['TEMPO'])
df[['MUNICIPIO', 'UF']] = df['LOCAL'].str.split('-', n=1, expand=True)
df['MUNICIPIO'] = df['MUNICIPIO'].str.strip()
df['UF'] = df['UF'].str.strip()

st.title("Dashboard Reclame Aqui - Ibyte")

# Filtros
estados = st.multiselect("Selecione o(s) Estado(s):", df['UF'].unique())
status = st.multiselect("Selecione o(s) Status:", df['STATUS'].unique())
min_palavras, max_palavras = st.slider(
    "Faixa de tamanho do texto da reclamação (nº de palavras):",
    0, 500, (0, 100)
)

def count_palavras(texto):
    return len(str(texto).split())

df['N_PALAVRAS'] = df['DESCRICAO'].apply(count_palavras)

# Aplicando filtros
df_filt = df.copy()
if estados:
    df_filt = df_filt[df_filt['UF'].isin(estados)]
if status:
    df_filt = df_filt[df_filt['STATUS'].isin(status)]
df_filt = df_filt[(df_filt['N_PALAVRAS'] >= min_palavras) & (df_filt['N_PALAVRAS'] <= max_palavras)]

# Série temporal
st.subheader("Série Temporal do Número de Reclamações")
serie = df_filt.groupby(df_filt['TEMPO'].dt.to_period('M')).size()
serie.index = serie.index.astype(str)
fig1 = px.line(serie, labels={'value':'Nº Reclamações', 'index':'Data'})
st.plotly_chart(fig1)

# Frequência por estado
st.subheader("Frequência de Reclamações por Estado")
fig2 = px.bar(df_filt['UF'].value_counts(), labels={'index':'Estado', 'value':'Nº Reclamações'})
st.plotly_chart(fig2)

# Frequência por STATUS
st.subheader("Frequência por Tipo de STATUS")
fig3 = px.bar(df_filt['STATUS'].value_counts(), labels={'index':'STATUS', 'value':'Nº Reclamações'})
st.plotly_chart(fig3)

# Distribuição do tamanho dos textos
st.subheader("Distribuição do Tamanho dos Textos das Reclamações")
fig4, ax = plt.subplots()
df_filt['N_PALAVRAS'].plot(kind='hist', bins=30, alpha=0.6, ax=ax, density=True)
df_filt['N_PALAVRAS'].plot(kind='kde', ax=ax)
ax.set_xlabel('Nº de Palavras')
st.pyplot(fig4)

# WordCloud
st.subheader("WordCloud das Palavras Mais Frequentes nas Descrições")
from wordcloud import STOPWORDS

# Stopwords padrão + adicionais do português
stopwords = set(STOPWORDS).union({
    'de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'é',
    'com', 'não', 'uma', 'os', 'no', 'se', 'na', 'por', 'mais', 'as',
    'dos', 'como', 'mas', 'foi', 'ao', 'ele', 'das', 'tem', 'à', 'seu',
    'sua', 'ou', 'ser', 'quando', 'muito', 'há', 'nos', 'já', 'está',
    'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre',
    'depois', 'sem', 'mesmo', 'aos', 'seus', 'quem', 'nas', 'me', 'esse',
    'eles', 'estão', 'você', 'tinha', 'foram', 'essa', 'num', 'nem',
    'suas', 'meu', 'às', 'minha', 'têm', 'numa', 'pelos', 'elas',
    'havia', 'seja', 'qual', 'será', 'nós', 'tenho', 'lhe', 'deles',
    'essas', 'esses', 'pelas', 'este', 'fosse', 'dele', 'tu', 'te',
    'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus',
    'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas',
    'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas',
    'isto', 'aquilo', 'pra', 'disse', 'fiz', 'deixei', 'dia', 'nada', 'fui',
    'não', 'sou', 'porém', 'estava', 'era', 'tempo', 'levei', 'pois', 'ainda', 'trocar', 'nao', 'agora',
    'hoje', 'lá', 'informado', 'poderia', 'quero', 'estou', 'peça', 'após', 'vou', 'ja',
    'tive', 'volta', 'deu', 'ate', 'hora', 'bem', 'então', 'menos', 'liguei'
})

texto = " ".join(df_filt['DESCRICAO'].astype(str))

wc = WordCloud(
    width=800,
    height=400,
    background_color="white",
    colormap="viridis",
    max_words=100,
    stopwords=stopwords
).generate(texto)

fig5, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig5)

# Mapa do Brasil com Reclamações
# Lista de siglas válidas (exemplo, carregue do geojson como já fez)
siglas_validas = [
    "AC","AL","AM","AP","BA","CE","DF","ES","GO","MA","MG","MS","MT",
    "PA","PB","PE","PI","PR","RJ","RN","RO","RR","RS","SC","SE","SP","TO"
]

# Filtra apenas linhas com UF válida
df = df[df['UF'].isin(siglas_validas)]

# Debug pós-limpeza
ufs_df = sorted(df['UF'].dropna().unique())

# --- Separação de MUNICIPIO e UF ---
df[['MUNICIPIO', 'UF']] = df['LOCAL'].str.split('-', n=1, expand=True)
df['MUNICIPIO'] = df['MUNICIPIO'].str.strip()
df['UF'] = df['UF'].str.strip()

# --- Lista de siglas válidas do GeoJSON ---
with open('datasets/brazil-states.geojson', 'r') as f:
    geojson = json.load(f)

ufs_geojson = [f['properties']['sigla'] for f in geojson['features']]

# --- Filtragem para manter apenas UFs válidas ---
df = df[df['UF'].isin(ufs_geojson)]

# --- Agrupamento por UF usando a coluna CASOS ---
# Se CASOS já contém a contagem correta
df_mapa = df[['UF', 'CASOS']].copy()
df_mapa = df_mapa.groupby('UF', as_index=False).sum()
df_mapa.rename(columns={'CASOS': 'reclamacoes'}, inplace=True)

# --- Conversão segura para int, removendo vírgulas se existirem ---
df_mapa['reclamacoes'] = df_mapa['reclamacoes'].replace(',', '', regex=True).astype(int)

# --- Geração do mapa ---
fig_mapa = px.choropleth(
    df_mapa,
    geojson=geojson,
    locations='UF',
    featureidkey="properties.sigla",
    color='reclamacoes',
    hover_name='UF',
    color_continuous_scale="Reds",
    labels={'reclamacoes':'Nº Reclamações'}
)
fig_mapa.update_geos(
    fitbounds="locations",
    visible=True,
    projection_type="mercator",
    center=dict(lat=-14.2350, lon=-51.9253),  # Centro aproximado do Brasil
    lataxis_range=[-35, 5],  # Latitude aproximada Brasil
    lonaxis_range=[-75, -35]  # Longitude aproximada Brasil
)

fig_mapa.update_geos(fitbounds="locations", visible=True)

# --- Exibição no Streamlit ---
st.subheader("Mapa de Reclamações - Por Estado")
st.plotly_chart(fig_mapa, use_container_width=True)

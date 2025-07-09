import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud
import geopandas as gpd

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


# Mapa do Brasil com heatmap (por estado)
# st.subheader("Mapa do Brasil - Reclamações por Estado e Ano")

# anos_disponiveis = sorted(df_filt['TEMPO'].dt.year.dropna().unique())
# if anos_disponiveis:
#     ano = st.selectbox("Selecione o ano:", anos_disponiveis)
#     df_ano = df_filt[df_filt['TEMPO'].dt.year == ano]

#     mapa = df_ano.groupby('UF').size().reset_index(name='reclamacoes')

#     gdf = gpd.read_file('datasets/brazil-states.geojson')

#     # Merge para trazer as reclamações ao GeoDataFrame
#     gdf = gdf.merge(mapa, left_on='sigla', right_on='UF', how='left').fillna(0)
#     gdf['reclamacoes'] = gdf['reclamacoes'].astype(int)

#     # Conversão para geojson dict
#     geojson = gdf.__geo_interface__

#     fig6 = px.choropleth(
#         gdf,
#         geojson=geojson,
#         locations='sigla',
#         featureidkey="properties.sigla",
#         color='reclamacoes',
#         hover_name='name',
#         color_continuous_scale="Reds",
#         labels={'reclamacoes':'Nº Reclamações'}
#     )
#     fig6.update_geos(fitbounds="locations", visible=False)
#     st.plotly_chart(fig6)

# else:
#     st.write("Nenhum dado disponível para o mapa.")
import json

# Lista de siglas válidas (exemplo, carregue do geojson como já fez)
siglas_validas = [
    "AC","AL","AM","AP","BA","CE","DF","ES","GO","MA","MG","MS","MT",
    "PA","PB","PE","PI","PR","RJ","RN","RO","RR","RS","SC","SE","SP","TO"
]

# Filtra apenas linhas com UF válida
df = df[df['UF'].isin(siglas_validas)]

# Debug pós-limpeza
ufs_df = sorted(df['UF'].dropna().unique())
st.write("Siglas no DataFrame (após limpeza robusta):", ufs_df)

# Carrega GeoJSON como dict
with open('datasets/brazil-states.geojson', 'r') as f:
    geojson = json.load(f)

# Extrai lista de siglas do GeoJSON
ufs_geojson = sorted([f['properties']['sigla'] for f in geojson['features']])

# Limpa a coluna UF do DataFrame antes do debug
df = df[df['UF'].isin(ufs_geojson)]

# Extrai lista única de UFs do DataFrame (após limpeza)
ufs_df = sorted(df['UF'].dropna().unique())

# Exibe no Streamlit ou print em script
st.write("Siglas no GeoJSON:", ufs_geojson)
st.write("Siglas no DataFrame (após limpeza):", ufs_df)

# Verifica diferença
ufs_faltando = set(ufs_df) - set(ufs_geojson)
st.write("Siglas no DF que NÃO estão no GeoJSON:", ufs_faltando)

# Filtra df antes do agrupamento (como já fez acima)
df_filt = df[df['UF'].isin(ufs_geojson)]

# debug da coluna casos e reclamações
df_mapa = df_filt[['UF', 'CASOS']].copy()
df_mapa = df_mapa.groupby('UF', as_index=False).sum()
df_mapa.rename(columns={'CASOS': 'reclamacoes'}, inplace=True)

st.write(df)
st.write(df_mapa)

import json
import plotly.express as px

# Carrega GeoJSON como dict
with open('datasets/brazil-states.geojson', 'r') as f:
    geojson = json.load(f)

# Lista de siglas válidas do GeoJSON
ufs_geojson = [f['properties']['sigla'] for f in geojson['features']]

# Filtra o DataFrame df (já deve ter sido carregado antes) para UFs válidas
df = df[df['UF'].isin(ufs_geojson)]

# Remove vírgulas e converte para int
df_mapa['reclamacoes'] = df_mapa['reclamacoes'].replace(',', '', regex=True).astype(int)

# Exibe para debug final
st.dataframe(df_mapa)

# Gera o mapa
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
fig_mapa.update_geos(fitbounds="locations", visible=True)

st.subheader("Mapa de Reclamações - Dados Reais")
st.plotly_chart(fig_mapa, use_container_width=True)

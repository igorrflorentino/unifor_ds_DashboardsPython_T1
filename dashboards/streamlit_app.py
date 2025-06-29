import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud
import geopandas as gpd

# Carregue os dados
df = pd.read_csv('datasets/RECLAMEAQUI_IBYTE.csv')

# Converte a coluna 'TEMPO' para o tipo datetime
df['TEMPO'] = pd.to_datetime(df['TEMPO'])

# Extrai MUNICIPIO e UF da coluna LOCAL
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
fig1 = px.line(serie, labels={'value':'Nº Reclamações', 'TEMPO':'Data'})
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
texto = " ".join(df_filt['DESCRICAO'].astype(str))
wc = WordCloud(width=800, height=400, background_color="white", colormap="viridis", max_words=100).generate(texto)
fig5, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig5)

# Mapa do Brasil com heatmap (por estado)
st.subheader("Mapa do Brasil - Reclamações por Estado e Ano")
ano = st.selectbox("Selecione o ano:", sorted(df_filt['TEMPO'].dt.year.unique()))
df_ano = df_filt[df_filt['TEMPO'].dt.year == ano]
mapa = df_ano.groupby('UF').size().reset_index(name='reclamacoes')

# Carregue um shapefile simplificado dos estados do Brasil (exemplo: 'br_states.geojson')
# Você pode baixar um geojson de estados brasileiros em https://github.com/codeforamerica/click_that_hood/blob/master/public/data/brazil-states.geojson
gdf = gpd.read_file('datasets/br_states.geojson')
gdf = gdf.merge(mapa, left_on='sigla', right_on='UF', how='left').fillna(0)

fig6 = px.choropleth(
    gdf,
    geojson=gdf.geometry,
    locations=gdf.index,
    color='reclamacoes',
    hover_name='nome',
    color_continuous_scale="Reds",
    labels={'reclamacoes':'Nº Reclamações'}
)
fig6.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig6)
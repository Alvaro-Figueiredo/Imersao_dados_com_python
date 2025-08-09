import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title='Dashboard de salários na área de dados', # - adiciona um título no site.
    page_icon='📊', # - adiciona esse emoji no icone da página.
    layout='wide' # - deixa grande o layout da página.
)

df = pd.read_csv('df_dados_limpo.csv')

# criação de filtros para o dashboard.
st.sidebar.header('🔍 Filtros') # - título da barra lateral.

#Filtro de ano
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect('ano', anos_disponiveis, default=anos_disponiveis)

#Filtro de Nivel de experiencia
nivel_de_experiencia_disponiveis = sorted(df['nivel_de_experiencia'].unique())
nivel_de_experiencia_selecionados = st.sidebar.multiselect('nivel_de_experiencia', nivel_de_experiencia_disponiveis, default=nivel_de_experiencia_disponiveis)

#Filtro por tipo de contrato 
tipo_de_emprego_disponiveis = sorted(df['tipo_de_emprego'].unique())
tipo_de_emprego_selecionados = st.sidebar.multiselect('tipo_de_emprego', tipo_de_emprego_disponiveis, default=tipo_de_emprego_disponiveis)

#Filtro por tamanho de empresa
tamanho_da_empresa_disponiveis = sorted(df['tamanho_da_empresa'].unique())
tamanho_da_empresa_selecionados = st.sidebar.multiselect('tamanho_da_empresa', tamanho_da_empresa_disponiveis, default=tamanho_da_empresa_disponiveis)

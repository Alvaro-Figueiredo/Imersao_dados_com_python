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

# filtro de ano
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect('Ano', anos_disponiveis, default=anos_disponiveis)

# filtro de Nivel de experiencia
nivel_de_experiencia_disponiveis = sorted(df['nivel_de_experiencia'].unique())
nivel_de_experiencia_selecionados = st.sidebar.multiselect('Nivel de experiencia', nivel_de_experiencia_disponiveis, default=nivel_de_experiencia_disponiveis)

# filtro por tipo de contrato 
tipo_de_emprego_disponiveis = sorted(df['tipo_de_emprego'].unique())
tipo_de_emprego_selecionados = st.sidebar.multiselect('Tipo de emprego', tipo_de_emprego_disponiveis, default=tipo_de_emprego_disponiveis)

# filtro por tamanho de empresa
tamanho_da_empresa_disponiveis = sorted(df['tamanho_da_empresa'].unique())
tamanho_da_empresa_selecionados = st.sidebar.multiselect('Tamanho da empresa', tamanho_da_empresa_disponiveis, default=tamanho_da_empresa_disponiveis)

# filtra o DataFrame com base nas seleções feitas na barra lateral
df_filtrado = df[
    (df['ano'].isin(anos_selecionados))&
    (df['nivel_de_experiencia'].isin(nivel_de_experiencia_selecionados))&
    (df['tipo_de_emprego'].isin(tipo_de_emprego_selecionados))&
    (df['tamanho_da_empresa'].isin(tamanho_da_empresa_selecionados))
]

# estilização da página
st.title('👨🏻‍💻 Dashboard de análise de salários na Área de Dados')
st.markdown('Explore os dados salariais na área de dados nos últimos anos. Utilize filtros a esquerda para refinar sua análise')

if not df_filtrado.empty:
    salario_medio = df_filtrado['salario_em_dolar'].mean()
    salario_maximo = df_filtrado['salario_em_dolar'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado['cargo'].mode()[0]

else:
    salario_medio, salario_mediano, salario_maximo, total_registros, cargo_mais_frequente = 0, 0, 0, 0, 0

col1, col2, col3, col4 = st.columns(4) # - divide a página em 4 colunas
col1.metric('Salário médio', f'${salario_medio:,.0f}')
col2.metric('Salário máximo', f'${salario_maximo:,.0f}')
col4.metric('Total de registros', f'{total_registros:,}')
col3.metric('Cargo mais frequente', cargo_mais_frequente)

st.markdown('---')

st.subheader('Gráficos')

col_graf1, col_graf2 = st.columns(2) # - cria um gráfico do lado do outro no dashboard.

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['salario_em_dolar'].mean().nlargest(10).sort_values(ascending= True).reset_index() #trás os 10 cargos com maior salário médio, agrupo o cargo por salário, sort_values coloca os valores em ordem.
        grafico_cargos = px.bar(
            top_cargos,
            x='salario_em_dolar',
            y='cargo',
            orientation='h',# - montamos o gráfico na horizontal, se fosse na vertical poderia deixar sem nada.
            title='Top 10 cargos por salário médio',
            labels= {'salario_em_dolar': 'Média salarial anual (USD)', 'cargo': ''}
        )
        grafico_cargos.update_layout(title_x = 0.1, yaxis={'categoryorder': 'total ascending'}) # - move o titulo um pouco para a direita.
        st.plotly_chart(grafico_cargos, use_container_width=True) # exibe o gráfico com o streamlit.

    else:
        st.warning('Nenhum dado para exibir no gráfico de cargos.') # - exibe um aviso caso ocorra um erro.

with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='salario_em_dolar',
            nbins=30,
            title='Distribuição de salários anuais', 
            labels={'salario_em_dolar': 'Faixa salarial (USD)', 'count': ''}
        )
        grafico_hist.update_layout(title_x = 0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    
    else:
        st.warning('Nenhum dado para exibir no gráfico de distribuição.')


col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['proporcao_remota'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_de_trabalho', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_de_trabalho',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole = 0.5
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)

    else:
        st.warning('Nenhum dado para exibir no gráfico dos tipos de trabalho.')

with col_graf4:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']''
        media_ds_pais = df_ds.groupby('local_da_residencia_do_funcionario_iso3')['salario_em_dolar'].mean().reset_index()
        grafico_paises = px.choropleth(
            media_ds_pais, 
            locations= 'local_da_residencia_do_funcionario_iso3',
            color='salario_em_dolar',
            color_continuous_scale='rdylgn',
            title='Salário médio de Cientista de Dados por país',
            labels= {'salario_em_dolar': 'Salário médio (USD)', 'local_da_residencia_do_funcionario_iso3': 'País'})
        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width = True)
        
    else:
        st.warning('Nenhum dado para exibir no fráfico de países.')
    
    st.subheader('Dados detalhados')
    st.dataframe(df_filtrado)
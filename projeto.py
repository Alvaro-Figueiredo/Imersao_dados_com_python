import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv('dados_para_imersao.csv')

df.head()

#print(df.head()) # - Exibe as 5 primeiras linhas da tabela.

#print(df.info) # - Exibe os tipos de dados do dataframe.

#print(df.describe()) # - Pega somente os valores numéricos (float e int), mostra quantos registros temos para aquela coluna, mostra os maiores valores, os menores valores, a média e mais algumas coisas.

#print(df.shape) # - é um atributo então não vai o '()', mostra quantas linhas e colunas tem o arquivo de dados.

linhas, colunas = df.shape[0], df.shape[1]

print('O número de linhas é:', linhas)
print('colunas:', colunas)

print("\n")

substituir_nivel_de_experiencia = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}

df["nivel_de_experiencia"] = df["nivel_de_experiencia"].replace(substituir_nivel_de_experiencia)


# Esse código comentado é referente analise dos dados principais.
''' 
print(df["nivel_de_experiencia"].value_counts()) # - me passa a quantidade de vezes que cada senioridade aparece nos dados.

print("\n")

print(df["tipo_de_emprego"].value_counts()) # - me passa o tipo de contrato de trabalho dos funcionarios.

print("\n")

print(df["ano"].value_counts())

print("\n")

print(df["cargo"].value_counts())

print("\n")

print(df["salario_em_dolar"].value_counts())

print("\n")

print(df["localizacao_da_empresa"].value_counts())

print("\n")

print(df["local_da_residencia_do_funcionario"].value_counts())

print("\n")

print(df["proporcao_remota"].value_counts())

print("\n")

print(df["tamanho_da_empresa"].value_counts()) 

print(df.describe(include="object"))

print("\n")

print(df.isnull()) # - exibe todos os dados e apresenta como true apenas os dados nulos.

print('\n')

print(df.isnull().sum()) # - somou todos valores nulos e encontrou que 10 pessoas não tinham o valor ano.

print('\n')

print(df['ano'].unique()) # - mostra como esta exibido esses valores nulos.

print('\n')

print(df[df.isnull().any(axis=1)]) # - me traz tudo da base onde o isnull é true e imprime isso para mim.


          Estratégia:	            |                             Quando usar:
     Imputação inteligente	        |       Quando os dados faltantes são significativos para a análise
       Remoção de linhas	        |        Quando o volume de nulos é pequeno e não afeta o dataset
Preenchimento baseado em regra	    |         Quando há lógica ou negócio claro para inferir o valor
'''


# Esse comentario são os testes de tratamento de dados nulos em novas Data Frames.
''' 
df_salarios = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Laura', 'Neto'],
    'salario': [4000, np.nan, 5000, np.nan, 100000]
    }) # - criação de um DataFrame de testes.

df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2)) # - df_salarios é a nossa base, salarios_media é a nova coluna que estamos criando lá, vai receber os salarios e vai completar os valores nulos com a média (.mean()) dos salarios, round2 é o arredondamento para apenas 2 casas decimais. Define a nova coluna 'salario_media' -> diz que é igual a salarios -> substitui os valores nulos pela média -> arredonda para duas casas decimais.

df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())# - agora criamos uma nova coluna chamada salario_mediana, as vezes é melhor fazer a mediana do que a média dependendo da base de dados. Calcula a mediana e substitui os nulos pela mediana.

print(df_salarios)

print('\n')

df_temperaturas = pd.DataFrame({
    'Dia': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo'],
    'Temperatura': [30, np.nan, np.nan, 28, 27, np.nan, 31]
})

df_temperaturas['preenchido_ffill'] = df_temperaturas['Temperatura'].ffill() # - o 'ffill' completa com o valor anterior, se eu usasse o 'bfill' eu completaria com o valor anterior.

print(df_temperaturas)

print('\n')

df_cidades = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Laura', 'Neto'],
    'cidade': ['São Paulo', np.nan, 'Curitiba', np.nan, 'Piedade']
})

df_cidades['cidades_preenchidas'] = df_cidades['cidade'].fillna('Não informado') # - troca os valores nulos pelo valor 'Não informado'.

print(df_cidades)
#chamada de funções e operações matematicas é o (), criação de uma dicionario ou listas usa-se [], criação de um DataFrame ou uma base de dados usa-se {}
'''


#Nesse comentario tratamos os dados do Data Frame principal.

df_dados_limpo = df.dropna() # - Exclui as linhas que contem dados nulos, podemos fazer isso porque tem apenas 10 linhas de dados nulos em um data set de 130000.

print(df_dados_limpo.isnull().sum()) # - mostra todas os valores que contem dados nulos, no caso não aparece porque excluimos eles.

print('\n')

print(df_dados_limpo.info()) # - aqui vemos os tipos dos dados, e notamos que o valor 'ano' é um float.

print('\n')

df_dados_limpo = df_dados_limpo.assign(ano = df_dados_limpo['ano'].astype('int64')) # - assign reconfigura toda coluna ano para o tipo int.

print(df_dados_limpo.head()) 

# - aqui fiz graficos de barras, histograma e boxplot, sem serem interativos.
'''
df_dados_limpo['nivel_de_experiencia'].value_counts().plot(
    kind='bar', 
    title= 'Distribuição de senioridade'
    )

plt.xlabel('Nível de Experiência')  # - adiciona uma descrição ao eixo X.
plt.ylabel('Quantidade')            # - adiciona uma descrição ao eixo Y.
plt.tight_layout()                  # - ajusta o layout para não cortar texto.
plt.show()                          # - exibe o gráfico.


#tem que seguir essa ordem para a criação do gráfico.
ordem = df_dados_limpo.groupby('nivel_de_experiencia')['salario_em_dolar'].mean().sort_values(ascending=False).index # - agrupa valores pro grupo em colunas, nivel de experiencia por salario em dolar, o .mean() calcula a média e o .sort_values(ascending=false) organiza em ordem decrescente.
plt.figure(figsize=(8, 5))                    # - define um tamanho para o gráfico.
sns.barplot(data = df_dados_limpo, x= 'nivel_de_experiencia', y= 'salario_em_dolar', order=ordem)
plt.title('Salário médio por nível de experiência') # - adiciona um título ao grafico.
plt.xlabel('Senioridade')
plt.ylabel('Salário médio anual (USD)')
plt.tight_layout()  
plt.show()

plt.figure(figsize=(8, 4))
sns.histplot(df_dados_limpo['salario_em_dolar'], bins= 50, kde=True) # - bin é a largura das barras exibidas no grafico, kde é a linha azul que contorna o gráfico.
plt.title('Distribuição dos salários anuais') 
plt.xlabel('Salário (USD)')
plt.ylabel('Frequência')
plt.tight_layout()  
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x = df_dados_limpo['salario_em_dolar']) # - é um gráfico muito técnico, as bolinhas são os valores muito descrepantes do resto, a linha no meio do retângulo azul é a mediana, as extremidades da direita e esquerda são os valores minimos e maximos, dentro do boxplot temos os quartis.
                     O que são quartis?
Primeiro Quartil (Q1): 25% dos dados estão abaixo deste valor.
Segundo Quartil (Q2): 50% dos dados estão abaixo deste valor, também conhecido como mediana.
Terceiro Quartil (Q3): 75% dos dados estão abaixo deste valor. 
plt.title('Boxplot salário') 
plt.xlabel('Salário (USD)')
plt.tight_layout()  
plt.show()


ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
plt.figure(figsize= (8, 5))
sns.boxplot(x = 'nivel_de_experiencia', y = 'salario_em_dolar', data = df_dados_limpo, order= ordem_senioridade, palette='Set2', hue= 'nivel_de_experiencia')
plt.title('Distribuição salarial por nível de senioridade') 
plt.xlabel('Nível de experiência')
plt.ylabel('Salário (USD)')
plt.tight_layout()  
plt.show()
'''

# aqui fiz graficos de barras, rosca e pizza, todos interativos
senioridade_media_salarial = df_dados_limpo.groupby('nivel_de_experiencia')['salario_em_dolar'].mean().sort_values(ascending=False).reset_index()

fig = px.bar(senioridade_media_salarial,
             x='nivel_de_experiencia',
             y = 'salario_em_dolar',
             title = 'Média salarial por senioridade',
             labels= {'nivel_de_experiencia': 'Nível de Experiência', 'salario_em_dolar': 'Média salarial anual (USD)'}
)
            
fig.show()



remoto_contagem = df_dados_limpo['proporcao_remota'].value_counts().reset_index()
remoto_contagem.columns = ['proporcao_remota', 'quantidade']

fig = px.pie(remoto_contagem,
            names='proporcao_remota', 
            values='quantidade',
            title = 'Proporção dos tipos de trabalho',
            #hole= 0.5 # - faz virar um gráfico de rosca.
)
            
fig.update_traces(textinfo = 'percent+label')
fig.show()
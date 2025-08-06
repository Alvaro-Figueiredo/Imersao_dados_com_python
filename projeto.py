import pandas as pd

df = pd.read_csv('testedadosimersaodedados.csv')

df.head()

#print(df.head()) # - Exibe as 5 primeiras linhas da tabela.

#print(df.info) # - Exibe os tipos de dados do dataframe.

#print(df.describe()) # - Pega somente os valores numéricos (float e int), mostra quantos registros temos para aquela coluna, mostra os maiores valores, os menores valores, a média e mais algumas coisas.

#print(df.shape) # - é um atributo então não vai o '()', mostra quantas linhas e colunas tem o arquivo de dados.

linhas, colunas = df.shape[0], df.shape[1]

print('O número de linhas é:', linhas)
print('colunas:', colunas)
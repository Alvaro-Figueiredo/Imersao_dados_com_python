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

print("\n")

substituir_nivel_de_experiencia = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}

df["nivel_de_experiencia"] = df["nivel_de_experiencia"].replace(substituir_nivel_de_experiencia)


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
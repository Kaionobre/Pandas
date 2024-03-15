import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

base_dados = pd.read_csv(url, sep=';')

#print(base_dados.head(10)) mostra as 5 primeiras linhas por padrão, e as N por parâmetro

#print(base_dados.shape) mostra as linhas e colunas do seu DataFrame

#print(base_dados.columns) mostra as informações de todas as colunas do seu DataFrame

#print(base_dados.info()) mostra as colunas, os dados não nulos e o tipo de dado de cada coluna

#print(base_dados['Tipo']) mostra a coluna especificada

# print(base_dados[['Quartos', 'Valor']]) mostra as colunas especificadas


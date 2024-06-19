# -*- coding: utf-8 -*-
"""Alura Dia 1 - Importação de dados.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13z7z1oCAWiy1XzMToS1eOti4yCni9VuO
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados_2010_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20101.csv?raw=true')
dados_2010_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20102.csv?raw=true')
dados_2011_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20111.csv?raw=true')
dados_2011_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20112.csv?raw=true')
dados_2012_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20121.csv?raw=true')
dados_2012_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20122.csv?raw=true')
dados_2013_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20131.csv?raw=true')
dados_2013_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20132.csv?raw=true')
dados_2014_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20141.csv?raw=true')
dados_2014_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20142.csv?raw=true')
dados_2015_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20151.csv?raw=true')
dados_2015_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20152.csv?raw=true')
dados_2016_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20161.csv?raw=true')
dados_2016_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20162.csv?raw=true')
dados_2017_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20171.csv?raw=true')
dados_2017_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20172.csv?raw=true')
dados_2018_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20181.csv?raw=true')
dados_2018_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20182.csv?raw=true')
dados_2019_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20191.csv?raw=true')
dados_2019_2 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20192.csv?raw=true')
dados_2020_1 = pd.read_csv('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/blob/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-20201.csv?raw=true')

#Concatenar os dataFrames
emprestimos_biblioteca = pd.concat([dados_2010_1,dados_2010_2,dados_2011_1,dados_2011_2,dados_2012_1,dados_2012_2,dados_2013_1,dados_2013_2,dados_2014_1,
                                    dados_2014_2,dados_2015_1,dados_2015_2,dados_2016_1,dados_2016_2,dados_2017_1,dados_2017_2,dados_2018_1,dados_2018_2,
                                    dados_2019_1,dados_2019_2,dados_2020_1],ignore_index=True)
emprestimos_biblioteca

emprestimos_biblioteca.info()

#verificar duplicatas
emprestimos_biblioteca.value_counts()

#Excluindo duplicatas
emprestimos_biblioteca = emprestimos_biblioteca.drop_duplicates()

emprestimos_biblioteca.value_counts()

emprestimos_biblioteca.head()

#Importando mais dados
dados_exemplares = pd.read_parquet('https://github.com/FranciscoFoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_1-Importando_dados/Datasets/dados_exemplares.parquet')

dados_exemplares

"""Unindo os dataframes"""

emprestimos_completo = emprestimos_biblioteca.merge(dados_exemplares)
emprestimos_completo

emprestimos_completo.info()

emprestimos_completo.isnull().sum()

#Formatando as dadtas com o dateTime
emprestimos_completo['data_emprestimo'] = pd.to_datetime(emprestimos_completo['data_emprestimo'])

emprestimos_completo['data_renovacao'] = pd.to_datetime(emprestimos_completo['data_renovacao'])

emprestimos_completo['data_devolucao'] = pd.to_datetime(emprestimos_completo['data_devolucao'])

#Separando os emprestimos por ano
emprestimos_completo['ano'] = emprestimos_completo['data_emprestimo'].dt.year

emprestimos_por_ano = emprestimos_completo.groupby('ano').size()
print(emprestimos_por_ano)

#Grafico para mostra a evolução dos empréstimos no tempo
plt.figure(figsize=(10, 6))
plt.plot(emprestimos_por_ano.index, emprestimos_por_ano.values, marker='o')
plt.title('Quantidade de Empréstimos de Livros ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Empréstimos')
plt.grid(True)
plt.show()

#Separando as devoluções por ano
emprestimos_completo['ano'] = emprestimos_completo['data_devolucao'].dt.year

emprestimos_por_ano = emprestimos_completo.groupby('ano').size()
print(emprestimos_por_ano)

#Gráfico para mostra a evolução das devoluções ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(emprestimos_por_ano.index, emprestimos_por_ano.values, marker='o')
plt.title('Quantidade de Devoluções de Livros ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Devoluções')
plt.grid(True)
plt.show()

#Separando as renovações por ano.
emprestimos_completo['ano'] = emprestimos_completo['data_renovacao'].dt.year

emprestimos_por_ano = emprestimos_completo.groupby('ano').size()
print(emprestimos_por_ano)

#Gráfico para mostra a renovação das devoluções ao longo do tempo
plt.figure(figsize=(10, 6))
plt.plot(emprestimos_por_ano.index, emprestimos_por_ano.values, marker='o')
plt.title('Quantidade de Renovação de Livros ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Renovação')
plt.grid(True)
plt.show()

"""Agrupar e Contar Empréstimos por Biblioteca"""

emprestimos_completo['data_emprestimo'] = pd.to_datetime(emprestimos_completo['data_emprestimo'])

emprestimos_completo['biblioteca'] = emprestimos_completo['biblioteca'].astype(str)

emprestimo_por_biblioteca = emprestimos_completo.groupby('biblioteca').size().reset_index(name = 'quantidade')
emprestimo_por_biblioteca = emprestimo_por_biblioteca.sort_values(by='quantidade', ascending=False)

plt.figure(figsize=(12,8))
sns.barplot(x = 'quantidade', y = 'biblioteca', data = emprestimo_por_biblioteca)
plt.title('Quantidade de empréstimos por Biblioteca')
plt.xlabel('Quantidade de Empréstimo')
plt.ylabel('Biblioteca')
plt.show

#entender e limpar os dados
emprestimos_completo['data_emprestimo'] = pd.to_datetime(emprestimos_completo['data_emprestimo'])
emprestimos_completo['colecao'] = emprestimos_completo['colecao'].astype(str)

#Relacionar tipo_vinculo_usuario com data_emprestimo
#Entender e limpar os dados.
emprestimos_completo['data_emprestimo'] = pd.to_datetime(emprestimos_completo["data_emprestimo"])
emprestimos_completo['tipo_vinculo_usuario'] = emprestimos_completo['tipo_vinculo_usuario'].astype(str)
#Analisar a relação entre as duas variáveis acima
emprestimos_completo['ano'] = emprestimos_completo['data_emprestimo'].dt.year
emprestimos_por_vinculo = emprestimos_completo.groupby(['ano', 'tipo_vinculo_usuario']).size().reset_index(name='quantidade')

plt.figure(figsize = (14, 8))
sns.lineplot(x ='ano', y='quantidade', hue='tipo_vinculo_usuario', data=emprestimos_por_vinculo, marker = 'o')
plt.title('Qauntidade de empréstimos por Tipo de Vinculo de usuario ao longo dos anos')
plt.xlabel('Ano')
plt.ylabel('Quantidade de empréstimo')
plt.legend(title = 'Tipo de vinculo do usuario')
plt.grid(True)
plt.show()


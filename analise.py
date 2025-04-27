import pandas as pd
import matplotlib as mt

df = pd.read_excel('Pasta1.xlsx')

table =  df.head() # Exibe a tabela
column = df.columns # Exibe as colunas
produtos = df['Produto'] # Exibe uma parte uma coluna em esprecifico
vendas = df[['Produto', 'Vendas']] # Exibe mais de uma coluna


print(produtos)
import pandas as pd
import matplotlib as mt

df = pd.read_excel('Pasta1.xlsx')

table =  df.head() # Exibe a tabela
column = df.columns # Exibe as colunas
itens = df['Produto'] # Exibe uma parte uma coluna em esprecifico
produtos = df[['Produto', 'Vendas']] # Exibe mais de uma coluna
vendas = df['Vendas']

print(table)

# Calcula o Total de vendas
vendas_total = 0
for venda in vendas:
    vendas_total += venda
print(f'Total de vendas: {vendas_total}')

# Calcula o total de vendas por produtos
eletronicos = df['Produto'] == 'Eletrônico'
soma = df[eletronicos]['Vendas'].sum()
print(f'Total de vendas de Eletronicos: {soma}')

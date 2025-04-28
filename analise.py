import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Pasta1.xlsx')

table =  df.head() # Exibe a tabela
column = df.columns # Exibe as colunas
itens =  set() # Exibe uma parte uma coluna em esprecifico
regiao = df['Região']
# produtos = df[['Produto', 'Vendas']] # Exibe mais de uma coluna
vendas = df['Vendas']

print(table)
# Calcula o Total de vendas
vendas_total = 0
for venda in vendas:
    vendas_total += venda
# print(f'Total de vendas: {vendas_total}')

# Calcula o total de vendas por produtos
eletronicos = df['Produto'] == 'Eletrônico'
soma = df[eletronicos]['Vendas'].sum()
# print(f'Total de vendas de Eletronicos: {soma}')

for item in df['Produto']:
    itens.add(item)
print(itens)


venda_produto = []
for item in itens:
    venda_produto = df[item]['Vendas'].sum()

print(venda_produto)

# fig, ax = plt.subplots()
# bar_label = ['orange', 'red', 'blue']
# bar_colors = ['tab:orange', 'tab:red', 'tab:blue']
#
# ax.bar(eletronicos, regiao,  color=bar_colors)
#
# ax.set_title('Vendas por Produtos')
# ax.set_ylabel('Vendas')
#
# plt.show()
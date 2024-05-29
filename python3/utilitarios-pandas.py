### UTILITARIOS PANDAS:

# percorrendo linhas em tabelas:

for linha in tabela.index:
    print(tabela.loc[linha, "Cliente"])
    print(tabela.loc[linha, "Endereço"])
    print(tabela.loc[linha, "Bairro"])
    
    
    
# - Para isso, vamos precisar filtrar. A forma de filtrar nos dataframes é uma "simples" comparação

quantidadeVendidaLoja1=0
quantidadeDevolvidaLoja1=0

for linha in vendas_df.index:
    if vendas_df.loc[linha,'Nome da Loja']=='Loja Contoso Europe Online ':
        quantidadeDevolvidaLoja1+=vendas_df.loc[linha,'Quantidade Devolvida']
        quantidadeVendidaLoja1+=vendas_df.loc[linha,'Quantidade Vendida']

if quantidadeVendidaLoja1>0:
    percentualDevolvidoLoja1=(quantidadeDevolvidaLoja1/quantidadeVendidaLoja1)*100
    print(f'{percentualDevolvidoLoja1=:.2f}%')
else:
    print('Sem vendas para essa loja\n')


# ou

# filtrando a tabela para que ela so tenha loja contoso europe online, podemos tambem usar o ID da loja (o nome da loja na tabela esta com um erro , possui um espaco no final do nome)
vendasLojaContosoEuropeOnline=vendas_df[vendas_df['Nome da Loja']=='Loja Contoso Europe Online ']
print(vendasLojaContosoEuropeOnline)

if vendasLojaContosoEuropeOnline['Quantidade Vendida'].sum()>0:
    percentualDevolvidoLojaContosoEuropeOnline=(vendasLojaContosoEuropeOnline['Quantidade Devolvida'].sum()/vendasLojaContosoEuropeOnline['Quantidade Vendida'].sum())*100

    print(f'{percentualDevolvidoLojaContosoEuropeOnline=:.2f}%\n')
else:
    print('Sem vendas para essa loja\n')
    
    
    

# OBSERVE QUE PODEMOS USAR AS COMPARACOES COMO RESULTADOS A SEREM LANCADOS NA TABELA PARA OBTERMOS FILTROS

# vendasLojaContosoEuropeOnline=vendas_df[vendas_df['Nome da Loja']=='Loja Contoso Europe Online ']
# vendasLojaContosoEuropeOnline=vendas_df[vendas_df['ID Loja']==306]

# lista a tabela apenas com vendas da loja ID 306
todasLojasId306=vendas_df[vendas_df['ID Loja']==306]
print(todasLojasId306)

# informa se a venda eh loja ID 306 ou nao
ehLoja306= vendas_df['ID Loja']==306
print(ehLoja306)

# vendeu mais de 50 pecas
vendeuMaisDe50= vendas_df['Quantidade Vendida'] > 50

# é loja 306 com mais de 50 vendas
ehLoja306ComMaisDe50Vendas= vendas_df[todasLojasId306 and vendeuMaisDe50]



### Desafio: e se eu quisesse criar uma tabela apenas com as vendas da Loja Contoso Europe Online e que não tiveram nenhuma devolução. Quero criar essa tabela e saber quantas vendas são.

# - Repare que nesse caso são 2 condições, como fazemos isso?

# tudo junto

import numpy as np

vendasLoja306SemDevolucao=vendas_df[np.logical_and(vendas_df['ID Loja']==306, vendas_df['Quantidade Devolvida']==0)]

# ou

# o parenteses em cada condicao eh obrigatorio
vendasLoja306SemDevolucao=vendas_df[(vendas_df['ID Loja']==306) & (vendas_df['Quantidade Devolvida']==0)]

print(vendasLoja306SemDevolucao)
print(vendasLoja306SemDevolucao['Quantidade Vendida'].sum())


# separado

vendasLoja306SemDevolucao = vendas_df[vendas_df['ID Loja']==306]
vendasLoja306SemDevolucao = vendasLoja306SemDevolucao[vendas_df['Quantidade Devolvida']==0]

print(vendasLoja306SemDevolucao)
print(vendasLoja306SemDevolucao['Quantidade Vendida'].sum())





# DATETIME EM PANDAS
# transformando a data da venda no formato object (texto) para o formato datetime, com o formato mostramos o que cada elemento é e separamos de acordo com as barras que ja estao nas informacoes do dataframe (poderia ser diferente)
vendas_df['Data da Venda']=pd.to_datetime(vendas_df['Data da Venda'], format='%d/%m/%Y')

print(vendas_df)
vendas_df.info()

# Conforme os dicionarios em python, caso uma coluna nao exista ele cria a coluna
vendas_df['Ano da Venda']=vendas_df['Data da Venda'].dt.year
vendas_df['Mes da Venda']=vendas_df['Data da Venda'].dt.month
vendas_df['Dia da Venda']=vendas_df['Data da Venda'].dt.day
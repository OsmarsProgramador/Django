# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


import copy

novos_produtos=copy.deepcopy(produtos) # nesse caso é opcional
novos_produtos=[{**produto, 'preco': produto['preco']*1.1} for produto in produtos]

print(novos_produtos) # [{'nome': 'Produto 5', 'preco': 11.0}, {'nome': 'Produto 1', 'preco': 24.552000000000003}, {'nome': 'Produto 3', 'preco': 11.121}, {'nome': 'Produto 2', 'preco': 116.45700000000001}, {'nome': 'Produto 4', 'preco': 76.89000000000001}]
novos_produtos[0]['preco']=20

print('----------------------------------------')

print(novos_produtos)

print('----------------------------------------')
print(produtos) # [{'nome': 'Produto 5', 'preco': 10.0}, {'nome': 'Produto 1', 'preco': 22.32}, {'nome': 'Produto 3', 'preco': 10.11}, {'nome': 'Produto 2', 'preco': 105.87}, {'nome': 'Produto 4', 'preco': 69.9}]
print('----------------------------------------')


print('\n----------------------------------------\n')


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)


produtos_ordenados_por_nome=sorted(copy.deepcopy(produtos),key=lambda produto: produto['nome'], reverse=True) # nesse caso o deep copy é obrigatorio

print(produtos_ordenados_por_nome)

print('----------------------------------------')

produtos_ordenados_por_nome[0]['preco']=20
print(produtos_ordenados_por_nome)
print('----------------------------------------')
print(produtos)


print('\n----------------------------------------\n')


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco=sorted(copy.deepcopy(produtos),key=lambda produto: produto['preco']) # nesse caso deepcopy obrigatorio tambem

print(produtos_ordenados_por_preco)
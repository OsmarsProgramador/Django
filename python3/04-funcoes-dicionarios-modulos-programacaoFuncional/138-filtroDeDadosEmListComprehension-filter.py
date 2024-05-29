# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

import pprint # (pretty print) ajuda a exibir de forma mais 'bonita' ou organizada


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
# print(list(range(10)))
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# # print(novos_produtos)
# print(novos_produtos)
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]


# FILTRO
# filtro geralmente vem como um if depois do for do map, ou apenas um if
# esquerda do for mapeamento, direita do for, filtro 

lista=list(range(10)) 
print(lista) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('-----------------------------------------')

lista2=[item for item in lista if item%2==0]
print(lista2) # [0, 2, 4, 6, 8]

print('-----------------------------------------')


produtosFilter=[{**produto} for produto in produtos if produto['preco']>10]
pprint.pprint(produtosFilter) # [{'nome': 'p1', 'preco': 20}, {'nome': 'p3', 'preco': 30}]

print('-----------------------------------------')
     
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
print(novos_produtos) # [{'nome': 'p1', 'preco': 20}, {'nome': 'p3', 'preco': 31.5}]
p(novos_produtos) # [{'nome': 'p1', 'preco': 20},
# {'nome': 'p3', 'preco': 31.5}]
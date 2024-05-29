# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]


# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']


# recomenda-se passar o valor inicial (terceiro parametro), pois na ausencia dele o primeiro item do iteravel sera o valor inicial, o que pode ocasionar problemas indesejaveis
total = reduce(
    lambda acum, prod: acum + prod['preco'], # funcao a ser desempenhada
    produtos, # iteravel
    0 # valor inicial
)

print('Total é', total) # Total é 44

print('-------------------------')

total = 0
for p in produtos:
    total += p['preco']

print(total) # 44

print('-------------------------')

print(sum([p['preco'] for p in produtos])) # 44
"""
enumerate - enumera iteráveis (índices)

funciona com listas, strings, tuplas, qualquer que seja o iteravel, facilita a utilizacao de indices no for por exemplo

quando enumeramos cada item da lista/tupla/string vira uma tupla com seu indice e valor
"""

# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

listaEnumerada=list(enumerate(lista, start=10)) # cria uma lista com enumeracao a partir da variavel lista e comecando no indice 10
print(listaEnumerada)

print('-------------------------------')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

print('-------------------------------')

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

print('-------------------------------')

for item in enumerate(lista):
    print(item)

print('-------------------------------')

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')

print('-----------------------------')

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(valor)

print('-----------------------------')

# funciona com strings
palavra='system'
for indice,item in enumerate(palavra):
    print(indice,item)
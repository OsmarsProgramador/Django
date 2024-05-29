# Exercício - Unir listas

# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

import copy

listaCidades=['Salvador', 'Ubatuba', 'Belo Horizonte']
listaEstados=['BA', 'SP', 'MG', 'RJ']

def funcaoZipper(lista1,lista2):
    if len(lista1)<len(lista2):
        menor=copy.deepcopy(lista1)
        maior=copy.deepcopy(lista2)
    else:
        menor=copy.deepcopy(lista2)
        maior=copy.deepcopy(lista1)

    listaZipper=copy.deepcopy(menor)


    for index,item in enumerate(listaZipper):
        listaZipper[index]=item,maior[index]

    return listaZipper

print(funcaoZipper(listaCidades,listaEstados))
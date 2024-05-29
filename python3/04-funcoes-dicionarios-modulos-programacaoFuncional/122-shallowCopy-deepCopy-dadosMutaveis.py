# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy # nesse modulo temos como fazer uma deep copy (copia total)

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

d3 = d1 # nao é copia, apenas aponta para o mesmo local na memoria (valores mutaveis)

d2 = d1.copy() # copia rasa - shallow copy
d4 = copy.copy(d1) # comando igual ao anterior fazendo copia rasa

d5 = copy.deepcopy(d1) # nesse caso será uma deep copy (copia profunda) onde nao havera mais direcionamento ao mesmo local da memoria

print(d1) # {'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}
print(d2) # {'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}
print(d5) # {'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}

print('---------------------------------')

d2['c1'] = 1000
d2['l1'][1] = 999999
d5['l1'][0]=55
# observe que o valor no meio da lista foi alterado em ambos os dicionarios pois nesse caso sao dados mutaveis, configurando a copia feita como uma copia rasa
print(d1) # {'c1': 1, 'c2': 2, 'l1': [0, 999999, 2]}
print(d2) # {'c1': 1000, 'c2': 2, 'l1': [0, 999999, 2]}
print(d5) # {'c1': 1, 'c2': 2, 'l1': [55, 1, 2]}
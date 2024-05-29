"""
for in com listas
"""
lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(nome, type(nome))


# *** IMPORTANTE: for in com acesso ao indice
for indice,nome in enumerate(lista):
    print(indice, nome)
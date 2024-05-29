# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# nesse caso p=lista[0], b=lista[1], *_=lista[2] e lista[3], ap=lista[4] e u=lista[5]
p, b, *_, ap, u = lista
print(*_) # 1 2
print(p, u, ap) # Maria Eduarda 3

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista) # Maria Helena 1 2 3 Eduarda
print(*string) # A B C D
print(*tupla) # Python é legal

# sep => separador (vai alterar o separador de espaco para pular linha)
print(*salas, sep='\n')
"""
output:

['Maria', 'Helena']
['Elaine']
['Luiz', 'João', 'Eduarda']

"""
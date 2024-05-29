"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final

    insert - Adiciona um item no índice escolhido

    pop - Remove do final ou do índice escolhido e retorna o item

    del - apaga um índice

    clear - limpa a lista

    extend - estende a lista

    + - concatena listas

Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
print(lista) # [10, 20, 30, 40, 'Luiz']

nome = lista.pop()
print(lista) # [10, 20, 30, 40]

lista.append(1233)
print(lista) # [10, 20, 30, 40, 1233]

del lista[-1] # otimo metodo para deletar o ultimo item da lista caso nao saiba o numero de elementos da mesma
print(lista) # [10, 20, 30, 40]


lista.insert(2, 100) # insere o valor 100 na posicao 2 da lista
print(lista) # [10, 20, 100, 30, 40]

print(lista[4]) # 40

lista.clear()
print(lista) # []
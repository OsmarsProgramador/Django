"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento

Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
lista[2] = 300
print(lista) # [10, 20, 300, 40]

del lista[2] # apaga o elemento da lista
print(lista) # [10, 20, 40]

print(lista[2]) # 40

lista.append(50) # adiciona o elemento no fim da lista
print(lista) # [10, 20, 40, 50]

lista.pop() # apaga o ultimo elemento da lista
print(lista) # [10, 20, 40]

lista.append(60)
lista.append(70)
print(lista)

ultimo_valor = lista.pop(3) # apaga o elemento de indice 3 E TAMBEM retorna o valor apagado

print(lista, 'Removido,', ultimo_valor)
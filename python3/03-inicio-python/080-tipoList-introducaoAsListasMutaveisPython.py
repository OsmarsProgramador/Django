"""
Listas em Python

Tipo list - Mutável (isso significa que podemos mudar cada indice de maneira independente, string por exemplo nao podemos fazer isso)

Suporta vários valores de qualquer tipo

Conhecimentos reutilizáveis - índices e fatiamento

Métodos úteis: append, insert, pop, del, clear, extend, +
"""

lista1=list([1,2,3]) # maneira alternativa de criar lista, pode ser utilizada em type conversion, para converter algum outro objeto/variavel em lista

lista1=[] # maneira mais comum de criar uma lista vazia

#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)


#        0    1      2              3    4
#       -5   -4     -3             -2   -1

lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria'

print(lista)
print(lista, type(lista))
print(bool([]))
print(lista[2], type(lista[2]))
# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor  in produto.items()
    if chave != 'categoria'
}
print(dc) # {'nome': 'CANETA AZUL', 'preco': 2.5}

print('-------------------------------')

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista
    # for (chave,valor) in lista # igual ao de cima, mostrando que chave, valor representa uma tupla
}
print(dc) # {'a': 'valor a', 'b': 'valor a'}

print('-------------------------------')

# set - nao garante a ordem
# criacao de set com chaves
s5={1,2,3}
print(type(s5))

s1 = {2 ** i for i in range(10)}
print(s1) # {32, 1, 2, 64, 4, 128, 256, 512, 8, 16}
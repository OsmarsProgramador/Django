import sys

# GENERATOR SAO funcoes que sabem pausar, generators sao iterators mas iterators nao sao generators

# O GENERATOR é igual a LISTA, mas os valores não estão todos na memória inicialmente, generator nao tem o tamanho, nem indice como a lista, nao se conhece o numero de elementos

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]

# Generator expression, nao é uma tupla
generator = (n for n in range(1000000))

print(sys.getsizeof(lista)) # 8448728 # tamanho da lista em bytes

print(sys.getsizeof(generator)) # 112 # tamanho do generator em bytes

# print(lista)
print(generator)

# printa todo o generator, mesmo nao tendo salvo todos os valores na memoria
# for n in generator:
    # print(n)

# print(generator[0]) # Erro!
# print(len(generator)) # Erro!
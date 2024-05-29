# Iteraveis/Iterables - Tem a responsabilidade de deter os valores sequenciais

# Iterador/Iterators - Responsabilidade de entregar um valor por vez, so sabe quem é o proximo valor, nao sabe quem eh o primeiro, o ultimo ou qualquer outro sem ser o proximo a ser entregue

iterable=['Eu','Tenho','__iter__']
iterator=iterable.__iter__()  # tem __iter__ e __next__
# iterator=iter(iterable) # identico ao anterior

# next chama o proximo elemento
print(next(iterator)) # Eu
print(next(iterator)) # Tenho
print(next(iterator)) # __iter__
print(next(iterator)) # Excesso de StopIteration


# print(iterator[1]) # Erro!
# print(len(iterator)) # Erro!
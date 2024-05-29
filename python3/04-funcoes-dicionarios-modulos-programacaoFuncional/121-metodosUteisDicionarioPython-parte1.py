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
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade']) # 900
print(len(pessoa)) # 3

# observe que os metodos abaixos estao sendo convertidos em lista para facilitar sua utilizacao, pois o retorno original eh o dictkeys que nao facilita muito o seu uso

print(pessoa.keys()) # dict_keys(['nome', 'sobrenome', 'idade'])
print(list(pessoa.keys())) # ['nome', 'sobrenome', 'idade']

print(pessoa.values()) # dict_values(['Luiz Otávio', 'Miranda', 900])
print(list(pessoa.values())) # ['Luiz Otávio', 'Miranda', 900]

print(pessoa.items()) # dict_items([('nome', 'Luiz Otávio'), ('sobrenome', 'Miranda'), ('idade', 900)])
print(list(pessoa.items())) # [('nome', 'Luiz Otávio'), ('sobrenome', 'Miranda'), ('idade', 900)]

print('---------------------------')

# for direto, sem coercao(convesao em lista ou tupla)
for valor in pessoa.values(): 
    print(valor)

print('---------------------------')

# for direto, sem coercao(convesao em lista ou tupla)
for chave, valor in pessoa.items():
    print(chave, valor)
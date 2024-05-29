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
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
print(p1['nome'])
print(p1.get('nome'))

nome = p1.pop('nome') # retorna Luiz e exclui a chave 'nome'
print(nome) # Luiz
print(p1) # {'sobrenome': 'Miranda'}
ultima_chave = p1.popitem() 
print(ultima_chave) # ('sobrenome', 'Miranda')
print(p1) # {}
p1.update({ # atualiza as chaves solicitadas mas nao mexe nos valores ja existentes, tambem pode criar novas chaves
    'nome': 'novo valor',
    'idade': 30,
})
p1.update(nome='novo valor', idade=30) # outra maneira de utilizar o update

p2={}
tupla = (('nome', 'novo valor'), ('idade', 30))
p2.update(tupla)

print('---------------------------------')

lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1) # {'nome': 'novo valor', 'idade': 30}
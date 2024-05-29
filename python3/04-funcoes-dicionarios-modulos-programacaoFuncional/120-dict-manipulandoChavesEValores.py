# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa) # {'nome': 'Luiz Otávio', 'sobrenome': 'Miranda'}
print(pessoa[chave]) # Luiz Otávio 

print('\n-------------------------\n')

pessoa[chave] = 'Maria'

del pessoa['sobrenome'] # apaga o par chave/valor inteiro
print(pessoa) # {'nome': 'Maria'}
print(pessoa['nome']) # Maria

print('\n-------------------------\n')

# print(pessoa.get('sobrenome')) # KeyError - erro de chave que nao existe
print(pessoa.get('nome')) # Maria
print(pessoa.get(chave)) # Maria

print('-------------------------')
if pessoa.get('sobrenome') is None: # o get retorna none caso a chave nao existe, se fizermos apenas com pessoa['sobrenome'] nao funcionará
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')
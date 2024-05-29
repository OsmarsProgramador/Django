# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b) # 2 1

print('----------------------------')

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# desempacotamento das keys
a,b=pessoa
print(a,b) # nome sobrenome

print('----------------------------')

# desenpacotamento dos values
a,b=pessoa.values()
print(a,b) # Aline Souza

print('----------------------------')

# ambos os valores, keys e values
a,b=pessoa.items()
print(a,b) # ('nome', 'Aline') ('sobrenome', 'Souza')

print('----------------------------')

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2) # nome Aline
print(b1, b2) # sobrenome Souza

print('----------------------------')

for chave, valor in pessoa.items():
    print(chave, valor)
# nome Aline
# sobrenome Souza

print('----------------------------')

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# nesse caso os dois ** extrai os dados dos dicionarios de origem (pessoa, dados_pessoa) dentro do novo dicionario (pessoas_completa) gerando um novo dicionario com os dados dos dois primeiros
pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa) # {'nome': 'Aline', 'sobrenome': 'Souza', 'idade': 16, 'altura': 1.6}


# nesse caso adicionamos mais um key, caso o key ja exista o value referente a ele sera sobrescrito
pessoa_completa={**pessoa_completa, 'departamento': 'logistica'}
print(pessoa_completa)
# {'nome': 'Aline', 'sobrenome': 'Souza', 'idade': 16, 'altura': 1.6, 'departamento': 'logistica'}


print('----------------------------')

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

# kwargs sempre sera com dois asteristicos
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(nome='Joana', qlq=123)


mostro_argumentos_nomeados(**pessoa_completa)

print('----------------------------')

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)
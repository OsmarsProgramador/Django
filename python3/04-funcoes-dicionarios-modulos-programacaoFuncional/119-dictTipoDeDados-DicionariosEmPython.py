# Dicionários em Python (tipo dict)

# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".

# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.

# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.

# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.

# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

pessoa2=dict()
pessoa2['nome']='Jorge'
pessoa2['sobrenome']='Nami Harbes'
pessoa2['idade']=39
print(pessoa2)

print('\n--------------------------------\n')

pessoa1 = dict(nome='Luiz Otávio', sobrenome='Miranda')
print(pessoa1)

print('\n--------------------------------\n')

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}

print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print('\n--------------------------------\n')

# dicionarios nao sao iteraveis, mas o python entrega a chave quando feito um for no dicionario facilitando sua utilizacao nessa logica de repeticao
for chave in pessoa:
    print(chave, pessoa[chave])
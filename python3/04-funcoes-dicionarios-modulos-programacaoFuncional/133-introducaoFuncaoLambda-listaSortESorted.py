# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
lista.sort()
print(lista) # [1, 4, 5, 6, 6, 21, 32, 34]

lista.sort(reverse=True) # [34, 32, 21, 6, 6, 5, 4, 1]
print(lista)

lista2=sorted(lista)
print(lista2)

print('----------------------------------')

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def ordena(item):
    return item['nome']

lista.sort(key=ordena) # passamos a funcao ordena como key mostrando que seu retorno é o parametro que deve ser usado como meio de ordenacao
print(lista)
for item in lista:
    print(item)
# {'nome': 'Aline', 'sobrenome': 'Souza'}
# {'nome': 'Daniel', 'sobrenome': 'Silva'}
# {'nome': 'Eduardo', 'sobrenome': 'Moreira'}
# {'nome': 'Luiz', 'sobrenome': 'miranda'}
# {'nome': 'Maria', 'sobrenome': 'Oliveira'}

print('-------------------------------')

lista2=[
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir(lista2):
    for item in lista2:
        print(item)
    print()


# lambda seria como def, item seria como o(s) parametro(s) e item['nome'] seria como o retorno da funcao
l1 = sorted(lista2, key=lambda item: item['nome']) # aqui cria uma nova lista l1 (copia rasa)

# ou

lista2.sort(key=lambda item: item['sobrenome']) # aqui altera a lista original lista2

exibir(l1)
exibir(lista2)
# Problema dos parâmetros mutáveis em funções Python

def addClientes(nome,lista=[]):
    lista.append(nome)
    return lista


client1=addClientes('luiz')
addClientes('Joana',client1)
print(client1) # ['luiz', 'Joana']

client2=addClientes('Helena')
addClientes('Maria',client2)
print(client2) # ['luiz', 'Joana', 'Helena', 'Maria']

print('-------------------------------')


def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1) # ['luiz', 'Joana', 'Fernando', 'Edu']
print(cliente2) # ['Helena', 'Maria']
print(cliente3) # ['Moreira', 'Vivi']
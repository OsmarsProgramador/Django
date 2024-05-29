"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

listaC=[1,2,3,4]
listaD=listaC # observe que ao igualar a variavel lista D apenas aponta para o endereco de memoria de listaC, ela nao COPIA os items

print(listaD)

listaD[0]=10 # sendo assim ao alterar o indice 0 estamos alterando o endereco de memoria do indice 0, consequentemente alterando em ambas as listas, listaD e listaC
print(listaC)
print(listaD)

print('--------------------------')


# no caso do copy será diferente, a lista é COPIADA e o endereco de cada uma na memoria será independente, ou seja, ao alterar uma a outra nao será alterada
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
"""

Iterável -> str, range, etc , significa que possui o metodo(__iter__)

Iterador -> quem sabe entregar um valor por vez

next -> me entregue o próximo valor

iter -> me entregue seu iterador

"""
texto1='Luiz'  # objeto iterável
textoTeste=iter(texto1) # ou __iter__(), iterator ou iterador
print(textoTeste) # <str_iterator object at 0x0000028CA2E9B760>

# tambem funciona com a funcao next()
# Exemplo abaixo seria next(textoTeste)
print(textoTeste.__next__()) # L
print(textoTeste.__next__()) # u
print(textoTeste.__next__()) # i
print(textoTeste.__next__()) # z
# print(textoTeste.__next__()) # ERRO ABAIXO MOSTRANDO QUE A ITERACAO ACABOU: 

# Traceback (most recent call last):
#   File "c:\Users\jharbes\Documents\GitHub\python3\03-inicio-python\074-mecanicaDoFor.py", 
# line 20, in <module>
#     print(textoTeste.__next__()) #
# StopIteration

print('---------------------------------')

# for letra in texto
texto = 'Luiz'  # iterável

iteratador = iter(texto)  # iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

print('---------------------------------')

for letra in texto:
    print(letra)
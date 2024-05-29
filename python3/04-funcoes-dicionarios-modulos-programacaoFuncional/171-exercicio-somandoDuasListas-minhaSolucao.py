"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

# fiz considerando a maior, nao prestei atencao ao enunciado 

lista_a=[1, 2, 3, 4, 5, 6, 7]
lista_b=[1, 2, 3, 4]

def somaListas(lista1,lista2):
    menor=lista1 if len(lista1)<len(lista2) else lista2
    maior=lista1 if len(lista1)>len(lista2) else lista2
    for indice,item in enumerate(menor):
        maior[indice]+=menor[indice]
    return maior


listaC=somaListas(lista_a,lista_b)
print(listaC)
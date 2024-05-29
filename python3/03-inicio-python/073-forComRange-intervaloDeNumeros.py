"""

For + Range
range -> range(start, stop, step)

o ultimo digito (stop) nao sera incluido no range

na ausencia do step ele será igual a 1

o step tambem pode ser negativo

"""
numeros = range(10)
print(numeros) # range(0,10)
# 0 1 2 3 4 5 6 7 8 9

numeros = range(5,10)
print(numeros)
# 5 6 7 8 9

numeros = range(0, 100, 8)
print(numeros) # numeros é um range e nao um vetor

for numero in numeros:
    print(numero)
"""
Fatiamento de strings (strings em python sao iteraveis - funcionam como arrays)
 012345678
 Olá mundo
-987654321   (negativo comeca do -1 e nao 0)

Fatiamento [i:f:p] [::]   => onde i = inicio, f = fim e p = passo

Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
variavel2 = 'Olá'


print(variavel[4:6]) # indice 4 ate o 6 (o indice final nao eh incluido)

print(variavel[4::]) # nessa caso inicio em 4 até o final (omissao do fim)
print(variavel[4:]) # identico ao interior

print((variavel[-8:])) # comeca do -8 ate o final de tras pra frente

print(variavel[::-1]) # vai comecar a imprimir do -1 e andar passo a passo -1 ate o fim, o passo negativo inverte os indices da string caso sejam omitidos
print(variavel[-1:-8:-2])

print(variavel[0::2]) # vai comecar do zero e imprimir de dois em dois passos na string
print(variavel[::2]) # idem ao anterior

print(variavel[0:5:2]) # vai comecar do zero ate o indice 4 (para com sempre em um a menos) com passos de dois a dois


print(len(variavel)) # length da string, caracteres com acentos contam como apenas um, espaços vazios tambem contam como caractere
print(len(variavel2))
print(len(variavel[4:]))
"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase1='Testando conversores em python'
frase1Separada=frase1.split()

# A ausencia do argumento no split faz com que ele divida a string em um array com base nos espacos existentes entre ela ' ', isso inclui \n \t \r \f
print(frase1Separada) # ['Testando', 'conversores', 'em', 'python']

print('--------------------------------------')

frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')
print(lista_frases_cruas) # ['   Olha só que   ', ' coisa interessante          ']

# como vemos abaixo split nao altera a frase original
print(frase) #    Olha só que   , coisa interessante

print('--------------------------------------')

# o metodo strip corta os espacos do comeco e do fim da string (inclusive os caracteres especiais \n \t \v \f), tambem existem os metodos LSTRIP e RSTRIP que funcionam para os espacos e caracteres especiais à ESQUERDA da string e da DIREITA da string respectivamente
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases) # ['Olha só que', 'coisa interessante'] 

print('--------------------------------------')

# join une os iteraveis (lista e string por exemplo) com base em algum separador a ser identificado, exemplo:
frases_unidas = ', '.join(lista_frases)
print(frases_unidas) # Olha só que, coisa interessante

stringSeparada='-'.join('abc')
print(stringSeparada) # a-b-c
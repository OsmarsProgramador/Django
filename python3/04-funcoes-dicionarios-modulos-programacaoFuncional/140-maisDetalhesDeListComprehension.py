# LIST COMPREHENSION

# list comprehension faz as mesmas coisas que funcoes map, filter, flatMap de outras linguagens e até mais do que isso.

# List comprehension será usada para por meio de um iterável gerar um outro iterável com algum processamento de dados (alteração, filtro, etc)

numeros=[1,2,3,4,5]
novosNumeros=numeros # nao gera copia! apenas aponta para o mesmo valor na memoria, mudar uma altera as duas (pois o local na memoria pra onde apontam altera os valores)

numeros[0]=20
print(novosNumeros) # [20, 2, 3, 4, 5]

print('-------------------------------')

# no caso de dados imutaveis internos (como uma lista de numeros) a copia rasa fornece uma copia completa
numeros2=[1,2,3,4,5]
novosNumeros2=numeros2.copy() # shallow copy/copia rasa
numeros2[0]=20
print(novosNumeros2) # [1, 2, 3, 4, 5]


print('-------------------------------')

numeros3=[1,2,3,4,5]
novosNumeros3=[n for n in numeros3] # list comprehension/gera uma deep copy, copias independentes  mesmo que os dados internos sejam mutaveis 
numeros3[0]=20
print(novosNumeros3) # [1, 2, 3, 4, 5]


# o metodo acima é identico ao de baixo, ambos geram uma deep copy:


numeros4=[1,2,3,4,5]
novosNumeros4=[]
for numero in numeros4:
    novosNumeros4.append(numero)
print(novosNumeros4) # [1, 2, 3, 4, 5]

print('-------------------------------')


# Agora usaremos a list comprehension para fazer uma copia da lista com alteracoes dos valores (semelhante a map)

numeros5=[1,2,3,4,5]
novosNumeros5=[n/2 for n in numeros5] 
multiplicacao=[n*2 for n in numeros5]
quadrado=[n**2 for n in numeros5]
squareRt=[n ** (1/2) for n in numeros5]

print(novosNumeros5) # [0.5, 1.0, 1.5, 2.0, 2.5]
print(multiplicacao) # [2, 4, 6, 8, 10]
print(quadrado) # [1, 4, 9, 16, 25]
print(squareRt) # [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979]


print('-------------------------------')


## LIST COMPREHENSION COMO FILTER, para filtragem o IF vem depois do for.

numbers=[1,2,3,4,5,6,7,8,9,10]
newNumbers=[n for n in numbers if n>5]
print(newNumbers) # [6, 7, 8, 9, 10]

newNumbers2=[n+2 for n in numbers if n%2!=0]
print(newNumbers2) # [3, 5, 7, 9, 11]

anotherIf=[(n*2+3) if n!=6 else 60 for n in numbers]
print(anotherIf) # [5, 7, 9, 11, 13, 60, 17, 19, 21, 23]

anotherIf2=[(n*2+3) if n!=6 else 60 for n in numbers if ((n*2+3) if n!=6 else 60)%2==0]
print(anotherIf2) # [60]

anotherIf3=[
    n
    if n!=6 else 600
    for n in numbers
    if n%2==0
]
print(anotherIf3) # [2, 4, 600, 8, 10]


# FOR ANINHADO EM LIST COMPREHENSION

linhasColunas=[
    (x,y)
    for x in range(1,11)
    for y in range(1,6)
]

print(linhasColunas) # [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5)]

print('-------------------------------')

linhasColunas=[
    (x,y)
    for x in range(1,11)
    for y in range(1,6)
    if x!=2
]

print(linhasColunas) # [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5)] 

print('-------------------------------')

linhasColunas=[
    (x,y) if y!=2 else (x*1000,y*1000)
    for x in range(1,11)
    for y in range(1,6)
    if x!=2
]

print(linhasColunas) # [(1, 1), (1000, 2000), (1, 3), (1, 4), (1, 5), (3, 1), (3000, 2000), (3, 3), (3, 4), (3, 5), (4, 1), (4000, 2000), (4, 3), (4, 4), (4, 5), (5, 1), (5000, 2000), (5, 3), (5, 4), (5, 5), (6, 1), (6000, 2000), (6, 3), (6, 4), (6, 5), (7, 1), (7000, 2000), (7, 3), (7, 4), (7, 5), (8, 1), (8000, 2000), (8, 3), (8, 4), (8, 5), (9, 1), (9000, 2000), (9, 3), (9, 4), (9, 5), (10, 1), (10000, 2000), (10, 3), (10, 4), (10, 5)]


print('-------------------------------')


## LIST COMPREHENSION COM STRINGS

string='Linux Kernel'
newString=[letter for letter in string]
print(newString) # ['L', 'i', 'n', 'u', 'x', ' ', 'K', 'e', 'r', 'n', 'e', 'l']


newStringUnited=''.join(newString)
print(newStringUnited) # Linux Kernel

numLetters=5
newString2=[
    string[i:i+numLetters]
    for i in range(0,len(string),numLetters)
]
print(newString2) # ['Linux', ' Kern', 'el']


numLetters=2
newString2='.'.join([
    string[i:i+numLetters]
    for i in range(0,len(string),numLetters)
])
print(newString2) # Li.nu.x .Ke.rn.el 


### DESAFIO: Colocar a ultima letra de cada nome maiuscula e todas as outras minusculas com list comprehension

nomes=['luiz','maria','helena','joana','felipe']

novosNomes=[nome[0:-1].lower()+nome[-1].upper() for nome in nomes]
print(novosNomes) # ['luiZ', 'mariA', 'helenA', 'joanA', 'felipE']


print('-------------------------------')


### FLAT MAP

numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x]
print(numeros) # [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]

print(flat) # [0, 0, 1, 1, 2, 4, 3, 9, 4, 16, 5, 25, 6, 36, 7, 49, 8, 64, 9, 81]
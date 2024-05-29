"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

print('------------------------------')

# IMPORTANTE::***

# Empacotamento/Desempacotamento:

# Para empacotarmos ou desempacotarmos usamos o mesmo operador * (antes do nome da variavel)

colecao1=(1,2,3,4,5)
print(colecao1)
print(*colecao1) # aqui o * efetua o desempacotamento da tupla

colecao2=[1,2,3,4,5]
print(colecao2)
print(*colecao2) # aqui o * efetua o desempacotamento da lista

a,b,c,d=5,6,7,8
print(a)
print(b)
print(c)
print(d)
_,*empacotados=a,b,c,d
print(empacotados,type(empacotados))



print('------------------------------')

# def soma(x, y):
#     return x + y

# observe que args é recebido como uma tupla, embora os valores recebidos originalmente nao sejam uma, caso seja necessario alterar os valores dentro da funcao podemos converter a tupla em uma lista com o comando args=list(args), # nesse caso soma() recebe os valores nao empacotados e o sinal de * na frente de args significa o empacotamento dos argumentos pois assim será mais facil que eles sejam manipulados em conjunto dentro da funcao (o nome args é uma mera convenção, o valor da variável não precisa ser esse) 
def soma(*args):
    total = 0
    print(args, type(args)) 
    for numero in args:
        total += numero
    return total

# nesse caso soma2() recebe os valores ja empacotados e efetua o somatorio, por isso nao precisa utilizar o * na frente de args (o nome args é uma mera convenção, o valor da variável não precisa ser esse)
def soma2(args):
    total=0
    print(args,type(args))
    for numero in args:
        total+=numero
    return total


soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

print('------------------------------')

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10

outra_soma = soma(*numeros) # como a nossa funcao soma vai realizar o empacotamento (*args) precisamos enviar valores desempacotados ou eles serao empacotados novamente (nesse caso virarao tuplas dentro de tuplas), logo teriamos que passar com o * na frente do nome da variavel
print(outra_soma)

print(sum(numeros))

print(*numeros) # o * na frente da variavel significa desenpacotamento/empacotamento, ou seja, ela deixa de ser uma tupla pra ser varias variaveis independentes

print(soma2([1,2,3])) # 6

print('------------------------------')

tupla1=(1,2,3,4)
lista1=[5,6,7,8]

print(sum(tupla1))
print(sum(lista1))
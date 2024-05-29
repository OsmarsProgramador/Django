# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    totalMultiplicacao=1
    for numero in args:
        try:
            float(numero)
            totalMultiplicacao*=numero
        except:
            print(f'Valor {numero} não é um número, ele será desconsiderado na operação')
    return totalMultiplicacao

variavel1=multiplica(2,3,4,5,6)
print(variavel1)
print(multiplica('a',2,3,4))
print(multiplica(5.5,3,4))
print(multiplica('l','m',5,8.8))

print('-----------------------------------')

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def parOuImpar(numero):
    if isinstance(numero, int):
        return f'{numero} é um número é par' if numero%2==0 else f'{numero} é um número é ímpar'
    else:
        return 'Função definida apenas para números inteiros'

print(parOuImpar(15))
print(parOuImpar(14))
print(parOuImpar(-4))
print(parOuImpar('a'))
print(parOuImpar(0.5))

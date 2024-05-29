"""
Exercicio A:
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entradaUsuario=input('Digite um numero inteiro: ')

try:
    numeroInteiro=int(entradaUsuario)
    if numeroInteiro%2 == 0:
        print('Número par')
    else:
        print('Número ímpar')
except:
    print("O número digitado não é um número inteiro.")
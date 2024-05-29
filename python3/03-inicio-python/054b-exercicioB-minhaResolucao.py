"""
Exercicio B:
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horaAtual=input('Digite a hora atual (apenas o numero inteiro da hora): ')

try:
    horaAtualInt=int(horaAtual)
    if horaAtualInt>=0 and horaAtualInt<=11:
        print('Bom dia')
    elif horaAtualInt>=12 and horaAtualInt<=17:
        print('Boa tarde')
    elif horaAtualInt>=18 and horaAtualInt<=23:
        print('Boa noite')
    else:
        print('Você precisa digitar um numero inteiro entre 0 e 23.')
except:
    print('Você precisa digitar um numero inteiro entre 0 e 23.')
"""
Exercicio C:
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nomeUsuario=input('Digite seu primeiro nome: ')

if nomeUsuario!='':
    if len(nomeUsuario)<=4:
        print('Seu nome é curto')
    elif len(nomeUsuario)==5 or len(nomeUsuario)==6:
        print('Seu nome é normal')
    elif len(nomeUsuario)>6:
        print('Seu nome é muito grande')
    else:
        print('Erro inesperado')
else:
    print('Você não digitou nada.')
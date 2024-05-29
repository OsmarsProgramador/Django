"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# import os para que possamos utilizar comandos desse modulo
import os

palavraSecreta='gol'
palavraSecreta=palavraSecreta.lower()

password=[]
for letra in enumerate(palavraSecreta):
    password.append('*') 

contador=0

print("JOGO DA PALAVRA SECRETA\n")

while True:
    letraTentativa=input('Digite uma letra: ').lower()

    if letraTentativa in palavraSecreta and len(letraTentativa)==1 and letraTentativa!='':
        for indice,letra in enumerate(palavraSecreta):
            if letraTentativa == letra:
                password[indice]=letra
    
    contador+=1

    print('Palavra formatada: ',end='')
    for letra in password:
        print(letra,end='')
    print()
    
    if '*' not in password:
        break

os.system('clear') # limpar a tela, pode ser qualquer comando que o sistema do usuario entenda em cmd ou bash dependendo do sistema
print('PARABÉNS! Você venceu!')
print('A palavra era ' + palavraSecreta)
print('Tentativas:',contador)
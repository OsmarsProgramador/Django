"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.

Por padrão, funções Python retornam None (nada).
"""



def Print():
    print('Várias1')
    print('Várias2')
    print('Várias3')
    print('Várias4')


# PARAMETROS sao os valores que sao recebidos (aqui nesse caso a, b, c)
# ARGUMENTOS sao os valores que sao passados para a funcao para que ela seja processada (no caso de baixo: 1, 2, 3)
def imprimir(a, b, c): # a, b, c sao parametros
    print(a, b, c)


Print()

imprimir(1, 2, 3) # 1, 2, 3 sao argumentos
imprimir(4, 5, 6) # 4, 5, 6 sao argumentos 

# na ausencia do argumento "nome" ele usará 'Sem nome' como argumento
def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()
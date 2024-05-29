"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

# escopo de funcoes sao absolutos, as variaveis declaradas nela funcionam apenas nelas e nas funcoes mais internas delas, as variaveis declaradas nas funcoes internas de uma funcao nao funcionam nas funcoes mais externas delas

# quando voce declara a variavel com mesmo nome dentro de uma funcao ela nao sera a varaivel externa e sim uma nova variavel com escopo proprio de funcao
k=5

def funcaoExterna():
    k = 10

    def funcaoInterna():
        k = 11
        j = 2
        print(k, j) # 11 2 -> utilizou o valor declarado nela mesma (funcaoInterna) e nao o valor da funcao funcaoExterna

    funcaoInterna()
    print(k) # 10 -> valor declarado na funcaoExterna e nao alterado pela funcaoInterna que tem escopo proprio


funcaoExterna()

print(k) # 5 -> observe que mesmo com a manipulacao de uma variavel k de mesmo nome a variavel exerna k permaneceu inalterada

print('\n--------------------------------\n')




x = 1

# ao utilizarmos o comando global x fazemos com que a funcao passe a UTILIZAR e ALTERAR a variavel x externa que possui escopo de modulo, ou seja, apos a funcao manipular a variavel x seu resultado final permanecera aquele adquirido dentro da funcao
def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)
    # print(y) <- nao funciona, pois o escopo de y é apenas interno da funcao outra_funcao, nao funciona na funcao de escopo maior


print(x) 
escopo()
print(x)

print('\n--------------------------------\n')

# aparentemente nao existe escopo de lacos de repeticao como pode se ver nos exemplos abaixo em python:
if True:
    z=10

vetor=[1,2,3]

for i,item in enumerate(vetor):
    w=item

print(z) # 10
print(i) # 2
print(w) # 3




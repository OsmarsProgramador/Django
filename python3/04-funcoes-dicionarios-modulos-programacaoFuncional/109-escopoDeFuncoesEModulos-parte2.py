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

w=6

def escopo():
    global x # possibilita alteracao da variavel x no ambito global pela funcao mesmo que seja efetuado internamente
    x = 10
    print(w) # 6 -> acessa variaveis do escopo global

    def outra_funcao():
        global x # possibilita alteracao da variavel x no ambito global pela funcao mesmo que seja efetuado internamente
        x = 11
        y = 2
        print(x, y) # 11 2
        print(w) # 6 -> acessa variaveis do escopo global

    outra_funcao()
    print(x) # 11
    # print(y) -> erro, y é inalcancavel no escopo da funcao escopo(), sendo apenas alcancavel no escopo da funcao outra_funcao()


print(x) # 1 -> x antes de ser processado pela funcao escopo

escopo()

print(x) # 11 -> como foi definido 'global x' dentro das funcoes escopo() e outra_funcao() ambas puderam alterar a variavel x no ambito do escopo global

# print(y) -> erro, y é inalcancavel no escopo da funcao escopo(), sendo apenas alcancavel no escopo da funcao outra_funcao()
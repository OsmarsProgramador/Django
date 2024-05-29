# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def x234(numero):
    valores=[]
    try:
        float(numero)
        multiplicador=2
        for item in range(0,3):
            valores.append(numero*multiplicador)
            multiplicador+=1
        return valores
    except:
        return 'Operação com erro: Valor não numérico'
    


print(x234(5))
print(x234(6.5))
print(x234('a'))
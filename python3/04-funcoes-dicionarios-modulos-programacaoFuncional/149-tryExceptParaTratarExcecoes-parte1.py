# (Parte1) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

# cada tipo de except trata apenas o tipo de erro respectivo, excetuando-se Exception que trata todos, caso o except nao tenha tipo tambem trata todos os tipos de erro

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError): # tratando dois erros em apenas uma linha (é possivel)
    print('TypeError + IndexError')
except Exception: # tratamento de erro generico (equivalente a ter so o except)
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')
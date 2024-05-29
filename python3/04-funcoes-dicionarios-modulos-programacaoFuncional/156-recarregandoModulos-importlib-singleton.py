import importlib # biblioteca utilizada para importar modulos do python

import moduloTeste156

print(moduloTeste156.variavel)

for i in range(10):
    import moduloTeste156 # observe que ele nao reimprime os dados, a importacao eh singleton, ou seja, so pode ter uma instancia por modulo (ele nao importa de novo por questao de eficiencia)

    importlib.reload(moduloTeste156) # comando para recarregar o modulo (o import puro nao funciona para isso se executado novamente)

    print(i)

print('Fim')

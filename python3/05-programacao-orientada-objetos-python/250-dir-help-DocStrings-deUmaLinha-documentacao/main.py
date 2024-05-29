import uma_linha

# mostra tudo que existe nesse modulo (tipos de informacoes, variaveis, funcoes, etc)
print(dir(uma_linha)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'funcao', 'variavel']

print(uma_linha.__doc__) # O que seu módulo faz

print(uma_linha.__file__) # c:\Users\jharbes\Documents\GitHub\python3\05-programacao-orientada-objetos-python\250-dir-help-DocStrings-deUmaLinha-documentacao\uma_linha.py

print(uma_linha.__name__) # uma_linha

print('\n---------------------------------------\n')

help(uma_linha)

# output:

# Help on module uma_linha:

# NAME
#     uma_linha - O que seu módulo faz

# FUNCTIONS
#     funcao()

# DATA
#     variavel = 'valor'

# FILE
#     c:\users\jharbes\documents\github\python3\05-programacao-orientada-objetos-python\250-dir-help-docstrings-deumalinha-documentacao\uma_linha.py
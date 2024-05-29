"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal

# no caso de usarmos o float puro (conversao e identificacao automatica de tipos do python) nao teremos a precisao de resposta para 0.8
numero1=0.1
numero2=0.7
numero3=numero1+numero2
print(numero3) # 0.7999999999999999
print(f'{numero3:.2f}') # 0.80
print(round(numero3, 2)) # 0.8
print(type(numero3)) # <class 'float'>

print('-------------------------------------')

# observe que com a utilizacao de float na conversao para decimal ainda existe imprecisao do float, para que seja correto deve ser utilizar string
num1 = decimal.Decimal(0.1)
num2 = decimal.Decimal(0.7)
num3 = num1 + num2 
print(num3) # 0.7999999999999999611421941381
print(f'{num3:.2f}') # 0.80
print(round(num3, 2)) # 0.80
print(type(num3)) # <class 'decimal.Decimal'>

print('-------------------------------------')

# a funcao decimal.Decimal precisa receber uma string para que seja retornado o valor correto, caso seja informado um float ainda havera erro conforme acima
numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2 # 0.8
print(numero_3) # 0.8
print(f'{numero_3:.2f}') # 0.80
print(round(numero_3, 2)) # 0.80
print(type(numero_3)) # <class 'decimal.Decimal'>
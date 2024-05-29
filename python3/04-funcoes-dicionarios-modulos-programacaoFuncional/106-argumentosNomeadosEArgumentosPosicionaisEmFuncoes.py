"""
Argumentos nomeados e não nomeados (posicionais) em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# execucao de funcao -> soma()
# nome de funcao -> soma
# definicao de funcao -> def soma

def soma(x, y, z): 
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

print(soma)

# apos nomear um argumento todos que vierem depois terao que ser nomeados, os que vierem antes nao precisam
soma(1, 2, 3) 
soma(1, y=2, z=5)
soma(5, z=2, y=7)

# aqui usamos os argumentos nomeados, ou seja, embora estejam fora da ordem normal da funcao eles obedecerao o nome definido nos parametros originais da funcao, z sera o 3o argumento, x sera o 1o argumento e y sera o 2o argumento mesmo aqui embaixo estando em ordem diferente
soma(z=11, x=1, y=5)

print(1, 2, 3, sep='-')
"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.

Refatorar: editar o seu código.
"""

# sempre que houve um valor padrao como z, todos os outros parametros que vierem DEPOIS tambem terao que ter valores padrao
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)


def multiplicacao(a, b=1, c=2):
    print('a * b * c =',a*b*c)
    return a*b*c 

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)
print()
multiplicacao(1)
multiplicacao(2,3)
multiplicacao(5,6,7)
print(multiplicacao(5))




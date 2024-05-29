import enum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

# ou

# podemos numerar as opcoes manualmente ou podemos usar como abaixo para que seja feita a enumeracao automatica (enum.auto()), que começará do 1.
class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()



# observe que os valores de enum podem ser mencionados de tres maneiras diferentes
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA) # Direcoes.ESQUERDA Direcoes.ESQUERDA Direcoes.ESQUERDA


# como chamar o nome (nome e valor)
print(Direcoes(1).name) # ESQUERDA
print(Direcoes.ESQUERDA.value) # 1



def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA) # Movendo para ESQUERDA (1)
mover(Direcoes.DIREITA) # Movendo para DIREITA (2)
mover(Direcoes.ACIMA) # Movendo para ACIMA (3)
mover(Direcoes.ABAIXO) # Movendo para ABAIXO (4)
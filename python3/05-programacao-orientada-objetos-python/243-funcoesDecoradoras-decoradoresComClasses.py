# Funções decoradoras e decoradores com classes

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


# cls leia-se class, apenas uma maneira de abreviar para nao usar a palavra reservada
def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil) # Time({'nome': 'Brasil'})
print(portugal) # Time({'nome': 'Portugal'})

print(terra) # Planeta({'nome': 'Terra'})
print(marte) # Planeta({'nome': 'Marte'})
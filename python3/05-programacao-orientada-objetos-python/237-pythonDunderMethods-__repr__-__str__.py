# Python Dunder Methods __repr__ e __str__

# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames

# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        # as duas expressoes abaixo para class_name retornarao o nome da classe:
        # class_name = self.__class__.__name__
        class_name = type(self).__name__

        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'


p1 = Ponto(1, 2)
p2 = Ponto(978, 876)

# observe que o metodo dunder __str__ manipulou o retorno para que fosse uma string da maneira que fosse conveniente e nao o retorno usual de local na memoria que o objeto esta vinculado
print(p1) # (1, 2)

# idem ao anterior porem com informacoes para ajudar os desenvolvedores a conhecerem o objeto, o __repr__ tem a funcao de retornar uma string com mais informacoes no auxilio do desenvolvedor
print(repr(p2)) # Ponto(x=978, y=876, z='String')


# em f strings {p2} retornaria o __str__ e {p2!r} retornaria o __repr__
print(f'{p2}') # (978, 876)
print(f'{p2!s}') # (978, 876)
print(f'{p2!r}') # Ponto(x=978, y=876, z='String')
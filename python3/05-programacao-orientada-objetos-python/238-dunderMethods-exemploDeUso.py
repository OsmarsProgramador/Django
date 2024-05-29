# Exemplo de uso de dunder methods (métodos mágicos)

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
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # representacao entre desenvolvedores, pois alem de ter os dados do objeto tambem possui informacoes da classe
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other): # __gt__ -> greater then
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other


if __name__ == '__main__':
    p1 = Ponto(4, 2)  # 6
    p2 = Ponto(6, 4)  # 10
    p3 = p1 + p2


    # observe que o dunder __add__ manipulou a expressao de soma para que ela retorne um valor da maneira que foi conveniente que fosse feita para o desenvolvedor, sem essa manipulacao nao haveria sequer um retorno
    print(p3) # Ponto(x=10, y=6)

    # Sem a criacao do metodo __add__ o retorno seria o seguinte:     
    # p3 = p1 + p2 TypeError: unsupported operand type(s) for +: 'Ponto' and 
    'Ponto'


    # idem ao anterior, o dunder __gt__ manipulou a expressao > de maneira que a expressao retornasse o valor 'MAIOR' de acordo com o interessante para o desenvolvedor, de maneira diferente nao haveria retorno

    

    print('P1 é maior que p2', p1 > p2) # P1 é maior que p2 False

    print('P2 é maior que p1', p2 > p1) # P2 é maior que p1 True

    # sem a criacao do metodo __gt__ o retorno seria o seguinte:
    # TypeError: '>' not supported between instances of 'Ponto' 
    # and 'Ponto'
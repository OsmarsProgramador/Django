# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno


# string = MinhaString('Luiz')
# print(string.upper())

class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        # print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs)

    def metodo(self):
        super().metodo()  # B # faça metodo em B
        super(B, self).metodo()  # A # faça metodo em A
        # super(A, self).metodo()  # object # erro
        A.metodo(self)
        B.metodo(self)
        print('C')


# mro() -> retorna o method resolution order (Ordem de resolucao dos metodos em relacao à herança)
print(C.mro())
print(B.mro())
print(A.mro())

c = C('Atributo', 'Qualquer')
print(c.atributo) # Atributo
print(c.outra_coisa) # Qualquer

c.metodo()
# B
# A
# A
# B
# C

print(c.atributo_a) # valor a
print(c.atributo_b) # valor b
print(c.atributo_c) # valor c

c.metodo()
# B
# A
# A
# B
# C
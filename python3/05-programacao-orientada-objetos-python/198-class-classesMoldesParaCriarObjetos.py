# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.

# Por convenção, usamos PascalCase para nomes de
# classes.

# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    ...


p1 = Pessoa()
p1.nome = 'Luiz'
p1.sobrenome = 'Otávio'

p2 = Pessoa()
p2.nome = 'Maria'
p2.sobrenome = 'Joana'

print(p1) # <__main__.Pessoa object at 0x0000020AF5BE0C10>
print(p1.nome) # Luiz
print(p1.sobrenome) # Otávio

print()

print(p2) # <__main__.Pessoa object at 0x0000020AF5BE0970>
print(p2.nome) # Maria
print(p2.sobrenome) # Joana
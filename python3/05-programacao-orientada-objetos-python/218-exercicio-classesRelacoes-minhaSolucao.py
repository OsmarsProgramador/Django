# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self,nome) -> None:
        self._nome=nome
        self._motor=None
        self._fabricante=None

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome=nome

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,motor):
        self._motor=motor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self,fabricante):
        self._fabricante=fabricante

    def printCarro(self):
        return f'Nome: {self.nome}\nMotor: {self.motor.tipo}\nFabricante: {self.fabricante.nome}\n'


class Motor:
    def __init__(self,tipo) -> None:
        self.tipo=tipo


class Fabricante:
    def __init__(self,nome) -> None:
        self.nome=nome

motor1=Motor('1.5 Turbo')
motor2=Motor('4.1 V8')


fabricante1=Fabricante('Volkswagen')
fabricante2=Fabricante('Chevrolet')

carro1=Carro('Golf GTI')
carro1.motor=motor1
carro1.fabricante=fabricante1

carro2=Carro('Camaro')
carro2.motor=motor2
carro2.fabricante=fabricante2

carro3=Carro('Corvette')
carro3.motor=motor1
carro3.fabricante=fabricante2

print(carro1.printCarro())
print(carro2.printCarro())
print(carro3.printCarro())
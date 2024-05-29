# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código

class Carro:
    # inicializando os atributos
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


string = 'Luiz'
# metodo da classe string
print(string.upper()) # LUIZ

fusca = Carro('Fusca')
print(fusca.nome) # Fusca
fusca.acelerar() # Fusca está acelerando...

celta = Carro(nome='Celta')
print(celta.nome) # Celta
celta.acelerar() # Celta está acelerando...
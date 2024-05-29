# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)

# Instância da class (objeto) - Tem os dados

# Uma classe pode gerar várias instâncias.

# Na classe o self é a própria instância.

# o nome 'self' é apenas uma convencao, poderia ser usado qualquer outro nome em seu lugar

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
fusca.acelerar() # Fusca está acelerando...
Carro.acelerar(fusca) # Fusca está acelerando...
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome='Celta')
celta.acelerar() # Celta está acelerando...
Carro.acelerar(celta) # Celta está acelerando...
# print(celta.nome)
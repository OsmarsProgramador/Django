# Atributos de classe

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual) # 2022
print(p1.ano_atual) # 2022

p1.ano_atual=0
# Pessoa.ano_atual = 1

print(Pessoa.ano_atual) # 2022
print(p1.ano_atual) # 0

print(p1.get_ano_nascimento()) # 1987
print(p2.get_ano_nascimento()) # 2010
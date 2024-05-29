# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)

# p1.nome = 'EITA'
print(p1.idade) # 35

p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'

print(p1.__dict__) # {'nome': 'João', 'idade': 35, 'outra': 'coisa'}

# apaga o atributo nome do objeto
del p1.__dict__['outra']

# imprime um dicionario que retem os atributos e valores do objeto
print(p1.__dict__) # {'nome': 'João', 'idade': 35}

# imprime um dicionario que retem os atributos e valores do objeto
print(vars(p1)) # {'nome': 'João', 'idade': 35}

# print(p1.outra)
# print(p1.nome)

# imprime um dicionario que retem os atributos e valores do objeto
print(vars(p1)) # {'nome': 'João', 'idade': 35}

print(p1.nome) # João
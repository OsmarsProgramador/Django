# Herança simples - Relações entre classes

# Associação - usa outro objeto
# Agregação - tem outro objeto
# Composição - É dono de outro objeto
# Herança - É um subtipo do objeto pai

#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    # self.__class__.__name__ imprime o nome da classe
    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('EITA, nem saí da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = 'cpf aluno'
    ...


c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_classe() 
# EITA, nem saí da classe CLIENTE
# Luiz Otávio Cliente

a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()
# Classe PESSOA
# Maria Helena Aluno

print(a1.cpf) # cpf aluno
print(a1.__dict__) # {'nome': 'Maria', 'sobrenome': 'Helena'}

help(Cliente)
"""
Help on class Cliente in module __main__:                       

class Cliente(Pessoa)
 |  Cliente(nome, sobrenome)
 |  
 |  Method resolution order:  ## ordem em que o python procura as informacoes nas classes
 |      Cliente
 |      Pessoa
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  falar_nome_classe(self)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from Pessoa:
 |  
 |  __init__(self, nome, sobrenome)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Pessoa:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)      
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Pessoa:
 |
 |  cpf = '1234'

"""
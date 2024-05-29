# abstractmethod para qualquer método já decorado (@property e setter)

# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.

# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.

from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    # colocar o @abstractmethod sempre o mais interno possivel
    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    # como o name nao pertence a classe Foo teremos que lancar antes o nome da classe de onde o atributo eh herdado
    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name


foo = Foo('Bar')

print(foo.__dict__)
print(foo.name) # Bar
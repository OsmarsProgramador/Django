# dir, hasattr, setattr e getattr em Python

# dir(objeto) - lista todos os atributos definidos para o objeto

# hasattr(objeto,metodo) - confere se o objeto possui aquele metodo/atributo

# getattr(objeto,metodo) - busca aquele metodo/atributo

string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    upperX=print(getattr(string, metodo)) # buscando o metodo referente às strings salvas, podemos jogar em uma variavel 
    print(getattr(string, metodo)()) # maneira de chamar um metodo cujo nome esteja numa variavel
else:
    print('Não existe o método', metodo)
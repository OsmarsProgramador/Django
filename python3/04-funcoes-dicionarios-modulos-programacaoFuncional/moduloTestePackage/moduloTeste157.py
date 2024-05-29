# quando a importacao for por meio do comando:
# from moduloTestePackage.moduloTeste157 import *
# poderemos usar o comando abaixo pra dizer o que sera efetivamente importado (__all__ = *), na ausencia dela o mesmo comando importara tudo que estiver no codigo do modulo

# observe que para importarmos um modulo na pasta irma teremos que mencionar tambem o package, isso se da porque o ponto de vista de importacao sempre sera em funcao da pasta main do projeto
from moduloTestePackage.moduloTeste158 import fala_oi

__all__ = [
    'variavel',
    'soma_do_modulo',
    'nova_variavel',
]

variavel = 'Alguma coisa'


def soma_do_modulo(x, y):
    return x + y


nova_variavel = 'OK'
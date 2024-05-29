from sys import path

import moduloTestePackage # importar o package apenas sozinho nao fara com que ele importe os modulos internos do package

import moduloTestePackage.moduloTeste157
from moduloTestePackage import moduloTeste157
from moduloTestePackage.moduloTeste157 import *

from moduloTestePackage.moduloTeste157 import soma_do_modulo

print(__name__)
print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(moduloTestePackage.moduloTeste157.soma_do_modulo(1, 2))
print(moduloTeste157.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)
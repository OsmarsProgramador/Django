from sys import path
# from sys import path

import moduloTestePackage.moduloTeste157
from moduloTestePackage import moduloTeste157
from moduloTestePackage.moduloTeste157 import *

from moduloTestePackage.moduloTeste157 import soma_do_modulo

print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(moduloTestePackage.moduloTeste157.soma_do_modulo(1, 2))
print(moduloTeste157.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)

from moduloTestePackage.moduloTeste157 import fala_oi, soma_do_modulo

print(__name__)
fala_oi()
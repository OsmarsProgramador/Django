"""

Por que a importacao de * é uma má pratica?

https://stackoverflow.com/questions/2386714/why-is-import-bad

"""

# utilizamos essa maneira de importacao, que em conjunto com o arquivo __init__.py na pasta escolhida para importacao pode importar logo todos os modulos presentes no package, atentar para o preenchimento do arquivo __init__ onde serao colocados os modulos desejados para inicializacao

# funciona assim mas é uma má pratica, nesse caso pode ser utilizado sim
from moduloTestePackage import *

from moduloTestePackage import fala_oi, soma_do_modulo, variavel

print(__name__)
fala_oi()
# print(__name__)
# fala_oi()

print(variavel)
print(soma_do_modulo(2, 3))
fala_oi()
# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

# importando o modulo inteiro, nesse caso os comandos demandam a sintaxe sys.parteNecessaria
import sys

# sys.exit() # finaliza o programa

platform = 'A MINHA' # nesse caso foi liberada a palavra platform para ser usada como variavel, se tivesse sido importada platform ai nao poderia usa-la como variavel

print(sys.platform)
print(platform)


# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# importando partes do modulo, nesse caso os comandos nao usarao sys na sintaxe, apenas exit ou platform direto
from sys import exit, platform

print(platform)

# alias 1 - import nome_modulo as apelido
import sys as s

sys = 'alguma coisa'
print(s.platform)
print(sys)


# alias 2 - from nome_modulo import objeto as apelido
from sys import exit as ex
from sys import platform as pf

print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# eh uma ma pratica pois agora todos os nomes estarao disponiveis e ocupados do modulo sys
# ex: exit, platform etc
from sys import *


# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
from sys import exit, platform


print(platform)
exit() # finaliza o programa (igual ao sys.exit(), so esta diferente porque foi importado de maneira diferente)
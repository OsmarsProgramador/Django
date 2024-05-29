# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

import sys
print(sys.path)

sys.path.append('C:\\Users\\jharbes\\Documents') # adiciona a pasta nas listas de path do sistema, agora seria possivel importar modulos de dentro dessa pasta

import moduloTeste
import moduloPython # modulo que esta no diretorio adicionado com o append de forma manual

print('Este módulo se chama', __name__)

print(*sys.path,sep='\n') # imprimindo todos os caminhos disponiveis para importacao de modulos
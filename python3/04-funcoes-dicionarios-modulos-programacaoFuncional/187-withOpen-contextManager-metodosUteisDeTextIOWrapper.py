# Criando arquivos com Python + Context Manager with
# with open (context manager) e métodos úteis do TextIOWrapper
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

caminho_arquivo = '.\\04-funcoes-dicionarios-modulos-programacaoFuncional\\187-aula-criandoArquivo.txt'

with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')

print('---------------------------------\n')

# w+ utiliza a funcao de escrita mais leitura
with open(caminho_arquivo, 'w+') as arquivo: 
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

    # observe o formato de tuplas ao enviar o writelines
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

    # tambem funciona com listas, ou seja, iteraveis em geral 
    arquivo.writelines(['Linha 5\n','Linha 6\n'])

    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0) # move o cursor para o ponto do arquivo desejado

    print(arquivo.readline(), end='') # o end='' remove o '\n' do fim da linha, pois com ele haveriam duas quebras de linha, a do '\n' e a do proprio comando print

    print(arquivo.readline().strip()) # .strip() funciona da mesma maneira que o end='', sendo que ele remove espaços do inicio e fim da linha, o \n é considerado um espaco no python 

    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())


print('---------------------------------\n')

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
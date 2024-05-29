import os


caminho_arquivo = '.\\04-funcoes-dicionarios-modulos-programacaoFuncional\\'

nomeArquivo='189-aula-criandoArquivo.txt'



with open(caminho_arquivo+nomeArquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

os.rename(caminho_arquivo+nomeArquivo, caminho_arquivo+'189-aula-criandoArquivo2.txt') # alterando o nome do arquivo

os.remove(caminho_arquivo+'189-aula-criandoArquivo2.txt') # ou unlink para apagar o arquivo
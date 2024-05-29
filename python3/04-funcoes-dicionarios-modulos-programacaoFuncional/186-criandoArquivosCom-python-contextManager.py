"""
.vscode/settings.json

{
  "window.zoomLevel": 1,
  "editor.fontSize": 26,
  "editor.hover.enabled": false,
  "editor.hover.enabled": true,
  "workbench.startupEditor": "none",
  "explorer.compactFolders": false,
  "terminal.integrated.fontSize": 24,

"""

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação, no entanto dificilmente é usado)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita, r+ ou w+)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = '.\\04-funcoes-dicionarios-modulos-programacaoFuncional\\186-aula-criandoArquivo.txt'

# abrindo o arquivo (e criando ao mesmo tempo caso nao exista)
arquivo = open(caminho_arquivo, 'w')

arquivo.close() # fechando o arquivo, importantissimo


## Context manager: (ja fecha automaticamente no fim do laço)
with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')
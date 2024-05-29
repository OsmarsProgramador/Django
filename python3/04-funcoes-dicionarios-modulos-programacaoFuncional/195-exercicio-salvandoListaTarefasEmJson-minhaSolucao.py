# Exercício - Lista de tarefas com desfazer e refazer

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar

# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']

# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import json

caminhoArquivoJson='.\\04-funcoes-dicionarios-modulos-programacaoFuncional\\195-json-arquivoAuxiliar.json'

try:
    with open(caminhoArquivoJson, 'r', encoding='utf8') as arquivo:
        listas = json.load(arquivo)

except:
    print('Arquivo JSON não localizado, lista inicial de tarefas será vazia.\n')
    listas={
        'todoList':[],
        'refazerList':[]
    }


def printarTarefas():
    print('TAREFAS:')
    if len(listas['todoList'])<1:
        print('Não há tarefas para serem listadas!')
    else:
        for task in listas['todoList']:
            print(task)
    print()



while True:
    print('Comandos: listar, desfazer, refazer, fim')
    tarefa=input('Digite uma tarefa ou comando: ')
    print()
    if tarefa=='listar':
        printarTarefas()
    elif tarefa=='desfazer':
        if len(listas['todoList'])<1:
            print('Não há tarefa para desfazer!\n')
        else:
            listas['refazerList'].append(listas['todoList'].pop())
            printarTarefas()
    elif tarefa=='refazer':
        if len(listas['refazerList'])<1:
            print('Não há tarefa para refazer!\n')
        else:
            listas['todoList'].append(listas['refazerList'].pop())
            printarTarefas()
    elif tarefa=='fim':
        break
    else:
        listas['todoList'].append(tarefa)
        printarTarefas()


with open(caminhoArquivoJson, 'w', encoding='utf8') as arquivo:
    json.dump(
        listas,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )
    
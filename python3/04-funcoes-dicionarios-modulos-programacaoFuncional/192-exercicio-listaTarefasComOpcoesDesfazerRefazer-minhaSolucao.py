# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)

# Everybody wants to rule the world - Tears for fears

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar

# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']

# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


todoList=[]
refazerList=[]


while True:
    print('Comandos: listar, desfazer, refazer, fim')
    tarefa=input('Digite uma tarefa ou comando: ')
    print()
    if tarefa=='listar':
        print('TAREFAS:')
        if len(todoList)<1:
            print('Não há tarefas para serem listadas!')
        else:
            for task in todoList:
                print(task)
        print()
    elif tarefa=='desfazer':
        if len(todoList)<1:
            print('Não há tarefa para desfazer!\n')
        else:
            refazerList.append(todoList.pop())
    elif tarefa=='refazer':
        if len(refazerList)<1:
            print('Não há tarefa para refazer!\n')
        else:
            todoList.append(refazerList.pop())
    elif tarefa=='fim':
        break
    else:
        todoList.append(tarefa)
        print('TAREFAS:')
        for task in todoList:
                print(task)
        print()
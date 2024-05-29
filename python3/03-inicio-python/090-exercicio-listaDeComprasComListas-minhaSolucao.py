"""
Faça uma lista de compras com listas, o usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de indices inexistentes na lista.
"""

listaCompras=[]

while True:
    print('\nLISTA DE COMPRAS\n')
    print('Opções disponíveis:')
    print('1- Inserir item na lista.')
    print('2- Excluir item da lista.')
    print('3- Listar itens da lista')
    print('0- Sair do programa\n')

    opcao=input('Digite a opção desejada: ')
    
    if opcao=='1':
        item=input('\nDigite o nome do item a ser adicionado na lista: ')
        listaCompras.append(item)
        continue
    elif opcao=='2':
        try:
            opcaoExclusao=input('\nSelecione o número do item a ser excluído: ')
            opcaoExclusao=int(opcaoExclusao)
            print(f'\nItem {listaCompras.pop(opcaoExclusao-1)} excluído com sucesso!\n')
            print()
        except: # podemos usar o except com as opcoes de tipo de erro de acordo com a solucao do professor, neste exercicio me pareceu desncessario
            print('\nNúmero de item inválido!\n')
    elif opcao=='3':
        print()
        if len(listaCompras)>=1:
            for indice,item in enumerate(listaCompras):
                print(f'Item nº{indice+1}: {item}')
            print()
        else:
            print('A lista está vazia.\n')
    elif opcao=='0':
        print('\nSaindo do programa...\n')
        break
    else:
        print('\nOpção inválida.\n')
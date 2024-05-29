# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contadorDeAcertos=0

for indice,item in enumerate(perguntas):
    print(item['Pergunta']+'\n')
    print('Opções:')
    for i1,resposta in enumerate(perguntas[indice]['Opções']):
        print(f'{i1}) {resposta}')
    
    opcaoEscolhida=input('Escolha uma opção: ')
    respostaQuestao=str(perguntas[indice]['Opções'].index(perguntas[indice]['Resposta']))

    if opcaoEscolhida==respostaQuestao:
        print('Acertou!\n')
        contadorDeAcertos+=1
    else:
        print('Errou!\n')

print(f'Você acertou {contadorDeAcertos} de 3 perguntas.')
        
            
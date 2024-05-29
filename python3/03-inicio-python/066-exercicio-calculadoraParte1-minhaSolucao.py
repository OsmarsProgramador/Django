""" Calculadora com while """
while True:
    try:
        primeiroNumero=input('Digite o primeiro valor da equacao: ')
        segundoNumero=input('Digite o segundo valor da equacao: ')
        operador=input('Escolha o operador (+, - ou *): ')
        primeiroNumero=float(primeiroNumero)
        segundoNumero=float(segundoNumero)
        if operador=='+':
            print(f'{primeiroNumero} + {segundoNumero} = {primeiroNumero+segundoNumero}')
        elif operador=='-':
            print(f'{primeiroNumero} - {segundoNumero} = {primeiroNumero-segundoNumero}')
        elif operador=='*':
            print(f'{primeiroNumero} * {segundoNumero} = {primeiroNumero*segundoNumero}')
        else:
            print('Operador desconhecido')
    except Exception as error: # gera o erro pra que possa ser impresso
        print(error) # imprime o erro que ocasionou a quebra do programa
        print('Serão aceitos apenas valores númericos')
    

    #########
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
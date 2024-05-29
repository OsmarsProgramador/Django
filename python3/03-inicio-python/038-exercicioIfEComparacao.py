primeiro_valor=input('Digite um valor: ')
segundo_valor=input('Digite um valor: ')

# observe que a resposta será correta mesmo sem que seja feita a conversao entre string e int/float, pois para essa comparacao o python utilizara a tabela unicode, ou seja, serve também para letras (apenas para respostas com um digito, de letras ou numeros)   

if primeiro_valor>segundo_valor:
    print(f'{primeiro_valor=} é maior do que {segundo_valor=}')
elif segundo_valor>primeiro_valor:
    print(f'{segundo_valor=} é maior do que {primeiro_valor=}')
else:
    print(f'{primeiro_valor=} é igual a {segundo_valor=}')
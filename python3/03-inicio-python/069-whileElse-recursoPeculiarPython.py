""" while/else """

# o else do while só será executado caso o while complete TODOS OS SEUS LOOPS, no exemplo abaixo como ele SAI DO LAÇO ANTES de completar todos os loops de repeticao ele NAO executará o else 

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')
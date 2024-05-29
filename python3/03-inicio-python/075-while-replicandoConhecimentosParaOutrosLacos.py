# Aqui deixamos claro que os comandos vistos anteriormente como continue, break e o else no fim também funcionam no for como funcionavam no while

# continue - pula pra proxima repeticao

# break - cai pra fora do laco

# else -  executa o que tem no else apenas se o for chegar ao seu fim com todas as execucoes completas


for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')
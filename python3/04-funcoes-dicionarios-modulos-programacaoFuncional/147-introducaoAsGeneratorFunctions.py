# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0, maximum=10):
    while True:
        yield n # yield pausa a execucao da funcao, se fizermos next nesse ponto do generator ele retornara n e depois somara 1 a n conforme o codigo ate que n seja menor que o maximum
        n += 1

        if n >= maximum:
            return # levanta uma excecao de StopIteration com o valor do return que houver (nao obrigatorio)


gen = generator(maximum=1000000)

print(next(gen))
print(next(gen))
print(next(gen))

print('-------------------------------')

gen2=generator(maximum=5)

print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
# print(next(gen2)) # erro, StopIteration

print('-------------------------------')

gen3=generator()

for n in gen3: # retorna/finaliza quando n=10 (nao imprime o 10)
    print(n)
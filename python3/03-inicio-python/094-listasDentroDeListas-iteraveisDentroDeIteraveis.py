"""
Lista de listas e seus índices (matrizes), (listas dentro de tuplas e vice versa), (strings dentro de listas)

Iteraveis dentro de iteraveis
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0,10,20,30,40)],  # 2
]

# a virgula com o espaco vazio no fim do vetor nao caracteriza um elemento sem valor (indice), ele eh exatamente como se nao estivesse aqui, abaixo os dois exemplos sao iguais
vetor=[1,2,3] 
vetor1=[1,2,3,]

print(vetor) # [1, 2, 3]
print(vetor1) # [1, 2, 3]
# print(vetor1[3]) # erro out of range

print('-----------------------------------')

print(salas)

print('-----------------------------------')

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[2][3][2])

print('-----------------------------------')

# for para alcancar os indices internos das listas dentro de listas, ou tuplas dentro de listas
for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2 
print(s3) # {1, 2, 3, 4}

s3 = s1 & s2
print(s3) # {2, 3}

# na diferenca a ordem importa
s3 = s2 - s1
print(s3) # {4}

# itens que nao estao nos dois (ao mesmo tempo), ou seja s1 + s2 - (s1 & s2)
s3 = s1 ^ s2
print(s3) # {1, 4}
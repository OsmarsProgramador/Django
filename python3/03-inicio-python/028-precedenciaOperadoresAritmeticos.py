# 1. (n + n)
# 2. **
# 3. * / // %  (operacoes com a mesma precedencia como essas sempre serao executadas da esquerda para a direita)
# 4. + -  (operacoes com a mesma precedencia como essas sempre serao executadas da esquerda para a direita)
conta1= 1 + 1 ** 5 + 5 # 7
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5) # 1024
conta_2 = (1 + int(0.5 + 0.5)) ** 5 + 5 # 37
print(conta1)
print(conta_1)
print(conta_2)
print(int(1.8)) # 1 (mantem apenas o valor inteiro)
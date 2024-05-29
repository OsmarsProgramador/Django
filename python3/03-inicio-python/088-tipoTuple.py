"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Maria', 'Helena', 'Luiz')
nomes2 = 'Maria', 'Helena', 'Luiz' # a ausencia dos colchetes tambem cria uma tupla
nomes3 = ['Maria', 'Helena', 'Luiz']

nomes3 = tuple(nomes) # converte de lista para tupla
nomes2 = list(nomes) # converte de tupla para lista

print(nomes[-1]) # Luiz
print(nomes) # ('Maria', 'Helena', 'Luiz')
print(nomes2) # ['Maria', 'Helena', 'Luiz']  -- ja convertido para lista
print(nomes3)
# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4)) # dessa maneira, adicionando essa tupla, colocaremos os elemntos um a um pois os iteraveis sao adicionados elemento a elemento, se adicionarmos uma palavra pura string serao adicionados as letras separadamente (no caso de mais de um elemento)
print(s1) # {1, 2, 3, 4, 'Luiz', 'Olá mundo'}

s2=set()
s2.add('Luiz')
print(s2) # {'Luiz'}    
# s1.clear() # Limpa o set
s1.discard('Olá mundo')
s1.discard('Luiz')
print(s1) # {1, 2, 3, 4}

# Operadores úteis:
# união | união (union) - Une
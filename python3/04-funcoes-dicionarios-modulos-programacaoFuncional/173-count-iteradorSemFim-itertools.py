# count é um iterador sem fim (itertools)
from itertools import count

c1 = count(step=8, start=8) # começa em 8 e anda de 8 em 8 mas nao tem fim

r1 = range(8, 100, 8) # comeca em 8, anda de 8 em 8 e termina no 100

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('---------------------------')

print('count')
for i in c1:
    if i >= 100:
        break

    print(i)
print()
print('range')
for i in r1:
    print(i)
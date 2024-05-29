a = 'AAAAA'
b = 'BBBBBB'
c = 1.1


# teste1=''.format(a,b,c)
# print(teste1)

string0 = 'a={} b={} c={}'
print(string0.format(a,b,c)) # nao sai nada

print() # pula uma linha por padrao

string1 = 'a={2} b={0} b={1} c={1}'.format(a,b,c) # tambem podemos pegar por indices, fazendo com que fiquem fora da ordem do format

print(string1,'\n')

string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
print(string)

print()

formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
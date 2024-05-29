"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

# inicio:
nova_string = ''
# resultado final:
nova_string += '*L*u*i*z* *O*t*á*v*i*o'


stringInterpolada=''
contador=0

while contador<len(nome):
    stringInterpolada+='*'
    stringInterpolada+=nome[contador]
    contador+=1

print(f'Resultado é {stringInterpolada}')
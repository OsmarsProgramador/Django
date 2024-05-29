# A funcao id() retorna a identidade de memoria da variavel em questao

# Exemplo:

v1='a'
print(id(v1))

# variaveis com valores iguais poderao utilizar a mesma identidade de memoria
v2='a'
print(id(v2))

v3='jorge'
print(id(v3))

v2='b'
print((id(v2))) # aqui ele mudou o endereco de memoria pois ela nao eh mais igual ao valor de v1 (endereco original)
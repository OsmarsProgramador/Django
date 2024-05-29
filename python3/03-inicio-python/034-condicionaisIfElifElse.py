# if / elif      / else
# se / se não se / se não
# 1 - python importante usar o : (dois pontos)

# 2 - parenteses sao opcionais nas condicoes 

# 3 - nao se usa else if e sim elif

# 4 - nao se utilizam chaves para delimitar o bloco, ele sera delimitado automaticamente pela indentacao corretamente feita

entrada = input('Você quer "entrar" ou "sair"? ')

if (entrada == 'entrar'):
    print('Você entrou no sistema')

    print(12341234)
elif entrada == 'sair': 
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')
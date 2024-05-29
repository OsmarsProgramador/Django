"""
Introdução ao empacotamento e desempacotamento
"""
lista1=[1,2,3]
num1,num2,num3=lista1

print(num1) # 1
print(num2) # 2
print(num3) # 3

# num1,num2=lista1 -- erro, poucas variaveis pra muitos valores na lista

print()

# num1,num2,num3,num4=lista1 -- erro, muitas variaveis para uma lista com tamanho insuficiente

lista2=[15,16,17,18]
num4, *resto=lista2 # nesse caso num4 recebera o primeiro valro da lista e a variavel resto recebera a lista sem o primeiro valor
print(num4) # 15
print(resto) # [16,17,18]

print()

_,nome1,*_=['Maria', 'Helena', 'Luiz'] 
print(nome1) # Helena
print(_) # ['Luiz']

print()

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz'] # utiliza-se os underlines para possibilitar que a variavel nome recebe o valor desejado que eh o 3o valor da lista. A utilizacao do _ (underline para isso é apenas uma convencao pois mostra no codigo um valor que nao sera utilizado e pode ser desprezado para aqueles que vierem a ler o codigo)
print(nome) # Luiz
print(resto) # []
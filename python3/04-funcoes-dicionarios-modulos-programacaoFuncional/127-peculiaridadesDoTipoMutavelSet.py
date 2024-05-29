# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# s1 = set()  # vazio
# s1 = {'Luiz', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s1={1,2,3,3,3,3,3,1}
print(s1) # {1 ,2 , 3} - observe que o set naturalmente ja exclui os elementos repetidos

# ELIMINANDO ELEMENTOS REPETIDOS COM SET *** (observe que a ordem pode nao ser garantida com set)
l1=[1,2,3,3,3,3,3,1]
s2=set(l1)
l2=list(s2)
print(l2,type(l2)) # [1, 2, 3] <class 'list'>

# s4={1,2,3,{123}} ERRO -> sets nao aceitam tipos mutaveis como seus elementos

# print(s1[0]) ERRO -> sets nao tem indice


s3 = {1, 2, 3}
print(3 not in s1) # False
print(2 in s1) # True
print(0 in s1) # False


for numero in s1:
    print(numero)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
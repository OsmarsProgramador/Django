# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
print(s1,type(s1)) # set() <class 'set'>

s2={} # CUIDADO! nesse caso nao cria um set e sim um dicionario
print(s2,type(s2)) # {} <class 'dict'>  

s1 = {'Luiz', 1, 2, 3}  # com dados
print(s1) # {1, 2, 3, 'Luiz'}  

s3={1,2,3}
print(s3,type(s3)) # {1, 2, 3} <class 'set'>

# nessa maneira de criacao de set ele vai iterar sobre a palavra luiz, e nao vai garantir a ordem dos elementos
s4=set('Luiz')
print(s4,type(s4)) # {'u', 'L', 'z', 'i'}  

s5={'Luiz'}
print(s5,type(s5)) # {'Luiz'} <class 'set'>

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
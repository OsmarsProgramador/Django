"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""
print(1234)

# Aspas simples
print('Luiz Otávio')
print(1, 'Luiz "Otávio"') # aspas duplas dentro de aspas simples sairao na impressao

# Aspas duplas
print("Luiz Otávio")
print(2, "Luiz 'Otávio'") # aspas simples dentro de aspas duplas sairao na impressao

# o caractere de ESCAPE (\) faz com que o proximo caractere nao seja 'interpretado' , ou seja, sera mantido na impressao
print("Luiz \"Otávio\"") 

# r  -- o r faz com que os caracteres de escape tambem sejam mantidos na impressao, ou seja, tudo sera impresso, muito usado tambem em expressoes regulares
print(r"Luiz \"Otávio\"")
# \r\n -> CRLF - carriage return line feed
# \n -> LF - line feed
print(12,34) # o python por padrao da um espaco entre as entradas de print
print(12, 34, 1011, sep="", end='#') # aqui ao setar o separador com vazio ele retira esse espaco, funciona com aspas simples ou aspas duplas
print('testando')
print('teste') # por padrao o python quebra a linha no fim do print
print(88, end="") # assim evitamos a quebra de linha, pois escolhemos o finalizador(automaticamente retirando o \n que eh o end/finalizador default)
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')
nome = 'Luiz Otávio'
altura = 1.80
peso = 95
mochila = 20
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso + mochila} quilos e seu imc é' # permite operacoes aritmeticas
linha_3 = f'{imc:.2f}' # mantem apenas duas casas decimais

print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.32

nome1 = "Luiz"
idade = 23
formato = f'{nome1} tem {idade:.2f} anos'
print(formato)
# 10.1 -> enxerga o numero em 32 ou 64 bits, ou seja ele traduz como uma sequencia de 64 numeros 0 ou 1.
# 10.2 -> idem anterior

# o que acontece é que quando é feita soma dos 64 bits dos dois numeros ele não dá exatamente 10.3 mas na verdade um número bem próximo do 10.3

preco_produto1=10.1
preco_produto2=10.2

valor_total=preco_produto1+preco_produto2

# observe que o resultado tem um output estranho nao arredondado da maneira que gostariamos
print(valor_total) # 20.299999999999997

# arredondando com duas casas decimais
print(round(valor_total,2)) # 20.3

# caso seja necessaria alta precisao

# essa biblioteca armazena o numero como se fosse texto, exemplo: '10.1'
from decimal import Decimal

preco1=Decimal('10.1')
preco2=Decimal('10.2')

valor_total2=preco1+preco2

print(valor_total2) # 20.3
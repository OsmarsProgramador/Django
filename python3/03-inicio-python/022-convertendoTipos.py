# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool


print(int('1'), type(int('1'))) # 1 int
print(float('1')+1, type(float('1') + 1)) # float
print(" ", bool(' ')) # True
print('', bool('')) # False
print(1, bool(1)) # True
print(0, bool(0)) # False
print(2, bool(2)) # True
print(1, bool(1)) # True
print(str(11) + 'b') # 11b
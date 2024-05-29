# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)

# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/

# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores. apos o * serao aceitos apenas argumentos nominais, precisamos ter pelo menos um argumento nominal após o *
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

 
def soma1(*args):
    print(sum(args))

soma1(1) # 1
soma1(1,2,3) # 6
soma1(1,3,4,5,6) # 19


# apos o * serao aceitos apenas argumentos nominais, precisamos ter pelo menos um argumento nominal após o *
def soma(a, b, /, *, c, **kwargs):
    print(kwargs) 
    print(a + b + c) 


# observe que após o * da funcao todos os argumentos devem ser nominais para que sejam aceitos
# observe que nesse caso o c pode ser nominal, porem o a e b so poderao ser posicionais pois eles estao antes da barra (/) nos parametros da funcao
soma(1, 2, c=3, nome='teste')
# {'nome': 'teste'}
# 6
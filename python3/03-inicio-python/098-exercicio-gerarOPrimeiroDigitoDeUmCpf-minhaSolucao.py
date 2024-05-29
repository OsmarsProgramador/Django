"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# stringCpf=input('Digite o CPF no formato XXX.XXX.XXX-XX: ')
stringCpf='746.824.890-70'

if len(stringCpf)==14 and stringCpf[3]=='.' and stringCpf[7]=='.' and stringCpf[11]=='-':
    try:
        int(stringCpf[0:3])
        int(stringCpf[4:7])
        int(stringCpf[8:11])
        int(stringCpf[12:14])

        stringLimpa=stringCpf.replace('.','').replace('-','')
        print(stringLimpa)

        multiplicadorCpf=10
        somadorCpf=0

        for indice,numero in enumerate(stringLimpa[0:9]):
            somadorCpf+=multiplicadorCpf*int(numero)
            multiplicadorCpf-=1

        primeiroDigitoCpf=(somadorCpf*10)%11 if (somadorCpf*10)%11 <= 9 else 0

        print('O primeiro digito do CPF digitado é',primeiroDigitoCpf)
    except:
        print('Número de CPF fora da conformidade, favor tentar novamente!')
else:
    print('Número de CPF fora da conformidade, favor tentar novamente!')



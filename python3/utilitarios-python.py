# utilitarios python

# ambos abaixo servem apenas para guardar lugar no codigo de algo a ser digitado/desenvolvido posteriormente
... or pass


# confere se uma string possui APENAS números: 
# (***CUIDADO: ele também retornará false para numeros com casas decimais como por exemplo 2.3

stringQualquer.isdigit() # True ou False



# impressao de formato percentual no .format com duas casas decimais

print('Percentual de Stockout: {:.2%}'.format(percentualStockout(vendas)))



# roda o conteudo que está em 'pass' APENAS se o arquivo em questao for o arquivo que for
# objeto da execução, caso ele esteja sendo importado, por exemplo, ele não
# executará o bloco em questao

if __name__=='__main__':
    pass






"""
Trocar o cursor entre janelas do editor e terminal no vscode

1 - Ctrl + Shift + ' vai abrir o terminal
2 - Ctrl + Tab vai voltar o cursor para a área do Editor
3 - Ctrl + ' vai sai do Editor e voltar pro Terminar
"""


# casas decimais em string no output

nome='jorge'
altura=1.82000
linha_1 = f'{nome} tem {altura:.2f} # output: jorge tem 1.80
print(linha_1)


# shell interativo em python:
# digitar no terminal python -i nome_do_arquivo.py
# quit() ou exit() sai do modo interativo


"""
Interpolação básica de strings (herança de C)
%s - string
%d e %i - int
%f - float
%x (com letras minusculas no hexadecimal) e %X (com letras maiusculas no hexadecimal) - Hexadecimal (ABCDEF0123456789)
%06X - seis digitos hexadecimal com minusculas
"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))
print('O hexadecimal de %d é %x' % (1500, 1500))


# operador ternario em python:

print('deu certo') if x == 2 else print('deu errado')



# Tratamento de exceções:

try:
    ...
except:
    ...
    
# ou também:

try:
    ...
except Exception as error:
    print(error)
    ...
    


# for em python (com indice)

for indice,item in enumerate(vetorOuString):
            print(letra)
            
            
            

# criando data e hora atual com formato editado
from datetime import datetime
import pytz # faz o ajuste de fuso horario

fusoHorarioBrasil=pytz.timezone('Brazil/East')

def dataHoraAtual():
    return datetime.now(fusoHorarioBrasil).strftime('%d/%m/%Y %H:%M:%S') # metodo strftime mostra a data/hora em modo mais amigavel e legivel


def dataHora():
    return datetime.now(fusoHorarioBrasil)



# criando formatacao para os valores (em reais)
import locale

locale.setlocale(locale.LC_MONETARY,'pt_BR.UTF-8')

def formatacaoMoeda(valor):
    return locale.currency(valor,grouping=True)




# formatando percentual
def formatacaoPercentual(valor):
    valor*=100
    return '{}%'.format(round(valor,2))
    

# recebe o percentual em decimal e retorna em percentual
# com duas casas decimais
def formatacaoPercentual2(valor):
    return '{:.2%}'.format(valor) 





# VALIDACAO PARA INPUT NUMERICO:
while True:
    idade=input('Digite sua idade: ')
    try:
        idade=int(idade)
        if idade>=0 and idade<=150:
            break
        else:
            print('\nVALOR INVÁLIDO! Idade deve ser entre 0 e 150 anos!')
            continue
    except:
        print('\nVALOR INVÁLIDO! Idade deve ser entre 0 e 150 anos!')



"""
### Tratamento Completo Erros:

try:
    tente fazer isso
except ErroEspecífico:
    deu esse erro aqui que era esperado 
else:
    caso não dê o erro esperado, rode isso.
finally:
    independente do que acontecer, faça isso.

    

    
- Cuidado: uma vez dentro do try, qualquer erro vai levar ao except

### Como "printar" um erro em uma function

raise Exception('O erro foi esse')

ou então avisando qual o tipo de erro que ele teve

raise TypeError('O erro foi esse')
raise ValueError('O erro foi esse')
raise ZeroDivisionError('O erro foi esse')

"""
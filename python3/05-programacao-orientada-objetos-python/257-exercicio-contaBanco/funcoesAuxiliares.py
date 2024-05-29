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
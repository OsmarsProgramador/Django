from abc import ABC, abstractmethod
from funcoesAuxiliares import formatacaoMoeda

class Conta(ABC):

    def __init__(self,agencia,numero_conta,saldo) -> None:
        self.agencia=agencia
        self.numero_conta=numero_conta
        self.saldo=saldo

    @abstractmethod
    def sacar(self,valor): ...

    def depositar(self,valor):
        self.saldo+=valor
        self.detalhes('DEPÓSITO VALOR {} EFETIVADO\n'.format(formatacaoMoeda(valor)))

    def detalhes(self,msg=''):
        print('{} - SALDO DA CONTA ATUAL: {}\n'.format(msg,formatacaoMoeda(self.saldo)))
from funcoesAuxiliares import formatacaoMoeda
from Conta import Conta

class ContaPoupanca(Conta):

    def sacar(self,valor):
        if self.saldo>=valor:
            self.saldo-=valor
            self.detalhes('SAQUE VALOR {} EFETIVADO\n'.format(formatacaoMoeda(valor)))
        else:
            self.detalhes('SALDO INSUFICIENTE\n')
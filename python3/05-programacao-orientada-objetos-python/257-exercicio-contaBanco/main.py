from Conta import Conta
from ContaPoupanca import ContaPoupanca
from funcoesAuxiliares import formatacaoMoeda, dataHora, dataHoraAtual

cp1=ContaPoupanca(2560,5665613,550.0)
cp1.sacar(500)
cp1.depositar(1000)
cp1.sacar(3000)
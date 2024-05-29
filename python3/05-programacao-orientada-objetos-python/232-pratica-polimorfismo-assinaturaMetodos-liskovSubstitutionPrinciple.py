# Polimorfismo em Python Orientado a Objetos

# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.

# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)

# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID

# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.

# Sobrecarga de métodos (overload)  🐍 = ❌ -- python nao da suporte a sobrecarga de metodos

# Sobreposição de métodos (override) 🐍 = ✅ -- python da suporte a sobreposicao de metodos

from abc import ABC, abstractmethod # importando o abstractmethod para que possa ser usado


# a classe Notificacao é abstrata caracterizada pelo (ABC), nao pode ser instanciada
class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    # o metodo enviar é abstrato entao ele tera que ser implementado nas subclasses
    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    # -> bool (type annotation ou type hinting), apenas para fazer acompanhamento da "assinatura" do metodo ou retorno
    def enviar(self) -> bool: 
        print('E-mail: enviando - ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False


# está especificando que o argumento 'notificacao' tem que ser do tipo Notificacao(classe)
# Ex: def notificar(notificacao: int) ou def notificar(notificacao: str)
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')


notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)



# passagem de parametro errada nao quebra o aplicativo, continua normalmente
def exemploTeste(numero: int):
    print(numero)

exemploTeste('cachorro')
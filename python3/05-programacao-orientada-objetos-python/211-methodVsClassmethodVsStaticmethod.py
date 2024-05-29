# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    # setter
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('LOG:', msg)


def connection_log(msg):
    print('LOG:', msg)


c2 = Connection()

c1 = Connection.create_with_auth('luiz','1234')

c2.set_user('cachorro')
 
c2.set_password('123')

print(Connection.log('Essa é a mensagem de log')) # LOG: Essa é a mensagem de log None 

print(c1.user) # luiz

print(c1.password) # 1234
print(c2.__dict__) # {'host': 'localhost', 'user': 'cachorro', 'password': '123'}
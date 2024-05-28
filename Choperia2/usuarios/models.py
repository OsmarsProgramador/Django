from django.db import models

# Usuario admin django
#user: admin
#email: 
#senha: 1234

# Usuario Choperia
#user: Osmar
#email: Osmar@gmail.com
#senha: 1234556789

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64) # sha256 vai transforma em uma hash unica e exclusiva de 64 caracteres
    ativo = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nome
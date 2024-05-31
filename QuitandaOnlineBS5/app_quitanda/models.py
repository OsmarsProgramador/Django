from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=9)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    receber_promocoes = models.BooleanField(default=False)

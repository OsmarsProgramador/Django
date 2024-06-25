# empresa/models.py
from django.db import models

class Empresa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=18)

    def __str__(self):
        return self.nome



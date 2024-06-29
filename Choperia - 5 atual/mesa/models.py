# mesa/models.py
from django.db import models

class Mesa(models.Model):
    nome = models.CharField(max_length=50)
    itens = models.JSONField(default=list)
    status = models.CharField(max_length=10, default='Fechada')
    pedido = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome


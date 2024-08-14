# mesa/models.py
from django.contrib.auth.models import User
from django.db import models

class Mesa(models.Model):
    nome = models.CharField(max_length=50)
    itens = models.JSONField(default=list)
    status = models.CharField(max_length=10, default='Fechada')
    pedido = models.PositiveIntegerField(default=0)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome



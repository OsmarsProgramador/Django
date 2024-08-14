# mesa/models.py
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Mesa(models.Model):
    nome = models.CharField(max_length=50)
    itens = models.JSONField(default=list)
    status = models.CharField(max_length=10, default='Fechada')
    pedido = models.PositiveIntegerField(default=0)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('mesa:abrir_mesa', args=[self.id])




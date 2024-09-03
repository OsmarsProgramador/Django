# mesa/models.py
from django.db import models
from django.contrib.auth.models import User
from produto.models import Produto

class Mesa(models.Model):
    numero = models.PositiveIntegerField()
    capacidade = models.PositiveIntegerField()
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    produtos = models.ManyToManyField(Produto, through='Pedido')

    def __str__(self):
        return f"Mesa {self.numero}"

    def is_aberta(self):
        """Retorna True se a mesa estiver aberta (sem produtos)"""
        return self.produtos.count() == 0

    def is_fechada(self):
        """Retorna True se a mesa estiver fechada (com produtos)"""
        return self.produtos.count() > 0

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} (Mesa {self.mesa.numero})"


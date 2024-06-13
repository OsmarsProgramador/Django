import datetime

from django.db import models
from django.utils import timezone


class Produto(models.Model):
    categoria = models.CharField(max_length=50) # models.ForeignKey(Categoria, on_delete=models.CASCADE) # Cascade deleta a categoria e os produtos ligados a ela
    # categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True) # # Cascade deleta a categoria e mantem os produtos ligados a ela, que ficam sem a categoria

    nome_produto = models.CharField(max_length=50)
    descricao = models.TextField(blank=True) # Não é obrigatório o preenchimento de informação
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    venda = models.DecimalField(max_digits=10, decimal_places=2)
    codigo = models.IntegerField()
    estoque = models.IntegerField(default=0)
    estoque_total = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome_produto

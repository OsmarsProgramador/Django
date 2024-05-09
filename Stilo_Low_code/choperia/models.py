import datetime

from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    categoria_text = models.CharField(max_length=50)
    data_pub = models.DateTimeField("data de publicação")

    def __str__(self):
        return self.categoria_text

    def foi_publicado_recentemente(self):
        return self.data_pub >= timezone.now() - datetime.timedelta(days=1)


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome_produto = models.CharField(max_length=50)
    descricao = models.TextField()
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    venda = models.DecimalField(max_digits=10, decimal_places=2)
    codigo = models.IntegerField()
    estoque = models.IntegerField()
    estoque_total = models.IntegerField()
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome
    
    """def foi_publicado_recentemente(self):
        return self.data_pub >= timezone.now() - datetime.timedelta(days=1)"""

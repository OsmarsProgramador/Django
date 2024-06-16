from django.db import models

class Produto(models.Model):
    categoria = models.CharField(max_length=50)
    nome_produto = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    venda = models.DecimalField(max_digits=10, decimal_places=2)
    codigo = models.IntegerField()
    estoque = models.IntegerField(default=0)
    estoque_total = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.nome_produto

class Mesa(models.Model):
    nome = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

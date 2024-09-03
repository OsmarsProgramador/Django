# produto/models.py
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)  # Preço de custo ou preço padrão
    venda = models.DecimalField(max_digits=8, decimal_places=2)  # Novo campo: Preço de venda
    codigo = models.CharField(max_length=50, unique=True)  # Defina um valor padrão Novo campo: Código único do produto
    estoque = models.PositiveIntegerField()  # Estoque disponível atualmente
    estoque_total = models.PositiveIntegerField()  # Novo campo: Estoque total
    imagem = models.ImageField(upload_to='produtos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome




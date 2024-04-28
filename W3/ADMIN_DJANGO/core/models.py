from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=20)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.ImageField()
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

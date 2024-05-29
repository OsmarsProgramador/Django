from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=20)
    categoria =  models.CharField(max_length=20)
    preco = models.IntegerField()
    quantidade = models.IntegerField()
    codigo =  models.CharField(max_length=20)
    descricao = models.TextField()
    def __str__(self):
        return self.nome

class Pessoas(models.Model):
    nome = models.CharField(max_length=20)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

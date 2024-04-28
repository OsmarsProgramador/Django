from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(null=True)
    preco = models.IntegerField()
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome

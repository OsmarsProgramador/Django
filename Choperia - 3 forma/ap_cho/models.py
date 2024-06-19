from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
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
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    itens = models.JSONField(default=list)  # Usamos JSONField para armazenar listas
    status = models.CharField(max_length=10, default='Fechada')
    pedido = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

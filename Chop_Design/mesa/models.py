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

"""
Relação entre Mesa, Produto e Pedido
Mesa: Representa uma mesa no restaurante.
Produto: Representa um produto (por exemplo, uma comida ou bebida) que pode ser pedido.
Pedido: Este é o modelo intermediário que liga Mesa a Produto. Ele não só faz a ligação entre Mesa e Produto, mas também armazena informações adicionais, como a quantidade de cada produto pedido para aquela mesa.
Como funciona a relação:
ManyToManyField com through:

O campo produtos em Mesa é uma relação de muitos-para-muitos com Produto, mas ao invés de usar a tabela de associação padrão criada automaticamente pelo Django, ele usa a tabela intermediária Pedido.
Isso permite que você adicione atributos extras à relação, como a quantidade de cada produto pedido.
Modelo Pedido:

O modelo Pedido tem ForeignKey para Mesa e Produto, o que significa que ele armazena a associação entre uma Mesa específica e um Produto específico, juntamente com informações adicionais, como a quantidade.
Vantagens do uso de through:
Informações adicionais: Permite armazenar informações extras na relação, como a quantidade de produtos em um pedido.
Controle total: Dá a você controle total sobre como a relação é gerenciada e representada no banco de dados.
Resumo
O through especifica um modelo intermediário que Django usará para gerenciar a relação ManyToMany. No seu exemplo, Pedido é o modelo intermediário que gerencia a relação entre Mesa e Produto, permitindo que você registre informações adicionais, como a quantidade de produtos pedidos em uma mesa.
"""

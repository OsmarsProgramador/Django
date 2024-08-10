# tarefas/models.py
from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    completa = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, related_name='tarefas', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, related_name='tarefas', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo



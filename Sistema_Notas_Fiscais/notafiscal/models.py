# notafiscal/models.py
from django.db import models
from empresa.models import Empresa

class NotaFiscal(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='notas_fiscais')
    serie = models.CharField('Série', max_length=20)
    numero = models.PositiveIntegerField('Número')
    descricao = models.CharField('Nome/Descrição', max_length=255)
    peso = models.DecimalField('Peso (kg)', max_digits=10, decimal_places=2)
    cubagem = models.DecimalField('Cubagem (m³)', max_digits=10, decimal_places=3)
    data_emissao = models.DateField('Data de Emissão')

    def __str__(self):
        return f'{self.serie} - {self.numero} - {self.descricao}'




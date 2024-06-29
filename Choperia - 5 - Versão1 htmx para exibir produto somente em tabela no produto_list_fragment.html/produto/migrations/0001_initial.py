# Generated by Django 5.0.6 on 2024-06-26 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('custo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('estoque', models.PositiveIntegerField()),
                ('estoque_total', models.PositiveIntegerField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagens/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.categoria')),
            ],
        ),
    ]

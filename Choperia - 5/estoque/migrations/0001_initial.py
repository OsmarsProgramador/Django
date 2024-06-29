# Generated by Django 5.0.6 on 2024-06-29 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('quantidade', models.PositiveIntegerField()),
                ('tipo', models.CharField(max_length=10)),
                ('data', models.DateField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estoques', to='empresa.empresa')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradas_saidas', to='produto.produto')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

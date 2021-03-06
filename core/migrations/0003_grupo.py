# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_campeonato_patrocinador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo_campeonato', to='core.Campeonato')),
            ],
            options={
                'db_table': 'grupo',
            },
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clube', '0001_initial'),
        ('core', '0003_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoClube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('clube', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupoclube_clube', to='clube.Clube')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupoclube_grupo', to='core.Grupo')),
            ],
            options={
                'db_table': 'grupo_clube',
            },
        ),
    ]

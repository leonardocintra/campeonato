from django.db import models

from clube.models import Clube
from .constants import TIPO_CAMPEONATO


class Campeonato(models.Model):
    descricao = models.CharField(max_length=200)
    tipo_campeonato = models.CharField(max_length=1, choices=TIPO_CAMPEONATO, default="Q")
    data_inicio = models.DateTimeField(blank=True, null=True)
    data_fim = models.DateTimeField(blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=False)
    patrocinador = models.CharField(max_length=200, blank=True)
    campeonato_principal = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'campeonato'


class Grupo(models.Model):
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE, related_name='grupo_campeonato')
    descricao = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'grupo'


class GrupoClube(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='grupoclube_grupo')
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE, related_name='grupoclube_clube')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} |  {} no {}'.format(self.grupo.campeonato.descricao, self.clube.nome, self.grupo.descricao) 

    class Meta:
        db_table = 'grupo_clube'
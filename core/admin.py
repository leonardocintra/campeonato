from django.contrib import admin
from .models import Campeonato, Grupo


class CampeonatoAdmin(admin.ModelAdmin):
    fields = ('descricao', 'patrocinador', 'tipo_campeonato', 'data_inicio', 'data_fim', 'ativo', 'campeonato_principal')

class GrupoAdmin(admin.ModelAdmin):
    fields = ('campeonato', 'descricao')


admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(Grupo, GrupoAdmin)
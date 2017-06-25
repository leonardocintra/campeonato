from django.contrib import admin
from .models import Campeonato


class CampeonatoAdmin(admin.ModelAdmin):
    fields = ('descricao', 'patrocinador', 'tipo_campeonato', 'data_inicio', 'data_fim', 'ativo', 'campeonato_principal')

admin.site.register(Campeonato, CampeonatoAdmin)
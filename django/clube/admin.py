from django.contrib import admin
from .models import Clube


class ClubeAdmin(admin.ModelAdmin):
    fields = ('nome', 'data_fundacao', )


admin.site.register(Clube, ClubeAdmin)
from django.db import models


class Clube(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    data_fundacao = models.DateTimeField(null=True, blank=True)
    #mascote = CloudinaryField('Foto Mascote', blank=True, null=True)
    #escudo = CloudinaryField('Foto Escudo', blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'clube'
        ordering = ('nome', )
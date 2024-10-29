from django.contrib import admin
from .models import Car, Marca


class CarAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'marca', 'ano_fabrica',
                    'ano_lancamento', 'quilometragem', 'combustivel', 'cambio', 'preco', 'foto_carro')
    search_fields = ('modelo', 'marca')


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


admin.site.register(Car, CarAdmin)
admin.site.register(Marca, MarcaAdmin)

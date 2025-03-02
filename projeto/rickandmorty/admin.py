#personagens
from django.contrib import admin
from .models import Personagem, Location

admin.site.register(Personagem)
class adminPersonagem(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'status', 'genero', 'origem', 'location')
    list_filter = ('status', 'genero')
    search_fields = ('nome', 'especie', 'status', 'genero', 'origem', 'location')
    list_per_page = 10

#localização
admin.site.register(Location)
class adminLocation(admin.ModelAdmin):
    list_display = ('name', 'type', 'dimension')
    list_filter = ('type', 'dimension')
    search_fields = ('name', 'type', 'dimension')
    list_per_page = 10

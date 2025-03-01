from django.contrib import admin
from .models import Personagem

admin.site.register(Personagem)
class adminPersonagem(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'status', 'genero', 'origem', 'location')

# Register your models here.

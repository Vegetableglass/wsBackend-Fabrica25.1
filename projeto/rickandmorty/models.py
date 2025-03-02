#personagens
from django.db import models

class Personagem(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    origem = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return (f'nome = {self.nome}, especie = {self.especie}, status = {self.status}, genero = {self.genero}, origem = {self.origem}, localização = {self.location}')

#localização
class Location(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    dimensao = models.CharField(max_length=50)
    
    def __str__(self):
        return (f'nome = {self.nome}, tipo = {self.tipo}, dimenção = {self.dimensao}')



 

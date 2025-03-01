from django.db import models

class Personagem(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    origem = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
   

# Create your models here.

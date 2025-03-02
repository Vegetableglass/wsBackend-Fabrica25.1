#personagens
from django import forms
from .models import Personagem, Location

class PersonagemForm(forms.ModelForm):
    class Meta:
        model = Personagem
        fields = ['nome']
        labels = {'nome': 'Nome'}
        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control'})}

#localização

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['nome']
        labels = {'nome': 'Nome'}
        widgets = {'nome': forms.TextInput(attrs={'class': 'form-control'})}

from django.shortcuts import render
from django.http import HttpResponse
from .models import Personagem
from .forms import PersonagemForm
from django.views.generic import ListView, UpdateView, DeleteView, FormView
import requests
from django.urls import reverse_lazy

def home(request):
    return HttpResponse("Olá!")

class PersonagemFormView(FormView):
    template_name = 'rickandmorty/personagem_form.html'
    form_class = PersonagemForm
    success_url = reverse_lazy('personagem_form')

# Consumir a api rick and morty
def form_valid(request):
    Personagem = None
    url = f'https://rickandmortyapi.com/api/character/?name={Personagem}' 
    response = requests.get(url)
    if response.status_code == 200:
        Personagem = response.json()
        Personagem.objects.create(
            nome=Personagem['name'],
            especie=Personagem['species'],
            status=Personagem['status'],
            genero=Personagem['gender'],
            origem=Personagem['origin']['name'],
            location=Personagem['location']['name']
            )
    else:
        print('Personagem não encontrado')
    return HttpResponse('Personagem cadastrado com sucesso!')





# Create your views here.

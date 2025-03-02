#personagens
from django.shortcuts import render,redirect
from .models import Personagem, Location
from .forms import PersonagemForm, LocationForm
from django.views.generic import ListView, DeleteView, FormView, UpdateView, DetailView
import requests
from django.urls import reverse_lazy

def home(request):
    return render(request, 'home.html')

class PersonagemFormView(FormView):
    template_name = 'personagem/procurar.html'
    form_class = PersonagemForm
    success_url = reverse_lazy('listar_personagem')

    def form_valid(self,form):
        personagem = form.cleaned_data['nome']
        response = requests.get(f'https://rickandmortyapi.com/api/character/?name={personagem}')
        data = response.json()
        if response.status_code == 200:
            personagem = data['results'][0]
            Personagem.objects.create(nome = personagem ['name'], especie = personagem ['species'], status = personagem ['status'], genero = personagem ['gender'], origem = personagem ['origin']['name'], location = personagem ['location']['name'] )
        else:
             return render(self.request, 'personagem/procurar.html', {
                'form': form, 
                'erro': 'Insira uma resposta compatível com o Universo Rick and Morty!'})
        return super().form_valid(form)
        
        
class PersonagemListView(ListView):
    model = Personagem
    template_name = 'personagem/listar.html'
    context_object_name = 'personagens'

class PersonagemUpdateView(UpdateView):
    model = Personagem
    form_class = PersonagemForm
    template_name = 'personagem/atualizar.html'
    context_object_name = 'personagem'
    success_url = reverse_lazy('listar_personagem')

class PersonagemDeleteView(DeleteView):
    model = Personagem
    template_name = 'personagem/deletar.html'
    context_object_name = 'personagem'
    success_url = reverse_lazy('listar_personagem')

class PersonagemDetailView(DetailView):
    model = Personagem 
    template_name = 'personagem/detalhes.html'
    context_object_name = 'personagem'

#localizações    
class LocationFormView(FormView):
    template_name = 'location/procurar.html'
    form_class = LocationForm
    success_url = reverse_lazy("listar_location")

    def form_valid(self,form):
        location = form.cleaned_data['nome']
        response = requests.get(f'https://rickandmortyapi.com/api/location?name={location}')
        data = response.json()
        if response.status_code == 200:
            location = data['results'][0]
            Location.objects.create(nome = location['name'], tipo = location['type'], dimensao = ['dimension'])
        else:
            
            return render(self.request, 'location/procurar.html', {
                'form': form, 
                'erro': 'Insira uma resposta compatível com o Universo Rick and Morty!'})
        return super().form_valid(form)
    

class LocationListView(ListView):
    model = Location
    template_name = 'location/listar.html'
    context_object_name = 'locations'

class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationForm
    template_name = 'location/procurar.html'
    context_object_name = 'location'
    success_url = reverse_lazy('listar_location')

class LocationDeleteView(DeleteView):
    model = Location
    template_name = 'location/deletar.html'
    context_object_name = 'location'
    success_url = reverse_lazy('listar_location')

class LocationDetailView(DeleteView):
    model = Location
    template_name = 'location/detalhes.html'
    context_object_name = 'location'




#personagens
from django.urls import path
from .views import (home, PersonagemFormView, PersonagemListView, PersonagemDeleteView, PersonagemUpdateView,PersonagemDetailView, LocationFormView, LocationListView, LocationDeleteView, LocationUpdateView, LocationDetailView)


urlpatterns = [
    path('', home, name='home'),
    path('personagem/', PersonagemFormView.as_view(), name='personagem'),
    path('listar_personagem/', PersonagemListView.as_view(), name='listar_personagem'),
    path('atualizar_personagem/<int:pk>/', PersonagemUpdateView.as_view(), name='atualizar_personagem'),
    path('deletar_personagem/<int:pk>/', PersonagemDeleteView.as_view(), name='deletar_personagem'),
    path('detalhes_personagem/<int:pk>/', PersonagemDetailView.as_view(), name='detalhes_personagem'),

#localização
    path('location/', LocationFormView.as_view(), name='location'),
    path('listar_location/', LocationListView.as_view(), name='listar_location'),
    path('atualizar_location/<int:pk>/', LocationUpdateView.as_view(), name='atualizar_location'),
    path('deletar_location/<int:pk>/', LocationDeleteView.as_view(), name='deletar_location'),
    path('detalhes_location/<int:pk>/', LocationDetailView.as_view(), name='detalhes_location'),
]


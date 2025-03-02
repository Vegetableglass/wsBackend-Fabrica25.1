# Django Templates Practice Project

Este é um projeto Django desenvolvido para prática e execução de Django Templates. O projeto consiste em dois aplicativos (`apps`) juntos: Buscador de Personagens e localizações de Rick and Morty e utiliza a estrutura de templates do Django para exibir dados e interagir com o usuário.

## Funcionalidades

### 1. **Buscador de Personagens e localizações de Rick and Morty**
O app `Buscador de Personagens e localizações de Rick and Morty` permite que o usuário insira um Personagem ou uma localização e, ao clicar em "Buscar", o sistema consulta a API rickandmorty para buscar o Personagem ou a localização correspondente ao nome informado. Os dados são exibidos na página, utilizando templates Django.(Os nomes das localizações precisam ser em ingles para que aplicação funcione corretamente.)


## Como Instalar:

### 1. Clonar o Repositório

```bash
git clone https://github.com/Vegetableglass/wsBackend-Fabrica25.1
cd wsBackend-Fabrica25.1
```
### 2. Criar e Ativar um Ambiente Virtual
```bash
python -m venv venv
.\venv/bin/activate 
```
## No Windows: 
```bash
.\venv\Scripts\activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```
### 4. Aplicar as Migrações
```bash
python manage.py makemigrations e python manage.py migrate.
```
### 5. Executar o Servidor de Desenvolvimento
```bash
python manage.py runserver
```
## Endpoints para Personagens
```bash
Listar Personagem: /listar_personagem/ - Mapeado para PersonagemListView
Detalhar Personagem: /detalhes_personagem/<int:pk>/ - Mapeado para PersonagemDetailView
Procurar Personagem: /personagem/ - Mapeado para PersonagemFormView
Atualizar Personagem: /atualizar_personagem/<int:pk>/ - Mapeado para PersonagemUpdateView
Deletar Personagem: /deletar_personagem/<int:pk>/ - Mapeado para PersonagemDeleteView
```
## Endpoints para Localizações
```bash
Listar Localização: /listar_location/ - Mapeado para LocationListView
Detalhar Localização: /detalhes_location/<int:pk>/ - Mapeado para LocationDetailView
Procurar Localização: /location/ - Mapeado para LocationFormView
Atualizar Localização: /atualizar_location/<int:pk>/ - Mapeado para LocationUpdateView
Deletar Localização: /deletar_location/<int:pk>/ - Mapeado para LocationDeleteView
```

### **Como Usar**
Para acessar a Aplicação
Buscador de personagens e localizações de Rick and Morty: Acesse http://127.0.0.1:8000/ para inserir um nome e buscar o personagem ou localização correspondente. Insira um nome válido (por exemplo, Rick Sanchez ou Earth) e veja os detalhes do personagem ou localização retornados pela API rickandmorty.
Notas Finais
Este projeto é voltado para a prática de Django Templates e integração com APIs externas, utilizando Django Models, Forms, e Views. Ele serve como um ótimo ponto de partida para entender como Django lida com templates e renderização de dados dinâmicos em páginas web.
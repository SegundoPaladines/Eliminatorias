from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from album.models import Selection, Player

# Create your views here.
#todas las selecciones
class SelectionListView(ListView):
    model = Selection
    #template_name = "./templates/album/selection_list.html"

#solo una seleccion
class SelectionDetailView(DetailView):
    model = Selection
    #template_name = "./templates/album/selection_detail.html"

#todos los jugadores
class PlayerListView(ListView):
    model = Player
    #template_name = "./templates/album/player_list.html"

#solo un jugador
class PlayerDetailView(DetailView):
    model = Player
    #template_name = "./templates/album/player_detail.html"
    
class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__' 

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')
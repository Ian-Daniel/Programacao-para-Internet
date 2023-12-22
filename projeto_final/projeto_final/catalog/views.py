from django.shortcuts import render
from catalog.models import Posicao, Jogador, Partida, Treinador
from django.views import generic

# Create your views here.
def index(request):
    numeroDePosicoes=Posicao.objects.all().count
    numeroDePartidas=Partida.objects.all().count
    numeroDeJogadores=Jogador.objects.count()
    
    context={
        'numeroDePosicoes':numeroDePosicoes,
        'numeroDePartidas':numeroDePartidas,
        'numeroDeJogadores':numeroDeJogadores,
    }
    
    return render(request,'index.html',context=context)

class JogadorListView(generic.ListView):
    model=Jogador
    paginate_by=5
    
class JogadorDetailView(generic.DetailView):
    model=Jogador
    
class TreinadorListView(generic.ListView):
    model=Treinador   
    
class TreinadorDetailView(generic.DetailView):
    model=Treinador
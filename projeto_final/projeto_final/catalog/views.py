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
    
class JogadorDetailView(generic.DetailView):
    model=Jogador
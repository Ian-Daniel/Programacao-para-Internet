from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Posicao(models.Model):
    nome = models.CharField(max_length = 200, help_text='Insira a posição do jogador.')

    def __str__(self):
        return self.nome

class Jogador(models.Model):
    nome = models.CharField(max_length = 200, help_text = 'Insira o nome do jogador.')
    treinador = models.ForeignKey('Treinador', on_delete = models.SET_NULL, null = True)
    numeroDaCamisa = models.CharField(max_length = 200, help_text = 'Insira o número da camisa.')
    posicao = models.ManyToManyField(Posicao, help_text = 'Insira a posição do jogador.')

    def __str__(self):
        return self.nome
    
    def get_absolute_urls(self):
        return reverse('Detalhes do jogador', args = [str(self.id)])

class Partida(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'ID único para partida dentro do histórico de partidas.')
    jogador = models.ForeignKey('Jogador', on_delete = models.SET_NULL = True)
    adversario = models.CharField(max_length = 200)
    dataHora = models.DateField(null = True, blank = True)

    def __str__(self):
        return f'{self.id} ({self.jogador.nome})'

class Treinador(models.Model):
    nome = models.CharField(max_length = 200, help_text = 'Insira o nome do treinador.')
    idade = models.CharField(max_length = 200, help_text = 'Insira a idade do treinador.')
    email = models.CharField(max_length = 200, help_text = 'Insira o e-mail do treinador.')

    def get_absolute_url(self):
        return reverse('Detalhes do treinador', args = [str(self.id)])

    def __str__(self):
        return self.nome

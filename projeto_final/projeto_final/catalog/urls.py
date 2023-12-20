from django.urls import path
from catalog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('jogadores/', views.JogadorListView.as_view(), name='jogadores'),
    path('jogador/<int:pk>', views.JogadorDetailView.as_view(), name='jogador-detail')
]

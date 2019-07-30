from django.urls import path, include
from website.views import index, cadastro, sobre, login, cadastrar_ideia, usuario

urlpatterns = [
    path('', index),
    path('cadastro', cadastro),
    path('login', login),
    path('sobre', sobre),
    path('ideias', cadastrar_ideia),
    path('usuario/<int:id>', usuario)
]

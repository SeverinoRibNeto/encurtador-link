from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("encurtar_link/", views.encurtar_link, name="encurtar_link"),
    path("<str:link_recebido>", views.redirecionador_de_link,
         name="redirecionador_de_link"),
]

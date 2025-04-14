from django.urls import path
from . import views

urlpatterns = [
    path('profil/', views.profil, name='profil'),
    path('changer_mdp/', views.change_mdp, name='change_mdp'),
]

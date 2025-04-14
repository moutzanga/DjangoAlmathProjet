from django.urls import path
from . import views

urlpatterns = [
    path('enregistre_clientP/', views.enregistrer_client_physique, name='enregistrer_client_physique'),
    path('enregistre_clientM/', views.enregistrer_client_moral, name='enregistrer_client_moral'),
    path('recherche_client/', views.recherche_client, name='recherche_client'),
    path('achat_devise/', views.achat_devise, name='achat_devise'),
    path('vente_devise/', views.vente_devise, name='vente_devise'),
]

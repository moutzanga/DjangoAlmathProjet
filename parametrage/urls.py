from django.urls import path
from django.urls import path
from app_auth import views as auth_views  
from app_auth.views import modifier_utilisateur_view
from . import views

app_name = 'parametrage'
urlpatterns = [
    path('creer_agence/', views.creer_agence, name='creer_agence'),
    path('creer_caisse/', views.creer_caisse, name='creer_caisse'),
    path('creer_utilisateur/', views.creer_utilisateur, name='creer_utilisateur'),
    path('maj_utilisateur/', views.maj_utilisateur_view, name='maj_utilisateur'),
    path('donnees_base/', views.donnees_base, name='donnees_base'),
    path('valider_donnees/', views.valider_donnees, name='valider_donnees'),
    path("modifier/<int:user_id>/", modifier_utilisateur_view, name="modifier_utilisateur"),
    path('utilisateurs/', auth_views.creer_utilisateur_view, name='creer_utilisateur'),
    path('utilisateurs/modifier/<int:user_id>/', auth_views.modifier_utilisateur_view, name='modifier_utilisateur'),
    path('utilisateurs/liste/', views.maj_utilisateur_view, name='maj_utilisateur'),
]
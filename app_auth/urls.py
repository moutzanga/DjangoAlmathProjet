from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import modifier_utilisateur_view, supprimer_utilisateur_view
urlpatterns = [
    path('connexion/', views.connexion_view, name='connexion'),
    path('deconnexion/', views.deconnexion_view, name='deconnexion'),
    path('accueil/', views.accueil_view, name='accueil'),
    path('inscription/', views.inscription_view, name='inscription'),
    path('logout/', LogoutView.as_view(next_page='connexion'), name='logout'),
    path('utilisateur/modifier/<int:user_id>/', modifier_utilisateur_view, name='modifier_utilisateur'),
    path('utilisateur/supprimer/<int:user_id>/', supprimer_utilisateur_view, name='supprimer_utilisateur'),
]

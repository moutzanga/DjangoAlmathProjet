from django.urls import path
from . import views

urlpatterns = [
    path('compte_rendu_beac/', views.compte_rendu_beac, name='compte_rendu_beac'),
    path('compte_rendu_dgmrfe/', views.compte_rendu_dgmrfe, name='compte_rendu_dgmrfe'),
    path('transaction_interne/', views.transaction_interne, name='transaction_interne'),
    path('transaction_charge/', views.transaction_charge, name='transaction_charge'),
]

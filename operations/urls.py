from django.urls import path
from . import views

urlpatterns = [
    path('encaissement/', views.encaissement, name='encaissement'),
    path('decaissement/', views.decaissement, name='decaissement'),
    path('rapport_caisse/', views.rapport_caisse, name='rapport_caisse'),
]

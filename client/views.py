# views.py pour l'application client
from django.shortcuts import render

def enregistrer_client_physique(request):
    return render(request, 'client/enregistre_clientP.html')

def enregistrer_client_moral(request):
    return render(request, 'client/enregistre_clientM.html')

def achat_devise(request):
    return render(request, 'client/achat_devise.html')

def vente_devise(request):
    return render(request, 'client/vente_devise.html')

def recherche_client(request):
    return render(request, 'client/recherche_client.html')
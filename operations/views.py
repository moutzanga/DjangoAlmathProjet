# views.py pour l'application operations
from django.shortcuts import render


def encaissement(request):
    return render(request, 'operations/encaissement.html')

def decaissement(request):
    return render(request, 'operations/decaissement.html')

def rapport_caisse(request):
    return render(request, 'operations/rapport_caisse.html')

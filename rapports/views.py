# views.py pour l'application rapports
from django.shortcuts import render


def compte_rendu_beac(request):
    return render(request, 'rapports/compte_renduBEAC.html')

def compte_rendu_dgmrfe(request):
    return render(request, 'rapports/compte_renduDGMRFE.html')

def transaction_interne(request):
    return render(request, 'rapports/transaction_interne.html')

def transaction_charge(request):
    return render(request, 'rapports/transaction_charge.html')


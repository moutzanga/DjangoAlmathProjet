from django.shortcuts import render

# views.py pour l'application profil_utilisateur
def profil(request):
    return render(request, 'profil_utilisateur/profil.html')

def change_mdp(request):
    return render(request, 'profil_utilisateur/change_mdp.html')

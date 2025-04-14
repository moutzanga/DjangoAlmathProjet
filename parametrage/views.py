from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from app_auth.models import Utilisateur
from app_auth.forms import InscriptionForm


# === Création d'un utilisateur via formulaire ===
def creer_utilisateur(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Utilisateur créé avec succès.")
            return redirect('accueil')
    else:
        form = InscriptionForm()

    return render(request, 'parametrage/creer_utilisateur.html', {'form': form})


# === Enregistrement manuel d'un utilisateur ===
def enregistrer_utilisateur(request):
    if request.method == 'POST':
        identifiant = request.POST.get('identifiant')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        agence = request.POST.get('agence')
        profil = request.POST.get('profil')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        photo = request.FILES.get('photo')

        if password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect('parametrage:creer_utilisateur')

        if Utilisateur.objects.filter(identifiant=identifiant).exists():
            messages.error(request, "Cet identifiant est déjà utilisé.")
            return redirect('parametrage:creer_utilisateur')

        utilisateur = Utilisateur(
            identifiant=identifiant,
            nom=nom,
            prenom=prenom,
            telephone=telephone,
            agence=agence,
            profil=profil,
            password=make_password(password),
            photo=photo
        )
        utilisateur.save()

        messages.success(request, "Utilisateur enregistré avec succès.")
        return redirect('parametrage:creer_utilisateur')


from django.core.paginator import Paginator

def maj_utilisateur_view(request):
    utilisateurs = Utilisateur.objects.all().order_by('nom')
    paginator = Paginator(utilisateurs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'parametrage/maj_utilisateur.html', {
        'page_obj': page_obj
    })



# === Pages de création diverses ===
def creer_agence(request):
    return render(request, 'parametrage/creer_agence.html')

def creer_caisse(request):
    return render(request, 'parametrage/creer_caisse.html')


# === Pages diverses de paramétrage ===
def donnees_base(request):
    return render(request, 'parametrage/donnees_base.html')

def valider_donnees(request):
    return render(request, 'parametrage/valider_donnees.html')

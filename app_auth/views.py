from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Utilisateur
from .forms import InscriptionForm, UtilisateurForm, UtilisateurCreationForm


# === Vue de connexion ===
def connexion_view(request):
    if request.method == "POST":
        profil = request.POST.get("profil")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.profil == profil:
                login(request, user)
                return redirect("accueil")
            else:
                messages.error(request, "Profil incorrect pour cet utilisateur.")
        else:
            messages.error(request, "Identifiants invalides.")
    return render(request, "app_auth/connexion.html")


# === Vue de déconnexion ===
def deconnexion_view(request):
    logout(request)
    return redirect("connexion")


# === Page d'accueil ===
@login_required
def accueil_view(request):
    return render(request, 'app_auth/accueil.html')


# === Vue d'inscription d'un nouvel utilisateur ===
def inscription_view(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Inscription réussie.")
            return redirect('connexion')
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = InscriptionForm()
    return render(request, 'app_auth/inscription.html', {'form': form})


# Création
def creer_utilisateur_view(request):
    if request.method == 'POST':
        form = UtilisateurCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Utilisateur créé avec succès.")
            return redirect('maj_utilisateur')  # Redirige vers la liste après création
    else:
        form = UtilisateurCreationForm()

    return render(request, 'parametrage/creer_utilisateur.html', {
        'form': form,
        'modifier': False
    })


# Modification
from .forms import ModifierUtilisateurForm

def modifier_utilisateur_view(request, user_id):
    utilisateur = get_object_or_404(Utilisateur, id=user_id)

    if request.method == 'POST':
        form = ModifierUtilisateurForm(request.POST, request.FILES, instance=utilisateur)
        if form.is_valid():
            utilisateur = form.save(commit=False)
            if form.cleaned_data['password']:
                utilisateur.set_password(form.cleaned_data['password'])
            utilisateur.save()
            return redirect('maj_utilisateur')
    else:
        form = ModifierUtilisateurForm(instance=utilisateur)

    return render(request, 'parametrage/modifier_utilisateur.html', {
        'form': form,
        'utilisateur': utilisateur
    })

# === Supprimer un utilisateur ===
@login_required
def supprimer_utilisateur_view(request, user_id):
    utilisateur = get_object_or_404(Utilisateur, id=user_id)

    if utilisateur.profil == 'Administrateur':
        messages.error(request, "Impossible de supprimer un administrateur.")
    else:
        utilisateur.delete()
        messages.success(request, "Utilisateur supprimé avec succès.")

    return redirect('maj_utilisateur')

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Utilisateur
from django.utils.translation import gettext_lazy as _


@admin.register(Utilisateur)
class UtilisateurAdmin(BaseUserAdmin):
    # Champs affichés dans la liste
    list_display = ('identifiant', 'nom', 'prenom', 'telephone', 'agence', 'profil', 'is_staff')

    # Filtres dans la sidebar
    list_filter = ('profil', 'agence', 'is_staff', 'is_superuser', 'is_active')

    # Champs de recherche
    search_fields = ('identifiant', 'nom', 'prenom', 'telephone')

    # Ordre par défaut
    ordering = ('nom',)

    # Champs à utiliser pour l'identifiant
    fieldsets = (
        (None, {'fields': ('identifiant', 'password')}),
        (_('Informations personnelles'), {'fields': ('nom', 'prenom', 'telephone', 'agence', 'profil', 'photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Dates importantes'), {'fields': ('last_login',)}),
    )

    # Champs pour la création depuis l'admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'identifiant', 'nom', 'prenom', 'telephone', 'agence', 'profil', 'photo', 'password1', 'password2'),
        }),
    )

    # Le champ utilisé pour l'identifiant
    add_form_template = None


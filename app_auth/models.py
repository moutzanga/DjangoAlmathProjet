from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Gestionnaire personnalisé
class UtilisateurManager(BaseUserManager):
    def create_user(self, identifiant, nom, prenom, telephone, agence, profil, password=None, **extra_fields):
        if not identifiant:
            raise ValueError("L'identifiant est obligatoire")
        user = self.model(
            identifiant=identifiant,
            nom=nom,
            prenom=prenom,
            telephone=telephone,
            agence=agence,
            profil=profil,
            **extra_fields
        )
        user.set_password(password)  # Hachage du mot de passe
        user.save(using=self._db)
        return user

    def create_superuser(self, identifiant, nom, prenom, telephone, agence, profil='Administrateur', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(identifiant, nom, prenom, telephone, agence, profil, password, **extra_fields)

# Modèle utilisateur personnalisé
class Utilisateur(AbstractBaseUser, PermissionsMixin):
    PROFILS = [
        ('Caissier', 'Caissier'),
        ('Chef Agence', 'Chef Agence'),
        ('Administrateur', 'Administrateur'),
        ('Rapporteur', 'Rapporteur'),
        ('Autre', 'Autre'),
    ]

    identifiant = models.CharField(max_length=100, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    agence = models.CharField(max_length=100)
    profil = models.CharField(max_length=50, choices=PROFILS)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'identifiant'  # Utilisé pour l’authentification
    REQUIRED_FIELDS = ['nom', 'prenom', 'telephone', 'agence', 'profil']

    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.profil})"


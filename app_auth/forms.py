from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from app_auth.models import Utilisateur

class InscriptionForm(UserCreationForm):
    identifiant = forms.CharField(
        label="Identifiant",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Entrez un identifiant unique'})
    )
    nom = forms.CharField(label="Nom", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nom en Majuscule'}))
    prenom = forms.CharField(label="Prénom", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Prénom, première lettre en majuscule'}))
    telephone = forms.CharField(label="Téléphone", max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Numéro au format: 00 000 00 00'}))
    agence = forms.CharField(label="Agence", max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nom de l\'agence en majuscule'}))
    profil = forms.ChoiceField(label="Profil", choices=Utilisateur.PROFILS)
    photo = forms.ImageField(label="Photo (optionnelle)", required=False)

    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}),
        help_text="8 caractères minimum, au moins 1 majuscule, 1 chiffre."
    )
    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer le mot de passe'})
    )

    class Meta:
        model = Utilisateur
        fields = [
            'identifiant', 'nom', 'prenom', 'telephone',
            'agence', 'profil', 'photo', 'password1', 'password2'
        ]

    def clean_identifiant(self):
        identifiant = self.cleaned_data.get('identifiant')
        if Utilisateur.objects.filter(identifiant=identifiant).exists():
            raise forms.ValidationError("Cet identifiant est déjà utilisé.")
        return identifiant

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        if not re.match(r'^\+?\d{7,15}$', telephone):
            raise forms.ValidationError("Numéro de téléphone invalide.")
        return telephone

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("Le mot de passe doit contenir au moins une majuscule.")
        if not re.search(r'[0-9]', password):
            raise forms.ValidationError("Le mot de passe doit contenir au moins un chiffre.")
        return password



class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['identifiant', 'nom', 'prenom', 'profil', 'agence','photo', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur


class UtilisateurCreationForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['identifiant', 'nom', 'prenom', 'telephone', 'profil', 'agence', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personnalisation des champs du modèle
        for field_name in self.fields:
            field = self.fields[field_name]
            if not isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control-file'

        # Ajout des champs password1 et password2 avec style
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Mot de passe'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmer le mot de passe'
        })
# forms.py dans app_auth
from django import forms
from .models import Utilisateur
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class ModifierUtilisateurForm(forms.ModelForm):
    password = forms.CharField(
        label='Nouveau mot de passe',
        widget=forms.PasswordInput,
        required=False,  # important
        help_text="Laisser vide pour ne pas changer le mot de passe."
    )

    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'telephone', 'profil', 'agence', 'identifiant', 'photo', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            # Valider uniquement si un mot de passe a été saisi
            try:
                validate_password(password)
            except ValidationError as e:
                raise forms.ValidationError(e)
        return password

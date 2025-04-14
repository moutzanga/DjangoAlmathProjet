from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Import pour redirection
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('connexion')),  # Redirection depuis /
    path('admin/', admin.site.urls),
    path('app_auth/', include('app_auth.urls')),
    path('', include('app_auth.urls')),
    path('client/', include('client.urls')),
    path('operations/', include('operations.urls')),
    path('rapports/', include('rapports.urls')),
    path('parametrage/', include('parametrage.urls')),
    path('profil_utilisateur/', include('profil_utilisateur.urls')),
    path("utilisateur/", include("parametrage.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

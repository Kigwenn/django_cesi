from django.contrib import admin

# Register your models here.
from django.contrib import admin
from membre.models import Membre

class Admin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'adresse', 'cp', 'tel', 'date_naissance', 'date_entre', 'date_sortie']
    fields = ['nom', 'prenom', 'adresse', 'cp', 'tel', 'date_naissance', 'date_entre', 'date_sortie']

admin.site.register(Membre, Admin)

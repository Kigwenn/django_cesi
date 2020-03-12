from django.contrib import admin

# Register your models here.
from django.contrib import admin
from promotion.models import Promotion

class Admin(admin.ModelAdmin):
    list_display = ['nom', 'libelle', 'annee_debut', 'annee_fin']
    fields = ['nom', 'libelle', 'annee_debut', 'annee_fin']

admin.site.register(Promotion, Admin)
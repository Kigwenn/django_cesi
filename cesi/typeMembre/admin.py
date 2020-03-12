from django.contrib import admin

# Register your models here.
from django.contrib import admin
from typeMembre.models import TypeMembre

class Admin(admin.ModelAdmin):
    list_display = ['nom']
    fields = ['nom']

admin.site.register(TypeMembre, Admin)



# Create your models here.
from django.db import models

class Membre(models.Model):
    object = models.Manager()

    nom = models.TextField(null=True)
    prenom = models.TextField(null=True)
    adresse = models.TextField(null=True)
    cp = models.TextField(null=True)
    tel = models.TextField(null=True)
    date_naissance = models.DateTimeField(null=True)
    date_entre = models.DateTimeField(null=True)
    date_sortie = models.DateTimeField(null=True)

    promotion = models.ForeignKey('promotion.Promotion', on_delete=models.CASCADE, null=True)
    # typeMembre = models.OneToOneField('typeMembre.TypeMembre', on_delete = models.CASCADE, related_name='+')

    def __str__(self):
        return self.nom
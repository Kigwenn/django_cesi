

# Create your models here.
from django.db import models

class Membre(models.Model):
    object = models.Manager()

    nom = models.TextField()
    prenom = models.TextField()
    adresse = models.TextField()
    cp = models.TextField()
    tel = models.TextField()
    img = models.ImageField(upload_to='users/')
    date_naissance = models.DateTimeField()
    date_entre = models.DateTimeField()
    date_sortie = models.DateTimeField()

    promotion = models.ForeignKey('promotion.Promotion', on_delete=models.CASCADE, null=True)
    # typeMembre = models.OneToOneField('typeMembre.TypeMembre', on_delete = models.CASCADE, related_name='+')

    def __str__(self):
        return self.nom


# Create your models here.
from django.db import models

class Membre(models.Model):
    nom = models.TextField()
    prenom = models.TextField()
    adresse = models.TextField()
    cp = models.TextField()
    tel = models.TextField()
    date_naissance = models.DateTimeField()
    date_entre = models.DateTimeField()
    date_sortie = models.DateTimeField()

    object = models.Manager()

    def __unicode__(self):
        return self.nom
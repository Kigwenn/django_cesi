

# Create your models here.
from django.db import models

class TypeMembre(models.Model):

    object = models.Manager()

    nom = models.TextField()

    membre = models.ForeignKey('membre.Membre', on_delete=models.CASCADE, null=True)

    def __unicode__(self):
        return self.nom
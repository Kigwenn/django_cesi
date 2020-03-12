

# Create your models here.
from django.db import models

class TypeMembre(models.Model):
    nom = models.TextField()

    object = models.Manager()

    def __unicode__(self):
        return self.nom
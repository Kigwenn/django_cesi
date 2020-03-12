

# Create your models here.

# class Etudiant(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()
#
#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)
from django.db import models

class Promotion(models.Model):
    nom = models.TextField()
    libelle = models.TextField()
    annee_debut = models.DateTimeField()
    annee_fin = models.DateTimeField()
    # <etudiants> = models.ForeignKey(<Etudiant>, on_delete=models.CASCADE)

    object = models.Manager()
    def __unicode__(self):
        return self.nom

    # class Meta:
    #     ordering = ['promotion']



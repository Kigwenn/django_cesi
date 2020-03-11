from django.db import models

# Create your models here.

class Etudiant(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Promotions(models.Model):
    promotion = models.TextField()
    libelle = models.TextField()
    annees_debut = models.TextField()
    annees_fin = models.TextField()
    <etudiants> = models.ForeignKey(<Etudiant>, on_delete=models.CASCADE)

    def __str__(self):
        return self.promotion

    class Meta:
        ordering = ['promotion']



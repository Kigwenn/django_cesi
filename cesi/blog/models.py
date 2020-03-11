from django.db import models

# Create your models here.

class Publication(models.Model):
    publication = models.TextField()
    titre = models.TextField()
    date_pub = models.DateTimeField()
    #<auteur> = models.ForeignKey(<Auteur>, on_delete=models.CASCADE)
    object = models.Manager()
    def __unicode__(self):
        return self.titre
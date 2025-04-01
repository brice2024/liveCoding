from django.db import models

# Create your models here.
class Document(models.Model):
    titre = models.CharField(max_length=255)
    fichier = models.FileField(upload_to='uploads/')
    date_charger = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
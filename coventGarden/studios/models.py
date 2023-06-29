from django.db import models
from django.contrib.auth.models import AbstractUser

# Global variables
LENGTH_NAME = 150
LENGTH_PASSWORD = 150
LENGTH_EMAIL = 320

# Create your models here.
class CustomUser(AbstractUser):
    # Add additional fields in here
    test_field = models.CharField(max_length=LENGTH_NAME, default="Test")
    #modification Luca ligne13



    def __str__(self):
        return self.username


#modification Luca nouvelle classe

class FicheTechnique(models.Model):
    Fiche_Technique = models.FileField(upload_to='media/public', null=True)
    Utilisateur = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null = True)

#remise en forme du fichier

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from .fields import *

class CustomUser(AbstractUser):
    test_field = MODELS_TEST
    phone = MODEL_USER_PHONE

    def __str__(self):
        return self.username

class CustomGroup(models.Model):
    name = MODEL_NAME
    email = MODEL_EMAIL
    phone = models.IntegerField(verbose_name='Phone')  # Correction: Utilisation de IntegerField pour le champ 'phone'
    members = MODEL_MEMBERS
    genre = MODEL_GENRE
    facebook = MODEL_FACEBOOK
    instagram = MODEL_INSTAGRAM
    twitter = MODEL_TWITTER
    biography = MODEL_BIOGRAPHY

    def __str__(self):
        return self.name


# new class : Event -> planning

class Events(models.Model):
    title = models.CharField(max_length=200, default='Untitled Event')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    recurrence = models.CharField(max_length=200, blank=True)
    Utilisateur =  models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)


from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from .fields import *

# Create your models here.
class CustomUser(AbstractUser):
    """
    Default
        username
        first_name
        last_name
        email
        password
    """
    test_field = MODELS_TEST
    phone = MODEL_USER_PHONE

    def __str__(self):
        return self.username

class CustomGroup(models.Model):
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name='my_groups'
    )
    name = MODEL_NAME
    email = MODEL_EMAIL
    phone = MODEL_GROUP_PHONE
    members = MODEL_MEMBERS
    genre = MODEL_GENRE
    facebook = MODEL_FACEBOOK
    instagram = MODEL_INSTAGRAM
    twitter = MODEL_TWITTER
    biography = MODEL_BIOGRAPHY

    def __str__(self):
        return f"{self.name}"

class Event(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, default='Untitled Event')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True) 
    recurrence = models.CharField(max_length=200, blank=True)

class TechnicalSheet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    pdf_file = models.FileField(upload_to='media/public', null=True)


class Salle(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'

class Reservation(models.Model):
    class Status(models.TextChoices):
        RESERVED = 'Reserver'
        INPROGRESS = 'En cours'

    class Duration(models.TextChoices):
        ONE_HOUR = 1
        TWO_HOUR = 2
        THREE_HOUR = 3
        FOUR_HOUR = 4
        FIVE_HOUR = 5

    # title = models.fields.CharField(default='Item', max_length=100)
    description = models.fields.CharField(max_length=1000)
    duration = models.fields.IntegerField(choices=Duration.choices)
    date_start = models.DateTimeField(null=False)
    date_end = models.DateTimeField(null=False)
    # hour_begin = models.TimeField(null=False)
    price = models.fields.IntegerField(validators=[MinValueValidator(1)])
    status = models.fields.CharField(choices=Status.choices, max_length=20)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
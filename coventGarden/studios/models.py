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

    """
    WIP
    phone
    my_groups
    my_bookings
    
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
    recurrence = models.CharField(max_length=200, blank=True)

from django.contrib.auth.models import AbstractUser

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
"""
    - Group name
    - E-mail
    - Phone
    - Members
    - Musical style
    - Facebook
    - Instagram
    - Twitter
    - Biography
    - Approval
"""
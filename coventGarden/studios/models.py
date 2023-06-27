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

    def __str__(self):
        return self.username

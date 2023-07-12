from django import forms
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import CustomPasswordValidator, phone_validator

"""
Arguments
"""
# Lengths
LENGTH_NAME = 150       # Name field maximum length is 150 (See django.contrib.auth)
LENGTH_PASSWORD = 255   # Password maximum length value is 4096
LENGTH_EMAIL = 320      # Email maximum length value
LENGTH_PHONE = 10       # Phone number default length value
LENGTH_URL = 200        # URL default length value
LENGTH_TEXT = 5000

# Labels
LABEL_USERNAME = "Nom d'utilisateur"
LABEL_FIRST_NAME = "Prénom"
LABEL_LAST_NAME = "Nom"
LABEL_EMAIL = "Adresse e-mail"
LABEL_PHONE = "Numéro de téléphone"
LABEL_PASSWORD = "Mot de passe"
LABEL_PASSWORD_CURRENT = "Mot de passe actuel"
LABEL_PASSWORD_CONFIRM = "Confirmer le mot de passe"

LABEL_GROUP_NAME = "Nom de groupe"
LABEL_MEMBERS = "Nombre de membres"
LABEL_GENRE = "Style musicale"
LABEL_FACEBOOK = "URL Facebook"
LABEL_INSTAGRAM = "URL Instagram"
LABEL_BIOGRAPHY = "Biographie"
LABEL_TECHNICAL_SHEET = "Fiche technique"
LABEL_LOGO = "Logo"
LABEL_VALIDATED = "Vérifié"

# Path
MEDIA_PATH = "media/public"



"""
Forms
"""
# Widgets
WIDGET_TEXT = forms.TextInput(attrs={'class': 'form-control'})
WIDGET_EMAIL = forms.EmailInput(attrs={'class': 'form-control'})
WIDGET_PASSWORD = forms.PasswordInput(attrs={'class': 'form-control'})

# Forms
FORM_USERNAME = forms.CharField(max_length=LENGTH_NAME, label=LABEL_USERNAME, widget=WIDGET_TEXT)
FORM_EMAIL = forms.EmailField(max_length=LENGTH_EMAIL, label=LABEL_EMAIL, widget=WIDGET_EMAIL)
FORM_PASSWORD = forms.CharField(max_length=LENGTH_PASSWORD, label=LABEL_PASSWORD, widget=WIDGET_PASSWORD)
FORM_PASSWORD_NEW = forms.CharField(max_length=LENGTH_PASSWORD, label=LABEL_PASSWORD, widget=WIDGET_PASSWORD, validators=CustomPasswordValidator)
FORM_PASSWORD_CONFIRM = forms.CharField(max_length=LENGTH_PASSWORD, label=LABEL_PASSWORD_CONFIRM, widget=WIDGET_PASSWORD)



"""
Models
"""
# Error messages
UNIQUE_USERNAME = {"unique": "Ce nom d'utilisateur est déjà utilisé"}
UNIQUE_EMAIL = {"unique": "Cette adresse email est déjà utilisée."}

# CustomUser
MODEL_USERNAME = models.CharField(max_length=LENGTH_NAME, verbose_name=LABEL_USERNAME, unique=True, error_messages=UNIQUE_USERNAME)
MODEL_EMAIL = models.EmailField(max_length=LENGTH_EMAIL, verbose_name=LABEL_EMAIL, unique=True, error_messages=UNIQUE_EMAIL)
MODEL_LAST_NAME = models.CharField(max_length=LENGTH_NAME, verbose_name=LABEL_FIRST_NAME)
MODEL_FIRST_NAME = models.CharField(max_length=LENGTH_NAME, verbose_name=LABEL_LAST_NAME)
MODEL_PHONE = models.CharField(max_length=LENGTH_PHONE, verbose_name=LABEL_PHONE)
MODEL_PASSWORD = models.CharField(max_length=LENGTH_PASSWORD, verbose_name=LABEL_PASSWORD, validators=CustomPasswordValidator)
MODEL_PASSWORD_CONFIRM = models.CharField(max_length=LENGTH_PASSWORD, verbose_name=LABEL_PASSWORD_CONFIRM, blank=True, null=True)

# CustomGroup
MODEL_GROUP_NAME = models.CharField(max_length=LENGTH_NAME, verbose_name=LABEL_GROUP_NAME, blank=True)
MODEL_GROUP_EMAIL = models.EmailField(max_length=LENGTH_EMAIL, verbose_name=LABEL_EMAIL, blank=True)
MODEL_GROUP_PHONE = models.CharField(max_length=LENGTH_PHONE, verbose_name=LABEL_PHONE, validators=[phone_validator], blank=True)
MODEL_MEMBERS = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)], verbose_name=LABEL_MEMBERS, default=1, blank=True)
MODEL_GENRE = models.CharField(max_length=LENGTH_NAME, verbose_name=LABEL_GENRE, blank=True)
MODEL_FACEBOOK = models.URLField(max_length=LENGTH_URL, blank=True, verbose_name=LABEL_FACEBOOK)
MODEL_INSTAGRAM = models.URLField(max_length=LENGTH_URL, blank=True, verbose_name=LABEL_INSTAGRAM)
MODEL_BIOGRAPHY = models.TextField(max_length=LENGTH_TEXT, verbose_name=LABEL_BIOGRAPHY, blank=True)
MODEL_TECHNICAL_SHEET = models.FileField(upload_to=MEDIA_PATH, verbose_name=LABEL_TECHNICAL_SHEET, blank=True, null=True)
MODEL_LOGO = models.FileField(upload_to=MEDIA_PATH, verbose_name=LABEL_LOGO, blank=True, null=True)
MODEL_VALIDATED = models.BooleanField(default=False, verbose_name=LABEL_VALIDATED, blank=True)

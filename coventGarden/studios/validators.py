import re
from django.core.exceptions import ValidationError

MIN_LENGTH = 8
MIN_NUMBER = 1
MIN_UPPER = 1
MIN_SPECIAL = 1


"""
User validator
"""


"""
Password validator
"""
def length_validator(password, user=None):
    if len(password) < MIN_LENGTH:
        raise ValidationError(
            "Votre mot de passe doit contenir au moins %i caractères." % MIN_LENGTH,
            code='password_too_short',
            params={'min_length': MIN_LENGTH})

def number_validator(password, user=None):
    if not re.findall('\d', password):
        raise ValidationError(
            "Votre mot de passe doit contenir au moins %i chiffre." % MIN_NUMBER,
            code='password_no_number')

def upper_validator(password, user=None):
    if not re.findall('[A-Z]', password):
        raise ValidationError(
            "Votre mot de passe doit contenir au moins %i majuscule." % MIN_UPPER,
            code='password_no_upper')

def special_validator(password, user=None):
    if not re.findall('[@#$%!^&*]', password):
        raise ValidationError(
            "Votre mot de passe doit contenir au moins %i caractère spécial." % MIN_SPECIAL,
            code='password_no_symbol')

CustomPasswordValidator = [length_validator, number_validator, upper_validator, special_validator]

"""
Phone validator
"""
def phone_validator(value):
    phone_regex = r'^\d{10}$'  # Regex pour vérifier les 10 chiffres
    if not re.match(phone_regex, value):
        raise ValidationError(
            "Le numéro de téléphone est incorrecte",
            code='phone')

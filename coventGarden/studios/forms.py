from django.contrib.auth.forms import (UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm)
from django.forms import ModelChoiceField, SelectDateWidget, ValidationError
from django_select2.forms import Select2Widget

from .models import CustomUser, CustomGroup, Event, TechnicalSheet, Concert
from .fields import *

# Register your forms here
"""
CustomUser (Tutorial)
"""
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

"""
Account
    - Sign In
    - Sign Up
"""
class SignInForm(forms.Form):
    username = FORM_USERNAME
    password = FORM_PASSWORD

class SignUpForm(forms.Form):
    username = FORM_USERNAME
    email = FORM_EMAIL
    last_name = FORM_LAST_NAME
    first_name = FORM_FIRST_NAME
    password = FORM_PASSWORD
    confirm_password = FORM_PASSWORD_CONFIRM

"""
Profile
    - User Update
    - Confirm Password
"""
class UserUpdateForm(forms.Form):
    username = FORM_USERNAME
    email = FORM_EMAIL
    last_name = FORM_LAST_NAME
    first_name = FORM_FIRST_NAME

class ConfirmPasswordForm(forms.Form):
    current_password = FORM_PASSWORD_CURRENT
    confirm_password = FORM_PASSWORD_CONFIRM

"""
Password Reset
    - Reset
    - Set
"""
class UserPasswordResetForm(PasswordResetForm):
    # Replaced PasswordResetForm fields with custom fields (See docs)
    email = FORM_EMAIL

class UserPasswordSetForm(SetPasswordForm):
    # Replaced SetPasswordForm fields with custom fields (See docs)
    new_password1 = FORM_PASSWORD
    new_password2 = FORM_PASSWORD_CONFIRM

"""
CustomGroup
    - Create
"""
class GroupCreateForm(forms.ModelForm):
    # User will be added manually in views.py
    class Meta:
        model = CustomGroup
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

"""
Planning
    - Event
"""
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_time', 'end_time', 'recurrence']

"""
Concert
    - TechnicalSheetForm
    - ConcertForm
"""
class TechnicalSheetForm(forms.ModelForm):
    class Meta:
        model = TechnicalSheet
        fields = ['pdf_file']


class ConcertForm(forms.ModelForm):
    groupe1 = ModelChoiceField(queryset=CustomGroup.objects.all(), widget=Select2Widget)
    groupe2 = ModelChoiceField(queryset=CustomGroup.objects.all(), widget=Select2Widget)
    groupe3 = ModelChoiceField(queryset=CustomGroup.objects.all(), widget=Select2Widget)

    date = forms.DateField(widget=SelectDateWidget)
    is_engaged = forms.BooleanField(
        required=True,
        label="Je m'engage à ce que les 3 groupes soient disponibles et que les fiches techniques de chacun soient déposées.",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    class Meta:
        model = Concert
        fields = ['groupe1', 'groupe2', 'groupe3', 'date', 'is_engaged']

    def clean_date(self):
        date = self.cleaned_data['date']
        if date.weekday() != 4:
            raise ValidationError("Vous devez choisir un vendredi.")

        group1 = self.cleaned_data['groupe1']
        group2 = self.cleaned_data['groupe2']
        group3 = self.cleaned_data['groupe3']

        if group1 and (group1 == group2 or group1 == group3):
            raise forms.ValidationError("Vous ne pouvez pas choisir le même groupe plus d'une fois.")

        if group2 and group2 == group3:
            raise forms.ValidationError("Vous ne pouvez pas choisir le même groupe plus d'une fois.")

        return date

"""
Booking
"""
class ReservationForm(forms.Form):
    name = forms.CharField(max_length=LENGTH_NAME, label="Nom de l'utilisateur")
    email = forms.EmailField(label="Email de utilisateur")

    salle = forms.CharField(max_length=20, label="Salle réservée")
    # description = models.fields.CharField(max_length=1000)
    duration = forms.IntegerField(label="Durée de la séance en (H)")
    date_start = forms.DateTimeField(label="Date de début reservation")
    date_end = forms.DateTimeField(label="Date de fin reservation")
    # hour_begin = forms.TimeField( label="Heure de début de la réservation")
    price = forms.IntegerField(label="Montant payé en €")

    # status = models.fields.CharField(choices=Status.choices, max_length=20)

    def __init__(self, *args):
        super(ReservationForm, self).__init__(*args)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class TestForm(forms.Form):
    test = FORM_GROUP_NAME

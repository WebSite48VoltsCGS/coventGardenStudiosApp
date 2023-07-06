from django.contrib.auth.forms import (UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm)
from django.forms import ModelChoiceField, SelectDateWidget, ValidationError
from django_select2.forms import Select2Widget

from .models import CustomGroup, Event, TechnicalSheet, Concert
from .fields import *

# Register your forms here
"""
Account
    - SignInForm
    - SignUpForm
"""
class SignInForm(forms.Form):
    username = FORM_USERNAME
    password = FORM_PASSWORD

class SignUpForm(forms.Form):
    username = FORM_USERNAME
    email = FORM_EMAIL
    last_name = FORM_LAST_NAME
    first_name = FORM_FIRST_NAME
    phone = FORM_PHONE
    password = FORM_PASSWORD_NEW
    confirm_password = FORM_PASSWORD_CONFIRM



"""
Profile
    - UserUpdateForm
    - ConfirmPasswordForm
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
    - UserPasswordResetForm
    - UserPasswordSetForm
"""
class UserPasswordResetForm(PasswordResetForm):
    email = FORM_EMAIL

class UserPasswordSetForm(SetPasswordForm):
    new_password1 = FORM_PASSWORD_NEW
    new_password2 = FORM_PASSWORD_CONFIRM



"""
Group
    - GroupCreateForm
"""
class CustomGroupForm(forms.ModelForm):
    # User will be added manually in views.py
    class Meta:
        model = CustomGroup
        fields = '__all__'
        exclude = ('user', 'validated')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



"""
Booking
    - EventForm
"""
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_time', 'end_time', 'recurrence']



"""
Pro Area
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

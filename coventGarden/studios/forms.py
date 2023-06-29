from django.contrib.auth.forms import (UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm)
from .models import CustomUser, CustomGroup
from .fields import *

# Register your forms here
"""
Tutorial
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
Main
"""
class ConfirmPasswordForm(forms.Form):
    current_password = FORM_PASSWORD_CURRENT
    confirm_password = FORM_PASSWORD_CONFIRM

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

class UserUpdateForm(forms.Form):
    username = FORM_USERNAME
    email = FORM_EMAIL
    last_name = FORM_LAST_NAME
    first_name = FORM_FIRST_NAME

class UserPasswordResetForm(PasswordResetForm):
    # Replaced PasswordResetForm fields with custom fields (See docs)
    email = FORM_EMAIL

class UserPasswordSetForm(SetPasswordForm):
    # Replaced SetPasswordForm fields with custom fields (See docs)
    new_password1 = FORM_PASSWORD
    new_password2 = FORM_PASSWORD_CONFIRM

class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = CustomGroup
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class TestForm(forms.Form):
    test = FORM_GROUP_NAME

###################################################################################################
from django import forms
from studios.models import Events

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'start_time', 'end_time','recurrence']

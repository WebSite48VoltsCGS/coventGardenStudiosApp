from django import forms

# Global variables
LENGTH_USERNAME = 256
LENGTH_PASSWORD = 256
LENGTH_EMAIL = 320

# Register your forms here
class SignUpForm(forms.Form):
    username = forms.CharField(max_length=LENGTH_USERNAME, label="Nom d'utilisateur")
    first_name = forms.CharField(max_length=LENGTH_USERNAME, label="Prénom")
    last_name = forms.CharField(max_length=LENGTH_USERNAME, label="Nom")
    email = forms.EmailField(max_length=LENGTH_EMAIL, label="Adresse e-mail")
    password = forms.CharField(max_length=LENGTH_PASSWORD, label="Mot de passe")
    confirm_password = forms.CharField(max_length=LENGTH_PASSWORD, label="Confirmer le mot de passe")

    # Class = 'form-control'
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class SignInForm(forms.Form):
    username = forms.CharField(max_length=LENGTH_USERNAME, label="Nom d'utilisateur")
    password = forms.CharField(max_length=LENGTH_PASSWORD, label="Mot de passe")

    # Class = 'form-control'
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class PasswordResetForm(forms.Form):
    email = forms.EmailField(max_length=LENGTH_EMAIL, label="Adresse e-mail")

    # Class = 'form-control'
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

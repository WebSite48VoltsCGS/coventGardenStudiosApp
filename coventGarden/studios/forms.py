# Forms
from django.forms import ModelChoiceField, SelectDateWidget, ValidationError

# Authentication
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.hashers import check_password

# Email confirmation
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token
from django.core.mail import EmailMessage

# Password reset
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

# Payment
from django_select2.forms import Select2Widget
from tempus_dominus.widgets import DatePicker, DateTimePicker
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.utils.html import format_html

# Models & Fields
from .models import CustomUser, CustomGroup, Event, Concert
from .fields import *

User = get_user_model()



# Register your forms here
"""
CustomUser
    - UserSignInForm
    - UserSignUpForm
    - UserUpdateForm
    - UserPasswordConfirmForm
    - UserPasswordResetForm
    - UserPasswordSetForm
"""
class UserSignInForm(forms.Form):
    username = FORM_USERNAME
    password = FORM_PASSWORD

    def clean(self):
        # Authenticate
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Le nom d'utilisateur ou le mot de passe est incorrect.", code="authentication_failed")

        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)


class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'last_name', 'first_name', 'phone', 'password', 'password_confirm')
        widgets = {'password': forms.PasswordInput(),
                   'password_confirm': forms.PasswordInput()}

    def clean(self):
        # Add to other validators such as "unique"
        self.cleaned_data = super().clean()

        # Password confirmation
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if not password == password_confirm:
            raise forms.ValidationError("Les deux mots de passes ne correspondent pas.", code="password_confirm")

        return self.cleaned_data

    def save_user(self, request):
        username = self.cleaned_data.get('username')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')

        # Create a deactivated user
        self.user = CustomUser.objects.create_user(
            username=username, email=email, last_name=last_name, first_name=first_name,
            phone=phone, password=password)
        self.user.is_active = False
        self.user.save()

        # Send a confirmation email
        self.send_email(request)

    def send_email(self, request):
        user = self.user
        current_site = get_current_site(request)
        mail_subject = 'Activate your blog account.'
        message = render_to_string('account/account_sign_up_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = self.cleaned_data.get('email')
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'last_name', 'first_name', 'phone')

    def update(self, request):
        user = request.user
        user.username = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.phone = self.cleaned_data.get('phone')
        user.save()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UserPasswordConfirmForm(forms.Form):
    password = FORM_PASSWORD
    password_confirm = FORM_PASSWORD_CONFIRM

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError("Les deux mots de passes ne correspondent pas", code="password_confirm")

    def password_check(self, request):
        password_user = request.user.password
        password = self.cleaned_data.get('password')
        if not check_password(password, password_user):
            self.add_error("password", "Le mot de passe ne correspond pas à celui de l'utilisateur.")
        return True


class UserPasswordResetForm(PasswordResetForm):
    email = FORM_EMAIL


class UserPasswordSetForm(SetPasswordForm):
    new_password1 = FORM_PASSWORD_NEW
    new_password2 = FORM_PASSWORD_CONFIRM




"""
CustomGroup
    - CustomGroupForm
"""
class CustomGroupForm(forms.ModelForm):
    class Meta:
        model = CustomGroup
        fields = '__all__'
        exclude = ('user', 'validated')

    def save_group(self, request):
        self.save(commit=False)
        self.user = request.user
        self.save()

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
class DateInput(forms.DateInput):
    input_type = 'date'
    
    

class ConcertForm(forms.ModelForm):
    groupe1 = ModelChoiceField(queryset=CustomGroup.objects.all(), widget=Select2Widget)
    groupe2 = ModelChoiceField(queryset=CustomGroup.objects.all(), widget=Select2Widget)
    groupe3 = ModelChoiceField(queryset=CustomGroup.objects.all(), widget=Select2Widget)

    date = forms.DateField( widget=DateInput )    
    

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
        if Concert.objects.filter(date=date).exists() :
            raise forms.ValidationError("Ce vendredi est indisponible.")
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

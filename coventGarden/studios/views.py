from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta, datetime
from django.contrib import messages
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)
from .forms import UserPasswordResetForm, UserPasswordSetForm

from .models import CustomGroup, Event, TechnicalSheet, CustomUser, Reservation, Salle
from .forms import (
    SignInForm, SignUpForm, GroupCreateForm,
    UserUpdateForm, ConfirmPasswordForm,
    EventForm, TechnicalSheetForm, ReservationForm)


User = get_user_model()

# Create your views here.
"""
WIP
    - Placeholder
"""
def placeholder(request):
    return render(request, 'home.html')


"""
Navigation
    - Home
    - News
    - Studios
    - Bar
    - Pro area
    - Contact
    - Booking
"""
def home(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Covent Garden",
    }

    return render(request, 'home.html', context)

def news(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Actualités",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": None, "name": "Actualités"}],
    }

    return render(request, 'news.html')

def studios(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Studios",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": None, "name": "Studios"}],
    }

    return render(request, 'studios.html')

def concert(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Concert",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": None, "name": "Concert"}],
    }

    return render(request, 'concert.html', context)

def bar(request):
    return render(request, 'bar.html')

@csrf_exempt
@login_required
def pro_area(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Espace Pro",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": None, "name": "Espace Pro"}],
        "form": None
    }

    # Submit form
    if request.method == 'POST':
        technical_sheet = TechnicalSheet.objects.all().filter(user=request.user).first()
        if not technical_sheet:
            technical_sheet = TechnicalSheet()

        context["form"] = TechnicalSheetForm(request.POST, request.FILES)
        if context["form"].is_valid():
            # Process
            deposited_file = context["form"].cleaned_data['pdf_file']
            technical_sheet.pdf_file = deposited_file
            technical_sheet.user = request.user
            technical_sheet.save()
            return render(request, 'pro_area.html', context)

    context["form"] = TechnicalSheetForm()
    return render(request, 'pro_area.html', context)

def contact(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Contact",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": None, "name": "Contact"}],
        "form": None
    }

    return render(request, 'contact.html', context)

def booking(request):
    return render(request, 'booking.html')


"""
Account
    - Sign in
    - Sign out
    - Log in (Redirect)
    - Log out (Redirect)
"""
def account_sign_in(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Se connecter à son compte",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": None, "name": "Connexion"}],
        "form": None
    }

    # Submit form
    if request.method == 'POST':
        context["form"] = SignInForm(request.POST)
        if context["form"].is_valid():
            # Form input
            username = request.POST["username"]
            password = request.POST["password"]

            # Log in the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Redirect on success
                login(request, user)
                return redirect('profile_detail')
            else:
                print("Error: User not found.")

    # Return an empty form if GET request or invalid form
    context["form"] = SignInForm()
    return render(request, 'account/account_sign_in.html', context)

def account_sign_up(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Créer un compte",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": None, "name": "Inscription"}],
        "form": None
    }

    # Submit form
    if request.method == 'POST':
        context["form"] = SignUpForm(request.POST)
        if context["form"].is_valid():
            # Form input
            username = request.POST["username"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            password = request.POST["password"]
            confirm_password = request.POST["confirm_password"]

            if password == confirm_password:
                # Create a new user
                user = User.objects.create_user(
                    username=username, email=email, password=password,
                    last_name=last_name, first_name=first_name)
                user.save()

                # Log in the user
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    # Redirect on success
                    login(request, user)
                    return redirect('profile_detail')
                else:
                    print("Error: User not found.")
            else:
                print("Error: Password and confirmation password do not match")

    # Return an empty form if GET request or invalid form
    context["form"] = SignUpForm()
    return render(request, 'account/account_sign_up.html', context)

def account_log_out(request):
    # Disconnect the user
    logout(request)

    # Redirect on success
    return redirect('account_sign_in')


"""
Profile
    - Detail
    - Update
"""
def profile_detail(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Validation de la demande",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": None, "name": "Compte"}]
    }

    # Redirect to login page if user is not logged in
    if not request.user.is_authenticated:
        return redirect("account_sign_in")

    return render(request, 'profile/profile_detail.html', context)

def profile_update(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Modifier mon profil",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": "profile_detail", "name": "Compte"},
            {"view": None, "name": "Modifier"}],
        "form": None, "confirm_form": None
    }

    # Redirect to login page if user is not logged in
    if not request.user.is_authenticated:
        return redirect("account_sign_in")

    # Create a new form with initial values
    def create_form():
        current_user = request.user
        new_form = UserUpdateForm(initial={
            "username": current_user.username,
            "email": current_user.email,
            "last_name": current_user.last_name,
            "first_name": current_user.first_name
        })
        return new_form

    # Submit form
    if request.method == 'POST':
        context["form"] = UserUpdateForm(request.POST)
        context["confirm_form"] = ConfirmPasswordForm(request.POST)
        if context["form"].is_valid() and context["confirm_form"].is_valid():
            if request.POST["current_password"] == request.POST["confirm_password"]:
                # Form input
                user = request.user
                user.username = request.POST["username"]
                user.email = request.POST["email"]
                user.last_name = request.POST["last_name"]
                user.first_name = request.POST["first_name"]

                # Update the user
                user.save()

                # Redirect on success
                return redirect('profile_detail')
            else:
                print("Error: Password and confirmation password do not match")

    # Return an empty form if GET request or invalid form
    context["form"] = create_form()
    context["confirm_form"] = ConfirmPasswordForm()
    return render(request, 'profile/profile_update.html', context)



"""
Groups
    - Detail
    - Create
    - Update
    - Delete
"""
def groups_detail(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Mes groupes",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": None, "name": "Groupes"}],
        "my_groups": None
    }

    # Redirect to login page if user is not logged in
    if not request.user.is_authenticated:
        return redirect("account_sign_in")

    # Get all groups object related to the current user
    context["my_groups"] = request.user.my_groups.all()

    return render(request, 'groups/groups_detail.html', context)

def groups_create(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Créer un groupe",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": "groups_detail", "name": "Groupes"},
            {"view": None, "name": "Créer"}],
        "form": None
    }

    # Redirect to login page if user is not logged in
    if not request.user.is_authenticated:
        return redirect("account_sign_in")

    def create_form():
        # Form initial value(s)
        current_user = request.user
        new_form = GroupCreateForm(initial={
            "email": current_user.email,
            "phone": current_user.phone,
        })
        return new_form

    # Submit form
    if request.method == 'POST':
        context["form"] = GroupCreateForm(request.POST)
        if context["form"].is_valid():
            # Associate the group to the current user
            group = context["form"].save(commit=False)
            group.user = request.user

            # Create a new group
            group.save()

            # Redirect on success
            return redirect('groups_detail')

    # Return an empty form if GET request or invalid form
    context["form"] = create_form()
    return render(request, 'groups/groups_create.html', context)

def groups_update(request, group_id):
    # Context: Variables passed to the web page
    context = {
        "title": "Modifier un groupe",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": "groups_detail", "name": "Groupes"},
            {"view": None, "name": "Modifier"}],
        "form": None
    }

    # Redirect to login page if user is not logged in
    if not request.user.is_authenticated:
        return redirect("account_sign_in")

    # Get group object with its id
    group = CustomGroup.objects.get(id=group_id)

    # Submit form
    if request.method == 'POST':
        context["form"] = GroupCreateForm(request.POST, instance=group)
        if context["form"].is_valid():
            # Update the group
            context["form"].save()

            # Redirect on success
            return redirect('groups_detail')

    # Return an empty form if GET request or invalid form
    context["form"] = GroupCreateForm(instance=group)
    return render(request, 'groups/groups_update.html', context)

def groups_delete(request, group_id):
    # Context: Variables passed to the web page
    context = {
        "title": "Supprimer un groupe",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": "groups_detail", "name": "Groupes"},
            {"view": None, "name": "Supprimer"}],
        "group": None
    }

    # Redirect to login page if user is not logged in
    if not request.user.is_authenticated:
        return redirect("account_sign_in")

    # Get group object with its id
    context["group"] = CustomGroup.objects.get(id=group_id)

    # Submit form
    if request.method == 'POST':
        # Delete the group
        context["group"].delete()

        # Redirect on success
        return redirect('groups_detail')

    return render(request, 'groups/groups_delete.html', context)



"""
Bookings
    - Detail
    - Create
"""
def bookings_detail(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Supprimer un groupe",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": None, "name": "Réservations"}],
        "my_bookings": None,
    }

    # Redirect to login page if user is not logged in
    if not request.user.is_authenticated:
        return redirect("account_sign_in")

    # Get all groups object related to the current user
    context["my_groups"] = request.user.my_groups.all()

    return render(request, 'bookings/bookings_detail.html', context)

def bookings_create(request):
    # Context: Variables passed to the web page
    context = {
        "title": "Créer un groupe",
        "breadcrumb": [
            {"view": "home", "name": "Accueil"},
            {"view": "bookings_detail", "name": "Réservations"},
            {"view": None, "name": "Créer"}],
        }

    # Redirect to login page if user is not logged in
    if not request.user.is_authenticated:
        return redirect("account_sign_in")

    # Return an empty form if GET request or invalid form
    return render(request, 'bookings/bookings_create.html', context)



"""
Password reset
    - Forgot: password_reset_forgot.html
    - Done: password_reset_done.html
    - Confirm: password_reset_confirm.html
    - Complete: password_reset_complete.html
"""
class CustomPasswordResetForgot(PasswordResetView):
    template_name = 'password_reset/password_reset_forgot.html'
    html_email_template_name = 'password_reset/password_reset_email.html'
    form_class = UserPasswordResetForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Context: Variables passed to the web page
        context["title"] = "Récupérer son compte"
        context["breadcrumb"] = [
            {"view": "home", "name": "Accueil"},
            {"view": None, "name": "Mot de passe oublié"}]
        return context

class CustomPasswordResetDone(PasswordResetView):
    template_name = 'password_reset/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Context: Variables passed to the web page
        context["title"] = "Validation de la demande"
        context["breadcrumb"] = [
            {"view": "home", "name": "Accueil"},
            {"view": "password_reset_forgot", "name": "Mot de passe oublié"},
            {"view": None, "name": "Envoi"}]
        return context

class CustomPasswordResetConfirm(PasswordResetView):
    template_name = 'password_reset/password_reset_confirm.html',
    form_class = UserPasswordSetForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Context: Variables passed to the web page
        context["title"] = "Modifier mon mot de passe"
        context["breadcrumb"] = [
            {"view": "home", "name": "Accueil"},
            {"view": "password_reset_forgot", "name": "Mot de passe oublié"},
            {"view": None, "name": "Envoi"},
            {"view": None, "name": "Modifier"}]
        return context

class CustomPasswordResetComplete(PasswordResetView):
    template_name = 'password_reset/password_reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Context: Variables passed to the web page
        context["title"] = "Confirmation"
        context["breadcrumb"] = [
            {"view": "home", "name": "Accueil"},
            {"view": "password_reset_forgot", "name": "Mot de passe oublié"},
            {"view": None, "name": "Envoi"},
            {"view": None, "name": "Modifier"},
            {"view": None, "name": "Confirmation"}]
        return context



"""
Planning
"""
def generate_occurrences(event):
    occurrences = [event.start_time]

    if event.recurrence == 'daily':
        current_time = event.start_time
        while current_time < event.end_time:
            current_time += timedelta(days=1)
            occurrences.append(current_time)

    return occurrences


def add_event(request):
    # Submit form
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})


def index(request):
    all_events = Event.objects.all()

    events = []
    for event in all_events:
        occurrences = generate_occurrences(event)
        for occurrence in occurrences:
            events.append({
                'title': event.title,
                'id': event.id,
                'start': occurrence.strftime("%Y-%m-%d %H:%M:%S"),
                'end': occurrence.strftime("%Y-%m-%d %H:%M:%S"),
            })

    context = {
        "events": events,
    }
    return render(request, 'index.html', context)


def all_events(request):
    events = Event.objects.all()
    out = []
    for event in events:
        out.append({
            'title': event.title,
            'id': event.id,
            'start': event.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'end': event.end_time.strftime("%Y-%m-%d %H:%M:%S"),
        })
    return JsonResponse(out, safe=False)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    event.start_time = start
    event.end_time = end
    event.title = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)


def calendar_view(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'calendar.html', context)

"""
Salles
    -Listing all Salle
Reservation
    - Listing reservation
"""
def list_salles(request):
    salles = Salle.objects.all()
    salle_data = [{"id": salle.id, "title": salle.name} for salle in salles]
    return JsonResponse(salle_data, safe=False)

def list_users(request):
    users = CustomUser.objects.all()
    user_data = [{"id": user.id, "title": user.username} for user in users]
    return JsonResponse(user_data, safe=False)


def accompte(request):

    # Submit form
    if request.method == 'POST':

        salle_id = int(request.POST["salle_id"])
        #salle_id = int(request.POST["salle_id"])
        salle = Salle.objects.get(id= salle_id)

        user_id = int(request.POST["user_id"])
        user = CustomUser.objects.get(id= user_id)

        start_date = request.POST["date_start"]
        end_date = request.POST["date_end"]

        form = ReservationForm()

        #print(form)

        duration = datetime.fromisoformat(end_date.rstrip('Z')) - datetime.fromisoformat(start_date.rstrip('Z'))
        duration_seconds = duration.total_seconds()
        duration_hours = duration_seconds / 3600
        print(duration_hours)

        duration = 1
        return render(request, 'payment.html', {"salle": salle, "user": user, "start_date": start_date,
        "end_date": end_date, "duration": duration_hours, "form": form})

    else:
        return redirect('booking')


def payment(request):

    print(request.POST)

    # Submit form
    if request.method == 'POST':

        salle_id = int(request.POST["salle_id"])
        user_id = int(request.POST["user_id"])

        form = ReservationForm(request.POST)

        if form.is_valid():

            salle = Salle.objects.get(id= salle_id)
            user = CustomUser.objects.get(id= user_id)

            description = "Reservation for user "+ user.username
            duration = form.cleaned_data["duration"]
            date_start = form.cleaned_data["date_start"]
            date_end = form.cleaned_data["date_end"]
            price = form.cleaned_data["price"]
            status = "En cours"
            """
            description = ""
            duration = request.POST["duration"]
            date_start = request.POST["date_start"]
            date_end = request.POST["date_end"]
            price = request.POST["price"]
            status = "En cours"
            """
            """
            description = models.fields.CharField(max_length=1000)
            duration = models.fields.IntegerField(choices=Duration.choices)
            date_start = models.DateTimeField(null=False)
            date_end = models.DateTimeField(null=False)
            hour_begin = models.TimeField(null=False)
            price = models.fields.IntegerField(validators=[MinValueValidator(1)])
            status = models.fields.CharField(choices=Status.choices, max_length=20)
            salle = models.ForeignKey(Salle, null=True, on_delete=models.SET_NULL)
            user = models.ForeignKey(Utilisateur, null=True, on_delete=models.SET_NULL)
            """
            reservation = Reservation.objects.create(
                description=description,
                duration=duration,
                date_start=date_start,
                date_end=date_end,
                price=price,
                status=status,
                salle=salle,
                user=user
            )

            messages.success(request, "Votre réservation a bien été prise en compte !")
            # Redirect to the detail page of the band we just created
            return redirect('booking')

    else:
        return redirect('booking')


def all_booking(request):
    reservations = Reservation.objects.all()
    datas = []
    for current in reservations:
        datas.append({
            'title': current.description,
            'id': current.id,
            'start': current.date_start.strftime("%Y-%m-%d %H:%M:%S"),
            'end': current.date_end.strftime("%Y-%m-%d %H:%M:%S"),
        })
    return JsonResponse(datas, safe=False)

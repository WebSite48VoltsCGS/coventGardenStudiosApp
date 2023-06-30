from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta

from .models import CustomGroup, Event, TechnicalSheet, CustomUser, Reservation, Salle
from .forms import (
    SignInForm, SignUpForm, GroupCreateForm,
    UserUpdateForm, ConfirmPasswordForm,
    EventForm, TechnicalSheetForm, ReservationForm)
from datetime import datetime
from django.contrib import messages

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
    return render(request, 'home.html')

def news(request):
    return render(request, 'news.html')

def studios(request):
    return render(request, 'studios.html')

def concert(request):
    return render(request, 'concert.html')

def bar(request):
    return render(request, 'bar.html')

@csrf_exempt
@login_required
def pro_area(request):
    if request.method == 'POST':
        technical_sheet = TechnicalSheet.objects.all().filter(user=request.user).first()
        if not technical_sheet:
            technical_sheet = TechnicalSheet()

        form = TechnicalSheetForm(request.POST, request.FILES)
        if form.is_valid():
            # Process
            deposited_file = form.cleaned_data['pdf_file']
            technical_sheet.pdf_file = deposited_file
            technical_sheet.user = request.user
            technical_sheet.save()
            return render(request, 'pro_area.html', {'form': form})

    form = TechnicalSheetForm()
    return render(request, 'pro_area.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')

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
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
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
    form = SignInForm()
    return render(request, 'account/account_sign_in.html', {'form': form})

def account_sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
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
    form = SignUpForm()
    return render(request, 'account/account_sign_up.html', {'form': form})

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
    return render(request, 'profile/profile_detail.html')

def profile_update(request):
    def empty_form():
        # Form initial value(s)
        current_user = request.user
        new_form = UserUpdateForm(initial={
            "username": current_user.username,
            "email": current_user.email,
            "last_name": current_user.last_name,
            "first_name": current_user.first_name
        })
        return new_form

    if request.method == 'POST':
        form = UserUpdateForm(request.POST)
        confirm_form = ConfirmPasswordForm(request.POST)
        if form.is_valid() and confirm_form.is_valid():
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
    form = empty_form()
    confirm_form = ConfirmPasswordForm()
    return render(request, 'profile/profile_update.html', {'form': form, 'confirm_form': confirm_form})


"""
Groups
    - Detail
    - Create
    - Update
    - Delete
"""
def groups_detail(request):
    # Get all groups object related to the current user
    my_groups = request.user.my_groups.all()

    return render(request, 'groups/groups_detail.html', {'my_groups': my_groups})

def groups_create(request):
    def empty_form():
        # Form initial value(s)
        current_user = request.user
        new_form = GroupCreateForm(initial={
            "email": current_user.email,
            "phone": current_user.phone,
        })
        return new_form

    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            # Associate the group to the current user
            group = form.save(commit=False)
            group.user = request.user

            # Create a new group
            group.save()

            # Redirect on success
            return redirect('groups_detail')

    # Return an empty form if GET request or invalid form
    form = empty_form()
    return render(request, 'groups/groups_create.html', {'form': form})

def groups_update(request, group_id):
    # Get group object with its id
    group = CustomGroup.objects.get(id=group_id)

    if request.method == 'POST':
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            # Update the group
            form.save()

            # Redirect on success
            return redirect('groups_detail')

    # Return an empty form if GET request or invalid form
    form = GroupCreateForm(instance=group)
    return render(request, 'groups/groups_update.html', {'form': form})

def groups_delete(request, group_id):
    # Get group object with its id
    group = CustomGroup.objects.get(id=group_id)

    if request.method == 'POST':
        # Delete the group
        group.delete()

        # Redirect on success
        return redirect('groups_detail')

    return render(request, 'groups/groups_delete.html', {'group': group})


"""
Bookings
    - Detail
    - Create
"""
def bookings_detail(request):
    return render(request, 'bookings/bookings_detail.html')

def bookings_create(request):
    return render(request, 'bookings/bookings_create.html')


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
Password reset
    - Forgot: password_reset_forgot.html
    - Done: password_reset_done.html
    - Confirm: password_reset_confirm.html
    - Complete: password_reset_complete.html
"""

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
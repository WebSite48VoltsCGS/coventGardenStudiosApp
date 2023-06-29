from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from .forms import (
    SignInForm, SignUpForm,
    UserUpdateForm, ConfirmPasswordForm,
    GroupCreateForm, TestForm)

User = get_user_model()

# Create your views here.
"""
Tutorial
"""
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "user_detail.html"

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

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

def bar(request):
    return render(request, 'bar.html')

def concert(request):
    return render(request, 'concert.html')

def contact(request):
    return render(request, 'contact.html')

def booking(request):
    return render(request, 'booking.html')

"""
Account
    - Sign in
    - Sign out
    - Log out
"""
def account_sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            # Log in the user
            username = request.POST["username"]
            password = request.POST["password"]
            account_log_in(request, username, password)
            return redirect('profile_detail')
        else:
            # Return an empty form if form is invalid
            form = SignInForm()
            return render(request, 'account/account_sign_in.html', {'form': form})

    # Return an empty form if GET request
    else:
        form = SignInForm()
        return render(request, 'account/account_sign_in.html', {'form': form})

def account_sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            password = request.POST["password"]
            confirm_password = request.POST["confirm_password"]

            if password == confirm_password:
                # Create a new user
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                # Log in the user
                account_log_in(request, username, password)
                return redirect('profile_detail')
            else:
                # Return an empty form if form is invalid
                form = SignUpForm()
                return render(request, 'account/account_sign_up.html', {'form': form})

    # Return an empty form if GET request
    else:
        form = SignUpForm()
        return render(request, 'account/account_sign_up.html', {'form': form})

def account_log_in(request, username, password):
    # Authenticate the user
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        print("Error: A user is already logged in.")

def account_log_out(request):
    # Disconnect the user
    if request.user:
        logout(request)
    else:
        print("Error: User is already logged out.")
    return redirect('account_sign_in')

"""
Profile
    - Detail
    - Update
    - Username update
    - Email update
    - Password update
"""
def profile_detail(request):
    return render(request, 'profile/profile_detail.html')

def profile_update(request):
    def empty_form():
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
                user = request.user
                user.username = request.POST["username"]
                user.email = request.POST["email"]
                user.last_name = request.POST["last_name"]
                user.first_name = request.POST["first_name"]
                user.save()
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
    return render(request, 'groups/groups_detail.html')

def groups_create(request):
    def empty_form():
        current_user = request.user
        new_form = GroupCreateForm(initial={
            "email": current_user.email,
            "phone": current_user.phone,
        })
        return new_form

    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups_detail')

    # Return an empty form if GET request or invalid form
    form = empty_form()
    return render(request, 'groups/groups_create.html', {'form': form})

def groups_update(request):
    return render(request, 'groups/groups.html')

def groups_delete(request):
    return render(request, 'groups/groups_delete.html')

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
Password reset
    - Forgot: password_reset_forgot.html
    - Done: password_reset_done.html
    - Confirm: password_reset_confirm.html
    - Complete: password_reset_complete.html
"""





"""
Unused
"""
def profile_username_update(request):
    """
    WIP
        Testing user fields
    """
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = request.POST["test"]
            user = request.user
            user.test_field = test
            user.save()
            print("Test successful")
            return redirect('profile_detail')

    # Return an empty form if GET request or form is invalid
    form = TestForm()
    return render(request, 'profile/profile_username_update.html', {'form': form})

def profile_email_update(request):
    return render(request, 'profile/profile_email_update.html')

def profile_password_update(request):
    return render(request, 'profile/profile_password_update.html')

###########################################################################################################################

from django.shortcuts import render
from django.http import JsonResponse 
from studios.models import Events 

from django.shortcuts import render, redirect
from .forms import EventForm

from django.core import serializers
from django.http import HttpResponse

from datetime import timedelta

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
    all_events = Events.objects.all()

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
    events = Events.objects.all()
    out = []
    for event in events :
        out.append({
            'title':event.title,
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
    event = Events.objects.get(id=id)
    event.start_time = start
    event.end_time = end
    event.title = title
    event.save()
    data = {}
    return JsonResponse(data)

 
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)


def calendar_view(request):
    events = Events.objects.all()
    context = {'events': events}
    return render(request, 'calendar.html', context)
#########################################################################################################################
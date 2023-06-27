from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from .forms import SignInForm, SignUpForm, TestForm

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

def pro_area(request):
    return render(request, 'pro_area.html')

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

    # Return an empty form if GET request or form is invalid
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

    # Return an empty form if GET request or form is invalid
    form = SignUpForm()
    return render(request, 'account/account_sign_up.html', {'form': form})

def account_log_in(request, username, password):
    # Authenticate the user
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        print("Error: A user is already logged in.")
    return redirect('profile_detail')

def account_log_out(request):
    logout(request)
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
    return render(request, 'profile/profile_update.html')

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
    return render(request, 'groups/groups_create.html')

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

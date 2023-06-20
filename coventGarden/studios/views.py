from django.http import HttpResponse
from django.shortcuts import redirect, render

def home(request):
    return render(request, 'studios/home.html')

def news(request):
    return render(request, 'studios/news.html')

def studios(request):
    return render(request, 'studios/studios.html')

def bar(request):
    return render(request, 'studios/bar.html')

def pro_area(request):
    return render(request, 'studios/pro_area.html')

def contact(request):
    return render(request, 'studios/contact.html')

def booking(request):
    return render(request, 'studios/booking.html')

def account(request):
    return render(request, 'studios/account.html')

def sign_in(request):
    return render(request, 'studios/signin.html')

def sign_up(request):
    return render(request, 'studios/base/signup.html')

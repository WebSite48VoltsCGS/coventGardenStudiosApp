"""coventGarden URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from studios import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Main
    path('', views.home, name='home'),
    path('actualités/', views.news, name='news'),
    path('studios/', views.studios, name='studios'),
    path('bar/', views.bar, name='bar'),
    path('espace_pro/', views.pro_area, name='pro_area'),
    path('contact/', views.contact, name='contact'),
    path('réservation/', views.booking, name='booking'),

    # Registration
    path('compte/', views.account, name='account'),
    path('compte/se_connecter/', views.sign_in, name='sign_in'),
    path('compte/créer_un_compte/', views.sign_up, name='sign_up'),
    path('compte/mot-de-passe-oublié/', views.password_reset_form, name='password_reset'),
    path('compte/mot-de-passe-oublié/confirmation', views.password_reset_done, name='password_reset_done'),
]

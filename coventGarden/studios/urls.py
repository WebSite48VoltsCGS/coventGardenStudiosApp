
from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from coventGarden import settings
from coventGarden.settings import STATIC_URL
from django.conf.urls.static import static 
from studios import views

from .forms import UserPasswordResetForm, UserPasswordSetForm


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),

    path('', views.placeholder, name='placeholder'),

    # Navigation
    path('', views.home, name='home'),
    path('actualites/', views.news, name='news'),
    path('studios/', views.studios, name='studios'),
    path('bar/', views.bar, name='bar'),
    path('espace_pro/', views.pro_area, name='pro_area'),
    path('contact/', views.contact, name='contact'),
    path('reservation/', views.booking, name='booking'),

    # Account
    path('compte/connexion/', views.account_sign_in, name='account_sign_in'),
    path('compte/inscription/', views.account_sign_up, name='account_sign_up'),
    path('compte/deconnexion/', views.account_log_out, name='account_log_out'),

    # Profile
    path('compte/mon_profil/', views.profile_detail, name='profile_detail'),
    path('compte/mon_profil/modifier/', views.profile_update, name='profile_update'),
    path('compte/mon_profil/modifier/utilisateur', views.profile_username_update, name='profile_username_update'),
    path('compte/mon_profil/modifier/email', views.profile_email_update, name='profile_email_update'),
    path('compte/mon_profil/modifier/mot_de_passe', views.profile_password_update, name='profile_password_update'),

    # Groups
    path('compte/mes_groupes/', views.groups_detail, name='groups_detail'),
    path('compte/mes_groupes/ajouter/', views.groups_create, name='groups_create'),
    path('compte/mes_groupes/modifier/', views.groups_update, name='groups_update'),
    path('compte/mes_groupes/supprimer/', views.groups_delete, name='groups_delete'),

    # Bookings
    path('compte/mes_reservations/', views.bookings_detail, name='bookings_detail'),
    path('compte/mes_reservations/ajouter/', views.bookings_create, name='bookings_create'),

    # Password Reset
    path('compte/mot-de-passe/oublie/',
         PasswordResetView.as_view(
             template_name='password_reset/password_reset_forgot.html',
             html_email_template_name='password_reset/password_reset_email.html',
             form_class=UserPasswordResetForm),
         name='password_reset_forgot'),
    path('compte/mot-de-passe-oublie/envoi/',
         PasswordResetDoneView.as_view(
             template_name='password_reset/password_reset_done.html'),
         name='password_reset_done'),
    path('compte/mot-de-passe-oublie/modification/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='password_reset/password_reset_confirm.html',
             form_class=UserPasswordSetForm),
         name='password_reset_confirm'),
    path('compte/mot-de-passe-oublie/confirmation/',
         PasswordResetCompleteView.as_view(
             template_name='password_reset/password_reset_complete.html'),
         name='password_reset_complete'),

    

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


#url fichier Luca modif ligne 76-82, et ligne 10 et 11 et 17



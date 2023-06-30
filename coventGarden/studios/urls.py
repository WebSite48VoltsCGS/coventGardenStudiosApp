from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)
from django.conf.urls.static import static

from coventGarden import settings
from studios import views
from .forms import UserPasswordResetForm, UserPasswordSetForm


urlpatterns = [
    path('', views.placeholder, name='placeholder'),

    # Navigation
    path('', views.home, name='home'),
    path('actualites/', views.news, name='news'),
    path('studios/', views.studios, name='studios'),
    path('concert/', views.concert, name='concert'),
    path('bar/', views.bar, name='bar'),
    path('espace_pro/', views.pro_area, name='pro_area'),
    path('reservation/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),

    # Account
    path('compte/connexion/', views.account_sign_in, name='account_sign_in'),
    path('compte/inscription/', views.account_sign_up, name='account_sign_up'),
    path('compte/deconnexion/', views.account_log_out, name='account_log_out'),

    # Profile
    path('compte/', views.profile_detail, name='profile_detail'),
    path('compte/modifier/', views.profile_update, name='profile_update'),

    # Groups
    path('compte/mes_groupes/', views.groups_detail, name='groups_detail'),
    path('compte/mes_groupes/ajouter/', views.groups_create, name='groups_create'),
    path('compte/mes_groupes/modifier/<int:group_id>/', views.groups_update, name='groups_update'),
    path('compte/mes_groupes/supprimer/<int:group_id>/', views.groups_delete, name='groups_delete'),

    # Bookings
    path('compte/mes_reservations/', views.bookings_detail, name='bookings_detail'),
    path('compte/mes_reservations/ajouter/', views.bookings_create, name='bookings_create'),

    # Planning
    path('all_events/', views.all_events, name='all_events'),
    path('add_event/', views.add_event, name='add_event'),
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
    path('calendar/', views.calendar_view, name='calendar'),

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
    
    #### Gestion des Booking

    path('api/all_booking/', views.all_booking, name='all_booking'),

    path('users/', views.list_users, name='list_users'),
    path('salles/', views.list_salles, name='list_salles'),
    path('paiement-accompte/', views.accompte, name='accompte'),
    path('payment/', views.payment, name='payment'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

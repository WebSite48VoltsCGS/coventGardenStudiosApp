from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)
from django.conf.urls.static import static

from coventGarden import settings
from studios import views
from .forms import UserPasswordResetForm, UserPasswordSetForm
#################################


urlpatterns = [
    path('', views.placeholder, name='placeholder'),

    # Navigation
    path('', views.HomeView.as_view(), name='home'),
    path('actualites/', views.NewsView.as_view(), name='news'),
    path('studios/', views.StudiosView.as_view(), name='studios'),
    path('concert/', views.ConcertView.as_view(), name='concert'),
    path('bar/', views.BarView.as_view(), name='bar'),
    path('reservation/', views.booking, name='booking'),
    path('contact/', views.ContactView.as_view(), name='contact'),

    # Account: Login / Logout
    path('compte/connexion/', views.AccountSignInFormView.as_view(),
         name='account_sign_in_form'),
    path('compte/deconnexion/', views.account_log_out,
         name='account_log_out'),

    # Account: Sign Up
    path('compte/inscription/', views.AccountSignUpFormView.as_view(),
         name='account_sign_up_form'),
    path('compte/inscription/envoi/', views.AccountSignUpDoneView.as_view(),
         name="account_sign_up_done"),
    path('compte/inscription/confirmation/<uidb64>/<token>/', views.AccountSignUpConfirmView.as_view(),
         name='account_sign_up_confirm'),
    path('compte/inscription/failed/', views.AccountSignUpFailedView.as_view(),
         name='account_sign_up_failed'),

    # Account: Password Forgot
    path('compte/mot-de-passe-oublie/', views.AccountPasswordForgotForm.as_view(),
         name='account_password_forgot_form'),
    path('compte/mot-de-passe-oublie/envoi/', views.AccountPasswordForgotDone.as_view(),
         name='account_password_forgot_done'),
    path('compte/mot-de-passe-oublie/modification/<uidb64>/<token>/', views.AccountPasswordForgotConfirm.as_view(),
         name='account_password_forgot_confirm'),
    path('compte/mot-de-passe-oublie/confirmation/', views.AccountPasswordForgotComplete.as_view(),
         name='account_password_forgot_complete'),

    # Profile
    path('compte/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('compte/modifier/', views.ProfileUpdateView.as_view(), name='profile_update'),

    # Groups
    path('compte/mes_groupes/', views.GroupDetailView.as_view(), name='groups_detail'),
    path('compte/mes_groupes/ajouter/', views.GroupCreateView.as_view(), name='groups_create'),
    path('compte/mes_groupes/modifier/<int:group_id>/', views.GroupUpdateView.as_view(), name='groups_update'),
    path('compte/mes_groupes/supprimer/<int:group_id>/', views.GroupDeleteView.as_view(), name='groups_delete'),

    # Bookings
    path('compte/mes_reservations/', views.BookingsDetailView.as_view(), name='bookings_detail'),
    path('compte/mes_reservations/ajouter/', views.BookingsCreateView.as_view(), name='bookings_create'),

    # Pro Area
    path('compte/espace_pro/', views.ProAreaView.as_view(), name='pro_area'),

    # Planning
    path('all_events/', views.all_events, name='all_events'),
    path('add_event/', views.add_event, name='add_event'),
    path('update/', views.update, name='update'),
    path('remove/', views.remove, name='remove'),
    path('calendar/', views.calendar_view, name='calendar'),

    # Booking
    path('api/all_booking/', views.all_booking, name='all_booking'),
    path('api/all_booking_event/', views.all_booking_event, name='all_booking_event'),
    path('set-reservation/<int:id_reservation>/', views.set_reservation, name='set_reservation'),
    path('users/', views.list_users, name='list_users'),
    path('salles/', views.list_salles, name='list_salles'),
    path('paiement-accompte/', views.accompte, name='accompte'),
    # path('payment_successful', views.payment_successful, name='payment_successful'),
    # path('payment_cancelled', views.payment_cancelled, name='payment_cancelled'),
    path('stripe_webhook', views.stripe_webhook, name='stripe_web'),

    # WIP
    path('create-checkout-session/', views.payment, name='payment'),

    # Deleted
    path('delete_technical_sheet/<int:pk>/', views.delete_technical_sheet, name='delete_technical_sheet'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

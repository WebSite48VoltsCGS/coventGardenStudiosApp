from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, CustomGroup, Event, TechnicalSheet, Salle, Reservation

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]

class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "email",
                    "phone", "members", "genre",
                    "facebook", "instagram", "biography"]

class EventAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "start_time", "end_time", "description"]

class TechnicalSheetAdmin(admin.ModelAdmin):
    list_display = ["user", "pdf_file"]

class SalleAdmin(admin.ModelAdmin):
   list_display = ('name', 'description')

class ReservationAdmin(admin.ModelAdmin):
   list_display = ('description', 'duration', 'date_start','date_end', 'price', 'status', 'salle', 'user')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomGroup, CustomGroupAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TechnicalSheet, TechnicalSheetAdmin)
admin.site.register(Salle, SalleAdmin)
admin.site.register(Reservation, ReservationAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, CustomGroup, Event, Salle, Reservation, Concert

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ["email", "username", "last_name", "first_name", "phone"]

class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "email", "phone", "members", "technical_sheet", "logo", "validated"]

class EventAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "start_time", "end_time", "description"]

class SalleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('description', 'duration', 'date_start','date_end', 'price', 'status', 'salle', 'user', 'is_active')

class ConcertAdmin(admin.ModelAdmin):
    list_display = ["user", 'groupe1', 'groupe2', 'groupe3', 'date', 'validated']
    list_filter = ['validated']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomGroup, CustomGroupAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Salle, SalleAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Concert, ConcertAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, CustomGroup, Event, TechnicalSheet, Salle, Reservation, Concert

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ["email", "username",
                    "last_name", "first_name",
                    "phone"]

class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "email",
                    "phone", "members", "genre",
                    "facebook", "instagram", "biography",
                    "validated"]

class EventAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "start_time", "end_time", "description"]

class TechnicalSheetAdmin(admin.ModelAdmin):
    list_display = ["user", "pdf_file", "pdf_logo"]

class SalleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('description', 'duration', 'date_start','date_end', 'price', 'status', 'salle', 'user')

class ConcertAdmin(admin.ModelAdmin):
    list_display = ["user",'groupe1', 'groupe2', 'groupe3', 'date', 'validated']
    list_filter = ['validated']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomGroup, CustomGroupAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TechnicalSheet, TechnicalSheetAdmin)
admin.site.register(Salle, SalleAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Concert, ConcertAdmin)

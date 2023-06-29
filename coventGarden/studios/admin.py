from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, CustomGroup, Event

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


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomGroup, CustomGroupAdmin)
admin.site.register(Event, EventAdmin)

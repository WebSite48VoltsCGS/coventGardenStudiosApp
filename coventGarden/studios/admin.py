from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, CustomGroup

#import event
from .models import Events

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]

class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ["name", "email",
                    "phone", "members", "genre",
                    "facebook", "instagram", "biography"]

admin.site.register(CustomGroup, CustomGroupAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

#nouvelle class

class eventAdmin(admin.ModelAdmin):
    list_display = ["Utilisateur","title", "start_time","end_time","description"]

admin.site.register(Events,eventAdmin)

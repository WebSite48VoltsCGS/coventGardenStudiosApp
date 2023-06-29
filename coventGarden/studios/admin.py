from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser
#ajout fiche technique Luca ligne 7
from .models import FicheTechnique  

from .models import CustomUser, CustomGroup, Event

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]
    #modification Luca ligne 15.
    

class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "email",
                    "phone", "members", "genre",
                    "facebook", "instagram", "biography"]

class EventAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "start_time", "end_time", "description"]


admin.site.register(CustomUser, CustomUserAdmin)


#Model for uploading, ajout Luca ligne 22 à 25

class FicheTechniqueadmin(admin.ModelAdmin):
    list_display = ["Utilisateur","Fiche_Technique"]

admin.site.register(FicheTechnique, FicheTechniqueadmin)

admin.site.register(CustomGroup, CustomGroupAdmin)
admin.site.register(Event, EventAdmin)

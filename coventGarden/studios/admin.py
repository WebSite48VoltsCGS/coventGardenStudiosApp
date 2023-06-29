from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
#ajout fiche technique Luca ligne 7
from .models import FicheTechnique  


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username"]
    #modification Luca ligne 15.
    

admin.site.register(CustomUser, CustomUserAdmin)


#Model for uploading, ajout Luca ligne 22 à 25

class FicheTechniqueadmin(admin.ModelAdmin):
    list_display = ["Utilisateur","Fiche_Technique"]

admin.site.register(FicheTechnique, FicheTechniqueadmin)
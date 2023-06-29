# studios/__init__.py

from django.apps import AppConfig

class StudiosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studios'

default_app_config = 'studios.StudiosConfig'

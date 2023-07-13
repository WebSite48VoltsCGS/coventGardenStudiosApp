"""
WSGI config for coventGarden project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
>>>>>>> 52f8c78af420c12d762aac510dbc4755b9199d2a
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coventGarden.settings')

application = get_wsgi_application()

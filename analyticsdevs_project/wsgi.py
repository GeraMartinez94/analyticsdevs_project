"""
WSGI config for analyticsdevs_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
# Si vas a usar WhiteNoise (pip install whitenoise), descomenta la siguiente línea:
# from whitenoise.middleware import WhiteNoiseMiddleware 

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'analyticsdevs_project.settings')

application = get_wsgi_application()

# Si usas WhiteNoise, descomenta esta línea. Esto permite que WhiteNoise 
# sirva tus archivos estáticos de forma eficiente en producción.
# application = WhiteNoiseMiddleware(application)
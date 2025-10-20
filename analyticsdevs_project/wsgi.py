"""
WSGI config for analyticsdevs_project project.
# ...
"""

import os
# Si vas a usar WhiteNoise (pip install whitenoise), descomenta la siguiente línea:
# from whitenoise.middleware import WhiteNoiseMiddleware


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'analyticsdevs_project.settings')
# ...
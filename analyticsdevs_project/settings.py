# analyticsdevs_project/settings.py

import os
from pathlib import Path
from dotenv import load_dotenv # Necesitas instalar: pip install python-dotenv

# Cargar variables de entorno desde el archivo .env (solo funciona localmente)
load_dotenv() 

# ... (BASE_DIR y otras configuraciones permanecen iguales) ...

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-tu-clave-por-defecto') 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True') == 'True' 

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.onrender.com'] 

# ... (El resto del settings.py debe ser el código final que acordamos, incluyendo STATIC_ROOT) ...
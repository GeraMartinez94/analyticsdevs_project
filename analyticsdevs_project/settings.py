import os # Importar para usar os.environ.get y definir rutas
from pathlib import Path
from dotenv import load_dotenv # Importar para leer el archivo .env

# Cargar variables de entorno desde el archivo .env (solo funciona localmente)
load_dotenv() 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
# Lee la SECRET_KEY de las variables de entorno (en .env o en el panel de PA)
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-tu-clave-por-defecto') 

# SECURITY WARNING: don't run with debug turned on in production!
# Lee el estado de DEBUG de las variables de entorno
DEBUG = os.environ.get('DEBUG', 'True') == 'True' 

# Permite hosts de desarrollo y el dominio de PythonAnywhere (GeraMar94.pythonanywhere.com)
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'GeraMar94.pythonanywhere.com'] 

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # CRÍTICO: Permite el comando collectstatic
    # Mis Apps:
    'core',
    'portafolio',
    'eventos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'analyticsdevs_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'analyticsdevs_project.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'es-es' # Usamos español de España

TIME_ZONE = 'America/Argentina/Buenos_Aires' # Ajusta tu zona horaria

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# ----------------------------------------
STATIC_URL = '/static/'

# Directorios donde Django busca archivos estáticos en desarrollo (core/static)
STATICFILES_DIRS = [
    BASE_DIR / 'core/static', 
]

# ----------------------------------------------------------------------
# >>> CONFIGURACIÓN PARA PRODUCCIÓN (collectstatic) <<<
# ----------------------------------------------------------------------

# Directorio donde 'collectstatic' reunirá todos los archivos estáticos.
STATIC_ROOT = BASE_DIR / 'staticfiles' 

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
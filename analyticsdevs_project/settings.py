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
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
# Permite hosts de desarrollo y el dominio de PythonAnywhere (GeraMar94.pythonanywhere.com)
RAILWAY_DOMAIN = os.environ.get('RAILWAY_PUBLIC_DOMAIN') or os.environ.get('RAILWAY_STATIC_URL')
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
if RAILWAY_DOMAIN:
    # Agrega el dominio público asignado por Railway
    ALLOWED_HOSTS.append(RAILWAY_DOMAIN)
# Opción de comodín (menos segura, pero asegura que funcione en el dominio .up.railway.app)
ALLOWED_HOSTS.append('.up.railway.app')
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


# settings.py

# ----------------------------------------------------
# CONFIGURACIÓN DE CORREO ELECTRÓNICO (EMAIL)
# LECTURA DE VARIABLES DESDE .env O ENTORNO DE PRODUCCIÓN
# ----------------------------------------------------

# La contraseña de aplicación de Google o la contraseña del host SMTP.
# Si el envío falla, revisa que EMAIL_HOST_PASSWORD esté definido en tu .env o en el entorno de PythonAnywhere.
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') 

# El correo que usará Django para autenticarse (debe ser la cuenta del servicio SMTP).
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') 

# Solo activa el envío real si las credenciales están presentes
if EMAIL_HOST_USER and EMAIL_HOST_PASSWORD:
    
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    
    # Configuración del servidor (usaremos Gmail como ejemplo por defecto)
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    
    # Remitentes por defecto (usando la cuenta de envío)
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    SERVER_EMAIL = EMAIL_HOST_USER
    
    # DEBUG: Si la clave no está presente, Django no intentará enviar correos.
else:
    # Si las variables no están cargadas, usamos el backend de consola para que no falle.
    # Los correos se imprimirán en la consola de Django.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    
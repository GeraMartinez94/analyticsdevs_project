from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR apunta a la carpeta principal del proyecto (donde está manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z#&j(j&hjhj&hjhj&hjhj&hjhj&hjhj&hjhj&hjhj&hjhj&hjhj&hjhj&hjhj&hjhj&hjhj&hjhj' # Reemplaza esto con tu clave real

# SECURITY WARNING: don't run with debug turned on in production!
# ¡IMPORTANTE! Esto soluciona el error CommandError en el entorno local.
DEBUG = True 

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '::1'] # Hosts permitidos para desarrollo local


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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
        # Busca plantillas en la carpeta 'templates' de cada app
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
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-es' # Usamos español de España

TIME_ZONE = 'America/Argentina/Buenos_Aires' # Ajusta tu zona horaria

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# ----------------------------------------
STATIC_URL = '/static/'

# Define dónde buscará Django los archivos estáticos a nivel de proyecto.
# Esto apunta directamente a la carpeta 'static' dentro de la app 'core'.
STATICFILES_DIRS = [
    BASE_DIR / 'core/static', 
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_ROOT = BASE_DIR / 'staticfiles' 
import os
from pathlib import Path
from dotenv import load_dotenv
# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
REDIS_HOST = os.getenv('REDIS_HOST', 'empty_redis_host')
REDIS_PORT = os.getenv('REDIS_PORT', 'empty_redis_port')

# Configuraciones comunes
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'default-secret-key')
DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ratelimit',
    "rest_framework",
    "pokemon",
    'drf_yasg',
]

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': str(REDIS_HOST)+':'+str(REDIS_PORT)+'/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

RATELIMIT_CACHE = 'default'
RATELIMIT_USE_CACHE = 'default'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-fm1*u_)qk9flvpak)o%e&bi$66%wtu*g16qjfdkc*#j*ib1l8-"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = "pokemon_project.urls"

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

WSGI_APPLICATION = "pokemon_project.wsgi.application"

# Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validadores de contraseñas
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

# Configuración internacional
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['your-staging-domain.com']

# Configuración de base de datos para staging (por ejemplo, PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your-db-name',
        'USER': 'your-db-user',
        'PASSWORD': 'your-db-password',
        'HOST': 'your-db-host',
        'PORT': 'your-db-port',
    }
}

# Otras configuraciones específicas para staging

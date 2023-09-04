import os
import secrets
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


# Base PATH
BASE_DIR = Path(__file__).resolve().parent.parent


# Security key
SECRET_KEY = os.getenv('SECRET_KEY', default=secrets.token_urlsafe(nbytes=64))


# Security developer
DEBUG = bool(int(os.getenv('DEBUG', '1')))


# Host indication
ALLOWED_HOSTS: list[str] = []


# Apps installed
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'app',
    'adminlte3',
    'bootstrap5',
]


# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Django rest-framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


# Url's base
ROOT_URLCONF = 'project.urls'
TEMPLATE_DIR = os.path.join(BASE_DIR, "base_templates")

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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


# Server productions
WSGI_APPLICATION = 'project.wsgi.application'

# Router Databases
# DATABASE_ROUTERS = ['path.to.MyRouter']

# Databases config
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DUSNEI_ENGINE', 'change-me'),
        'NAME': os.getenv('DUSNEI_DB', 'change-me'),
        'USER': os.getenv('DUSNEI_USER', 'change-me'),
        'PASSWORD': os.getenv('DUSNEI_PASSWORD', 'change-me'),
        'HOST': os.getenv('DUSNEI_HOST', 'change-me'),
        'PORT': os.getenv('DUSNEI_PORT', 'change-me'),
    },
    'dusnei_dev': {
        'ENGINE': os.getenv('DB_ENGINE', 'change-me'),
        'NAME': os.getenv('POSTGRES_DB', 'change-me'),
        'USER': os.getenv('POSTGRES_USER', 'change-me'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'change-me'),
        'HOST': os.getenv('POSTGRES_HOST', 'change-me'),
        'PORT': os.getenv('POSTGRES_PORT', 'change-me'),
    }
}


# Authentication password
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
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / 'base_static',
]


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from pathlib import Path
from dotenv import load_dotenv
import os


load_dotenv(override=True)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-e+w2hyyg2c)5ft07v=a@pw99o+jf0$s=i@wjw)79qnz02k33zn'

DEBUG = True

ALLOWED_HOSTS = []

SWAGGER_SETTINGS = {
    'DEFAULT_INFO': 'web_app.urls.swagger_info',
    'FORCE_SCRIPT_NAME': os.getenv("BACKEND_ADDR"),
    'DEFAULT_SERVER': os.getenv("DEFAULT_SERVER"),
}

CORS_ALLOWED_ORIGINS = ['http://localhost:8000', 'http://localhost:3000']
CORS_ORIGIN_WHITELIST = ('localhost:8000', 'localhost:3000')
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://localhost:3000']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web_app',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'main_app.urls'

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

WSGI_APPLICATION = 'main_app.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': os.getenv("POSTGRES_DBNAME"),
      'USER': os.getenv("POSTGRES_USER"),
      'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
      'HOST': os.getenv("POSTGRES_HOST"),
      'PORT': os.getenv("POSTGRES_PORT")
    }
}

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

VENV_PATH = os.path.dirname(BASE_DIR)
MEDIA_ROOT = os.path.join(VENV_PATH, BASE_DIR)
MEDIA_URL = '/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')
STATIC_URL = '/static/'

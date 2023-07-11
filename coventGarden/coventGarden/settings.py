"""
Django settings for coventGarden project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os


FIRST_DAY_OF_WEEK = 1

  
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t6xn!i_)c0l3g08x!c7hn(f0k^d3+j_91xjsyhtibbxuov$u-p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'studios',
    'django_select2',
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

ROOT_URLCONF = 'coventGarden.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'coventGarden.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'coventgarden',
#        'USER': 'admin',
#        'PASSWORD': 'admin123',
#        'HOST': 'localhost',
#        'PORT': '5432',
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

"""
New
"""
# Custom user
AUTH_USER_MODEL = "studios.CustomUser"

# Authentication
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# Forgot password
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"

# Store file
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = '/media/'

# Stripe
#STRIPE_PUBLIC_KEY = 'pk_live_51NQQVfLFsoxR8h1Y29pGzKczYrkurCqRbfCAASoFOko9Xq7hEtp9hSQQukZ0a1tSwiqsQ6x3at0xSTggVzBsDKT700xng7y7qK'
#STRIPE_SECRET_KEY = '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'

STRIPE_PUBLISHABLE_KEY = 'pk_test_51NQItyDSzBAtu4IYN48unJrRuxo4GrWvMznSyubCODHEWxzKjHiclGYKugjss127b0wK7UsyYNbOnyYxCtEBKit800SEvM0Mks'
STRIPE_SECRET_KEY = 'sk_test_51NQItyDSzBAtu4IYprr1y9hU8CqLinNb4779aYxd4qS3pYVikVwQmzmAYtjVeD5TSiQ0ngZAkHubTaDdPP8ceRcM00OUdfopPp'

PRODUCT_PRICE = 'price_1NQRh0LFsoxR8h1YJfhWjrxJ'
# PRODUCT_PRICE = 'price_1NQlqPLFsoxR8h1Y6DL1xPOL'
REDIRECT_DOMAIN = "home"

# ---------- Required ----------
# pip3 install django-select2
# pip3 install stripe
# pip3 install 
# ------------------------------
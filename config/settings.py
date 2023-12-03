"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from config.utils import get_database_config_variables

# Loads variables from .env
load_dotenv()
# Loads variables from .env.email, and possibly overwrites variables from .env
load_dotenv(".env.email")

# Get the value of the ENVIRONMENT environment variable, or use a default
# value of "development" if it's not set
ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")

# Set DEBUG based on the ENVIRONMENT value
# If ENVIRONMENT is "production", DEBUG is False
# If ENVIRONMENT is anything else, DEBUG is True
DEBUG = ENVIRONMENT != "production"


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    # List `accounts.apps.AccountsConfig` app first so the templates of
    # that app override the default ones in `django.contrib.admin`.
    "accounts.apps.AccountsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admindocs",
    "self_enquiry.apps.SelfEnquiryConfig",
    "vitals.apps.VitalsConfig",
    "app_tracker.apps.AppTrackerConfig",
    "cbt.apps.CbtConfig",
    "career_organizerator.apps.CareerOrganizeratorConfig",
    "pharma_tracker.apps.PharmaTrackerConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Email
# https://docs.djangoproject.com/en/4.0/topics/email/
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa E501
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

THE_SITE_NAME = "Personal Assistant"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


if ENVIRONMENT == "production":
    MIDDLEWARE = MIDDLEWARE + ["whitenoise.middleware.WhiteNoiseMiddleware"]
    database_config_variables = get_database_config_variables(
        os.environ.get("DATABASE_URL")
    )
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": database_config_variables["DATABASE_NAME"],
            "HOST": database_config_variables["DATABASE_HOST"],
            "PORT": database_config_variables["DATABASE_PORT"],
            "USER": database_config_variables["DATABASE_USER"],
            "PASSWORD": database_config_variables["DATABASE_PASSWORD"],
        }
    }
    ALLOWED_HOSTS = ["flynnt-knapp-8e0b83ab9b88.herokuapp.com"]
    SECRET_KEY = os.environ.get("SECRET_KEY")
    STATIC_ROOT = BASE_DIR / "staticfiles"
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    SECRET_KEY = "django-insecure-mm8cx0al6wo$$0hhv3&eevzsst9dbw&(5p$#9k(1rx%e@j+=$l"  # noqa E501

# To create a new `SECRET_KEY`:
"""
    python manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
"""
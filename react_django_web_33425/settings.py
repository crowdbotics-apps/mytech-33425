from pathlib import Path
import os
from pickle import TRUE
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env_file = os.path.join(BASE_DIR, ".env")
env = environ.Env()
env.read_env(env_file)

DEBUG = env.bool("DEBUG", default=False)

SECRET_KEY = env.str("SECRET_KEY")

ALLOWED_HOSTS = env.list("HOST", default=["*"])

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("SECURE_REDIRECT", default=False)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    # my apps
    'accounts',
    'store',
    'category',
    'cart',
    'orders',
    'api',
    'newsletter',
    'django_filters',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     #"whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

REST_FRAMEWORK = {
    
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ],
}

SESSION_EXPIRE_SECONDS = 900  # 15 minutes
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_TIMEOUT_REDIRECT = 'accounts/login'


ROOT_URLCONF = 'react_django_web_33425.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'category.context_processors.menu_links',
                'cart.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'react_django_web_33425.application'

AUTH_USER_MODEL ='accounts.Account'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


if env.str("DATABASE_URL", default=None):
    DATABASES = {"default": env.db()}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
# STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = 'store'
LOGOUT_REDIRECT_URL = 'store'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}



#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME", "")
AWS_STORAGE_REGION = env.str("AWS_STORAGE_REGION", "")

AWS_S3_CUSTOM_DOMAIN = env.str("AWS_S3_CUSTOM_DOMAIN", "")
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_DEFAULT_ACL = env.str("AWS_DEFAULT_ACL", "public-read")
AWS_MEDIA_LOCATION = env.str("AWS_MEDIA_LOCATION", "media")
AWS_AUTO_CREATE_BUCKET = env.bool("AWS_AUTO_CREATE_BUCKET", True)

# s3 public static settings
STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'react_django_web_33425.storage_backends.StaticStorage'
# s3 public media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = env.str(
    "DEFAULT_FILE_STORAGE", "react_django_web_33425.storage_backends.MediaStorage"
)

# s3 public media settings
# PUBLIC_MEDIA_LOCATION = 'media'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
# DEFAULT_FILE_STORAGE = env.str(
#     "DEFAULT_FILE_STORAGE", "react_django_web_33425.storage_backends.MediaStorage"
# )
# MEDIA_URL = '/mediafiles/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
# AWS_DEFAULT_ACL = None
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

# s3 static settings
# STATIC_LOCATION = 'static'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
# STATICFILES_STORAGE = 'react_django_web_33425.storage_backends.StaticStorage'
# STATICFILES_DIRS = (os.path.join(BASE_DIR, STATIC_LOCATION),)
# # s3 public media settings
# PUBLIC_MEDIA_LOCATION = 'media'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
# DEFAULT_FILE_STORAGE = 'react_django_web_33425.storage_backends.PublicMediaStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
                       'pathname=%(pathname)s lineno=%(lineno)s '
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

# for AWS Elastic Beanstalk Deploy

# After added DB credentials, while local venv is activated run python manage.py makemigrations

# Then git add -A and git commit

# In project root directory, create a folder called .ebextensions, inside it create a file called django.config and add

# option_settings:
  # aws:elasticbeanstalk:application:environment:
    # DJANGO_SETTINGS_MODULE: "mytech.settings"
    # PYTHONPATH: "/var/app/current:$PYTHONPATH"
  # aws:elasticbeanstalk:container:python:
    # WSGIPath: "mytech.wsgi:application"
# container_commands:
  # 01_migrate:
    # command: "source /var/app/venv/*/bin/activate && python3 manage.py migrate --noinput"
    # leader_only: true
  # 02_collectstatic:
    # command: "source /var/app/venv/*/bin/activate && python3 manage.py collectstatic --noinput"
    # leader_only: true

# Inside project directory, create a file storage_backends.py and add the following

# from django.conf import settings
# from storages.backends.s3boto3 import S3Boto3Storage

# class StaticStorage(S3Boto3Storage):
    # location = 'static'
    # default_acl = 'public-read'


# class PublicMediaStorage(S3Boto3Storage):
    # location = 'media'
    # default_acl = 'public-read'
    # file_overwrite = False
    
# In settings.py, add the following, to use additional S3 Bucket as staticfiles storage independently from the default 
# Elastic Beanstalk S3 bucket



"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import shutil

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hv_4y40dd1j)5g+s(h466w4&hbgqznvlz_+o^a01#wqqm+)mdl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mako_plus',
    'homepage',
    'account',
    'store',
    'portal',
    'adminportal',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_mako_plus.RequestInitMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)


DEFAULT_FROM_EMAIL = 'riffnotif@gmail.com'
SERVER_EMAIL = 'riffnotif@gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'riffnotif@gmail.com'
EMAIL_HOST_PASSWORD = 'pRimv6Y5SdEtsGJHj5S2'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'NAME': 'django_mako_plus',
        'BACKEND': 'django_mako_plus.MakoTemplates',
        'OPTIONS': {
            # see the DMP documentation, "configuration options" page for available options
            'CONTENT_PROVIDERS': [
                {   'provider': 'django_mako_plus.JsContextProvider' },
                {   'provider': 'django_mako_plus.CompileScssProvider',
                    'sourcepath': lambda p: os.path.join(p.app_config.name, 'styles', p.template_relpath + '.scss'),
                    'targetpath': lambda p: os.path.join(p.app_config.name, 'styles', p.template_relpath + '.scss.css'),
                    # if you need to override the default command:
                    #'command': lambda p: [ 'sass', f'--load-path="{BASE_DIR}"', p.sourcepath, p.targetpath ],
                },
                {   'provider': 'django_mako_plus.CssLinkProvider',
                    'filepath': lambda p: os.path.join(p.app_config.name, 'styles', p.template_relpath + '.scss.css'),
                },
                {   'provider': 'django_mako_plus.JsLinkProvider' },
            ],
        },
    },
    {
        'NAME': 'django',
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

WSGI_APPLICATION = 'mysite.wsgi.application'

AUTH_USER_MODEL = 'account.User'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# [START db_setup]
if os.getenv('GAE_APPLICATION', None):
#if(True):
    print("THIS ONE IS CONNECTING")
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': '/cloudsql/rifftideproject:us-central1:rifftidesite',
            'NAME': 'rifftidesitedata',
            'USER': 'isaacadmin',
            'PASSWORD': 'keepflyingtwentyseventeen',
        }
    }
else:
    # Running locally so connect to either a local MySQL instance or connect 
    # to Cloud SQL via the proxy.  To start the proxy via command line: 
    #    $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306 
    # See https://cloud.google.com/sql/docs/mysql-connect-proxy
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'rifftidesitedata',
            'USER': 'isaacadmin',
            'PASSWORD': 'keepflyingtwentyseventeen',
        }
    }
# [END db_setup]

SBCLIENTID = 'ARrw0jrQihOusmFX6Fto0okQj6c-4DvHbt901Rb_z37I4ViAHAjc4Yg5kKaNGpXIlfnALrlDSthlmnQM'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = 'https://storage.googleapis.com/rifftidesite-content/static/'

STATICFILES_DIRS = (
    # SECURITY WARNING: this next line must be commented out at deployment
    # BASE_DIR,
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# A logger for DMP
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG  # SECURITY WARNING: never set this True on a live site
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'dmp_simple': {
            'format': '%(levelname)s::DMP %(message)s'
        },
    },
    'handlers': {
        'dmp_console':{
            'class':'logging.StreamHandler',
            'formatter': 'dmp_simple'
        },
    },
    'loggers': {
        'django_mako_plus': {
            'handlers': ['dmp_console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

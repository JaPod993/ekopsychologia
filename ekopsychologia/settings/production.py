# -*- encoding: utf-8 -*-
from base import *

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

BASE_URL = 'https://.pl'

ADMINS = (('M.G.', 'cappuccio@silvercube.pl'), ('D.N.', 'dnowak@silvercube.pl'))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dev_ekopsychologia',
        'USER': 'devSC',
        'PASSWORD': 'scDeV12$',
        'HOST': '',
        'PORT': '',
    }
}

STATICFILES_FINDERS = ("django.contrib.staticfiles.finders.FileSystemFinder",
                       "django.contrib.staticfiles.finders.AppDirectoriesFinder",
                       "compressor.finders.CompressorFinder")

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.silvercube.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply@silvercube.pl'
EMAIL_HOST_PASSWORD = 'fUcUwAuE'
EMAIL_FROM_USER = 'AM2" <noreply@silvercube.pl>'
EMAIL_DEFAULT_SUBJECT = u"Formularz kontaktowy z serwisu WWW"
DEFAULT_FROM_EMAIL = EMAIL_FROM_USER
SERVER_EMAIL = EMAIL_HOST_USER



CORECMS_CONTACT_FORM_SUBJECT = "Wiadomość z serwisu www"
CORECMS_CONTACT_FORM_RECIPIENTS = ['noreply@silvercube.pl']


SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s [%(module)s %(funcName)s %(lineno)d] - %(message)s'
        },
        'extended': {
            'format': '%(asctime)s %(levelname)s [%(module)s]: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['null'],  # Quiet by default!
            'propagate': False,
            'level': 'DEBUG',
        },
    }
}

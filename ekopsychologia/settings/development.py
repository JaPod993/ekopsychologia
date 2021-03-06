# -*- encoding: utf-8 -*-
from base import *

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

BASE_URL = 'http://ekopsychologia.dev2.silvercube.pl'

ADMINS = (('M.G.', 'cappuccio@silvercube.pl'), ('D.N.', 'dnowak@silvercube.pl'))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dev_ekopsychologia2dj',
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
DEFAULT_FROM_EMAIL = "noreply@silvercube.pl"
SERVER_EMAIL = "noreply@silvercube.pl"


CORECMS_CONTACT_FORM_SUBJECT = u"Wiadomość z serwisu www"
CORECMS_CONTACT_FORM_RECIPIENTS = ['noreply@silvercube.pl']


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
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

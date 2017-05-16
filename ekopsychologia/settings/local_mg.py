# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']
BASE_URL = 'http://127.0.0.1:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ekopsychologia',
        'USER': 'mysql',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
    'oldbase': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ekopsychologia_php',
        'USER': 'mysql',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.silvercube.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply@silvercube.pl'
EMAIL_HOST_PASSWORD = 'fUcUwAuE'
EMAIL_FROM_USER = 'ECO <noreply@silvercube.pl>'

CORECMS_CONTACT_FORM_SUBJECT = u"Wiadomość z serwisu www"
CORECMS_CONTACT_FORM_RECIPIENTS = ['contact.form.ekopsychologia@supermailing.eu']


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
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, "logs/debug.log"),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'WARNING',
            'propagate': True,
        },
        'sorl.thumbnail': {
            'handlers': ['file', ],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INSTALLED_APPS = list(INSTALLED_APPS) + ['debug_toolbar',]

INTERNAL_IPS = ['127.0.0.1']

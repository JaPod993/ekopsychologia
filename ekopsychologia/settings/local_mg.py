# -*- encoding: utf-8 -*-
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']
BASE_URL = 'http://127.0.0.1:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ekopsychologia',
        'USER': 'root',
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

CORECMS_CONTACT_FORM_SUBJECT = "Wiadomość z serwisu www"
CORECMS_CONTACT_FORM_RECIPIENTS = ['contact.form.ekopsychologia@supermailing.eu']
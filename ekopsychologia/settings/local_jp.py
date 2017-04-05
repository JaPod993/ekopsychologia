# -*- encoding: utf-8 -*-
from base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

BASE_URL = "http://127.0.0.1:8000"

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
      'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ekopsychologia',
        'USER': 'labamba',
        'PASSWORD': 'obojetne',
        'HOST': '10.0.0.3',
        'PORT': '',
    }
}


#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.silvercube.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply@silvercube.pl'
EMAIL_HOST_PASSWORD = 'fUcUwAuE'
EMAIL_FROM_USER = 'AM2 <noreply@silvercube.pl>'

CORECMS_CONTACT_FORM_SUBJECT = "Wiadomość z serwisu www"
CORECMS_CONTACT_FORM_RECIPIENTS = ['contact.form.am2@supermailing.eu']
MEDIA_ROOT = '/home/janek/ekopsychologia/media'
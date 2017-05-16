# -*- encoding: utf-8 -*-
import os
import sys
import locale

from django.db.models import Q

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append(os.path.dirname(BASE_DIR))
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=41#sape7s5bot&j+m-7s+dh88(bs#jw@!a1k$=$7a#=@+e$uu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
THUMBNAIL_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'corecms.context_processors.add_translate_settings',
                'website.context_processors.default',
            ],
        },
    },
]


INSTALLED_APPS = (
    'override_app',
    'django_extensions',
    'materialtemplate',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'mptt',
    'taggit',
    'compressor',
    'widget_tweaks',
    'account',
    'corecms',
    'website',
    'cms',
    'blockslider',

)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corecms.middleware.TranslateMiddleware',
    'corecms.middleware.BreadcrumbsMiddleware',
]


ROOT_URLCONF = 'ekopsychologia.urls'

WSGI_APPLICATION = 'ekopsychologia.wsgi.application'

locale.setlocale(locale.LC_ALL, "pl_PL.UTF-8")

os.environ['LC_ALL'] = "pl_PL.UTF-8"

LANGUAGE_CODE = 'pl'
TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_L10N = False
USE_TZ = False

DATE_FORMAT = "d.m.Y"
DATETIME_FORMAT = "d.m.Y, H:i"

DATE_INPUT_FORMATS = (
    '%d.%m.%Y', '%d.%m.%y',  # '25.10.2006', '25.10.06'
    '%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y',  # '25-10-2006', '25/10/2006', '25/10/06'
    '%d %b %Y',  # '25 Oct 2006',
    '%d %B %Y',  # '25 October 2006',
)

DATETIME_INPUT_FORMATS = (
    '%d.%m.%Y %H:%M:%S',     # '2006.10.25 14:30:59'
    '%d.%m.%Y %H:%M',     # '2006.10.25 14:30'
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y',              # '10/25/2006'
    '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%m/%d/%y %H:%M',        # '10/25/06 14:30'
    '%m/%d/%y',              # '10/25/06'
)


MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
STATIC_URL = '/static/'



AUTH_USER_MODEL = 'account.User'

gettext = lambda s: s
LANGUAGES = (
    ('pl', u'Polski'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

#zastrzezone slugi
RESTRICTED_SLUGS = [
    'static', 'media', 'admin', 'i18n', 'login', 'logout', 'contact-form',
]

LOGIN_REDIRECT_URL = '/admin/'

LOGO_PATH = '/static/website/images/sercepogorza_logo_mini.svg'

CMS_PLUGINS = (
    {'name': 'form_generator', 'modules': None},
    {'name': 'gallery', 'modules': ('article', 'site')}
)

MATERIALTEMPLATE_CONFIG = {
    # 'MENU': (
    #     'sites',
    #     {'app': 'cms', 'models': ['article', 'site', 'textblock', 'menu', 'slider', 'tag']},
    #     {'label': u'Repozytorium plików', 'url': 'admin:cms_repositorymediafile_changelist', 'icon': 'md md-attach-file'},
    #     {'label': 'Konfiguracja', 'icon': 'md md-settings', 'models': [
    #         {'label': 'Ustawienia', 'url': 'admin:cms_configcms_changelist', 'icon': 'md md-settings'}
    #     ]},
    #
    #     {'app': 'account'},
    # ),
    'EXTRA_SCRIPTS': [
        STATIC_URL + 'corecms/js/lang.scripts.js'
    ],

    # misc
    # 'LIST_PER_PAGE': 15
}


SEARCH_SETTINGS = {
    'cms.Article': {'fields': ['identity', 'shortcut', 'content', 'slug'], 'template': 'website/site/element/article_list.html', 'filter': Q(status=1)},
    'cms.Site': {'fields': ['identity', 'slug', 'content'], 'template': 'website/site/element/article_list.html', 'filter': Q(status=1)},
}

THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.wand_engine.Engine'
THUMBNAIL_PRESERVE_FORMAT = True
THUMBNAIL_BACKEND = "corecms.sorlbackend.SEOThumbnailBackend"
THUMBNAIL_SEO_NAME = True

#ratio dla miniatur
BASE64_IMAGE_FIELD = {
    'corecms_article_thumbnail': {
        'ratio': '360:200'
    },
    'corecms_article_main_image': {
        'ratio': '1920:300'
    },
    'corecms_site_thumbnail': {
        'ratio': '360:200'
    },
    'corecms_site_main_image': {
        'ratio': '1920:300'
    },
}
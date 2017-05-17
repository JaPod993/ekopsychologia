# -*- encoding: utf-8 -*-
import sys
from shutil import copyfile

from corecms.forms.forms import get_slug_for_site_or_article
from corecms.models.gallery import Gallery
from django.core.files.uploadedfile import UploadedFile, SimpleUploadedFile
from django.core.management.base import BaseCommand
import os, errno
from django.core.files import File
from io import BytesIO
from PIL import Image
from django.template.defaultfilters import slugify
from unidecode import unidecode

from cms.models import Article, Site

reload(sys)
sys.setdefaultencoding("utf-8")


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        for a in Article.objects.filter(identity__contains='"'):
            slug = orig = slugify(unidecode(a.identity)[:200])
            a.slug = get_slug_for_site_or_article(a, slug, orig, 200)
            a.save()
            print a.slug

        for a in Site.objects.filter(identity__contains='"'):
            slug = orig = slugify(unidecode(a.identity)[:200])
            a.slug = get_slug_for_site_or_article(a, slug, orig, 200)
            a.save()
            print a.slug

# -*- encoding: utf-8 -*-
import sys
from shutil import copyfile

from corecms.models.gallery import Gallery
from django.core.files.uploadedfile import UploadedFile, SimpleUploadedFile
from django.core.management.base import BaseCommand
import os, errno
from django.core.files import File
from io import BytesIO
from PIL import Image

reload(sys)
sys.setdefaultencoding("utf-8")


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        for gallery in Gallery.objects.all():
            if gallery.images.count() == 0:
                print gallery
                gallery.delete()
# -*- encoding: utf-8 -*-
from shutil import copyfile

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
        file_name = "/home/cappuccio/Workspace/ekopsychologia2/media/temp/tmpt_7r06fu.jpeg"
        file_name = "/home/cappuccio/Workspace/ekopsychologia2/media/temp/1-ptak.jpeg"
        #file_name = "/home/cappuccio/Workspace/ekopsychologia2/media/temp/imageToSave.jpg"
        file_handle2 = File(open(file_name, 'rb'))

        file_handle = SimpleUploadedFile('x.jpeg', file_handle2.read())
        #UploadedFile(open(tmp_file.name, 'rb'))


        print(file_handle.size)

        file_bytes = BytesIO(file_handle.read())


        image = Image.open(file_bytes)
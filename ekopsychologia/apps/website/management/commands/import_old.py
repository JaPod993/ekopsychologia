# -*- encoding: utf-8 -*-
from __future__ import unicode_literals


import hashlib
from pprint import pprint

from django.core.files.base import File

from corecms.forms.forms import get_slug_for_site_or_article
from corecms.models.connector import Connector
from corecms.models.gallery import Gallery
from django.contrib.contenttypes.models import ContentType
import os
from urlparse import urlparse, urljoin

import uuid
#from html.parser import HTMLParser
from HTMLParser import HTMLParser
import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from django.conf import settings

from django.template.defaultfilters import slugify, truncatewords
from shutil import copyfile


from unidecode import unidecode
from django.db import connections
from django.db import transaction
from cms.models import Site, Article, RelationArticleSite, MediaFile, IsSite
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

User = get_user_model()


logger = logging.getLogger('oirp.importer')


def dictfetone(cursor):

    desc = cursor.description
    one = cursor.fetchone()
    if one:
        return dict(zip([col[0] for col in desc], one))
    return None


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


if os.environ['DJANGO_SETTINGS_MODULE'] == 'settings.production':
    def get_old_path(old_path):
        return os.path.join(settings.MEDIA_ROOT, 'old' + old_path.lstrip("\.\/"))
else:
    def get_old_path(old_path):
        return os.path.join(os.path.dirname(settings.MEDIA_ROOT), old_path.lstrip("\.\/"))


#nadpisuje tresci, connetcory, pliki itp artykułów nawet jesli sa juz w bazie, jesli false to w starych nic nie zmienia
OVERRIDE_IF_EXIST = True

#wszystkie arty z tej strony i podkategori laduja do tej strony
MODE_ALL_TO_PARENT = 'all-to-parent'

SITES = []

#act - akt prawny

#lista kategorii do zaimportowania
SITE_MATCH = {
    # 7: {'slug': 'akty-prawne', 'mode': MODE_ALL_TO_PARENT, 'act': True},
    # 25: {'slug': 'komunikaty-i-ogloszenia-dla-radcow'},
    # 28: {'slug': 'doskonalenie-zawodowe'},
    # 153: {'slug': 'szkolenia'},
    # 154: {'slug': 'inne-szkolenia'},
    # 122: {'slug': 'obowiazki-zawodowe', 'mode': MODE_ALL_TO_PARENT },
    # 123: {'slug': 'turystyka-i-kultura'},
    # 2071: {'slug': 'urzedowki'},
    # 1494: {'slug': 'wykaz-lekarzy-sadowych'},
    # 124: {'slug': 'harmonogram-konsultacji'},
    # 402: {'slug': 'klub-seniora'},
    # 1892: {'slug': 'przeszukanie-kancelarii-radcy-prawnego'},
    # 14: {'slug': 'komunikaty-i-ogloszenia-dla-aplikantow'},
    #
    # 210: {'slug': 'lex-oferta-dla-aplikanta'},
    # 125: {'slug': 'nabor-na-aplikacje'},
    # 134: {'slug': 'wpis-na-liste-radcow-prawnych'},
    # 135: {'slug': 'wpis-na-liste-prawnikow-zagranicznych'},
    # 1206: {'slug': 'dam-prace'},
    # 2006: {'slug': 'radca-szuka-pracy'},
    # 3434: {'slug': 'radca-szuka-wspolnika'},
    # 2007: {'slug': 'aplikant-szuka-pracy'},
    # 2766: {'slug': 'mediacje'},
    # 2008: {'slug': 'podejme-sie-zastepstwa-procesowego'},
    # 2009: {'slug': 'szukam-zastepstwa-procesowego'},
    # 1451: {'slug': 'lokale'},

    # 28: {'slug': 'doskonalenie-zawodowe'},
    # 153: {'slug': 'szkolenia'},
    # 3728: {'slug': 'inne-szkolenia'},
    # 154: {'slug': 'objete-patronatem-rady'},
    # 3729: {'slug': 'uniwersyteckie'},
    # 1146: {'slug': 'materialy-ze-szkolen'},

    # 17: {'slug': 'i-rok'},
    # 18: {'slug': 'ii-rok'},
    # 19: {'slug': 'iii-rok'},

    128: {'slug': 'egzamin-radcowski'},
}


class Command(BaseCommand):
    args = ''
    help = ''
    cursor = None

    def reset_site(self):
        print("Delete all article")
        for a in Article.objects.all():
            a.delete()

    def get_files(self, parent_id):
        self.cursor.execute("SELECT *  FROM `CONNECTORS` WHERE `PARENT_ID` = %s AND PARENT_NAME = 'Site' AND OBJECT_NAME = 'File'" % parent_id)
        files_id = {str(x['OBJECT_ID']): x['DESCRIPTION'] for x in dictfetchall(self.cursor)}
        if len(files_id) == 0:
            return []
        self.cursor.execute("SELECT * FROM FILES AS s JOIN FILES_lang AS sl ON s.id = sl.id_main_table WHERE id IN (%s) AND language = 'pl'" % ', '.join(files_id.keys()))
        rtn = dictfetchall(self.cursor)
        for f in rtn:
            f['kind'] = files_id[str(f['id'])]
        return rtn

    def get_images(self, parent_id):
        rtn = []
        self.cursor.execute("SELECT *  FROM `CONNECTORS` WHERE `PARENT_ID` = %s AND PARENT_NAME = 'Site' AND OBJECT_NAME = 'JP_Image' ORDER BY POSITION_PARENT DESC" % parent_id)
        for connector in dictfetchall(self.cursor):
            self.cursor.execute("SELECT * FROM IMAGES AS s JOIN IMAGES_lang AS sl ON s.id = sl.id_main_table WHERE id = %s AND language = 'pl'" % connector['OBJECT_ID'])
            image = dictfetone(self.cursor)
            image['main'] = connector['DESCRIPTION'] == "main"
            rtn.append(image)
        return rtn

    def get_galleries(self, parent_id):
        self.cursor.execute("SELECT *  FROM `CONNECTORS` WHERE `PARENT_ID` = %s AND PARENT_NAME = 'Site' AND OBJECT_NAME = 'Gallery'" % parent_id)
        galleries_id = [str(x['OBJECT_ID']) for x in dictfetchall(self.cursor)]

        if len(galleries_id) == 0:
            return []
        self.cursor.execute("SELECT * FROM GALLERIES AS s JOIN GALLERIES_lang AS sl ON s.id = sl.id_main_table WHERE id IN (%s) AND language = 'pl'" % ', '.join(galleries_id))
        rtn = []
        for gallery in dictfetchall(self.cursor):
            self.cursor.execute("SELECT *  FROM `CONNECTORS` WHERE `PARENT_ID` = %s AND PARENT_NAME = 'Gallery' AND OBJECT_NAME = 'JP_Image'" % gallery['id'])
            images_id = [str(x['OBJECT_ID']) for x in dictfetchall(self.cursor)]
            if len(images_id) == 0:
                rtn.append((gallery, []))
            else:
                self.cursor.execute("SELECT * FROM IMAGES AS s JOIN IMAGES_lang AS sl ON s.id = sl.id_main_table WHERE id IN (%s) AND language = 'pl'" % ', '.join(images_id))
                images = dictfetchall(self.cursor)
                rtn.append((gallery, images))
        return rtn

    def count_children(self, parent_id):
        self.cursor.execute("SELECT count(id) as counter FROM  SITES AS s JOIN SITES_lang AS sl ON s.id = sl.id_main_table WHERE status >=0 AND parent=%s AND language = 'pl'" % parent_id)
        return self.cursor.fetchone()[0]

    def get_children(self, parent_id):
        self.cursor.execute("SELECT * FROM SITES AS s JOIN SITES_lang AS sl ON s.id = sl.id_main_table WHERE status >=0 AND parent=%s AND language = 'pl'" % parent_id)
        return dictfetchall(self.cursor)

    def import_objects(self, objects, parent=None, archived=False, act=False, import_to_parent=False):

        html_parser = HTMLParser()

        i = 1
        for row in objects:
            with transaction.atomic():

                if parent:
                    print(int(row['id']), "[{0}]".format(parent), row['title'])
                else:
                    print(int(row['id']), row['title'])
                #print("-- item %s" % truncatewords(row['title'], 5), row['id']
                slug = orig = slugify(unidecode(row['title']))[:255]

                if parent and parent.identity == "Aktualności":
                    is_site = False
                else:
                    try:
                        is_site = IsSite.objects.get(cms_id=row['id']).is_site
                    except IsSite.DoesNotExist:
                        var = raw_input(u"Site ? {0}: ".format(row['title']).encode('utf-8'))
                        var = var or None
                        is_site = var == "1"
                        IsSite.objects.create(cms_id=row['id'], is_site=is_site)

                #jesli jest w tabelce kategorii lub posiada dzieci
                if is_site:
                    #jest to kategoria z SITE_MATCH
                    slug = get_slug_for_site_or_article(Site, slug, orig, 255)
                    obj, created = Site.objects.get_or_create(old_cms_id=row['id'],
                                                              defaults={'identity': html_parser.unescape(row['title']),
                                                                        'order': 1,
                                                                        }
                                                              )

                    if created:
                        print('Utworzono SITE w nowej strukturze: {0}'.format(obj))
                    else:
                        pass

                    if parent and obj.parent is None:
                        obj.parent = parent
                        obj.save()


                else:
                    #nie ma dzieci wiec zakładam ze jest to artykuł wiec importuje
                    slug = get_slug_for_site_or_article(Article, slug, orig, 255)
                    obj, created = Article.objects.get_or_create(old_cms_id=row['id'],
                                                                 defaults=dict(
                                                                     identity=html_parser.unescape(row['title']),
                                                                     slug=slug,
                                                                     article_date=row['createDate'])
                                                                 )

                    if created:
                        print('Utworzono Article w nowej strukturze: {0}'.format(obj))
                    else:
                        pass

                    if parent:
                        RelationArticleSite.objects.get_or_create(child=obj, parent=parent, defaults=dict(main=True, position=0))

                url_paths = []

                #print("----------- Nowy (%s)" % 'utworzyłem' if created else "jest juz utworzony"

                if created or OVERRIDE_IF_EXIST:
                    obj.shortcut = row['shortcut']
                    obj.content = row['content']
                    obj.status = Article.STATUS_PUBLISHED if row['status'] == 2 else Article.STATUS_HIDDEN
                    obj.save()

                    # usuniecie juz podłaczonych
                    for f in obj.files:
                        f.delete()
                    # dodanie plików
                    for frow in self.get_files(row['id']):
                        old_path = get_old_path(frow['fileSource'])
                        if os.path.exists(old_path):
                            target_dir = obj.get_file_save_directory(settings.MEDIA_ROOT)
                            upload_name = "_".join([uuid.uuid4().hex, frow['originalName']])
                            path = os.path.join(target_dir, upload_name)
                            if not os.path.exists(target_dir):
                                os.makedirs(target_dir, 0o755)
                            copyfile(old_path, path)
                            file_object = MediaFile()
                            file_object.title = frow['name']
                            file_object.name = frow['originalName']
                            file_object.path = path
                            if frow['kind'] == '1':
                                file_object.distinction.downloadable = True
                            file_object.content_object = obj
                            file_object.save()
                            url_paths.append((frow['fileSource'].lstrip("\."), urljoin(settings.MEDIA_URL, file_object.path)))
                            print("Import pliku: %s" % old_path)
                        else:
                            print("ERROR: brak pliku: %s" % old_path)

                    # usuniecie galerii
                    gallery_ct = ContentType.objects.get_for_model(Gallery)
                    for connector in obj.connector_children.filter(children_type=gallery_ct):
                        connector.children.delete()

                    images = self.get_images(row['id'])

                    if images:
                        obj_gallery = Gallery()
                        obj_gallery.name = obj.identity
                        obj_gallery.save()
                        connector = Connector()
                        connector.parent = obj
                        connector.children = obj_gallery
                        connector.save()
                        i = 0
                        for frow in images:
                            old_path = get_old_path(frow['fileSource'])
                            if os.path.exists(old_path):
                                if frow['main']:
                                    image_name = os.path.basename(old_path)
                                    with open(old_path, 'rb') as f:
                                        obj.thumbnail.save(image_name, File(f), save=True)
                                    continue
                                target_dir = obj_gallery.get_file_save_directory(settings.MEDIA_ROOT)
                                upload_name = "_".join([uuid.uuid4().hex, frow['originalName']])
                                path = os.path.join(target_dir, upload_name)
                                if not os.path.exists(target_dir):
                                    os.makedirs(target_dir, 0o755)
                                copyfile(old_path, path)
                                file_object = MediaFile()
                                file_object.title = frow['name']
                                file_object.name = frow['originalName']
                                file_object.path = path
                                # if frow['kind'] == 'file.download':
                                #     file_object.distinction.downloadable = True
                                file_object.content_object = obj
                                file_object.save()
                                file_object.__class__.objects.filter(pk=file_object.pk).update(position=i)
                                obj_gallery.images.add(file_object)
                                #print("Import pliku: %s" % old_path
                                i += 1
                            else:
                                print("ERROR: brak pliku: %s" % old_path)

                    # dodanie galerii
                    # for gallery, images in self.get_galleries(row['id']):
                    #     obj_gallery = Gallery.objects.create(name=gallery['NAME'])
                    #     connector = Connector.objects.create(parent=obj, children=obj_gallery)
                    #
                    #     for frow in images:
                    #         old_path = get_old_path(frow['fileSource'])
                    #         if os.path.exists(old_path):
                    #             target_dir = obj_gallery.get_file_save_directory(settings.MEDIA_ROOT)
                    #             upload_name = "_".join([uuid.uuid4().hex, frow['originalName']])
                    #             path = os.path.join(target_dir, upload_name)
                    #             if not os.path.exists(target_dir):
                    #                 os.makedirs(target_dir, 0o755)
                    #             copyfile(old_path, path)
                    #             file_object = MediaFile()
                    #             file_object.title = frow['name']
                    #             file_object.name = frow['originalName']
                    #             file_object.path = path
                    #             if frow['kind'] == 'file.download':
                    #                 file_object.distinction.downloadable = True
                    #             file_object.content_object = obj
                    #             file_object.save()
                    #             obj_gallery.images.add(file_object)
                    #             #print("Import pliku: %s" % old_path
                    #         else:
                    #             print("ERROR: brak pliku: %s" % old_path)

                    #poprawienie sciezek do plików w treści
                    if len(url_paths) > 0:
                        for url_path in url_paths:
                            if hasattr(obj, 'shortcut'):
                                obj.shortcut = html_parser.unescape(obj.shortcut.replace(url_path[0], url_path[1]))
                            obj.content = html_parser.unescape(obj.content.replace(url_path[0], url_path[1]))

            if isinstance(obj, Site):
                objects = self.get_children(row['id'])
                self.import_objects(objects, obj)
            i += 1


                # if i > 5:
                #     break

        print('--------------------------------------')

    def import_content(self):
        self.cursor.execute("SELECT * FROM  SITES AS s JOIN SITES_lang AS sl ON s.id = sl.id_main_table WHERE status >=0 AND parent=0 AND language = 'pl'")
        #self.cursor.execute("SELECT * FROM  SITES AS s JOIN SITES_lang AS sl ON s.id = sl.id_main_table WHERE status >=0 AND language = 'pl' AND s.id=209")
        self.import_objects(dictfetchall(self.cursor))


    def handle(self, *args, **options):
        self.cursor = connections['oldbase'].cursor()
        #self.reset_site()
        self.import_content()
        self.set_news()


    def set_news(self):
        projekty_site = Site.objects.get(old_cms_id=4)
        parent = Site.objects.get(identity="Aktualności", parent=None)

        for article in Article.objects.filter(sites__in=projekty_site.get_descendants().filter(identity="Aktualności")):
            RelationArticleSite.objects.get_or_create(child=article, parent=parent, defaults=dict(main=False, position=0))


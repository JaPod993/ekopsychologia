# -*- encoding: utf-8 -*-
from shutil import copyfile
from django.core.management.base import BaseCommand
import os, errno
from cms.models import Site
from corecms.models.default.models import Menu
from corecms.models.menu import RelationMenuSite


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):

        sites = []

        sites_menu_top = [u"Strona główna", u"O nas", u"Projekty", u"Aktualności", u"Współpraca", u"Publikacje",
                          u"Galeria", u"Kontakt",]

        menu_top, created = Menu.objects.get_or_create(slug="menu-top", defaults={'name': u'Menu górne'})
        menu_bottom, created = Menu.objects.get_or_create(slug="menu-bottom", defaults={'name': u'Menu dolne'})

        old_cms_sites = [2L, 4L, 3L, 29L, 5L, 16L]

        for site in Site.objects.filter(old_cms_id__in=old_cms_sites).all():
            RelationMenuSite.objects.get_or_create(parent=menu_top, child=site)
            RelationMenuSite.objects.get_or_create(parent=menu_bottom, child=site)

        # for site_name in sites:
        #     site, created = Site.objects.get_or_create(identity=site_name, defaults={'status': Site.STATUS_PUBLISHED})
        #     RelationMenuSite.objects.get_or_create(parent=menu_top, child=site)
        #     print(site, site.slug)

        # sliders = [
        #     (u'Slide 1', u'Lorem iam eu arcu lacinia interdum. Praesent consectetur iaculis leo eget fermentum.'),
        #     (u'Slide 2', u'Nunc mollis malesuada ornare. Ut faucibus libero magna, eu posuere nibh ornare quis. Praesent consectetur euismod bibendum.'),
        #     (u'Slide 3', u'Etiam congue, dolor iaculis elementum iaculis, dolor tortor interdum neque, a suscipit augue neque auctor arcu.'),
        # ]
        #
        # slider_home, created = Slider.objects.get_or_create(slug='home-top', defaults={'name': u'Strona główna góra'})
        #
        # for slide_name, slide_text in sliders:
        #     SliderRow.objects.get_or_create(name=slide_name, parent=slider_home, defaults={'text': slide_text})


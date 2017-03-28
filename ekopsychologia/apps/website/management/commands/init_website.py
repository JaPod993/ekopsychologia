# -*- encoding: utf-8 -*-
from shutil import copyfile
from django.core.management.base import BaseCommand
import os, errno
from cms.models import Site
from corecms.models.menu import Menu, RelationMenuSite
from corecms.models.slider import Slider, SliderRow


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):

        sites = [u"O nas", u"Aktualności", u"Kompedium wiedzy o akustyce", u"Wpływ na ludzi",
                    u"Przepisy", u"Sposoby poprawy", u"Dla prasy", u"Kontakt",]

        menu_top, created = Menu.objects.get_or_create(slug="menu-top", defaults={'name': u'Menu górne'})
        menu_bottom, created = Menu.objects.get_or_create(slug="menu-bottom", defaults={'name': u'Menu dolne'})

        for site_name in sites:
            site, created = Site.objects.get_or_create(identity=site_name, defaults={'status': Site.STATUS_PUBLISHED})
            RelationMenuSite.objects.get_or_create(parent=menu_top, child=site)
            print site, site.slug

        sliders = [
            (u'Slide 1', u'Lorem iam eu arcu lacinia interdum. Praesent consectetur iaculis leo eget fermentum.'),
            (u'Slide 2', u'Nunc mollis malesuada ornare. Ut faucibus libero magna, eu posuere nibh ornare quis. Praesent consectetur euismod bibendum.'),
            (u'Slide 3', u'Etiam congue, dolor iaculis elementum iaculis, dolor tortor interdum neque, a suscipit augue neque auctor arcu.'),
        ]

        slider_home, created = Slider.objects.get_or_create(slug='home-top', defaults={'name': u'Strona główna góra'})

        for slide_name, slide_text in sliders:
            SliderRow.objects.get_or_create(name=slide_name, parent=slider_home, defaults={'text': slide_text})


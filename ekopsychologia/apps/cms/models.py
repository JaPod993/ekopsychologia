# -*- encoding: utf-8 -*-
from corecms.models.base_element import BaseElement
from corecms.models.config import ConfigCMSAbstract
from django.db import models
from positions.fields import PositionField
from corecms.models.site import SiteAbstract
from corecms.models.article import ArticleAbstract
from corecms.models.text_block import TextBlockAbstract
from corecms.models.media_file import AbstractMediaFile


class Site(SiteAbstract):

    old_cms_id = models.IntegerField(null=True, default=None)
    logo = models.ImageField("Logo", upload_to="site/images/", default=None, null=True, blank=True)
    execution_time = models.CharField(u"Czas realizacji", max_length=255, default="", blank=True)
    budget = models.CharField(u"Budżet całkowity", max_length=255, default="", blank=True)
    areas = models.ManyToManyField('self', verbose_name="Obszary działania", blank=True, related_name="+")
    url = models.URLField(u"Link", default="", blank=True)
    archived = models.BooleanField(u"Projekt archiwalny", default=False, blank=True)

    class Meta(SiteAbstract.Meta):
        abstract = False
        app_label = 'cms'

    @staticmethod
    def get_template_list():
        return [
            ('website/site/templates/site_obszary_dzialalnosci.html', u'Obszary działania (lista)'),
            ('website/site/templates/site_obszar.html', u'Obszar działania'),
            ('website/site/templates/site_contact.html', u'Kontakt'),
            ('website/site/templates/site_partnership.html', u'Wspolpraca'),
            ('website/site/templates/site_publication.html', u'Publikacje'),
            ('corecms/site/templates/articles_list_layout.html', u'Aktualności - lista'),

    ]

    def allow_redirect_to_children(self):
        if self.template == 'website/site/templates/site_obszary_dzialalnosci.html':
            return False
        return True

    def show_in_menu(self):
        if self.level < 2:
            return True
        return False


class Article(ArticleAbstract):
    alternative_url = models.CharField(u"Link alternatywny", max_length=255, default="", blank=True, help_text="Link na który bedzie wskazywała ten artykuł")
    old_cms_id = models.IntegerField(null=True, default=None)
    areas = models.ManyToManyField('cms.Site', verbose_name="Obszary działania", blank=True, related_name="+")

    class Meta(ArticleAbstract.Meta):
        app_label = 'cms'

    def get_absolute_url(self, category=None):
        if self.alternative_url != "":
            return self.alternative_url
        return super(Article, self).get_absolute_url(category)


class TextBlock(TextBlockAbstract):
    class Meta(TextBlockAbstract.Meta):
        app_label = 'cms'


class RelationArticleSite(models.Model):
    child = models.ForeignKey('cms.Article')
    parent = models.ForeignKey('cms.Site')
    position = PositionField(collection='parent')
    main = models.BooleanField(default=False)

    class Meta:
        app_label = 'cms'
        ordering = ['-id']
        unique_together = ("child", "parent")


class MediaFile(AbstractMediaFile):
    class Meta(AbstractMediaFile.Meta):
        abstract = False
        app_label = 'cms'


class ConfigCMS(ConfigCMSAbstract):

    events = models.IntegerField(verbose_name=u'Ilość wydarzeń', default=0) # 370
    participants = models.IntegerField(verbose_name=u'Uczestnicy', default=0) # 15000
    institutions = models.IntegerField(verbose_name=u'Inistytucji w Porozumieniu Karpackim', default=0) # 70
    experts = models.IntegerField(verbose_name=u'Ekspertów', default=0) # 300
    founds = models.IntegerField(verbose_name=u'Milionów złotych pozyskanych na działania', default=0) # 5
    projects = models.IntegerField(verbose_name=u'Zrealizowane Projekty', default=0) # 22

    class Meta(ConfigCMSAbstract.Meta):
        abstract = False
        app_label = 'cms'


class IsSite(models.Model):

    cms_id = models.IntegerField()
    is_site = models.BooleanField(default=False)

    class Meta():
        app_label = 'cms'


class GalleryDistinction(models.Model):

    gallery = models.ForeignKey('cms.Gallery')
    in_global = models.BooleanField(default=False)

    class Meta:
        app_label = 'cms'


class Founder(models.Model):
    site = models.ForeignKey(u"cms.Site")
    name = models.CharField(u"Nazwa", max_length=255)
    logo = models.ImageField("Logo", upload_to="site/founder/images/")
    url = models.URLField(u"Link", default="", blank=True)

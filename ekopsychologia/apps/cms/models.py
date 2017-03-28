# -*- encoding: utf-8 -*-
from corecms.models.config import ConfigCMSAbstract
from django.db import models
from positions.fields import PositionField
from corecms.models.site import SiteAbstract
from corecms.models.article import ArticleAbstract
from corecms.models.text_block import TextBlockAbstract
from corecms.models.media_file import AbstractMediaFile


class Site(SiteAbstract):
    class Meta(SiteAbstract.Meta):
        abstract = False
        app_label = 'cms'

    @staticmethod
    def get_template_list():
        return [('website/site/kontakt.html', u'Kontakt'), ('website/site/faq.html', u'FAQ'), ('website/site/akustyka.html', u'Akustyka')
                ]


class Article(ArticleAbstract):
    alternative_url = models.CharField(u"Link alternatywny", max_length=255, default="", blank=True, help_text="Link na który bedzie wskazywała ten artykuł")

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
    class Meta(ConfigCMSAbstract.Meta):
        abstract = False
        app_label = 'cms'

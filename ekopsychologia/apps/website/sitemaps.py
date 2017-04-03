# coding=utf-8

from django.contrib.sitemaps import Sitemap
from urlparse import urlparse

from cms.models import Article, Site


class EcophonSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def location(self, obj):
        url = obj.get_absolute_url()
        parsed_uri = urlparse(url)
        return parsed_uri.path

    def items(self):
        return Article.objects.filter(status=Article.STATUS_PUBLISHED)

    def lastmod(self, obj):
        return obj.updated_at


class EcophonSitesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def location(self, obj):
        url = obj.get_absolute_url()
        parsed_uri = urlparse(url)
        return parsed_uri.path

    def items(self):
        return Site.objects.filter(status=Article.STATUS_PUBLISHED)

    def lastmod(self, obj):
        return obj.updated_at

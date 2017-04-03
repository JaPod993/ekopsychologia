# -*- encoding: utf-8 -*-
from django.conf.urls import  url
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from website.sitemaps import EcophonSitemap
from website.sitemaps import EcophonSitesSitemap
from ..views.site import HomepageView
sitemaps = {
    'Articles': EcophonSitemap(),
    'Sites': EcophonSitesSitemap(),
}
urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='website.index'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

# -*- encoding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import FormView
from django.views.generic.base import TemplateView, View
from cms.models import Site, Article
from corecms.models.default.slider import Slider
from corecms.models.gallery import Gallery


class HomepageView(TemplateView):
    template_name = 'website/site/homepage.html'

    def _get_site_by_slug(self, slug):
        try:
            return Site.objects.published().get(slug=slug)
        except Site.DoesNotExist:
            return None

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        #context['sites'] = Site.objects.published().all()
        context['homepage_onas'] = self._get_site_by_slug("o-nas")
        context['homepage_projekty'] = self._get_site_by_slug("projekty")
        if context['homepage_projekty']:
            context['homepage_projekty_list'] = context['homepage_projekty'].children.published()[:8]
        context['homepage_aktualnosci'] = self._get_site_by_slug("aktualnosci")
        if context['homepage_aktualnosci']:
            context['homepage_aktualnosci_list'] = context['homepage_aktualnosci'].articles.filter(for_lang=True).published()[:3]
        context['homepage_publikacje'] = self._get_site_by_slug("publikacje")
        if context['homepage_publikacje']:
            context['homepage_publikacje_list'] = []
            for item in context['homepage_publikacje'].articles.filter(for_lang=True).published()[:12]:
                file = item.all_files.filter(publish=True).first()
                context['homepage_publikacje_list'].append((item, file))

        context['partnership_slider_list'] = Slider.objects.filter(slug__in=["fundatorzy", "partnerzy", "patroni", "media", "partnerzy-biznesowi"])

        context['homepage_site'] = Site.objects.get_or_create(slug="strona-glowna",
                                                             defaults=dict(identity="Strona główna",
                                                                           identity_pl="Strona główna"))[0]
        gallery_ct = ContentType.objects.get_for_model(Gallery)
        context['homepage_gallery'] = context['homepage_site'].connector_children.filter(children_type=gallery_ct).first()
        return context



# -*- encoding: utf-8 -*-
from corecms.models.gallery import Gallery
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import FormView
from django.views.generic.base import TemplateView, View
from cms.models import Site, Article

from blockslider.models import BlockSlider


class HomepageView(TemplateView):
    template_name = 'website/site/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['blocks'] = BlockSlider.objects.filter(visible=True).order_by('order')
        context['articles'] = Article.objects.published().all()[:3]
        context['homepage_site'] = Site.objects.get_or_create(slug="strona-glowna",
                                                            defaults=dict(identity="Strona główna",identity_pl="Strona główna"))[0]

        gallery_ct = ContentType.objects.get_for_model(Gallery)
        context['homepage_gallery'] = context['homepage_site'].connector_children.filter(children_type=gallery_ct).first()
        print context['homepage_gallery']
        return context



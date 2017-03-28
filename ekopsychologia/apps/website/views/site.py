# -*- encoding: utf-8 -*-
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import FormView
from django.views.generic.base import TemplateView, View
from cms.models import Site, Article


class HomepageView(TemplateView):
    template_name = 'website/site/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        #context['sites'] = Site.objects.published().all()
        return context



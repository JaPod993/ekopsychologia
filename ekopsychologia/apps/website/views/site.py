# -*- encoding: utf-8 -*-
from corecms.views.site import ContentItemDetailView as BaseContentItemDetailView, RedirectException
from django.contrib.contenttypes.models import ContentType
from django.http.response import JsonResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from cms.models import Site, Article
from corecms.models.default.slider import Slider
from corecms.models.gallery import Gallery

from blockslider.models import BlockSlider
from website.forms import NewsletterSignForm


class HomepageView(TemplateView):
    template_name = 'website/site/homepage.html'

    def _get_site_by_slug(self, slug):
        try:
            return Site.objects.published().get(slug=slug)
        except Site.DoesNotExist:
            return None

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)

        context['blocks'] = BlockSlider.objects.filter(visible=True).order_by('order')
        context['homepage_onas'] = self._get_site_by_slug("o-nas")
        context['homepage_projekty'] = self._get_site_by_slug("projekty")
        if context['homepage_projekty']:
            context['homepage_projekty_list'] = context['homepage_projekty'].children.published()
        context['homepage_aktualnosci'] = self._get_site_by_slug("aktualnosci")
        if context['homepage_aktualnosci']:
            context['homepage_aktualnosci_list'] = context['homepage_aktualnosci'].articles.filter(for_lang=True).published()[:3]
        context['homepage_publikacje'] = self._get_site_by_slug("publikacje")
        if context['homepage_publikacje']:
            context['homepage_publikacje_list'] = []
            for item in context['homepage_publikacje'].articles.filter(for_lang=True).published():
                file_item = item.all_files.filter(publish=True).first()
                if file_item and file_item.is_pdf():
                    context['homepage_publikacje_list'].append((item, file_item))
            context['homepage_publikacje_list'] = context['homepage_publikacje_list'][:24]

        context['homepage_partnership'] = self._get_site_by_slug("wspolpraca")
        context['partnership_slider_list'] = Slider.objects.filter(slug__in=["fundatorzy", "partnerzy", "patroni", "media", "partnerzy-biznesowi"])

        context['homepage_site'] = Site.objects.get_or_create(slug="strona-glowna",
                                                              defaults=dict(identity="Strona główna",
                                                                            identity_pl="Strona główna"))[0]
        gallery_ct = ContentType.objects.get_for_model(Gallery)
        context['homepage_gallery'] = context['homepage_site'].connector_children.filter(children_type=gallery_ct).first()
        return context


class NewsletterSignView(FormView):
    http_method_names = ["post"]
    form_class = NewsletterSignForm

    def form_invalid(self, form):
        error_email = dict(form.errors.items()).get('email')
        response = {
            "status": "NOK",
            "error": " ".join(error_email) if error_email else "Podany email jest niepoprawny"
        }
        return JsonResponse(response)

    def form_valid(self, form):
        form.save()
        response = {
            "status": "OK",
            "success": "Zostałeś zapisany do newslettera"
        }
        return JsonResponse(response)


class GalleryListView(ListView):
    model = Gallery
    template_name = "website/site/gallery.html"
    paginate_by = 5

    def get_queryset(self):
        queryset = super(GalleryListView, self).get_queryset()
        queryset = queryset.filter(gallerydistinction__in_global=True)
        return queryset


class ContentItemDetailView(BaseContentItemDetailView):

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if isinstance(self.object, Site):
            if self.get_children_queryset().count() == 0 and self.object.content == "" and self.object.allow_redirect_to_children():
                redirect_site = self.object.children.published().first()
                if redirect_site:
                    return HttpResponseRedirect(redirect_site.get_absolute_url())
        try:
            return super(DetailView, self).get(request, *args, **kwargs)
        except RedirectException as r:
            return HttpResponseRedirect(r.url)

    def get_context_data(self, **kwargs):
        context = super(ContentItemDetailView, self).get_context_data(**kwargs)

        if self.request.path.startswith("/projekty/"):
            category_slugs = self.kwargs['hierarchy'].split('/')
            category_project = Site.objects.get_by_slug(category_slugs[1])
            if category_project.is_published():
                context['category_project'] = category_project
        return context

# -*- encoding: utf-8 -*-
from urlparse import urlparse

from django.core.paginator import Paginator, InvalidPage
from django.http.response import Http404

from corecms.models.default.slider import Slider
from corecms.templatetags.corecms_tags import get_previous_breadcrumb
from django import template
from cms.models import Article, Site

from django.utils.translation import ugettext_lazy as _
register = template.Library()


@register.simple_tag
def get_site_thumbnail(article=None):
    try:
        return article.get_main_parent().main_image.url
    except (ValueError, AttributeError):
        return '/static/website/images/2.jpg'


@register.simple_tag(takes_context=True)
def get_site_identity(context, article=None):
    if article is None:
        return get_previous_breadcrumb(context)
    else:
        try:
            return article.get_main_parent().identity
        except AttributeError:
            return article.identity


@register.assignment_tag
def get_opinie_list():
    return Site.objects.get(slug="opinie").articles.published()
    try:
        return Site.objects.get(slug="opinie").articles.published()
    except:
        return None


def paginate_queryset(queryset, context):

    paginator = Paginator(queryset, 5)

    page = context['request'].GET.get('p') or 1

    try:
        page_number = int(page)
    except ValueError:
        if page == 'last':
            page_number = paginator.num_pages
        else:
            raise Http404(_("Page is not 'last', nor can it be converted to an int."))
    try:
        page = paginator.page(page_number)
        return paginator, page, page.object_list, page.has_other_pages()
    except InvalidPage as e:
        raise Http404(_('Invalid page (%(page_number)s): %(message)s') % {
            'page_number': page_number,
            'message': str(e)
        })

@register.inclusion_tag('website/site/templates/_site_obszar_content.html', takes_context=True)
def render_obszary_dzialania_content(context, site):
    rtn = dict()
    rtn['projects'] = Site.objects.published().filter(areas=site, parent__slug='projekty')
    rtn['sites'] = Site.objects.published().filter(areas=site).exclude(parent__slug='projekty')
    rtn['articles'] = Article.objects.published().filter(areas=site)
    publication_site = Site.objects.filter(slug="publikacje").first()
    if publication_site:
        rtn['articles'] = rtn['articles'].exclude(sites=publication_site)
        rtn['publications'] = Article.objects.published().filter(areas=site, sites=publication_site)
    context['related_items'] = rtn

    paginator, page, queryset, is_paginated = paginate_queryset(rtn['articles'], context)
    context.update({
        'paginator': paginator,
        'page_obj': page,
        'is_paginated': is_paginated,
        'object_list': queryset
    })
    context['related_items']['articles'] = queryset
    return context


@register.filter
def to_hash_url(url):
    splited = url.rstrip("/").split("/")
    return "/".join(splited[0:len(splited)-1]) + "#" + splited[-1]


@register.assignment_tag
def get_partnership_slider(slug):
    try:
        return Slider.objects.get(slug=slug)
    except Slider.DoesNotExist:
        return None


@register.filter
def get_domain(url):
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain


@register.assignment_tag
def get_first_pdf(article):
    for f in article.published_files:
        if f.is_pdf:
            return f
    return None

@register.assignment_tag
def get_top_wrapper(category_project, category, article):
    if article and article.main_image:
        return article.main_image

    if category_project and category_project.main_image:
        return category_project.main_image

    if category and category.main_image:
        return category.main_image

    return None
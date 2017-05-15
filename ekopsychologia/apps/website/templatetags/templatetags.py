# -*- encoding: utf-8 -*-
from urlparse import urlparse
from corecms.models.default.slider import Slider
from corecms.templatetags.corecms_tags import get_previous_breadcrumb
from django import template
from cms.models import Article, Site

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


@register.assignment_tag
def get_obszary_dzialania_content(site):
    rtn = dict()
    rtn['sites'] = Site.objects.published().filter(areas=site)
    rtn['articles'] = Article.objects.published().filter(areas=site)
    return rtn


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
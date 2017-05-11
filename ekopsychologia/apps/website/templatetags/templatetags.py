# -*- encoding: utf-8 -*-
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
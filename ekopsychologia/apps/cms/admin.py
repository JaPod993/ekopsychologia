# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import json

from corecms.models.gallery import Gallery
from django.contrib import admin

from corecms.admin import ArticleAdmin as BaseArticleAdmin
from django.contrib.contenttypes.models import ContentType

from cms.models import Article, GalleryDistinction


class ArticleAdmin(BaseArticleAdmin):
    change_form_template = "cms/admin/change_form_article.html"

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        article = Article.objects.get(pk=object_id)

        gallery_ct = ContentType.objects.get_for_model(Gallery)
        galleries = [child.children_id for child in article.connector_children.filter(children_type=gallery_ct)]

        extra_context['global_galleries'] = []

        if galleries:
            extra_context['global_galleries'] = list(GalleryDistinction.objects.\
                filter(gallery_id__in=galleries, in_global=True).values_list('gallery_id', flat=True))

        extra_context['global_galleries_json'] = json.dumps(extra_context['global_galleries'])
        return super(ArticleAdmin, self).change_view(request, object_id, form_url, extra_context)


admin.site.unregister(Article)
admin.site.register(Article, ArticleAdmin)
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from corecms.admin import ArticleAdmin as BaseArticleAdmin

from cms.models import Article


class ArticleAdmin(BaseArticleAdmin):
    change_form_template = "cms/admin/change_form_article.html"

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        article  = Article.objects.get(pk=object_id)

        return super(ArticleAdmin, self).change_view(request, object_id, form_url, extra_context)


admin.site.unregister(Article)
admin.site.register(Article, ArticleAdmin)
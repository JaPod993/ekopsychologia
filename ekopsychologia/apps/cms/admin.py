# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import json

from corecms.forms.forms import SiteAdminForm as BaseSiteAdminForm, ArticleAdminForm as BaseArticleAdminForm
from corecms.models.gallery import Gallery
from corecms.widgets import Select2RelatedMultipleWidget
from django.contrib import admin

from corecms.admin import ArticleAdmin as BaseArticleAdmin, SiteAdmin as BaseSiteAdmin
from django.contrib.contenttypes.models import ContentType

from cms.models import Article, GalleryDistinction, Site, Founder


class ArticleAdminForm(BaseArticleAdminForm):

    def __init__(self, *args, **kwargs):
        super(ArticleAdminForm, self).__init__(*args, **kwargs)
        self.fields['areas'].queryset = Site.objects.filter(parent__slug="obszary-dzialania")
        self.fields['areas'].widget = Select2RelatedMultipleWidget(rel=Site, choices=self.fields['areas'].widget.choices)

    class Meta:
        model = Article
        fields = ('identity', 'shortcut', 'content', 'status', 'slug',
                  'template', 'article_date', 'thumbnail', 'main_image', 'for_lang', 'tags', 'areas')


class ArticleAdmin(BaseArticleAdmin):
    form = ArticleAdminForm
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


class SiteAdminForm(BaseSiteAdminForm):

    def __init__(self, *args, **kwargs):
        super(SiteAdminForm, self).__init__(*args, **kwargs)
        self.fields['areas'].queryset = Site.objects.filter(parent__slug="obszary-dzialania")
        self.fields['areas'].widget = Select2RelatedMultipleWidget(rel=Site, choices=self.fields['areas'].widget.choices)

    class Meta:
        model = Site
        fields = ('identity', 'content', 'status', 'parent', 'slug', 'template', 'thumbnail',
                  'main_image', 'logo', 'url', 'execution_time', 'budget', 'areas')


class FounderInline(admin.TabularInline):
    model = Founder


class SiteAdmin(BaseSiteAdmin):
    form = SiteAdminForm
    change_form_template = "cms/admin/change_form_site.html"

    def get_inline_instances(self, request, obj=None):
        if obj is not None and obj.parent is not None and obj.parent.slug == 'projekty':
            inline_instances = []
            for inline_class in [FounderInline]:
                inline = inline_class(self.model, self.admin_site)
                if request:
                    if not (inline.has_add_permission(request) or
                            inline.has_change_permission(request, obj) or
                            inline.has_delete_permission(request, obj)):
                        continue
                    if not inline.has_add_permission(request):
                        inline.max_num = 0
                inline_instances.append(inline)
            return inline_instances
        return []

admin.site.unregister(Site)
admin.site.register(Site, SiteAdmin)

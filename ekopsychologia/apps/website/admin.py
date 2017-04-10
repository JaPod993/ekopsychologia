# -*- encoding: utf-8 -*-

from django.contrib import admin

from website.models import NewsletterEmail


class NewsletterEmailAdmin(admin.ModelAdmin):
    pass


admin.site.register(NewsletterEmail, NewsletterEmailAdmin)
from corecms.admin import ArticleAdmin
from django.contrib import admin

from cms.forms import EcophonArticleForm
from cms.models import Article

admin.site.unregister(Article)


class EcophoneArticleAdmin(ArticleAdmin):
    change_form_template = 'corecms/change_form_article.html'
    form = EcophonArticleForm


admin.site.register(Article, EcophoneArticleAdmin)

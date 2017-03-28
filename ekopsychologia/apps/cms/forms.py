from corecms.forms.forms import ArticleAdminForm


class EcophonArticleForm(ArticleAdminForm):
    class Meta(ArticleAdminForm.Meta):
        fields = ('identity', 'shortcut', 'content', 'status', 'slug', 'template', 'article_date', 'thumbnail', 'main_image', 'for_lang', 'tags', 'alternative_url')

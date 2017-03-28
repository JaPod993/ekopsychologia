from modeltranslation.translator import translator, TranslationOptions
from cms.models import Site, Article, TextBlock, MediaFile


class SiteTranslationOptions(TranslationOptions):
    fields = ('identity', 'content', 'slug')

translator.register(Site, SiteTranslationOptions)


class ArticleTranslationOptions(TranslationOptions):
    fields = ('identity', 'content', 'slug', 'for_lang')

translator.register(Article, ArticleTranslationOptions)


class TextBlockTranslationOptions(TranslationOptions):
    fields = ('content',)

translator.register(TextBlock, TextBlockTranslationOptions)


class MediaFileTranslationOptions(TranslationOptions):
    fields = ('for_lang',)

translator.register(MediaFile, MediaFileTranslationOptions)



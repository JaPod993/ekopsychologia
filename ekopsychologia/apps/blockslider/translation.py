#coding=utf-8
from modeltranslation.translator import TranslationOptions, translator
from .models import BlockSlider


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'background', 'background_color', 'url', 'more_button_text', 'box_size', 'full_height', 'visible')

translator.register(BlockSlider, ProductTranslationOptions)

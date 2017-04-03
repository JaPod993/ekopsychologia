#coding=utf-8

#from corecms.admin import CMSTranslationAdmin
from django.contrib import admin
from materialtemplate.admin.admin import SortableModelAdmin
from modeltranslation.admin import TranslationAdmin
from .models import BlockSlider, BlockSliderFile, BlockSliderCategory


class BlockFileAdmin(admin.TabularInline):
    model = BlockSliderFile
    extra = 1
    template = 'blockslider/admin/blockfile_inline.html'


class BlockSliderAdmin(SortableModelAdmin, TranslationAdmin):
    list_display = ('title', 'category', 'url', 'box_size', 'visible',)
    list_filter = ('visible',)
    inlines = [BlockFileAdmin]

    class Media:
        css = {
            'all': ('blockslider/codemirror/lib/codemirror.css',)
        }
        js = ('blockslider/codemirror/lib/codemirror.js','blockslider/codemirror/mode/xml/xml.js', 'blockslider/codemirror/addon/edit/closetag.js', 'blockslider/codemirror/mode/htmlmixed/htmlmixed.js', 'blockslider/blockslider.js')


class BlockSliderCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'identity',)


admin.site.register(BlockSlider, BlockSliderAdmin)
admin.site.register(BlockSliderCategory, BlockSliderCategoryAdmin)
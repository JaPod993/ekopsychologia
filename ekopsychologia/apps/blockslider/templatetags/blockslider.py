#coding=utf-8
from django import template
from apps.blockslider.models import BlockSlider

register = template.Library()


@register.assignment_tag
def get_blocks_by_category(category_slug):
    return BlockSlider.objects.filter(category__identity=category_slug)
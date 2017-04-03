#coding=utf-8
from django import template

register = template.Library()

@register.assignment_tag
def get_blocks_by_category(category_slug):
    from blockslider.models import BlockSlider
    return BlockSlider.objects.filter(category__identity=category_slug)
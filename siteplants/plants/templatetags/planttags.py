from django import template
from django.db.models import Count

import plants.views as views
from plants.models import Category, TagPost

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('plants/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(count_posts=Count("posts")).filter(count_posts__gt=0)

    return {'cats': cats, "cat_selected": cat_selected}


@register.inclusion_tag('plants/list_tags.html')
def show_tags():
    tags = TagPost.objects.annotate(count_tags=Count("tags")).filter(count_tags__gt=0)
    return {'tags': tags}

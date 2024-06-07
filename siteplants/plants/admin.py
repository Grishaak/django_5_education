from django.contrib import admin
from django.core.paginator import Paginator

from plants.models import Plant, Category, TagPost


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'slug', 'time_created', 'time_updated', 'is_published', 'brief_info')
    list_display_links = ('id', 'title')
    ordering = ['id', 'time_created', 'title']
    list_editable = ('is_published',)
    list_per_page = 6

    @admin.display(description='Кратное описание', ordering='content')
    def brief_info(self, plant: Plant):
        return f"Описание контента: {len(plant.content)}"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    ordering = ['id', 'name']


@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'slug')
    list_display_links = ('id', 'tag')
    ordering = ['id', 'tag']

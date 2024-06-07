from django.urls import path, re_path
from plants.views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>', show_post, name='post'),
    path('addpage/', addpage, name='addpage'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('category/<slug:category_slug>', show_category, name='category'),
    path('tag/<slug:tag_slug>', show_tags_postlist, name='tag')
]

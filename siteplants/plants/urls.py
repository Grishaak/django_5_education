from django.urls import path, re_path
from plants.views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('post/<slug:post_slug>', post, name='post'),
    path('addpage/', addpage, name='addpage'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('category/<int:category_id>', category, name='category'),
]

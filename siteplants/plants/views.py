from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.template.loader import render_to_string

from plants.models import Plant, Category, TagPost

menu = [{'title': 'Главная страница', 'url': 'index'},
        {'title': 'О сайте', 'url': 'about'},
        {'title': 'Доавить статью', 'url': 'addpage'},
        {'title': 'Обратная связь', 'url': 'contact'},
        {'title': 'Войти', 'url': 'login'}]

data_db = Plant.published.all()


def index(request):
    data = {'title': 'главная страница',
            'menu': menu,
            'posts': data_db.select_related('cat'),
            'cat_seleted': 0}
    return render(request, 'plants/index.html', context=data)


def about(request):
    data = {'title': 'О сайте',
            'menu': menu}
    return render(request, 'plants/about.html', context=data)


def show_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Plant.published.filter(cat_id=category.pk).select_related('cat')
    data = {'title': f'Рубрика : {category.name}',
            'menu': menu,
            'posts': posts,
            # 'category': category,
            'cat_selected': category.pk}
    return render(request, 'plants/index.html', context=data)


def show_post(request, post_slug):
    post = get_object_or_404(Plant, slug=post_slug)
    data = {'title': post.title,
            'menu': menu,
            'post': post,
            'cat_selected': 0}
    return render(request, 'plants/post.html', context=data)


def show_tags_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    post_by_tag = tag.tags.filter(is_published=Plant.Status.PUBLISHED).select_related('cat')
    data = {'title': f'Тег: {tag.tag}',
            'menu': menu,
            'posts': post_by_tag,
            'cat_selected': 0}
    return render(request, 'plants/index.html', context=data)


def addpage(request):
    return HttpResponse(f'<h1>Добавьте свою статью здесь.</h1>')


def contact(request):
    return HttpResponse(f'<h1>Свяжитесь с нами.</h1>')


def login(request):
    return HttpResponse(f'<h1>Свяжитесь с нами.</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не определена</h1>')

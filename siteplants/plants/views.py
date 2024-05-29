from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, reverse, render
from django.template.loader import render_to_string

menu = [{'title': 'Главная страница', 'url': 'index'},
        {'title': 'О сайте', 'url': 'about'},
        {'title': 'Доавить статью', 'url': 'addpage'},
        {'title': 'Обратная связь', 'url': 'contact'},
        {'title': 'Войти', 'url': 'login'}]
data_db = [
    {'id': 1, 'title': 'Person_1', 'content': '''content_1content'is_published': True
    'is_published': True
    'is_published': Trueco'is_published': True'is_published': True'is_published': True'is_published': True''',
     'is_published': True},
    {'id': 2, 'title': 'Person_2', 'content': 'content_2', 'is_published': True},
    {'id': 3, 'title': 'Person_3', 'content': 'content_3', 'is_published': False},
]

cats_db = [
    {'id': 1, 'name': 'Голосеменные'},
    {'id': 2, 'name': 'Покрытоосеменные'},
    {'id': 3, 'name': 'Лишайники'}
]


def index(request):
    data = {'title': 'главная страница',
            'menu': menu,
            'posts': data_db,
            'cat_seleted': 0}
    return render(request, 'plants/index.html', context=data)


def about(request):
    data = {'title': 'О сайте',
            'menu': menu}
    return render(request, 'plants/about.html', context=data)


def category(request, category_id):
    data = {'title': 'главная страница',
            'menu': menu,
            'posts': data_db,
            'cat_selected': category_id}
    return render(request, 'plants/index.html', context=data)


def post(request, post_id):
    return HttpResponse(f'<h1>Тут страница статьи по id.</h1>'
                        f'<h2><p>id: {post_id}</p><h2>')


def addpage(request):
    return HttpResponse(f'<h1>Добавьте свою статью здесь.</h1>')


def contact(request):
    return HttpResponse(f'<h1>Свяжитесь с нами.</h1>')


def login(request):
    return HttpResponse(f'<h1>Свяжитесь с нами.</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не определена</h1>')

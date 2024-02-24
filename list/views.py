from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
# from users.models import Contact
from .models import *

menu = [
    {'title': 'Главная страница', 'url_name': 'index'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Пользователи', 'url_name': 'users'},
    # {'title': 'Зарегистрироваться', 'url_name': 'users_signup'},
    {'title': 'Войти', 'url_name': 'login'}
]


def index(request):
    # wishes = Wish.objects.all()
    # users = Contact.objects.all()
    context = {
        'menu': menu,
        'title': 'Главная страница',
        # 'users': users,
        # 'wishes': wishes,
        'heading': 'Список Желаний'
    }
    return render(request, 'list/index.html', context)


def details(request, wish_pk):
    wish = get_object_or_404(Wish, pk=wish_pk)
    context = {'menu': menu, 'wish': wish}
    return render(request, 'list/details.html', context)


def about(request):
    context = {'menu': menu, 'title': 'О сайте', 'heading': 'О сайте'}
    return render(request, 'list/about.html', context)


def users(request):
    # # users = Contact.objects.all()
    # context = {
    #     # 'users': users,
    #     'menu': menu,
    #     'title': 'Пользователи',
    #     'heading': 'Пользователи'
    # }
    # return render(request, 'list/users.html', context)
    return HttpResponse(f"Пользователи")



def person(request, person_id):
    return HttpResponse(f"Страница пользователя {person_id}")


def login(request):
    return HttpResponse(f"Авторизация")


# def page_not_found(request, exсeption):
#     return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def serverError(request, exception):
#     return HttpResponseServerError('<h1>Ошибка сервера</h1>')

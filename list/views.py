from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, login
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateWishForm, RegisterUserForm, LoginUserForm
from .models import *
from .utils import *


class WishIndex(DataMixin, ListView):
    model = Wish
    template_name = 'list/index.html'
    context_object_name = 'wishes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Главная страница',
            heading='Список Желаний'
        )
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_queryset(self):
        return Wish.objects.filter(gift=False)


class DetailWish(DataMixin, DetailView):
    model = Wish
    template_name = 'list/details.html'
    slug_url_kwarg = 'wish_slug'
    context_object_name = 'wish'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['wish'])
        return dict(list(context.items()) + list(c_def.items()))


class CreateWish(LoginRequiredMixin, DataMixin, CreateView):
    form_class = CreateWishForm
    template_name = 'list/create.html'
    success_url = reverse_lazy('wishlist:index')
    login_url = reverse_lazy('wishlist:index')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Добавить желание',
            heading='Добавить желание'
        )
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    context = {'menu': menu, 'title': 'О сайте', 'heading': 'О сайте'}
    return render(request, 'list/about.html', context)


def person(request, person_id):
    return HttpResponse(f"Страница пользователя {person_id}")


# def login(request):
#     return HttpResponse(f"Авторизация")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'list/register.html'
    success_url = reverse_lazy('wishlist:login')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('wishlist:index')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'list/login.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('wishlist:index')


def logout_user(request):
    logout(request)
    return redirect('wishlist:login')

# def page_not_found(request, exсeption):
#     return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def serverError(request, exception):
#     return HttpResponseServerError('<h1>Ошибка сервера</h1>')

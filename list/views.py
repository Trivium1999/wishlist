from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateWishForm
from .models import *
from .utils import *


class WishIndex(DataMixin, ListView):
    model = Wish
    template_name = 'list/index.html'
    context_object_name = 'wishes'
    paginate_by = 6

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



# def create(request):
#     if request.method == 'POST':
#         form = CreateWishForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('wishlist:index')
#     else:
#         form = CreateWishForm()
#     context = {
#         'menu': menu,
#         'title': 'Добавить желание',
#         'heading': 'Добавить желание',
#         'form': form
#     }
#     return render(request, 'list/create.html', context)


def about(request):
    context = {'menu': menu, 'title': 'О сайте', 'heading': 'О сайте'}
    return render(request, 'list/about.html', context)


def person(request, person_id):
    return HttpResponse(f"Страница пользователя {person_id}")


def login(request):
    return HttpResponse(f"Авторизация")


# def page_not_found(request, exсeption):
#     return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def serverError(request, exception):
#     return HttpResponseServerError('<h1>Ошибка сервера</h1>')

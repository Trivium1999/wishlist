from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CreateWishForm
from .models import *
from .utils import *


class WishIndex(DataMixin, ListView):
    model = get_user_model()
    template_name = 'list/home.html'
    context_object_name = 'users'
    extra_context = {
        'title': 'Главная страница',
        'heading': 'Список Пользователей'
    }


class WishesForUser(DataMixin, ListView):
    model = Wish
    template_name = 'list/index.html'
    context_object_name = 'wishes'
    extra_context = {
        'title': 'Список желаний',
        'heading': 'Список желаний'
    }
    
    def get_queryset(self):
        return Wish.objects.filter(author_id=self.kwargs['author_id'])


class DetailWish(DataMixin, DetailView):
    model = Wish
    template_name = 'list/details.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'wish'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['wish'])
        return dict(list(context.items()) + list(c_def.items()))


class CreateWish(LoginRequiredMixin, DataMixin, CreateView):
    form_class = CreateWishForm
    template_name = 'list/create.html'
    success_url = reverse_lazy('wishlist:index')
    extra_context = {
        'title': 'Добавить желание',
        'heading': 'Добавить желание'
    }
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateWish(AuthorRequiredMixin, SuccessMessageMixin, DataMixin, UpdateView):
    model = Wish
    fields = ['title', 'image', 'description']
    template_name = 'list/create.html'
    pk_url_kwarg = 'wish_pk'
    success_url = reverse_lazy('wishlist:index')
    success_message = 'Желание было успешно обновлено'
    extra_context = {
        'is_edit': True,
        'title': 'Редактирование желания',
        'heading': 'Редактирование желания'
    }


class DeleteWish(AuthorRequiredMixin, DataMixin, DeleteView):
    model = Wish
    success_url = reverse_lazy('wishlist:index')
    context_object_name = 'wish'
    pk_url_kwarg = 'wish_pk'
    template_name = 'list/delete.html'
    extra_context = {
            'title': 'Удаление',
            'heading': 'Удаление'
    }


@login_required
def about(request):
    context = {'menu': menu, 'title': 'О сайте', 'heading': 'О сайте'}
    return render(request, 'list/about.html', context)

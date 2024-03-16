from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateWishForm
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
    # login_url = reverse_lazy('wishlist:index')
    # raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Добавить желание',
            heading='Добавить желание'
        )
        return dict(list(context.items()) + list(c_def.items()))
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateWish(UpdateView):
    model = Wish
    fields = ['title', 'image', 'description']
    template_name = 'list/create.html'
    success_url = reverse_lazy('wishlist:index')
    extra_context = {
            'title': 'Редактирование желания',
            'heading': 'Редактирование желания'
    }

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(
    #         title='Редактирование желания',
    #         heading='Редактирование желания'
    #     )
    #     return dict(list(context.items()) + list(c_def.items()))


@login_required
def about(request):
    context = {'menu': menu, 'title': 'О сайте', 'heading': 'О сайте'}
    return render(request, 'list/about.html', context)

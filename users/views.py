from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from list.utils import *
from .forms import RegisterUserForm, LoginUserForm, ProfileUserForm, UserPasswordChangeForm


def person(request, person_id):
    return HttpResponse(f"Страница пользователя {person_id}")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     return redirect('wishlist:index')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))


class ProfileUser(LoginRequiredMixin, DataMixin, UpdateView):
    model = get_user_model()
    form_class =ProfileUserForm
    template_name = 'users/profile.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Профиль пользователя")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change_form.html'


class UserPasswordChangeDoneView(DataMixin, PasswordChangeDoneView):
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Пароль успешно изменён!")
        return dict(list(context.items()) + list(c_def.items()))

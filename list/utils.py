from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.shortcuts import redirect


menu = [
    {'title': 'Главная страница', 'url_name': 'wishlist:index'},
    {'title': 'Добавить желание', 'url_name': 'wishlist:create'},
    {'title': 'О сайте', 'url_name': 'wishlist:about'}
]


class DataMixin:
    paginate_by = 9

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        return context


class AuthorRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if request.user.is_authenticated:
            if request.user != self.get_object().author or request.user.is_staff:
                messages.info(request, 'Изменение и удаление доступно только автору.')
                return redirect('wishlist:index')
        return super().dispatch(request, *args, **kwargs)

menu = [
    {'title': 'Главная страница', 'url_name': 'wishlist:index'},
    {'title': 'Добавить желание', 'url_name': 'wishlist:create'},
    {'title': 'О сайте', 'url_name': 'wishlist:about'}
]

class DataMixin:
    paginate_by = 6

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        return context
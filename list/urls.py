from django.urls import path
from list.views import WishIndex, DetailWish, CreateWish, person, about, login

app_name = 'list'

urlpatterns = [
    path('', WishIndex.as_view(), name='index'), # отображаются пользователи, с фото и именами
    path('about/', about, name='about'), # о проекте
    path('person/<slug:person_id>/', person, name='person'),  # страница пользователя со списком подарков
    # path('users/', users, name='users'), # все пользователи, с фото и именами
    path('login/', login, name='login'),
    path('create/', CreateWish.as_view(), name='create'),
    path('details/<slug:wish_slug>/', DetailWish.as_view(), name='details_wish') # подробная информация о подарке
]

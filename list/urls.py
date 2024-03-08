from django.urls import path
from list.views import WishIndex, DetailWish, CreateWish, RegisterUser, person, about, LoginUser, logout_user

app_name = 'list'

urlpatterns = [
    path('', WishIndex.as_view(), name='index'), # отображаются пользователи, с фото и именами
    path('about/', about, name='about'), # о проекте
    path('person/<slug:person_id>/', person, name='person'),  # страница пользователя со списком подарков
    # path('users/', users, name='users'), # все пользователи, с фото и именами
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('create/', CreateWish.as_view(), name='create'),
    path('details/<slug:wish_slug>/', DetailWish.as_view(), name='details_wish') # подробная информация о подарке
]

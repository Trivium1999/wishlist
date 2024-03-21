from django.urls import path
from .views import (WishIndex,
                    DetailWish,
                    CreateWish,
                    about,
                    UpdateWish,
                    WishHome)

app_name = 'list'

urlpatterns = [
    path('', WishHome.as_view(), name='index'), # отображаются пользователи, с фото и именами
    path('about/', about, name='about'), # о проекте
    path('create/', CreateWish.as_view(), name='create'),
    path('edit/<int:pk>/', UpdateWish.as_view(), name='edit_wish'),
    path('details/<int:pk>/', DetailWish.as_view(), name='details_wish') # подробная информация о подарке
]

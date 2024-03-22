from django.urls import path
from .views import (WishesOneUser,
                    DetailWish,
                    CreateWish,
                    about,
                    UpdateWish,
                    WishIndex)

app_name = 'list'

urlpatterns = [
    path('', WishIndex.as_view(), name='index'),
    path('wish_user/<int:author_id>/', WishesOneUser.as_view(), name='all_wish'),
    path('about/', about, name='about'), # о проекте
    path('create/', CreateWish.as_view(), name='create'),
    path('edit/<int:pk>/', UpdateWish.as_view(), name='edit_wish'),
    path('details/<int:pk>/', DetailWish.as_view(), name='details_wish') # подробная информация о подарке
]

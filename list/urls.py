from django.urls import path
from .views import (WishesForUser,
                    DetailWish,
                    DeleteWish,
                    CreateWish,
                    about,
                    UpdateWish,
                    WishIndex)

app_name = 'list'

urlpatterns = [
    path('', WishIndex.as_view(), name='index'),
    path('wish_user/<int:author_id>/', WishesForUser.as_view(), name='all_wish'),
    path('about/', about, name='about'),
    path('create/', CreateWish.as_view(), name='create'),
    path('edit/<int:wish_pk>/', UpdateWish.as_view(), name='edit_wish'),
    path('delete/<int:wish_pk>/', DeleteWish.as_view(), name='delete_wish'),
    path('details/<int:pk>/', DetailWish.as_view(), name='details_wish')
]

from django.urls import path
from list.views import index, person, about, users, login, details


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('person/<slug:person_id>/', person, name='person'),
    path('users/', users, name='users'),
    path('login/', login, name='login'),
    # path('create/', create),
    path('details/<int:wish_pk>/', details, name='details')
]

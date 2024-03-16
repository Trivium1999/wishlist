from django.urls import path
from django.contrib.auth.views import (LogoutView, 
                                       PasswordChangeView)
from .views import (RegisterUser,
                    person,
                    LoginUser,
                    ProfileUser,
                    UserPasswordChange,
                    UserPasswordChangeDoneView)

app_name = 'users'

urlpatterns = [
    path('person/<slug:person_id>/', person, name='person'),  # страница пользователя со списком подарков
    # path('users/', users, name='users'), # все пользователи, с фото и именами
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', ProfileUser.as_view(), name='profile'),
    path('password-change/', UserPasswordChange.as_view(), name='password_change'),
    path('password-change/done/', UserPasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done')
]

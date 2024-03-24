from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, generate_password, verification_view

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/confirm/<str:token>', verification_view, name='register_confirm'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('genpassword/', generate_password, name='generate_password'),
]

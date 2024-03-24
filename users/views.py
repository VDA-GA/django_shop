import random

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User

ALPHABET_1 = ''.join([chr(i) for i in range(65, 91)])
ALPHABET_2 = ''.join([chr(i) for i in range(97, 123)])
NUMERIC = ''.join([str(i) for i in range(0, 10)])
LIST_FOR_GENERATION = ALPHABET_1 + ALPHABET_2 + NUMERIC


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('Skystore:product_list')
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save()
        self.object.verification_code = ''.join(random.choice(LIST_FOR_GENERATION) for _ in range(12))
        current_site = self.request.get_host()
        verification_link = f'http://{current_site}/users/register/confirm/{self.object.verification_code}'
        message = f'Для верификации Вашего email перейдите по ссылке: {verification_link}'
        send_mail(
            subject='Смена пароля',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('Skystore:product_list')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        alphabet = [chr(i) for i in range(65, 123)]
        new_password = ''.join(random.choice(LIST_FOR_GENERATION) for _ in range(10))
        send_mail(
            subject='Смена пароля',
            message=f'Ваш новый пароль: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        user.set_password(new_password)
        user.save()
    return render(request, 'users/gen_password.html')


def verification_view(request, token):
    user = User.objects.get(verification_code=token)
    if user:
        user.is_verify = True
        user.save()
    return redirect(reverse('users:login'))

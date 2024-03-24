from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='номер телефона')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    country = models.CharField(max_length=100, **NULLABLE, verbose_name='страна')
    is_verify = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=50, **NULLABLE, verbose_name='токен')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

from django.contrib.auth.models import AbstractUser
from django.db import models

from default import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='старна', **NULLABLE)
    token = models.CharField(max_length=22, verbose_name='Token для верификации почты', **NULLABLE)

    is_active = models.BooleanField(default=False, verbose_name='верифицированна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

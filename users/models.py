from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from common.models import IndexedTimeStampedModel
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=20)
    description = models.TextField(max_length=250, blank=True)
    karma = models.IntegerField(default=0)
    avatar = models.ImageField(blank=True, default="reditiavatar.png")
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

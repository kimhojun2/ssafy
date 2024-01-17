from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, PermissionsMixin
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    device_permission = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'


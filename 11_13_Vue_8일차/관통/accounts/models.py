from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    age = models.IntegerField()
    money = models.IntegerField()
    salary = models.IntegerField()
    nickname = models.TextField(null=True)
    financial_products = models.TextField(null=True, blank=True)



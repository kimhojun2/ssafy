from django.db import models
from accounts.models import User


class Device(models.Model):
    device_num = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='using_device')

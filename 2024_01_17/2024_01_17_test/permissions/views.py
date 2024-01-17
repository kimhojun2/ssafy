from django.shortcuts import render
from django.contrib.auth.models import Permission
from django.http import JsonResponse
from accounts.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Device
# Create your views here.

def grant(request, username, device_num):
    user = get_object_or_404(User, username=username)
    device = get_object_or_404(Device, device_num=device_num)
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    print(device)
    user.device_permission = True
    device.user = user
    device.save()
    user.save()
    return JsonResponse({'message':'권한 획득'})


def revoke(request, username, device_num):
    user = get_object_or_404(User, username=username)
    device = get_object_or_404(Device, device_num=device_num)
    user.device_permission = False
    user.save()
    device.user = None
    device.save()
    return JsonResponse({'message':'권한 삭제'})
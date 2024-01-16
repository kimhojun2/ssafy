from django.shortcuts import render
from django.contrib.auth.models import User, Permission
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status, permissions
Permission._meta.get_field('user').related_model = User
# Create your views here.

def grant(request, username):
    user = get_object_or_404(User, username=username)
    print('##############################################################',user)
    device_ok_permission, created = Permission.objects.get_or_create(
    codename='device_ok',
    name='Can access device functionality',
    )
    user.user_permissions.add(device_ok_permission)
    return Response(status=status.HTTP_100_CONTINUE)
    # user = get_object_or_404(User, username=username)
    # device_ok_permission = Permission.objects.get(codename='device_ok')

    # user.user_permissions.add(device_ok_permission)

    # return HttpResponse(f"Permission granted to user: {username}")
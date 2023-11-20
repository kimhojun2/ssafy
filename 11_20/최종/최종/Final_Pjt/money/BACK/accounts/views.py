from django.conf import settings
from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import CustomRegisterSerializer, ItemSerializer
import requests

# Create your views here.
@api_view(['GET', 'PUT'])
def profile(request, username):
    if request.method == 'GET':
        oneprofile = User.objects.get(username=username)
        serializer = ItemSerializer(oneprofile)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ItemSerializer(User, data=request.data, partial=True)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
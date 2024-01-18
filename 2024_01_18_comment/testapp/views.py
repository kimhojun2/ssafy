from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth.decorators import login_required, permission_required

from rest_framework.views import APIView
from accounts.decorators import device_permission_required



# Create your views here.
# @login_required
@api_view(['GET', 'POST'])
def list(request):
    if request.method == 'GET':
        posts = get_list_or_404(Post)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

# @login_required
@api_view(['GET','PUT','DELETE'])
def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
@device_permission_required
class DevicePermissionView(APIView):
    def get(self, request):
        return Response({'message':'기능 사용 가능'})   
    


#qr
from django.http import HttpResponse
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image


def generate_qr(request):
    google_link = "https://semantle-ko.newsjel.ly/"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(google_link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_bytes_io = BytesIO()
    img.save(img_bytes_io, format='PNG')

    response = HttpResponse(img_bytes_io.getvalue(), content_type="image/png")
    return response
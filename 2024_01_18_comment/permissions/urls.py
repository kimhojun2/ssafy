from django.urls import path, include
from . import views

urlpatterns = [
    path('grant/<str:username>/<int:device_num>/', views.grant),
    path('revoke/<str:username>/<int:device_num>/', views.revoke),
]

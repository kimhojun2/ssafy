from django.urls import path, include
from . import views

urlpatterns = [
    path('grant/<str:username>/', views.grant),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.list),
    path('list/<int:post_pk>/', views.detail),
    path('list/<int:post_pk>/comments/', views.comment_create),
    path('device/', views.DevicePermissionView.as_view()),
    path('generate_qr/', views.generate_qr),
]

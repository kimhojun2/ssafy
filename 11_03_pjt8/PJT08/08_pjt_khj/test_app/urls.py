from django.urls import path
from . import views

urlpatterns = [
    path('normal_sort/', views.normal_sort),
    path('priority_queue/', views.priority_queue),
    path('bubble_sort/', views.bubble_sort),
    path('p1/', views.p1),
    path('p2/', views.p2),
    path('p3/', views.p3),

]


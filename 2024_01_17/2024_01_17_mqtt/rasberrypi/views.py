from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('hi')


def mqttTest(request):
    return render(request, 'mqtt.html')
import random
from django.shortcuts import render

# Create your views here.
def certification1(request):
    age = range(25,31)
    grade = ['a','b','c','s']
    context = {
        'age1' : age,
        'grade1' : grade,
    }
    return render(request, 'certification/certification1.html', context)

def certification2(request):
    age = range(25,31)
    grade = ['a','b','c','s']
    context = {
        'age2' : age,
        'grade2' : grade,
    }
    return render(request, 'certification/certification2.html', context)

def certification3(request):
    age = range(25,31)
    grade = ['a','b','c','s']
    context = {
        'age3' : age,
        'grade3' : grade,
    }
    return render(request, 'certification/certification3.html', context)
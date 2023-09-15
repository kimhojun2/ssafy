from django.shortcuts import render

# Create your views here.
def first(request):
    second = request.GET.get('second')
    if second is None:
        second = '아무것도 받지 못함'
    context = {
        'second' : second,
    }
    return render(request, 'throw_catch/first.html', context)

def second(request):
    first = request.GET.get('first')
    context = {
        'first' : first,
    }
    return render(request, 'throw_catch/second.html', context)
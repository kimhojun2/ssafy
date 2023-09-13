from django.shortcuts import render
import random
# Create your views here.
def first(request):
    third = request.GET.get('third')
    if third is None:
        third = 'nothing'
    context = {
        'third' : third,
    }
    return render(request, 'throw_loops/first.html', context)

def second(request):
    first = request.GET.get('first')
    context = {
        'first' : first,
    }
    return render(request, 'throw_loops/second.html', context)

def third(request):
    second1 = request.GET.get('second1')
    second2 = request.GET.get('second2')
    lst = [second1,second2]
    pick = random.choice(lst)
    context = {
        'second1' : second1,
        'second2' : second2,
        'pick' : pick,
        
    }
    return render(request, 'throw_loops/third.html', context)
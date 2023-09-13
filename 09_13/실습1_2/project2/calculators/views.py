from django.shortcuts import render

# Create your views here.
def result(request):
    pass

def calculation(request):
    return render(request, 'calculators/calculation.html')

def result(request):
    message = int(request.GET.get('message'))
    message2 = int(request.GET.get('message2'))
    mul = message*message2
    minus =  message - message2
    if message2 != 0:
        sksnrl =  message/message2
    else:
        sksnrl = 0
    context = {
        'message' : message,
        'message2' : message2,
        'mul' : mul,
        'minus' : minus,
        'sksnrl' : sksnrl,
    }
    return render(request, 'calculators/result.html', context)

from django.shortcuts import render

# Create your views here.
def calculator(request, num1, num2):
    mul = num1*num2
    minus = num1 - num2
    if num2 != 0:
        sksnrl = num1/num2
    else:
        sksnrl = 0
    context = {
        'num1' : num1,
        'num2' : num2,
        'mul' : mul,
        'minus' : minus,
        'sksnrl' : sksnrl,
    }
    return render(request, "calculator/calculator.html", context)
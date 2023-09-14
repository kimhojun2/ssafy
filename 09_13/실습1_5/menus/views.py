from django.shortcuts import render

# Create your views here.
def food(request):
    food = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
    context = {
        'food' : food
    }
    return render(request, 'menu/food.html', context)

def drink(request):
    drink = ["cider","coke","miranda","fanta", "eye of finetree"]
    context = {
        'drink' : drink
    }
    return render(request, 'menu/drink.html', context)

def receipt(request):
    message = request.GET.get('message').lower()
    food = ["피자","치킨","국밥","초밥", "민초흑당로제마라탕"]
    drink = ["cider","coke","miranda","fanta", "eye of finetree"]
    context = {
        'message' : message,
        'food' : food,
        'drink' : drink,
    }
    return render(request, 'menu/receipt.html', context)

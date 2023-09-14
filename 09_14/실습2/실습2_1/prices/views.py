from django.shortcuts import render

# Create your views here.
def price(request, thing, cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    result = 0
    if thing in product_price:
        total = product_price[thing]*cnt
        result = 1
    else:
        total = 0
    context = {
        'thing' : thing,
        'cnt' : cnt,
        'total' : total,
        'result' : result
    }

    return render(request, 'price/price.html', context)

from django.shortcuts import render
from .models import User
# Create your views here.


# def test(request):
#     financial_products = User.objects.values_list('financial_products', flat=True)
#     ages = User.objects.values_list('age', flat=True)
#     context = {
#         'financial_products' : financial_products,
#         'ages' : ages,
#     }
#     return render(request, 'accounts/test.html', context)

def test(request):
    financial_products = User.objects.values_list('financial_products', flat=True)
    ages = User.objects.values_list('age', flat=True)

    # financial_products와 ages를 쌍으로 묶기
    data = zip(financial_products, ages)

    # age가 20 이하인 데이터 필터링
    filtered_data = [(product, age) for product, age in data if age == 18 and product is not '']

    context = {
        'filtered_data': filtered_data,
    }

    return render(request, 'accounts/test.html', context)
